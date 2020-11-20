import inspect

"""
A Coroutine is an object that encapsulates the ability to resume an underlying function
that has been suspended before completion 
"""

# note: coroutine is the async function return value


async def f():
    return 123

# coro is the coroutine object returned by f()
coro = f()

# print(coro)
# <coroutine object f at 0x7f007a891240>

# print('type of f: ', type(f))
# type of f:  <class 'function'>

# print('is f a coroutine function? ', inspect.iscoroutinefunction(f))
# is f a coroutine function?  True

# print('is coro a coroutine? ', inspect.iscoroutine(coro))
# is coro a coroutine?  True

# print('type of coro', type(coro))
# type of coro <class 'coroutine'>

try:
    # calling coro.send(None) to initiate the coroutine
    # note: that's the manual way of doing it,
    # "await" will manage that automatically behind the scene by the event loop
    coro.send(None)
except StopIteration as e:
    # when the coroutine returns, a special exception is raised, called StopIteration
    # you can access the return value by the value attribute of the exception itself
    print('The answer was:', e.value)


# there are similarities between generators and async functions
def g():
    yield 123


gen = g()
# print('type of g ', type(g))
# type of g  <class 'function'>

# print('type of gen ', type(gen))
# type of gen  <class 'generator'>
