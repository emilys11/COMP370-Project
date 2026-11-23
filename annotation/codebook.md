# Codebook

**Spider-Man: Brand New Day, The Odyssey, Moana**

## 1. Motivation and context

A media company wants to know how people reacted to a movie on social media, and how much attention it got compared with other movies released around the same time. The first part of that is a question about topics: *what aspect of the movie is each post about?* Some people write about the acting, some about the money it made, some just say whether they liked it. To count how much of each there is, every post has to be given one label, and the labels have to mean the same thing no matter who assigns them.

This codebook is the set of labels and the rules for using them. We built it by open coding: Jackson read 200 randomly chosen posts, wrote down what each one was about in his own words, and then merged those labels into the 8 types below.

**The data:** 501 English Bluesky posts, 167 per movie (Spider-Man: Brand New Day, The Odyssey, Moana), taken from the first 10 days after each release and filtered for spam, duplicates and relevance. A post is the text only; we don't follow links.

## 2. Overview of the types

Every post gets **exactly one** type. The 8 types fall into four groups:

| Group | Types | What they have in common |
|---|---|---|
| About the film itself | Verdict, Story and craft, Cast, Adaptation | The post talks about the film's content or how it came to be |
| About the film as a product | Box office, Release and promotion | The post talks about money, marketing or the release |
| About watching it | Viewing experience | The post talks about the act of watching, not the film |
| Outside the film | Not about the film | The title shows up, but the post isn't about the film |

**How the types relate.** Verdict is the broad one: an overall opinion. The other types in the first group are specific things a post can focus on. If a post focuses on one specific thing, that specific type wins over Verdict. Verdict is for posts that give a general opinion without going into one particular aspect.

**Posts that could fit two types.** Label the post by its main point, meaning what the poster most wants to say. If two things are equally prominent, use the one mentioned first. A post whose main content is plans or excitement about going to see the film is Release and promotion.

---

## 3. The types

### Verdict

**Definition:** Overall judgment of the film after seeing it: loved it, hated it, a rating, a short review, or a quality comparison to other films ("best since Spider-Man 2").

**Fits**
- "...it was very, very good. Probably one of the better Marvel movies in some time." (plain verdict)
- "live action moana is just painful to watch." (judgment of the whole film)
- "I thought THE ODYSSEY was a solid 7 out of 10." (a rating)

