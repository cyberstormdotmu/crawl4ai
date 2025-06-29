import asyncio
from crawl4ai.async_webcrawler import AsyncWebCrawler   # import the function directly from the file, not from pypi packages.

## Steps requires to test it.
### NOTE: ALL THIS IS RAN ON THE ROOT DIRECTORY OF CRAWL4AI
# 1. create a virtual environment using `py -m venv .venv`, creates a hidden directory for virtual environment.
# 2. activate the virtual environment by running `.\.venv\Scripts\activate` (in windows), `source .venv/bin/activate` (in linux)
# 3. Install the required python pacakges by running, `pip3 install -r requirements.txt`.
# 4. run `playwright install`, this install the required packages for the headless browser to install.
# 5. run `py test.py` / `python3 test.py` (needs to be on )


async def main():
    async with AsyncWebCrawler() as crawler:

        result = await crawler.arun("https://books.toscrape.com/")
        print(result.markdown)  # Print first 300 chars

if __name__ == "__main__":
    asyncio.run(main())
