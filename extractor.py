from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin


IMPORTANT_PATHS = [
    "",
    "/about",
    "/services",
    "/solutions",
    "/case-studies",
    "/testimonials",
    "/faq",
]


def scrape_site(base_url):
    pages = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        for path in IMPORTANT_PATHS:

            try:
                url = urljoin(base_url, path)

                print(f"Visiting: {url}")

                page.goto(url, timeout=60000)

                page.wait_for_timeout(3000)

                html = page.content()

                soup = BeautifulSoup(html, "lxml")

                text = soup.get_text(separator=" ", strip=True)

                pages[url] = text

            except Exception as e:
                print(f"Failed: {url} -> {e}")

        browser.close()

    return pages
