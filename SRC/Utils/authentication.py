from Utils.debug import Debug
from nicegui import ui
import yaml
import time
import base64

# potential errors
#  - FileNotFoundError  TODO exception handling for this error

file_debug = False # leave disabled unless debugging authentication

with open("SRC/Config/config.yml", "r") as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.FullLoader)


# encryption type
# 0 - plain text - default when testing
# 1 - base64 - default when live? | needs testing
# 2 - sha-256

class Authentication:
  try: # error handling
    with open("SRC/Config/accounts.yml", "r") as ymlfile:
      accounts = yaml.load(ymlfile, Loader=yaml.FullLoader) #FileNotFoundError
  except FileNotFoundError as err:
    Debug.error(err)

  def current_milli_time():
    return round(time.time() * 1000)

  def auth_username(username:str): # linear search
    start_time = Authentication.current_milli_time() # start timer
    index_step = 0
    found = False
    if username == '': # blank input returns empty string
      ui.notify('Username is blank', color='negative')
      return False
    while index_step <= len(Authentication.accounts["credentials"]) and not found:
      if index_step >= len(Authentication.accounts["credentials"]) - 1:
        break
      index = "account_" + str(index_step)
      try:
        if Authentication.accounts["credentials"][index]["username"] == username:
          Debug.info('Username Pass')
          Debug.info(f"found at index {index_step}")
          end_time = Authentication.current_milli_time() # end timer
          elapsed_time = end_time - start_time # timer output
          Debug.info(f"Elapsed time: {elapsed_time} ms")
          found = True
        else:
          index_step += 1
        if found:
          return index # breaks loop
        else:
          found = False
      except BaseException as err:
        if file_debug:
          Debug.critical(err)
        Debug.error('Silent Internal Error | indexing failed due to blank username')

  def auth_password(index: dict, password:str):
    try:
      if not Authentication.accounts["credentials"][index]["security"]["enabled"]:
        if password == Authentication.accounts["credentials"][index]["password"]:
          Debug.info('Password Passed')
          return True
        else:
          ui.notify(message='Wrong Username or Password', color='negative')
          if password == '' or password == None:
            Debug.info('Blank Password')
          else:
            Debug.info('Password Failed')
          return False
    except BaseException as err:
      if file_debug:
        Debug.critical(err)
      Debug.error('Silent Internal Error | indexing failed due to blank username')

  def auth_login(username:str, password:str):
    username_passed = Authentication.auth_username(username)
    if type(username_passed) == bool and not username == '':
      ui.notify(message='Wrong Username or Password', color='negative')
      Debug.info('Username Not Found')
      return False
    else:
      return Authentication.auth_password(username_passed, password)


class Sign_Up(): # WIP
  try:
    with open('SRC/Config/accounts.yml', 'r') as ymlfile:
      account = yaml.load(ymlfile, Loader=yaml.SafeLoader)
  except FileNotFoundError as err:
      Debug.error(err, notify=True)

  def sign_up() -> None:
    username = ui.input(label='Username')
    # email = ui.input(label='email')
    password = ui.input(label='Password')

    for username_check in Sign_Up.account['credentials']:
      pass
    