from playwright.async_api import async_playwright
import asyncio


async def scrape_page(page, url):

    try:

        await page.goto(url, timeout=60000)

        await page.wait_for_timeout(3000)

        content = await page.content()

        return content

    except Exception as e:

        print(f"Failed to scrape {url}: {e}")

        return ""


async def scrape_site_async(base_url):

    data = {}

    async with async_playwright() as playwright:

        browser = await playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = await browser.new_page()

        urls_to_visit = [
            base_url,
            f"{base_url}/about",
            f"{base_url}/services",
            f"{base_url}/industries",
            f"{base_url}/who-we-help",
            f"{base_url}/clients",
            f"{base_url}/solutions"
        ]

        for url in urls_to_visit:

            print(f"Scraping: {url}")

            content = await scrape_page(page, url)

            if content:
                data[url] = content

        await browser.close()

    return data


def scrape_site(url):

    return asyncio.run(scrape_site_async(url))
