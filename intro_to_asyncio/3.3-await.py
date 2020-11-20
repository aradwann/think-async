"""
the "await" keyword will accept only a thing called an awaitable, which is one of these:
-> A coroutine
-> Any object implementing the __await__() special method,
   that special method must return an iterator
"""

import asyncio


async def f():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('I was cancelled!')
    else:
        return 123

'''
async def main():
    # we await the coroutine returned by the f()
    # so the value of the result will be 123 when f() completess
    result = await f()
    return result
'''

"""
We can use <coroutine>.throw() to inject exceptions into a coroutine
internally it will raise asyncio.CancelledError inside your coroutine
at the await point
Note: StopIteration exception is the normal way that coroutines exit
"""

coro = f()
coro.send(None)
coro.throw(asyncio.CancelledError)
