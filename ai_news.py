import time
from datetime import datetime
from duckduckgo_search import DDGS

QUERY = "artificial intelligence"
RESULTS = 10
SLEEP_SECONDS = 3600

def fetch_news():
    with DDGS() as ddgs:
        return list(ddgs.news(QUERY, max_results=RESULTS))

def main():
    while True:
        print(f"\n{datetime.now():%Y-%m-%d %H:%M:%S} - Top {RESULTS} news about '{QUERY}':\n")
        for i, res in enumerate(fetch_news(), start=1):
            print(f"{i}. {res['title']}\n   {res['url']}")
        time.sleep(SLEEP_SECONDS)

if __name__ == '__main__':
    main()
