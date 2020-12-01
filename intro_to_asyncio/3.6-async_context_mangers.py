"""
using async with context managers 
"""
from contextlib import contextmanager, asynccontextmanager
import asyncio


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    # __aenter__ is special method for async context manager

    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return conn

    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async with Connection('localhost', 9001) as conn:
    # <do stuff with conn>
    pass

####################
# The blocking way
####################


@contextmanager  # transforms generator function into a context manager
def web_page(url):
    data = download_webpage(url)  # this might be blocking
    yield data
    update_stats(url)


with web_page('google.com') as data:
    process(data)  # this might be blocking

####################
# The non-blocking way
####################


@asynccontextmanager
async def web_page(url):
    # note: here we added await keyword that means we also modified download_webpage() to be a coroutine
    # note: async support needs to be added down at the socket level, but if we can't change the code to
    # that level which is common with many third party libraries like requests, use excutors
    data = await download_webpage(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)


####################
# The non-blocking excutor way
####################
"""
excutor run the blocking calls in a separate thread
the default excutor is a ThreadPoolExecutor
"""


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_stats, url)

async with web_page('google.com') as data:
    process(data)
