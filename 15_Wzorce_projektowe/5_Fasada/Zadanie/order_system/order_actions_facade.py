from order_system.integration_api import auth_client
from order_system.integration_api.order_management_client import OrderManagementClient
from order_system.integration_api import order_directory_client


def update_order_status(order_number: str, new_status: str) -> None:
    login = "LOAD_FROM_ENV"
    password = "LOAD_FROM_ENV"
    # TODO
    token = auth_client.obtain_token(login, password)
    order_identifier = order_directory_client.get_order_identifier_by_number(order_number)
    order_management_client = OrderManagementClient()
    order_management_client.connect(token)
    order_management_client.update_status(order_identifier, new_status)
