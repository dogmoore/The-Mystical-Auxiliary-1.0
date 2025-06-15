from Utils.debug import Debug

import asyncio
import yaml

with open('SRC/Config/config.yml', 'r') as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.SafeLoader)

class Delays:
  async def small_delay() -> None:
    if config['debug']['debug_mode'] and config['debug']['flags']['ignore_delays']:
      return
    else:
      await asyncio.sleep(2)

  async def medium_delay() -> None:
    if config['debug']['debug_mode'] and config['debug']['flags']['ignore_delays']:
      return
    else:
      await asyncio.sleep(5)

  async def long_delay() -> None:
    if config['debug']['debug_mode'] and config['debug']['flags']['ignore_delays']:
      return
    else:
      await asyncio.sleep(10)

  async def custom_delay(Seconds: int) -> None:
    if config['debug']['debug_mode'] and config['debug']['flags']['ignore_delays']:
      return
    else:
      await asyncio.sleep(Seconds)