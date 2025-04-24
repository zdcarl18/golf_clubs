import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import json

# Function to scrape products from a specific URL
async def scrape_meta_products(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)

        # Get the 'meta' variable from the page
        meta_data = await page.evaluate("() => window.meta")

        await browser.close()

        if meta_data and "products" in meta_data:
            return meta_data["products"]
        else:
            return None

# Function to save the products to a CSV file
def save_products_to_csv(products, filename="products.csv"):
    df = pd.json_normalize(products)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} products to {filename}")

# Function to save the products to a JSON file
def save_products_to_json(products, filename="products.json"):
    with open(filename, "w") as f:
        json.dump(products, f, indent=2)
    print(f"Saved {len(products)} products to {filename}")

# Function to scrape multiple pages
async def scrape_multiple_pages(base_url, max_pages=2):  # ⬅ Max pages set to 2
    all_products = []
    page_number = 1

    while page_number <= max_pages:
        url = f"{base_url}?page={page_number}"
        print(f"Scraping page {page_number}...")
        products = await scrape_meta_products(url)
        
        if products:
            all_products.extend(products)
            print(f"Found {len(products)} products on page {page_number}")
        else:
            print(f"No products found on page {page_number}. Stopping.")
            break
        
        page_number += 1

    return all_products

# Run the scrape and save to CSV + JSON
if __name__ == "__main__":
    base_url = "https://www.golfclubs4cash.co.uk/collections/drivers"
    max_pages = 2  # ⬅ Scrape only up to page 2
    all_products = asyncio.run(scrape_multiple_pages(base_url, max_pages))

    if all_products:
        save_products_to_csv(all_products)
        save_products_to_json(all_products)
    else:
        print("No products found.")
