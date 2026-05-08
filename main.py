import os
import json
import pandas as pd

from extractor import scrape_site
from cleaner import clean_text
from analyzer import analyze_website


OUTPUT_FILE = "output/results.csv"

os.makedirs("output", exist_ok=True)


def save_result(data):

    df = pd.DataFrame([data])

    file_exists = os.path.isfile(OUTPUT_FILE)

    df.to_csv(
        OUTPUT_FILE,
        mode='a',
        header=not file_exists,
        index=False
    )


def process_website(url):

    pages = scrape_site(url)

    combined_content = ""

    for page_url, content in pages.items():

        cleaned = clean_text(content)

        combined_content += f"\n\nPAGE: {page_url}\n"

        combined_content += cleaned

    analysis = analyze_website(combined_content)

    return analysis


def main():

    df = pd.read_csv("input.csv")

    for index, row in df.iterrows():

        url = row["website"]

        print("=" * 60)
        print(f"Processing: {url}")

        try:

            result = process_website(url)

            result["website"] = url

            save_result(result)

            print("Saved Successfully")

        except Exception as e:

            error_data = {
                "website": url,
                "error": str(e)
            }

            save_result(error_data)

            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
