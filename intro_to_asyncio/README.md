# Python asyncio by Caleb Hattengh

### I tried to collect useful code examples from Caleb's book to understand how asyncio works and how to use it

He tried to explain it through building blocks based on his understanding shown in the following table

Table 3-1. Features of asyncio arranged in a hierarchy; for end-user developers, the most
important tiers are highlighted in bold
Level

| Level      |          Concept           |                                                                Implementation |
| ---------- | :------------------------: | ----------------------------------------------------------------------------: | --- | ---------- | -------------- | ----------------------------- |
| **Tier 9** |    **Network: streams**    | StreamReader, StreamWriter, asyncio.open_connection(), asyncio.start_server() |
| Tier 8     |     Network: TCP & UDP     |                                                                      Protocol |
| Tier 7     |    Network: transports     |                                                                 BaseTransport |
| **Tier 6** |         **Tools**          |                                                                 asyncio.Queue |
| **Tier 5** | **Subprocesses & threads** |                                        run_in_executor() , asyncio.subprocess |
| Tier 4     |           Tasks            |                                          asyncio.Task , asyncio.create_task() |
| Tier 3     |          Futures           |                                                                asyncio.Future |     | **Tier 2** | **Event loop** | asyncio.run() , BaseEventLoop |
| **Tier 1** |   **(Base) Coroutines**    |                                    async def , async with , async for , await |
