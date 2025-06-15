import random
import yaml
from Utils.debug import Debug

with open('SRC/Config/config.yml', 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.SafeLoader)

notify = config['debug']['notify']
prefix = 'RNG |'

class Dice():
    async def flip_coin():
        result = random.randint(1,2)
        if config['rng']['always_high']:
            result = 2
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d3():
        result = random.randint(1,3)
        if config['rng']['always_high']:
            result = 3
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d4():
        result = random.randint(1,4)
        if config['rng']['always_high']:
            result = 4
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d6():
        result = random.randint(1,6)
        if config['rng']['always_high']:
            result = 6
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result

    async def roll_d8():
        result = random.randint(1,8)
        if config['rng']['always_high']:
            result = 8
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d10():
        result = random.randint(1,10)
        if config['rng']['always_high']:
            result = 10
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d12():
        result = random.randint(1,12)
        if config['rng']['always_high']:
            result = 12
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_d20():
        result = random.randint(1,20)
        if config['rng']['always_high']:
            result = 20
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result

    async def roll_d100():
        result = random.randint(1,100)
        if config['rng']['always_high']:
            result = 100
        elif config['rng']['always_low']:
            result = 1
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
    
    async def roll_custom(min:int = 0, max:int = 5):
        result = random.randint(min, max)
        if config['rng']['always_high']:
            result = max
        elif config['rng']['always_low']:
            result = min
        Debug.info(f'{prefix} Result was {result}', notify=notify)
        return result
