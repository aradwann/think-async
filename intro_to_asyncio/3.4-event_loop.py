"""
Event loop in asyncio handles all the switching between coroutines, 
as well as catching those StopIteration exceptions and much more, 
such as listening to sockets and file descriptors for events

you code without interacting with the event loop directly
your code can be written entirely using await calls, initiated by an asyncio.run(coro)

but if you wannt to interact with the event loop, there are two ways:
  1-(recommmended) asycio.get_running_loop(), callable from inside the context of a coroutine,
    a task, or a function called from one of those, it always provide the current running event loop 
  2-(discouraged) asycio.get_event_loop(), callable from anywhere,
    works only within the same thread, so it will fail, if it's called inside new thread
"""

import asyncio


async def f():
    await asyncio.sleep(0)
    return 111


loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop is loop2)
coro = f()

loop.run_until_complete(coro)
