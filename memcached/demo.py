#!/bin/env python3

from pymemcache.client import base

client1 = base.Client(('localhost', 11211))
client2 = base.Client(('localhost', 11211))
client3 = base.Client(('localhost', 11211))

for i in range(100,4565):
    client2.set('another_key'+str(i),str(i))

for i in range(9999,13433):
    client1.get('some_key'+str(i))

for i in range(10000,34535):
    client2.set('another_key'+str(i),str(i))

for i in range(1000):
    client3.get('some_key'+str(i))
