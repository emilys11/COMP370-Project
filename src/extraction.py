import sys
import os
import json
import time
from datetime import datetime, timedelta, timezone
import requests

# authentication
AUTH_ENDPOINT = "https://bsky.social/xrpc/com.atproto.server.createSession"
SEARCH_ENDPOINT = "https://bsky.social/xrpc/app.bsky.feed.searchPosts"

# queries
MOVIES = {
    "spiderman_bnd": {"q": '"Spider-Man Brand New Day"', "release": "2026-07-31"},
    "odyssey": {"q": '"The Odyssey" Nolan', "release": "2026-07-17"},
    "moana": {"q": '"Moana" live action', "release": "2026-07-10"},
}

# important reusable constants
OUTPUT_DIR = "raw_data"
WINDOW_DAYS = 10
SLICE_HOURS = 6
PAGE_LIMIT = 100
SLEEP_BETWEEN_CALLS = 1.5
MAX_ATTEMPTS = 5

# format dates to iso utc
def format_date(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# authentication
def authentication(session, handle, password):
    try:
        response = session.post(
            AUTH_ENDPOINT,
            json={"identifier": handle, "password": password},
            timeout=30,
        )
        response.raise_for_status()
        token = response.json()["accessJwt"]
    except (requests.RequestException, KeyError, ValueError) :
        sys.exit(1)

    return {"Authorization": f"Bearer {token}"}


# returns json body
def fetch_page(session, headers, params):
    for attempt in range(MAX_ATTEMPTS):
        try:
            response = session.get(SEARCH_ENDPOINT, params=params, headers=headers, timeout=30)

            if response.status_code == 429:
                time.sleep(15 * (attempt + 1))
                continue

            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(10 * (attempt + 1))

    return None


# builds filename
def save_raw(data, movie,date, outdir):
    filename = os.path.join(outdir, f"{movie}_{date}.json")

    output = {"movie": movie,"date": date,"posts": data}

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    except IOError:
        sys.exit(1)

    return filename


# collect posts for movie
def collect(movie, cfg, session, headers):
    outdir = os.path.join(OUTPUT_DIR, movie)
    os.makedirs(outdir, exist_ok=True)

    window_start = datetime.strptime(cfg["release"], "%Y-%m-%d").replace(tzinfo=timezone.utc)

    total = 0

    for day_offset in range(WINDOW_DAYS):
        day_start = window_start + timedelta(days=day_offset)
        day_end = day_start + timedelta(days=1)
        date_str = day_start.strftime("%Y-%m-%d")

        params = {
            "q": cfg["q"],
            "lang": "en",
            "since": format_date(day_start),
            "until": format_date(day_end),
            "sort": "latest",
            "limit": PAGE_LIMIT,
        }

        all_posts = []
        seen_cursors = set()

        while True:
            data = fetch_page(session, headers, params)

            if data is None:
                break

            posts = data.get("posts", [])
            all_posts.extend(posts)
            total += len(posts)

            cursor = data.get("cursor")

            if not cursor or cursor in seen_cursors:
                break

            seen_cursors.add(cursor)
            params["cursor"] = cursor
            time.sleep(SLEEP_BETWEEN_CALLS)

        save_raw(all_posts, movie, date_str, outdir)

        print(f"[{movie} | {date_str}] {len(all_posts)} posts")

        time.sleep(SLEEP_BETWEEN_CALLS)

    print(f"[{movie}] {total} posts!!!")
    return total


def main():
    handle = os.getenv("BLUESKY_HANDLE")
    password = os.getenv("BLUESKY_APP_PASSWORD")

    with requests.Session() as session:
        headers = authentication(session, handle, password)

        for movie in MOVIES:
            collect(movie, MOVIES[movie], session, headers)


if __name__ == "__main__":
    main()