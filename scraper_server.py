from flask import Flask, request, jsonify
import asyncio
from crawl4ai import CrawlerHub

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get("url")
    crawler_name = data.get("crawler")  # Pass which crawler to use

    if not url or not crawler_name:
        return jsonify({"error": "URL and crawler name are required"}), 400

    try:
        crawler_cls = CrawlerHub.get(crawler_name)
        if not crawler_cls:
            return jsonify({"error": f"Crawler '{crawler_name}' not found"}), 404

        crawler_instance = crawler_cls()

        result = asyncio.run(crawler_instance.run(url))

        return jsonify({"scraped": result}), 200

    except Exception as e:
        return jsonify({"error": "Failed to scrape", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)



