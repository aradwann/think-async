"""
a Future represents a future completion state of some activity and is managed by the loop
    The Future class represents a state of something that is interacting with a loop
    it's like when future instance is created as toggle of completion, the toggle is
    set to "not yet completed" but some later itme it will be "completed"

a Task is exactly the same, but the specific "activity" is a coroutine -- 
    probably one of yours that you created with an (( async def function plus create_task() ))
"""

import asyncio
from asyncio import Future, Task
from contextlib import suppress

'''
async def f():
    """
    The intention is to launch completely new tasks inside the coroutine.
    they will run independently of the exexcution context inside coroutine function f()
    """
    # Create some tasks

    for i in range():
        asyncio.create_task(< some other coro > )
'''

# f: asyncio.Future Type signature Task is also accepted because it's a subclass of Future


async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        # Task API doesn't allow us to set_result
        f.set_result("I have finished")
    except RuntimeError as e:
        print(f'No longer allowed: {e}')
        f.cancel()

loop = asyncio.get_event_loop()
# create a task instance instead of a future
fut = Task(asyncio.sleep(1_000_000))
print(fut.done())

# pass the task
loop.create_task(main(fut))
with suppress(asyncio.CancelledError):

    loop.run_until_complete(fut)

print(fut.done())
print(fut.cancelled())


#################################
# Create a Task? Ensure a Future?
#################################
"""
asyncio.ensure_future()
    schedule the excution of a coroutine objcet: wrap it in a future. Return a Task object
    if the argument is a Future, it is returned directly 
"""


async def f():
    pass

coro = f()
loop = asyncio.get_event_loop()

task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task
