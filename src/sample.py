import json
import os
import random

# number of posts to randomly sample from each movie
N = 167

INPUT_DIR = "filtered_data"
OUTPUT_DIR = f"{N*3}_sampled_posts"

MOVIES = ["spiderman_bnd", "odyssey", "moana"]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for movie in MOVIES:
        input_path = os.path.join(INPUT_DIR, f"{movie}_filtered.json")

        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        posts = data.get("posts", [])

        sampled = random.sample(posts, min(N, len(posts)))
        sampled = [post.get("record", {}).get("text", "") for post in sampled]

        output_path = os.path.join(OUTPUT_DIR, f"{movie}_sampled.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                {"movie": movie, "posts": sampled},
                f,
                ensure_ascii=False,
                indent=2
            )

        print(f"{movie}: sampled {len(sampled)} / {len(posts)} posts")

    print(f"\nSamples saved in '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    random.seed(42069)
    main()
