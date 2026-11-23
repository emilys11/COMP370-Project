# Final Project — Role Breakdown and Status (Team 17)

**Movie: Spider-Man: Brand New Day** · **Comparison movies: Moana, The Odyssey**

**Deadline: Mon Dec 7** · Last updated: Mon Nov 23

---

## TL;DR

- **Where we are:** Data collection (Nov 20), open coding and the codebook (Nov 23) are done. Annotation is next.
- **4 roles, ~25% of the rubric each:**
  - **A, Data (Emily):** collection. **Done.**
  - **B, Codebook (Jackson):** topic design and definitions. **Done Nov 23.** Combines the final dataset after annotation.
  - **C, Analysis (Uday):** tf-idf, distributions, volume, figures. Nov 25–30.
  - **D, Report (Maryam):** framing, Discussion, editing. Nov 30–Dec 4.
- **Everyone labels by hand:**
  - Open coding: 200 posts, done by Jackson (8 topics).
  - Annotation: ~70 posts each (281 rows in `annotation/annotation.csv`), committed through GitHub.
- **Each person writes the report section for their own rubric rows.** D merges everything into one voice.
- **No LLM annotation.** All labels are assigned by us. AI is only for assistance (debugging, editing), and we must disclose it.
- **Report format:** a Word document (`COMP370_Team17_Report.docx`) that follows the AAAI template.

---

## 1. The task

Write a 5–7 page AAAI-format report that answers two questions:

1. **What aspect of Spider-Man: Brand New Day is each post about?** This is the topics question.
2. **How much coverage did it get compared to Moana and The Odyssey?** This is the volume question.

Only the report is graded. Anything not written down counts as not done.

**Decisions already made:**

- **Platform:** Bluesky, which has a public API and keyword search. Reddit's API is closed to new users, and YouTube would need an extra step to find relevant videos.
- **Window:** 10 days after each movie's release, English only, same for every movie.
- **Search terms:** "Nolan" added for The Odyssey and "live-action" added for Moana, so the searches don't match the book or the animated film.
- **Dataset:** 501 posts sampled at random, 167 per movie (`data/501_sampled_posts`).

## 2. Who owns which rubric points

| Rubric row | Pts | Owner | Report section |
|---|---|---|---|
| Data collection | 10 | **A** (Emily) | Data |
| Annotation quality | 10 | **A** (process) | Methods |
| Topic design | 15 | **B** (Jackson) | Methods |
| Topic validity | 15 | **B** (Jackson) | Results (topic table) |
| Results: distribution + tf-idf | 20 | **C** (Uday) | Results |
| Style: figures | 5 | **C** (Uday) | — |
| Findings | 20 | **D** (Maryam) | Discussion |
| Style: text | 5 | **D** (Maryam) | All |

## 3. Roles

### A — Data (Emily) — DONE Nov 20

- Collected 10 days of Bluesky posts per movie, saved as raw JSON per day (`data/raw_data`).
- **Filtering** (`data/filtered_data`):
  - English only.
  - Removed spam, duplicates, "author flooding" and posts mentioning 2 or more of the compared movies.
  - Removed posts not actually about the movie.
- **Counts:**

| Movie | Raw | Filtered |
|---|---|---|
| Spider-Man: Brand New Day | 6,596 | 4,136 |
| The Odyssey | 4,540 | 3,162 |
| Moana | 1,004 | 684 |

- **Spot-check:** 50 posts per movie, 100% relevant (`data/150_sampled_posts`).
- **Sampling:** 167 posts per movie, random, fixed seed (`data/501_sampled_posts`).
- **Still to do:**
  - Fill in the README's "Sampling decisions" section.
  - Write the limitations **explicitly** (the rubric gives 5 pts for data that is "explicitly aware of its limitations"):
    - the query terms differ per movie ("Nolan", "live-action"), which can bias volume against those movies;
    - the movies were released on different dates (Moana Jul 10, The Odyssey Jul 17, Spider-Man Jul 31);
    - Moana has the smallest sample;
    - the author-flooding and spam filters remove posts unevenly across movies;
    - Bluesky users are not representative of moviegoers.
  - Write the Data section and the annotation-process paragraph in Methods.

### B — Codebook (Jackson) — DONE Nov 23

- **Open coding** on 200 random posts from the 501 (all three movies): free-text labels, merged into **8 topics**. Each post is in exactly one topic.
- **Topics:** Verdict, Adaptation, Story and craft, Release and promotion, Cast, Box office, Viewing experience, Not about the film.
- **Codebook** (`annotation/codebook.md`): for each topic a definition, examples that fit and don't fit, and edge cases, plus a tie-break rule.
- **"Other" is small:** Not about the film is under 5% of the open-coded posts.
- **Annotation:** the 281 remaining posts are in `annotation/annotation.csv`, grouped by person. Each person labels their rows and makes one commit.
- **Still to do:** combine all 501 labelled posts into `data/annotated/final_dataset.csv` after annotation.
- **Writes:**
  - The topic design process in Methods.
  - The topic definition table in Results.

### C — Analysis (Uday) — Nov 25–30

