import json
import os
import random
import requests

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "expressions.json")


def load_expressions():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def format_message(expr):
    return (
        f"📚 *오늘의 영어 표현 #{expr['id']}*\n"
        f"\n"
        f"💬 *{expr['expression']}*\n"
        f"📖 뜻: {expr['meaning']}\n"
        f"✏️ 예문: _{expr['example']}_"
    )


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    expressions = load_expressions()
    expr = random.choice(expressions)
    message = format_message(expr)
    result = send_telegram_message(message)
    print(f"Sent expression #{expr['id']}: {expr['expression']}")
    print(f"Telegram response OK: {result['ok']}")


if __name__ == "__main__":
    main()
