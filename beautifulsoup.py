
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.bbc.com"
URL = BASE_URL + "/innovation/technology"
CATEGORY = "Technology"
CSV_FILE = "news.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 Chrome/120 Safari/537.36"
}


def fetch_news():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles = []
        seen = set()

        headline_tags = soup.find_all(
            attrs={"data-testid": "card-headline"}
        )

        if not headline_tags:
            headline_tags = soup.find_all(["h2", "h3"])

        for tag in headline_tags:
            headline = tag.get_text(strip=True)

            if len(headline) < 15 or headline in seen:
                continue

            seen.add(headline)

            card = tag

            for _ in range(5):
                if card.parent is None:
                    break
                card = card.parent

            time_tag = card.find("time")

            if time_tag:
                date = (
                    time_tag.get("datetime")
                    or time_tag.get_text(strip=True)
                )
            else:
                date = datetime.now().strftime("%Y-%m-%d")

            articles.append({
                "headline": headline,
                "date": date,
                "category": CATEGORY
            })

            if len(articles) == 5:
                break

        return articles

    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        return []


def save_to_csv(articles):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["headline", "date", "category"]
        )

        writer.writeheader()
        writer.writerows(articles)

    print("Data saved successfully in news.csv")


def main():
    articles = fetch_news()

    if not articles:
        print("No headlines extracted.")
        return

    for article in articles:
        print("Headline:", article["headline"])
        print("Date:", article["date"])
        print("Category:", article["category"])
        print("-" * 40)

    print("Total headlines extracted:", len(articles))

    save_to_csv(articles)


if __name__ == "__main__":
    main()
