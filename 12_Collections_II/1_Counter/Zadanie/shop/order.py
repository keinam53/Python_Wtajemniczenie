from __future__ import annotations
from collections import Counter
from products_directory import product_price


class Order:
    def __init__(self) -> None:
        # TODO: Init empty order
        self.elements: Counter[str] = Counter()

    def add_element(self, product_name: str, quantity: int = 1) -> None:
        # TODO
        self.elements[product_name] = self.elements[product_name] + quantity

    def remove_element(self, product_name: str, quantity: int = 1) -> None:
        # TODO
        self.elements[product_name] = self.elements[product_name] - quantity
        if self.elements[product_name] < 1:
            del self.elements[product_name]

    def merge_orders(self, order_to_merge: Order) -> None:
        # TODO
        self.elements = self.elements + order_to_merge.elements

    @property
    def total_sum(self) -> int:
        # TODO use product_price to get product price by product name
        result = 0
        for element, quantity in self.elements.items():
            result += quantity * product_price(element)
        return result

    @property
    def products(self) -> list[str]:
        # TODO return list of unique products in order
        return list(self.products)

    def __str__(self) -> str:
        # TODO: all elements with numbers and prices + total sum
        results = [
            f"{element} x {quantity} -> {product_price(element) * quantity} "
            for element, quantity in self.elements.items()
        ]
        results.append(f"Total: {self.total_sum}")
        return "\n".join(results)
