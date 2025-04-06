import configuration

import data

import requests

def post_new_body(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
                        params={"t": track})
