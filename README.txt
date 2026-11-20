# Data collection files:
1. extraction.py collects raw posts and stores them in raw_data
2. filter.py filters the posts to make sure they are relevant about the movie and stores them in filtered_data
3. sample.py randomly samples N posts and stores them in N_sampled_posts

# Why Bluesky?
- Bluesky provides a public and accessible API, making it easy and convenient to retrieve posts for the raw dataset.
- Bluesky supports searches using specific keywords, so it's possible to retrieve posts relevant to the movies.
  This was particularly useful for The Odyssey and Moana (live-action), since the search of these titles could be confused with the original book and animated film, respectively.
  By including additional keywords such as "Nolan" and "live-action", the searches are narrowed down to posts about the movies we are looking for.
- It was also a process of elimination. Other platforms were considered but presented additional challenges that Bluesky doesn't have.
  YouTube's API was not selected because collecting relevant comments would first require identifying relevant videos, adding an extra step to the data collection and filtering process.
  Reddit's API was not selected because Reddit no longer accepts new Data API access requests.

# Design decisions made for collection:
- Using keyword search queries to retrieve posts possibly related to the movies. For Odyssey, we want the director keyword "Nolan" included. For Moana, it would be "live-action"
- The collection period is the next 10 days after the movies' release date. This helps to find posts while the movie is recently out, so we avoid irrelavant discussions from
  an unlimited time range.
- With Bluesky, it is possible to filter the English only posts during the raw collection process.
- Use pagination to collect more than 100 posts because 100 posts is the per-request limit on Bluesky.

# What was filtered and how?
- Removal of posts suspected to be spam/scams : Searching for certain keywords like "free streaming" and "betting", seeing if there are too many links/hashtags
- Removal of a duplicate post: compares posts to see if they are exactly the same, removes one of them
- Removal of posts that talk about 2+ of the compared movies: If keywords from different movies appear in the same post, it is removed.
- Removal of irrelevant posts: If the posts do not contian any of the desired keywords that signal relevance to the movie, it is removed.
- Detecting relevant posts: mentions of the title of the movie, famous actors/directors featured in the movie

# Sampling decisions:


# Data collection statistics:
- Number of raw posts collected for spiderman: 6596
- Number of raw posts collected for odyssey: 4540
- Number of raw posts collected for moana: 1004

- Number of filtered posts for spiderman: 4136
- Number of filtered posts for odyssey: 3162
- Number of filtered posts for moana: 684

- % Relevancy of posts for spider-man in a sample of 50: 100%
- % Relevancy of posts for odyssey in a sample of 50: 100%
- % Relevancy of posts for moana in a sample of 50: 100%
