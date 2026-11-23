# Annotation

Everything for labelling the posts with topics.

## Files

- `codebook.md`: the 8 topics and how to use them. Read this first.
- `annotation.csv`: the posts to label (281 rows).
- `open_coding/open_coding.csv`: the 200 posts we used to build the codebook.
- `../data/annotated/`: where the final labelled dataset goes.

## How to annotate

1. Clone the repo (or `git pull` if you already have it).
2. Read `annotation/codebook.md`.
3. Open `annotation/annotation.csv`. Your rows are the ones with your name in `assigned_to` (Jackson 71, Emily 70, Uday 70, Maryam 70).
4. For each of your rows, type one topic in the `topic` column. Use the exact names: `Verdict`, `Adaptation`, `Story and craft`, `Release and promotion`, `Cast`, `Box office`, `Viewing experience`, `Not about the film`.
5. Don't change ids, post text, anyone else's rows, or the order of the file.
6. When all your rows are done, make one commit (for example "Annotate Emily's posts") and push.

**Deadline:** Nov 25, 11:59 PM

## Rules

- One topic per post. Use the post text only, not links.
- Label by hand. No LLMs. If you use AI for anything else, write down what for.

## After annotation

Jackson combines all 501 labelled posts into `data/annotated/final_dataset.csv`.
