"""
Stub module for cryptocurrency exchange API integration.

This module contains placeholder functions representing operations 
to interact with a cryptocurrency exchange, such as placing and 
retrieving orders. It currently returns mock data and can be extended 
to integrate with real exchange APIs.
"""


def get_current_price(symbol: str) -> float:
    """
    Returns a mock current price for the given symbol.

    Args:
        symbol (str): The trading pair symbol, e.g., 'BTCUSDT'.
    Returns:
        float: Mock price.
    """
    # TODO: Replace mock value with API call
    mock_prices = {
        'BTCUSDT': 30000.0,
        'ETHUSDT': 2000.0,
        'BNBUSDT': 300.0
    }
    return mock_prices.get(symbol, 0.0)


def place_order(symbol: str, side: str, quantity: float, price: float) -> dict:
    """
    Places a mock order and returns order details.

    Args:
        symbol (str): The trading pair symbol.
        side (str): 'buy' or 'sell'.
        quantity (float): Amount to trade.
        price (float): Order price.
    Returns:
        dict: Mock order confirmation.
    """
    # TODO: Implement real order placement via API
    return {
        'symbol': symbol,
        'side': side,
        'quantity': quantity,
        'price': price,
        'status': 'filled',
        'order_id': 'MOCK123456'
    }


def get_order_status(order_id: str) -> dict:
    """
    Retrieves mock order status.

    Args:
        order_id (str): The order identifier.
    Returns:
        dict: Mock order status.
    """
    # TODO: Implement real order status check
    return {
        'order_id': order_id,
        'status': 'filled',
        'filled_quantity': 1.0,
        'remaining_quantity': 0.0
    }
