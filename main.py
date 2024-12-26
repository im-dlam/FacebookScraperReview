from flask import Flask, request, jsonify
import time
from scrape import ReviewScrape

app = Flask(__name__)

# Bộ nhớ tạm để lưu thời gian gọi API lần gần nhất
last_request_time = {}

# Helper function to scrape Facebook reviews
def scrape_facebook_reviews(url):
    # Placeholder for scraping logic
    # For now, simulate with dummy data
    if "facebook.com" not in url or "reviews" not in url:
        return []  # Return empty for non-business or no reviews

    # Simulated scraped data
    reviews = ReviewScrape().run(url)
    return reviews

@app.route('/FacebookScraper', methods=['GET'])
def facebook_scraper():
    global last_request_time
    url = request.args.get('url')

    if not url:
        return jsonify({"error": "No URL provided."}), 400

    # Kiểm tra khoảng thời gian kể từ lần gọi gần nhất
    current_time = time.time()
    if url in last_request_time and current_time - last_request_time[url] < 1:
        return jsonify({"error": "Requests are limited to 1 per second per URL."}), 429

    # Cập nhật thời gian gọi API
    last_request_time[url] = current_time

    # Xử lý scrape
    reviews = scrape_facebook_reviews(url)

    if not reviews:
        return jsonify([]), 200  # Return empty list if no reviews or invalid page

    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5076)
