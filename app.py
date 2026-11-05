from flask import Flask
import os
import redis

app = Flask(__name__)

mode = os.getenv("MODE", "dev")
port = int(os.getenv("PORT", "5000"))
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("hits")
    return f"Hello! mode={mode}, hits={count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)