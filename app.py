from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

def run_bot():
    import bot  # or main, whichever starts the bot

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
