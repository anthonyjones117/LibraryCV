#!/usr/bin/env python
import requests
#res = requests.post('http://127.0.0.1:5000/data', json={"mytext":"lalala"})
res = requests.post('http://127.0.0.1:5000/books/', json={"mytext":"lalala"})
if res.ok:
    print(res.json())