from flask import Flask, render_template
import html
import requests

app = Flask(__name__)

# Dummy product list to simulate fetching from a Shopify store or database
# You should replace this with actual product data from Shopify or your own source
products = [
    {"title": "Wooden Stacking Toy", "link": "https://babyandtoys.us/products/wooden-stacking-toy", "description": "A classic wooden stacking toy for developing coordination and motor skills."},
    {"title": "Plush Teddy Bear", "link": "https://babyandtoys.us/products/plush-teddy-bear", "description": "Super soft and cuddly teddy bear, perfect for nap time."},
    {"title": "Colorful Baby Rattle", "link": "https://babyandtoys.us/products/colorful-baby-rattle", "description": "Engaging rattle with colors and textures to stimulate your baby’s senses."}
]

@app.route('/')
def home():
    return "Baby & Toys RSS Feed Generator is working!"

@app.route('/feed')
def feed():
    # Generate dynamic RSS feed
    feed_items = ""

    # Loop through the products and build the RSS items
    for product in products:
        feed_items += f"""
            <item>
                <title>{html.escape(product['title'])}</title>
                <link>{product['link']}</link>
                <description>{html.escape(product['description'])}</description>
            </item>
        """
    
    # Return the full RSS feed with dynamic product data
    rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>{html.escape('Baby & Toys Product Feed')}</title>
            <link>https://free-rss-feed-generator.onrender.com/</link>
            <description>{html.escape('Latest products from Baby & Toys')}</description>
            {feed_items}
        </channel>
    </rss>"""

    return rss_feed

if __name__ == '__main__':
    app.run(debug=True)
