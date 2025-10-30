# api/index.py (Vercel 無伺服器函式)

from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 本地 Flask 伺服器的 URL（請改為您的公網 IP 或動態域名）
LOCAL_SERVER_URL = os.environ.get("LOCAL_SERVER_URL") or "http://114.35.41.49:5000"

@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    if request.method == "POST":
        # 將請求內容轉發給本地儲存伺服器
        try:
            res = requests.post(LOCAL_SERVER_URL, json=request.get_json())
            return "OK"
        except Exception as e:
            print("轉發至本地伺服器時出錯：", e)
            return "Error", 500
    else:
        # 非POST請求的簡單回應
        return "Hello, this is a LINE Bot webhook endpoint."
