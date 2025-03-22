import requests
import json
import datetime
import boto3
from websocket import create_connection, WebSocketConnectionClosedException



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



while True:
    data = json.loads(ws.recv())




    