- **Volume comparison** (can start now, using the filtered data): post counts per movie, plus a volume-over-time plot.
- **Topic distribution:** counts and % per topic, from `data/annotated/final_dataset.csv` (after annotation is done).
- **Topic engagement:** the handout's Results section asks for it. The filtered data has `likeCount`, `repostCount`, `replyCount` and `quoteCount` per post, and all 501 sampled posts match back to them by text. Report engagement per topic (e.g. mean likes and reposts), and say how you defined it.
- **tf-idf:**
  - Top 10 words per topic.
  - State the preprocessing (e.g. stopwords, whether the movie title was removed).
  - Explain any odd words.
- **LLM summary of each topic:** record the **model name and exact prompt**.
- **Figures:** 2–3 useful figures only. The rubric deducts points for "fluffy" images.
- **Writes:** the Results section.

### D — Report (Maryam) — Nov 30–Dec 4

- Set up the report document and follow the AAAI formatting strictly.
- **Writes:**
  - The Introduction.
  - The Discussion: **2 big-picture points and a conclusion**, each tied to specific numbers from Results.
  - **Integration (5 pts):** connect the results to prior knowledge, such as the movies' marketing, reviews and box office, and cite real references.
  - Group contributions.
  - The AI disclosure.
- **Final editing:** one voice, grammar, and a page count of 5–7.

## 4. Shared work (everyone)

| Task | Per person |
|---|---|
| Open coding | Jackson, 200 posts |
| Annotation | ~70 rows each in `annotation/annotation.csv` (Jackson 71, the others 70), one commit each |
| Peer review of another role's section | 1 section |
| Log any AI use (tool + what for) | ongoing |

## 5. Timeline

| Dates | Milestone | Owner | Status |
|---|---|---|---|
| Nov 9–12 | Repo, project option, movie and roles chosen | All | Done |
| Nov 18–20 | Collect, filter and sample the data | A | Done |
| Nov 22–23 | Open coding of 200 posts, 8 topics, codebook | B | Done |
| Nov 24–25 | Annotate the 281 posts (deadline Nov 25, 11:59 PM) | All | |
| Nov 26 | Combine into `data/annotated/final_dataset.csv` so Uday can start | B | |
| Nov 25–30 | Volume plot (can start now); topic distribution, tf-idf, LLM summaries, figures from Nov 26 | C | |
| Nov 30–Dec 4 | Write and merge the report; each person's sections in by Dec 1 | D (+all) | |
| Dec 5–7 | Review and **submit by Dec 7** | All | |

Weekly 30-min check-in, plus a group chat.

## 6. Open issues

- **Topic scope:** The handout doesn't say whether topics cover only Spider-Man or all three movies. We went with all three. Confirm with the TA.
- **The 20 test-round posts:** They are part of the 501 but not in `annotation.csv`, so nobody is assigned to label them. Add them to the CSV or the final dataset will have 481 posts.
- **No test round:** We dropped the group agreement check. The rubric gives points for a sound annotation process, so the Methods section should say what we did instead.
- **Annotation deadline:** Nov 25, 11:59 PM, so Uday can start the topic results on Nov 26.
- **README gaps:** "Sampling decisions" and limitations are not written yet (Emily).
- **Original Dec 1 target:** Replaced by the Nov 11 role deadlines (Report ends Dec 4, review Dec 5–7).

## 7. Final checklist

- [x] Platform chosen and justified, raw data saved.
- [x] Filtering done and counts recorded.
- [x] Relevance spot-check reported (50 posts per movie).
- [x] Open coding done, 8 topics, codebook written.
- [ ] Data section has the counts, filters, time window and limitations.
- [ ] Methods explains how the topics were built, including the merge and how annotation was done.
- [x] Every topic has a definition, and "other" is small and explained.
- [ ] Top-10 tf-idf words per topic.
- [ ] LLM summaries with the model name and the prompt.
- [ ] Volume comparison uses the same windows for every movie.
- [ ] Discussion has 2 big-picture points and a conclusion backed by numbers.
- [ ] Figures are clear and necessary.
- [ ] AAAI format; 5–7 pages (excluding references and the AI disclosure).
- [ ] Group contributions and AI disclosure are included.

---

## 8. Rubric coverage check (against the handout)

| Rubric row (pts) | What earns full marks | Covered by |
|---|---|---|
| Style: text (5) | Clear, concise, good grammar | D edits all sections; each person proofreads a peer's section |
| Style: figures (5) | Easy to understand; no fluffy images | C: 2–3 figures only (topic distribution, volume over time, maybe engagement) |
| Data collection (10) | Works, and **explicitly aware of limitations**; sampled without bias | A: Data section with the limitations list above; same window and filters for all movies |
| Topic design (15) | A process that clearly produces valid topics; missing detail counts as not done | B: Methods paragraph covering the 200-post open coding, merge and the 8 topics |
| Topic validity (15) | Definitions, suitable topics, minimal subjectivity, careful "other" | B: codebook with examples, edge cases, tie-break; small "other" |
| Annotation quality (10) | A sound process in line with the class | A + B: codebook with examples and rules, hand labels only, single annotation |
| Results (20) | Topic distribution (10) and tf-idf characterization (10), plus engagement and LLM summaries; explain outliers | C |
| Findings (20) | 2 big-picture points (5 each), conclusion (5), integration with prior knowledge (5) | D |

Not graded for COMP 370: double annotation, kappa, classifiers, statistical tests (graduate only).
