from flask import Flask, Response
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SHOP = "babyandtoys.us"
API_VERSION = "2024-04"
ACCESS_TOKEN = os.getenv("dd1807435fd5b0a34bf83637687473df-1745238790")

@app.route("/")
def home():
    return "✅ Baby & Toys RSS Feed Generator is working!"

@app.route("/rss.xml")
def rss_feed():
    headers = {
        "X-Shopify-Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    url = f"https://{SHOP}/admin/api/{API_VERSION}/products.json?published_status=published"
    response = requests.get(url, headers=headers)
    products = response.json().get("products", [])

    rss_items = ""
    for product in products:
        title = product['title']
        link = f"https://{SHOP}/products/{product['handle']}"
        description = product.get('body_html', '')
        rss_items += f"""
        <item>
            <title>{title}</title>
            <link>{link}</link>
            <description><![CDATA[{description}]]></description>
        </item>
        """

    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>Baby and Toys Product Feed</title>
            <link>https://{SHOP}</link>
            <description>Latest published products from Baby and Toys</description>
            {rss_items}
        </channel>
    </rss>"""

    return Response(rss, mimetype='application/rss+xml')
