import httpx


def notify():
    return httpx.post("https://hooks.example.com/notify", json={"ok": True}, timeout=10.0)
