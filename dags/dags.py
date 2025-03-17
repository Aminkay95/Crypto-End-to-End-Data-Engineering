import requests
import json
import datetime
#from env import keys
from websocket import create_connection, WebSocketConnectionClosedException


def extract_coinbase()
    ws = create_connection('wss://ws-feed.exchange.coinbase.com')

    ws. send(
        json.dumps(
            {
                'type':'subscribe',
                'product_ids':['BTC-USD','ETH-USD','SOL-USD'],
                'channels':['matches']
                
            }
        )
    )



    data = json.loads(ws.recv())
    data1 = json.dumps(data)
    with open('coinbase_prices.json','w') as file:
        file.write(data1)

    