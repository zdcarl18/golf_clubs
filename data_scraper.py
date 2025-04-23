from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# Set up headless Chrome browser
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

BASE_URL = "https://www.golfclubs4cash.co.uk/collections/driver?page={}"

def scrape_golfclubs4cash(pages=2):
    all_data = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        print(f"Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for JS to render

        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = soup.select("div.product-card")

        print(f"🧪 Found {len(products)} products")

        for product in products:
            try:
                name_tag = product.select_one(".product-card__title")
                name = name_tag.get_text(strip=True) if name_tag else "Unknown"

                price_tag = product.select_one(".price")
                price_text = price_tag.get_text(strip=True).replace("£", "") if price_tag else ""
                price = float(price_text.replace(",", "")) if price_text else None

                image_tag = product.select_one("img")
                image_url = image_tag["src"] if image_tag else ""

                all_data.append({
                    "name": name,
                    "type": "driver",
                    "brand": name.split()[0],
                    "price": price,
                    "description": name,
                    "image_url": image_url
                })

            except Exception as e:
                print(f"⚠️ Error extracting product: {e}")

    return all_data

def save_to_csv(data, filename="data/golfclubs4cash_drivers.csv"):
    if not data:
        print("⚠️ No data to save.")
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Saved {len(data)} clubs to {filename}")

if __name__ == "__main__":
    data = scrape_golfclubs4cash(pages=2)
    save_to_csv(data)
    driver.quit()
