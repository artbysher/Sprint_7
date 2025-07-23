import requests
import data


class OrdersMethods:
    @staticmethod
    def create_order(body):
        return requests.post(data.Url.ORDERS_URL, json=body)

    @staticmethod
    def get_list_order():
        return requests.get(data.Url.ORDERS_URL)


    @staticmethod
    def get_order_id(track):
        responce =requests.get(f'{data.Url.ORDERS_URL}/track?t={track}')
        return responce.json()["order"]["id"]

    @staticmethod
    def get_order(track):
        return requests.get(f'{data.Url.ORDERS_URL}/track?t={track}')

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(f'{data.Url.ACCEPT_ORDER_URL}/{order_id}?courierId={courier_id}')

