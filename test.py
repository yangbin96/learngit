import threading
import asyncio

async def hello1():
    print('Hello world!')
    await hello2()
    print('Hello again!')

async def hello2():
    print('Hello world!2')
    await asyncio.sleep(4)
    print('Hello again!2 ')

loop = asyncio.get_event_loop()
tasks = [hello1()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
