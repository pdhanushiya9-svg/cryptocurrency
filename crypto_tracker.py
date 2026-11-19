
import requests
import pandas as pd
import webbrowser

webbrowser.open("https://www.coingecko.com/")

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": "false"
}

try:
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    coins = response.json()

    data = []

    for coin in coins:
        data.append({
            "Rank": coin.get("market_cap_rank"),
            "Name": coin.get("name"),
            "Symbol": coin.get("symbol"),
            "Price": coin.get("current_price"),
            "24h Change": coin.get("price_change_percentage_24h"),
            "Market Cap": coin.get("market_cap"),
            "Total Volume": coin.get("total_volume")
        })

    df = pd.DataFrame(data)
    df.to_csv("crypto_market_data.csv", index=False)

    print("Total Coins Scraped:", len(df))
    print("Data saved successfully!")

except requests.exceptions.RequestException as e:
    print("Connection Error:", e)
