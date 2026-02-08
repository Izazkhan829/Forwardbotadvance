from flask import Flask
import subprocess
import os
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

# Start bot using the SAME python interpreter
subprocess.Popen([sys.executable, "bot.py"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
