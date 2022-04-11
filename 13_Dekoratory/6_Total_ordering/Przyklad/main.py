from shop.order import Order, OrderElement


def run_example() -> None:
    mariusz_order = Order(client_name="Mariusz")
    jakub_order = Order(client_name="Jakub")

    mariusz_order.add_element(OrderElement(name="Opona rowerowa", value=150))
    mariusz_order.add_element(OrderElement(name="Gra planszowa", value=85))

    jakub_order.add_element(OrderElement(name="Dysk HDD", value=280))
    jakub_order.add_element(OrderElement(name="Klawiatura", value=120))

    print(mariusz_order.overall_value)
    print(jakub_order.overall_value)

    print(mariusz_order < jakub_order)


if __name__ == "__main__":
    run_example()
