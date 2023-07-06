import webbrowser
import random

# List of 20 random search queries
search_queries = [
    "cat videos",
    "recipe for chocolate cake",
    "top tourist destinations",
    "best programming languages",
    "world news today",
    "funny memes",
    "popular movies",
    "healthy dinner recipes",
    "DIY home improvement",
    "latest technology trends",
    "famous quotes",
    "fitness tips",
    "music playlist",
    "travel hacks",
    "book recommendations",
    "interesting facts",
    "art inspiration",
    "sports highlights",
    "financial planning",
    "celebrity gossip"
]

# Open 20 random searches in browser tabs
for _ in range(20):
    random_query = random.choice(search_queries)
    url = f"https://www.bing.com/search?q={random_query}"
    webbrowser.open_new_tab(url)
