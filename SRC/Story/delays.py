from Utils.debug import Debug

import asyncio

class Delays:
  async def small_delay() -> None:
    await asyncio.sleep(2)
  
  async def medium_delay() -> None:
    await asyncio.sleep(5)
  
  async def long_delay() -> None:
    await asyncio.sleep(10)
  
  async def custom_delay(Seconds: int) -> None:
    await asyncio.sleep(Seconds)