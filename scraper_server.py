from crawl4ai import CrawlerHub
from flask import Flask, request, jsonify

app = Flask(__name__)
hub = CrawlerHub()

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    result = hub.crawl(url)
    return jsonify({"scraped": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


