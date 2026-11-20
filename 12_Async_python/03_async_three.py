# Example of fetching multiple URLs asynchronously.

import asyncio
import aiohttp # check their documentation for code. we are following that.

async def fetch_url(session, url):
    # Make an HTTP GET request and close its response when the block ends.
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    # Repeating this URL creates three independent requests.
    urls = ["https://httpbin.org/delay/2"] * 3
    # Reuse one client session for all requests; async with closes it afterward.
    async with aiohttp.ClientSession() as session:
        # Create one coroutine per URL, then wait for all of them concurrently.
        tasks = [fetch_url(session, url) for url in urls]
        # Without *, gather(tasks) passes the whole list as one argument, but
        # gather() expects each coroutine separately. Here, *tasks expands to
        # gather(tasks[0], tasks[1], tasks[2]), so it can await all three.
        await asyncio.gather(*tasks)


# asyncio.run() creates an event loop, runs main(), and then closes the loop.
asyncio.run(main())

# Summary: Send three concurrent GET requests to the same delayed endpoint and
# print each response's HTTP status.