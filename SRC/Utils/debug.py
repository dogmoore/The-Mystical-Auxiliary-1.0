import yaml
import colorama
from colorama import Fore
from nicegui import ui

with open("SRC/Config/config.yml", "r") as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.FullLoader)

colorama.init(autoreset=True)

theme = {
  'info': Fore.BLUE,
  'alert': Fore.GREEN,
  'minor error': Fore.YELLOW,
  'critical error': Fore.RED
}


class Debug:
  def info(message:str, console:bool = True, notify: bool = False) -> None:
    if config["debug"]["info"]:
      if console:
        print(f"{theme['info']}INFO | {message}")
      if notify:
        ui.notify(message=message)

  def error(err:str, console:bool = True, notify: bool = False) -> None:
    if config["debug"]["error"]:
      if console:
        print(f"{theme['minor error']}MINOR ERROR | {err}")
      if notify:
        ui.notify(message=err)

  def critical(err:str, console:bool = True, notify: bool = False) -> None:
    if config["debug"]["critical"]:
      if console:
        print(f"{theme['critical error']}CRITICAL ERROR | {err}")
      if notify:
        ui.notify(message=err)
    
  def alert(message:str, console:bool = True, notify: bool = False) -> None:
    if config["debug"]["alert"]:
      if console:
        print(f"{theme['alert']}ALERT | {message}")
      if notify:
        ui.notify(message=message)