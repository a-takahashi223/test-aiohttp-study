import asyncio

import pytest
from aiohttp import web


async def main():
    app = web.Application()
    app.add_routes([web.get("/get", get)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, pytest.main)
    await runner.cleanup()


async def get(request: web.Request):
    return web.json_response(dict(url=str(request.url)))


if __name__ == "__main__":
    asyncio.run(main())
