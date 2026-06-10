from binance.client import Client

API_KEY = "EzgIfR8msOYjCIPhy2vCF1pqudcpS7ahsXSYz05BzQHqKyKz9o2AWHtBYbfqkl9r"
API_SECRET = "Z7xY7PoyVnx5RNpmJSTVvj2m8QqAc7IfhJgV451N2s0T8jctDEbXPp43QXtL8ujq"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="LIMIT",
        quantity=0.001,
        price="50000",
        timeInForce="GTC"
    )

    print("SUCCESS!")
    print(order)

except Exception as e:
    print("ERROR:", e)