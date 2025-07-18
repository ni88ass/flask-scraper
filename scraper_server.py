from flask import Flask, request, jsonify
from crawl4ai import CrawlerHub

app = Flask(__name__)
hub = CrawlerHub()

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

      try:
        result = hub.run(url)  # or use .execute(url) if .run doesn't exist
        return jsonify({"scraped": result}), 200

    except Exception as e:
        return jsonify({"error": "Failed to scrape", "details": str(e)}), 500