**Doesn't fit**
- "I loved Tom Holland's performance in this movie..." (the acting, so Cast)
- "Nolan doesn't write good dialogues... He is great with visuals..." (writing and visuals, so Story and craft)
- "I'm about to see the Moana live action remake." (hasn't seen it, so Release and promotion)

**Edge cases**
- Praise or criticism of one specific thing goes to that thing's type. Praising everything at once ("the story, the writing, the directing, the cast...") is Verdict.
- "It flopped because it's bad" is Verdict only if quality is the point; otherwise it's Box office.
- Continuity, lore or faithfulness to a source is Adaptation, not Verdict.
- A bare "watched it" with no opinion is Viewing experience.

### Adaptation

**Definition:** The film as a remake, adaptation, sequel or franchise entry: faithfulness to the source, continuity with earlier films, why it was made, what it changed.

**Fits**
- "in the live action she just stood there... a stain on the original artist's hard work" (judged against the original)
- "who was this movie for? The answer? The Rock." (why the remake exists)
- "five of the major differences between Spider-Man BND the movie and the comic event" (film versus source)

**Doesn't fit**
- "Nolan follows a non-linear structure... His voyage is then told in flashbacks." (plot on its own terms, so Story and craft)
- "The third act of The Odyssey is one of all time greatest payoffs in film history." (ending on its own terms, so Story and craft)

**Edge cases**
- Plot or ending judged on its own merits is Story and craft, even if the source is mentioned. It's Adaptation when the main point is faithfulness, changes or why it was made.
- Complaints about the remake from people who haven't seen it ("who asked for this?") are still Adaptation.

### Story and craft

**Definition:** The plot, themes and ending; writing and dialogue; and how the film looks and sounds (directing, music, score, cinematography, effects), judged on its own merits.

**Fits**
- "Nolan follows a non-linear structure... His voyage is then told in flashbacks." (how the story is told)
- "...IMAX 70mm format it was meant to be experienced in... The picture. The SOUND." (how it looks and sounds)
- "i have some thoughts on the score" (the score)
- "Nolan doesn't write good dialogues since... ever." (writing and dialogue)

**Doesn't fit**
- "those saying Nolan weakened the hero have never read the epic poem" (judged against the source, so Adaptation)
- "Lin-Manuel Miranda on Writing the Song 'Along The Way' in a Week..." (an interview, so Release and promotion)
- "#JustWatched Spider-Man: Brand New Day" (watch log, so Viewing experience)

**Edge cases**
- Interviews are press (Release and promotion), but the director's or composer's choices in the film are Story and craft.
- The picture and sound of the film itself are Story and craft. Projection problems, ads and audience behavior are Viewing experience.

### Release and promotion

**Definition:** Marketing, press, trailers, interviews, merchandise, behind-the-scenes and production news, and anticipation before seeing it ("can't wait", "seeing it Sunday").

**Fits**
- "I'm about to see the Moana live action remake. Wish me luck!" (anticipation)
- "compilation of the clips, interviews, premieres and behind the scenes footage from the global press tour" (press)
- "I'm seeing spider-man brand new day on Sunday!" (anticipation)

**Doesn't fit**
- "PLEASE stop letting Christopher Nolan have final say the audio mixing!" (director's choices in the film, so Story and craft)
- "it's like Spider-Man 2 levels good." (has seen it, so Verdict)

**Edge cases**
- Seen it means Verdict. Hasn't seen it and the main point is plans or excitement means Release and promotion.
- People who haven't seen the film but argue about money, casting or the remake keep those types.

### Cast

**Definition:** Who is in the film: casting choices, cameos, specific roles and the acting.

**Fits**
- "Sadie Sink's (not so) secret role in 'Spider-Man: Brand New Day'" (a specific role)
- "Christopher Nolan cast a Black actress..." (a casting choice)
- "I loved Tom Holland's performance." (the acting)

**Doesn't fit**
- "...The picture. The SOUND." (how it looks and sounds, so Story and craft)
- "Nolan doesn't write good dialogues since... ever." (writing, so Story and craft)

**Edge cases**
- Actors, casting and cameos are Cast. Directing, writing and dialogue are Story and craft.

### Box office

**Definition:** Money: opening weekend, budget, records, flops.

**Fits**
- "scores opening weekend record with $360 million, topping 'Avengers: Endgame'" (money and records)
- "opened with $43M at the domestic box office. The film had a reported $250M budget." (money)

**Doesn't fit**
- "them CGI-ing out Dwayne's nipples is the main reason why it's flopping" (the point is the CGI, so Story and craft)
- "live action moana is just painful to watch... NO WAY IN HELL that i'm watching this in a theater" (judgment, no money, so Verdict)

**Edge cases**
- A post that mentions a flop but argues about the cause takes the cause's type.

### Viewing experience

**Definition:** Watching the film, not the film itself: watch logs and bare titles with no opinion, theater anecdotes, ads, projection problems, audience behavior.

**Fits**
- "#JustWatched Spider-Man: Brand New Day #FilmSky" (watch log)
- "Since when did they start showing ads (not movie previews) during the previews???" (about the cinema)
- "breaking off the projector twice, then restarted on slightly misaligned DCP" (a projection problem)

**Doesn't fit**
- "...The picture. The SOUND." (the film's own picture and sound, so Story and craft)
- "my favorite #SpiderMan film since #SpiderMan2" (a verdict, so Verdict)

**Edge cases**
- "Watched it, loved it" is Verdict. A bare log is Viewing experience.
- A cinema story that mainly makes a point about the film ("it was so good I cried") is Verdict.

### Not about the film

**Definition:** Uses the title but has no film content and isn't about watching it: gaming, memes or jokes with no point about the film, self-promotion, unrelated conversation.

**Fits**
- "POST SPIDER-MAN: BRAND NEW DAY GAMING! | Marvel's Spider-Man 2 Continuing my Spider-man 2 playthrough" (a video game)
- "So does anyone want me on a podcast to talk about Spider-man: Brand New Day?" (self-promotion)
- "I pulled wayyy back and did a grand total of 3 signings" (a comic signing)

**Doesn't fit**
- "Watched The Odyssey (d. Nolan, w. Nolan, Homer)" (bare watch log, so Viewing experience)
- "Tom Holland left a hand-written message for the crew" (behind-the-scenes, so Release and promotion)
- "the CGI'd off nipples of The Rock go in the live action Moana remake" (a joke about the CGI, so Story and craft)

**Edge cases**
- A joke or meme that makes a point about the film keeps that type. One with no point lands here.
- Only for posts with no film content and no viewing experience.

---

## 4. Evidence that the types cover the data

We open coded 200 random posts from the dataset, and every one fit one of the 8 types. Not about the film holds under 5% of them.

| Type | Posts | Share |
|---|---|---|
| Verdict | 44 | 22% |
| Adaptation | 42 | 21% |
| Story and craft | 36 | 18% |
| Release and promotion | 25 | 12.5% |
| Cast | 18 | 9% |
| Box office | 16 | 8% |
| Viewing experience | 10 | 5% |
| Not about the film | 9 | 4.5% |
