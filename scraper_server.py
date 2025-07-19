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
        result = hub.crawl(url)
        return jsonify({"scraped": result}), 200
    except Exception as e:
        return jsonify({"error": "Failed to scrape", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)



