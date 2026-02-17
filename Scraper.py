import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"

if __name__ == "__main__":
    try:
        response = requests.get(URL)
        if response.status_code != 200:
            print("Failed to retrieve webpage.")
            exit()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h2")
        extracted_titles = []
        for tag in headlines:
            title = tag.get_text(strip=True)
            if title and title not in extracted_titles:
                extracted_titles.append(title)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            for index, title in enumerate(extracted_titles, start=1):
                file.write(f"{index}. {title}\n")
        print(f"{len(extracted_titles)} headlines saved to {OUTPUT_FILE}")
    except Exception as e:
        print("Error occurred:", e)