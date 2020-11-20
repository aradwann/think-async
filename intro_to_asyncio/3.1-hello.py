import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    "a regular function that would have blocked the main thread"
    # note: we made sleep for 0.5 sec shorter than asyncio 1 sec
    time.sleep(0.5)
    print(f'{time.ctime()} Hello from a thread!')


loop = asyncio.get_event_loop()
task = loop.create_task(main())

# the default executor here schedules the blocking function
# to run after run_until_complete() is called
# note: the excutor returns a Future
loop.run_in_executor(None, blocking)
# run loop until task completed
loop.run_until_complete(task)

# get all tasks that are pending if the loop stopped for any reason
pending = asyncio.all_tasks(loop=loop)

for task in pending:
    task.cancel()

# gather the pending tasks
group = asyncio.gather(*pending, return_exceptions=True)
# run the gathered tasks to complete
loop.run_until_complete(group)
# close the loop
# note: stopped loop can be restarted but closed loop is gone for good
loop.close()
