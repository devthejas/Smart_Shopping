import requests
import pandas as pd
import time
import random
from typing import List, Dict

# --- CONFIGURATION: Replace these with your real API keys ---
SERPAPI_API_KEY = "YOUR_SERPAPI_KEY_HERE"
FLIPKART_AFFILIATE_ID = "YOUR_FLIPKART_AFFILIATE_ID"
FLIPKART_AFFILIATE_TOKEN = "YOUR_FLIPKART_AFFILIATE_TOKEN"
FLIPKART_API_BASE = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json"


def fetch_from_serpapi_amazon(item: str) -> Dict:
    """Fetch product info for `item` from Amazon via SerpApi."""
    params = {
        "api_key": SERPAPI_API_KEY,
        "engine": "amazon",
        "k": item,
    }
    try:
        resp = requests.get("https://serpapi.com/search", params=params, timeout=10)
        data = resp.json()
        organic = data.get("organic_results", [])
        if not organic:
            return None
        first = organic[0]
        price = first.get("extracted_price") or first.get("price")
        link = first.get("link")
        if not price or not link:
            return None
        try:
            price_num = float(str(price).replace("₹", "").replace(",", "").strip())
        except ValueError:
            return None

        return {"item": item, "store": "Amazon", "price": price_num, "link": link}
    except Exception as e:
        print(f"⚠️ Amazon fetch failed for {item}: {e}")
        return None


def fetch_from_flipkart_affiliate(item: str) -> Dict:
    """Fetch product info for `item` from Flipkart Affiliate API."""
    params = {"query": item, "affiliateId": FLIPKART_AFFILIATE_ID}
    headers = {"Fk-Affiliate-Token": FLIPKART_AFFILIATE_TOKEN}
    try:
        resp = requests.get(FLIPKART_API_BASE, params=params, headers=headers, timeout=10)
        data = resp.json()
        product_list = data.get("productInfoList", [])
        if not product_list:
            return None

        base = product_list[0].get("productBaseInfo", {})
        price_info = base.get("flipkartSpecialPrice", {}) or base.get("flipkartSellingPrice", {})
        price_str = price_info.get("amount")
        link = base.get("productUrl")
        if not price_str or not link:
            return None

        return {"item": item, "store": "Flipkart", "price": float(price_str), "link": link}
    except Exception as e:
        print(f"⚠️ Flipkart fetch failed for {item}: {e}")
        return None


def fetch_prices(item_list: List[str]) -> List[Dict]:
    """
    Fetch prices for all items from Amazon and Flipkart.
    Falls back to local mock data if APIs fail.
    """
    results = []

    for item in item_list:
        # Fetch from Amazon
        res_amz = fetch_from_serpapi_amazon(item)
        if res_amz:
            results.append(res_amz)

        # Fetch from Flipkart
        res_fk = fetch_from_flipkart_affiliate(item)
        if res_fk:
            results.append(res_fk)

        # Delay to prevent rate-limit issues
        time.sleep(random.uniform(1, 2))

    # --- Fallback: if no API results, load mock CSV ---
    if not results:
        print("⚠️ No API data found — loading fallback mock dataset.")
        try:
            data = pd.read_csv("data/sample_data.csv")
            results = data.to_dict(orient="records")
        except Exception as e:
            print("❌ Failed to load mock data:", e)
            # Generate random placeholders
            results = [
                {"item": item, "store": "FallbackStore", "price": random.uniform(50, 500), "link": "#"}
                for item in item_list
            ]

    return results
