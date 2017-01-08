from distributed import Client
import time

client = Client("192.168.0.106:8786")
client.restart()

from funcs import create_dirs, get_dirs, add_flag

future = client.map(create_dirs, range(10))
flags = client.submit(get_dirs, future)
client.gather(flags)
print(flags)
