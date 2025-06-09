import random
import yaml
from Utils.debug import Debug

with open('SRC/Config/config.yml', 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.SafeLoader)

notify = config['debug']['notify']

class Dice():
    def flip_coin():
        result = random.randint(1,2)
        Debug.info(f'Result was {result}', notify= notify)
        return result

    def roll_d3():
        result = random.randint(1,3)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d4():
        result = random.randint(1,4)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d6():
        result = random.randint(1,6)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d8():
        result = random.randint(1,8)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d10():
        result = random.randint(1,10)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d12():
        result = random.randint(1,12)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d20():
        result = random.randint(1,20)
        Debug.info(f'Result was {result}', notify=notify)
        return result

    def roll_d100():
        result = random.randint(1,100)
        Debug.info(f'Result was {result}', notify=notify)
        return result
    
    def roll_custom(min:int = 0, max:int = 5): # for internal checks only
        result = random.randint(min, max)
        Debug.info(f'Result was {result}', notify= notify)
        return result