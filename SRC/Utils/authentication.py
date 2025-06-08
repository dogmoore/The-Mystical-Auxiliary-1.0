from Utils.debug import Debug
from nicegui import ui
import asyncio
import os
import yaml
import time
import base64

# potential errors
#  - FileNotFoundError

with open("SRC/Config/config.yml", "r") as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.FullLoader)

with open("SRC/Config/accounts.yml", "r") as ymlfile:
  accounts = yaml.load(ymlfile, Loader=yaml.FullLoader) #FileNotFoundError

# encryption type
# 0 - plain text - default when testing
# 1 - base64
# 2 - sha-256

class Authentication:
  def current_milli_time():
    return round(time.time() * 1000)

  def auth_username(username:str): # linear search
    start_time = Authentication.current_milli_time() # start timer
    index_step = 0
    found = False
    while index_step <= len(accounts["credentials"]) and not found:
      if index_step >= len(accounts["credentials"]) - 1:
        break
      index = "account_" + str(index_step)
      if accounts["credentials"][index]["username"] == username:
        print("username pass")
        print(f"found at index {index_step}")
        end_time = Authentication.current_milli_time() # end timer
        elapsed_time = end_time - start_time # timer output
        print(f"Elapsed time: {elapsed_time} ms")
        found = True
      else:
        index_step += 1
    if found:
      return index
    else:
      return False

  def auth_password(index: dict, password:str):
    if not accounts["credentials"][index]["security"]["enabled"]:
      if password == accounts["credentials"][index]["password"]:
        print("password passed")
        return True
      else:
        print("password failed")
        return False

  def auth_login(username:str, password:str):
    username_passed = Authentication.auth_username(username)
    if type(username_passed) == bool:
      print("Username not found")
      return False
    else:
      return Authentication.auth_password(username_passed, password)
