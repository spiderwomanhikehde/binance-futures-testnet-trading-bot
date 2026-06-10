import argparse

from client import get_client
from validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from logging_config import logger


def place_market_order(client, symbol, side, quantity):

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )


def place_limit_order(client, symbol, side, quantity, price):

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and args.price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        logger.info(
            f"Order Request | {symbol} | {side} | "
            f"{order_type} | Qty={quantity}"
        )

        client = get_client()

        if order_type == "MARKET":

            response = place_market_order(
                client,
                symbol,
                side,
                quantity
            )

        else:

            response = place_limit_order(
                client,
                symbol,
                side,
                quantity,
                args.price
            )

        logger.info(f"API Response: {response}")

        print("\n========== ORDER RESPONSE ==========")

        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Average Price :", response.get("avgPrice", "N/A"))

        print("\nSUCCESS")

    except Exception as e:

        logger.error(str(e))

        print("\nFAILED")
        print("Error:", e)


if __name__ == "__main__":
    main()