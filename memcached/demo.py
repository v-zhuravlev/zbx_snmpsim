#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

from pymemcache.client import base

client1 = base.Client(('localhost', 11211))
client2 = base.Client(('localhost', 11211))
client3 = base.Client(('localhost', 11211))
for i in range(1000):
    client1.set('some_key'+str(i),str(i))

for i in range(5000):
    client2.set('another_key'+str(i),str(i))

for i in range(10000,145435):
    client2.set('another_key'+str(i),str(i))

for i in range(9999,34343):
    client1.get('some_key'+str(i))

for i in range(10000,345435):
    client2.set('another_key'+str(i),str(i))

for i in range(1000):
    client3.get('some_key'+str(i))
