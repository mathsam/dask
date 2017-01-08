from distributed import Client
import time

client = Client("192.168.0.106:8786")
client.restart()

from funcs import launch_more_task

future = client.map(launch_more_task, range(10))
client.gather(future)
print(flags)
