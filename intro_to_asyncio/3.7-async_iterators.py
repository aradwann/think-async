################################
# traditional non-async iterator
################################

from aioredis import create_redis
import asyncio


class A:
    def __iter__(self):
        """
        __iter__() must return a iterable, an object that implement __next__()        
        """
        self.x = 0  # initializing starting state

        return self

    def __next__(self):
        """
        this will be called for every step in the iteration sequence
        until StopIteration is raised
        """
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x


for i in A():
    print(i)


################################################################
# async iterator for fetching data from redis
################################################################
"""
we can get the data from Redis associated with this key.
which means tha other code can run on the event loop while we wait on network I/O

even when iterating over data where that iteration itself os performing I/O
The benefit is that you can process enormous amounts of data with a single loop, 
because you have to deal with each chunk only in tiny batches
"""


async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']
    # imagine the each of the values associated with these keys is quite
    # large and stored in the Redis instance
    # we're using async for: the point is that iteration is able to suspend itself
    # while waiting for the next datum to arrive
    async for value in OneAtATime(redis, keys):
        await do_something_with(value)


class OneAtATime:
    def __init__(self, redis, keys):
        self.resdis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration
        value = await radis.get(k)
        return value


asyncio.run(main())
