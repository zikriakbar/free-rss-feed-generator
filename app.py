from flask import Flask, render_template, Response

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return "✅ Baby & Toys RSS Feed Generator is working!"

# RSS feed route
@app.route('/feed')
def rss_feed():
    products = [
        {
            "title": "Wooden Stacking Toy",
            "url": "https://babyandtoys.us/products/wooden-stacking-toy",
            "description": "A classic wooden stacking toy for developing coordination and motor skills."
        },
        {
            "title": "Plush Teddy Bear",
            "url": "https://babyandtoys.us/products/plush-teddy-bear",
            "description": "Super soft and cuddly teddy bear, perfect for nap time."
        },
        {
            "title": "Colorful Baby Rattle",
            "url": "https://babyandtoys.us/products/colorful-baby-rattle",
            "description": "Engaging rattle with colors and textures to stimulate your baby’s senses."
        }
    ]

    rss_xml = render_template("rss.xml", products=products)
    return Response(rss_xml, mimetype='application/rss+xml')

if __name__ == '__main__':
    app.run(debug=True)
