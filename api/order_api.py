import requests
import os
from dotenv import load_dotenv

load_dotenv()


class OrderAPI:
    """API client for order-related operations"""

    def __init__(self, auth_headers=None):
        self.base_url = os.getenv(
            "API_BASE_URL", "https://stellarburgers.nomoreparties.site/api"
        )
        self.headers = {"Content-Type": "application/json"}
        if auth_headers and "Authorization" in auth_headers:
            self.headers["Authorization"] = auth_headers["Authorization"]

    def _make_request(self, method, endpoint, data=None):
        """Helper method to make API requests"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, headers=self.headers)
        if not response.ok:
            raise Exception(
                f"API request failed: {response.status_code} - {response.text}"
            )
        return response

    def get_ingredients(self):
        """Get all available ingredients"""
        return self._make_request("GET", "/ingredients")

    def create_order(self, ingredients):
        """Create a new order with the given ingredient IDs"""
        return self._make_request("POST", "/orders", data={"ingredients": ingredients})

    def get_user_orders(self):
        """Get orders for the authenticated user"""
        return self._make_request("GET", "/orders")

    def get_order_by_number(self, order_number):
        """Get order details by order number"""
        return self._make_request("GET", f"/orders/{order_number}")

    def get_all_orders(self):
        """Get all orders (feed)"""
        return self._make_request("GET", "/orders/all")