"""
1. english only
2. spam removal
3. duplicate removal
4. remove posts that mention 2+ of the movies
5. remove posts that don't talk about the movie 
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

RAW_DIR = "raw_data"
OUT_DIR = "filtered_data"
MOVIES = ["spiderman_bnd", "odyssey", "moana"]

#limitations to detect spams
MAX_HASHTAGS = 4
MAX_URLS = 3
MAX_MENTIONS = 5
IDENTICAL_COPIES_SPAM = 3
MAX_POSTS_PER_AUTHOR = 15

#regexes to detect spam like links,metions,hashtags
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.I)
HASHTAG_RE = re.compile(r"#\w+")

SPAM_RE = re.compile(
r"\b(?:"
    r"watch\s+(?:it\s+)?(?:online|free|now)|"
    r"free\s+(?:stream|streaming|download|movie)|"
    r"full\s+movie|"
    r"download\s+(?:now|free|hd)|"
    r"stream\s+(?:it\s+)?(?:free|online)|"
    r"1080p|720p|4k\s+hd|hdrip|webrip|bluray|camrip|putlocker|123movies|fmovies|torrent|"
    r"promo\s*code|discount\s+code|coupon|giveaway|link\s+in\s+bio|dm\s+me|"
    r"click\s+(?:here|the\s+link)|"
    r"sign\s*up\s+(?:now|today)|"
    r"buy\s+now|limited\s+offer|"
    r"crypto|onlyfans|casino|betting|rainbet"
    r"cheap\s+tickets|ticket\s+resale|"
    r"earn\s+\$|make\s+money|"
    r"mrbeast(?:'?s)?\s+crypto"
    r")\b"
)

# talks about the movie by detecting keywords that are strongly related to movie
MENTION_PATTERNS = {
    "spiderman_bnd": re.compile(
        r"spider[\s\-_]?man|spidey|brand[\s\-_]*new[\s\-_]*day|\bbnd\b", re.I),
    "odyssey": re.compile(
        r"\bodyssey\b|christopher\s+nolan|\bnolan\b|#theodyssey", re.I),
    "moana": re.compile(r"\bmoana\b", re.I),
}

# relevance keywords to make sure post is relevant about the movie
SPIDER1 = re.compile(r"spider[\s\-_]?man|spidey|peter\s+parker", re.I)
SPIDER2 = re.compile(r"brand[\s\-_]*new[\s\-_]*day|\bbnd\b", re.I)
# "odyssey" and Nolan to avoid posts about the book
ODYSSEY1 = re.compile(r"\bodyssey\b", re.I)
ODYSSEY2 = re.compile(r"\bnolan\b", re.I)
# moana and live action to avoid posts about the animated movie and moana 2
MOANA1 = re.compile(r"\bmoana\b", re.I)
MOANA2 = re.compile(
    r"live[\s\-]?action|remake|dwayne|the\s+rock|laga.?aia|disney|"
    r"\bmaui\b|\btrailer\b|\bcasting\b|\bmovie\b|\bfilm\b|\bcinema\b|\bbox\s+office\b",
    re.I,
)
MOANA_LIVE = re.compile(r"live[\s\-]?action|remake", re.I)
MOANA_2 = re.compile(r"moana\s*2", re.I)


# helper function
def get_text(post):
    return (post.get("record") or {}).get("text", "") or ""

# used for duplicate detection
def normalize(text):
    t = URL_RE.sub(" ", text.lower())
    t = re.sub(r"[^\w\s#]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def author(post):
    return (post.get("author") or {}).get("handle", "")


# load the raw data
def load_raw():
    data = {}
    for movie in MOVIES:
        folder = os.path.join(RAW_DIR, movie)
        posts = []

        for fn in sorted(os.listdir(folder)):
            if fn.endswith(".json"):
                with open(os.path.join(folder, fn), encoding="utf-8") as f:
                    posts.extend(json.load(f).get("posts", []))

        data[movie] = posts
    return data

def is_english(post):
    langs = (post.get("record") or {}).get("langs") or []
    return "en" in langs

# filters out spam
def spam_reason(post, text_copies, author_counts):
    text = get_text(post)
    if SPAM_RE.search(text):
        return "spam_keywords"
    if len(HASHTAG_RE.findall(text)) > MAX_HASHTAGS:
        return "too_many_hashtags"
    if len(URL_RE.findall(text)) > MAX_URLS:
        return "too_many_links"
    if text_copies[normalize(text)] >= IDENTICAL_COPIES_SPAM:
        return "repeated_identical_text"
    if author_counts[author(post)] > MAX_POSTS_PER_AUTHOR:
        return "author_flooding"
    return None


# 2+ movies mentioned have to be removed
def movies_mentioned(text):
    return {m for m, rx in MENTION_PATTERNS.items() if rx.search(text)}


# post has to be about the movie
def is_about_movie(movie, text):
    if movie == "spiderman_bnd":
        return bool(SPIDER1.search(text) and SPIDER2.search(text))
    if movie == "odyssey":
        return bool(ODYSSEY1.search(text) and ODYSSEY2.search(text))
    if movie == "moana":
        if not MOANA1.search(text):
            return False
        if MOANA_2.search(text) and not MOANA_LIVE.search(text):
            return False  # about the animated sequel
        return bool(MOANA2.search(text))
    return False

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    raw = load_raw()

    uri_movies = defaultdict(set)
    for movie, posts in raw.items():
        for p in posts:
            uri_movies[p.get("uri")].add(movie)

    # making a removed posts report to see how many posts are filtered out and why
    removed_log = open(os.path.join(OUT_DIR, "removed_posts.jsonl"), "w", encoding="utf-8")
    report = {}

    def remove(movie, post, reason):
        removed_log.write(json.dumps(
            {"movie": movie, "reason": reason, "uri": post.get("uri"),
             "text": get_text(post)}, ensure_ascii=False) + "\n")

    for movie in MOVIES:
        posts = raw[movie]
        rep = {"raw": len(posts)}
        reasons = Counter()


        # spam
        text_copies = Counter(normalize(get_text(p)) for p in posts)
        author_counts = Counter(author(p) for p in posts)
        kept = []
        for p in posts:
            if is_english(p):
                kept.append(p)
            else:
                remove(movie, p, "not_english")
                reasons["not_english"] += 1

        posts = kept
        rep["after_english"] = len(posts)

        # spam
        text_copies = Counter(normalize(get_text(p)) for p in posts)
        author_counts = Counter(author(p) for p in posts)

        kept = []
        for p in posts:
            r = spam_reason(p, text_copies, author_counts)
            if r:
                remove(movie, p, r)
                reasons[r] += 1
            else:
                kept.append(p)

        posts = kept
        rep["after_spam"] = len(posts)

        # dupes, keep the first
        seen_text, kept = set(), []
        for p in posts:
            key = normalize(get_text(p))
            if key in seen_text:
                remove(movie, p, "duplicate_text")
                reasons["duplicate_text"] += 1
            else:
                seen_text.add(key)
                kept.append(p)
        posts = kept
        rep["after_duplicates"] = len(posts)

        # remove the 2+ movies mention
        kept = []
        for p in posts:
            if len(movies_mentioned(get_text(p))) >= 2 or len(uri_movies[p.get("uri")]) >= 2:
                remove(movie, p, "multi_movie")
                reasons["multi_movie"] += 1
            else:
                kept.append(p)
        posts = kept
        rep["after_multi_movie"] = len(posts)

        # keep the ones that talk about the movie
        kept = []
        for p in posts:
            if is_about_movie(movie, get_text(p)):
                kept.append(p)
            else:
                remove(movie, p, "not_about_movie")
                reasons["not_about_movie"] += 1
        posts = kept
        rep["final"] = len(posts)
        rep["removed_by_reason"] = dict(reasons)
        report[movie] = rep

        with open(os.path.join(OUT_DIR, f"{movie}_filtered.json"), "w", encoding="utf-8") as f:
            json.dump({"movie": movie, "posts": posts}, f, ensure_ascii=False, indent=2)

    removed_log.close()
    with open(os.path.join(OUT_DIR, "filter_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    main()