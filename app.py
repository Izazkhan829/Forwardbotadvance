from flask import Flask
import subprocess
import sys, os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

# Start the bot using the correct entrypoint
subprocess.Popen([sys.executable, "main.py"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
