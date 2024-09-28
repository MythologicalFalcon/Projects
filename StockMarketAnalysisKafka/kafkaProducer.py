import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json


import six
import sys
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

producer = KafkaProducer(bootstrap_servers=['{Instance public IP}:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

producer.send('demo_test', value={'name':'value'})

df = pd.read_csv("indexProcessed.csv")
print(df.head(5))

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    sleep(1)

producer.flush() #clear data from kafka server

