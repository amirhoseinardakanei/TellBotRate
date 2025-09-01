from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/send", methods=["POST"])
def send_message():
    try:
        data = request.json
        text = data.get("text") if data else None

        if not text:
            return jsonify({"error": "No text provided"}), 400

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        resp = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text}, timeout=10)

        # برگردوندن پاسخ تلگرام برای دیباگ
        return jsonify({
            "status_code": resp.status_code,
            "telegram_response": resp.json()
        }), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
