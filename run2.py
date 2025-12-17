from app.logging_config import setup_logging
from app import create_app

setup_logging()   # ⬅ BẮT BUỘC

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
l