from nicegui import ui, app, background_tasks
from Utils.authentication import *
from Story.intro import Introduction
from Utils.events import Events
from Utils.debug import Debug
import colorama
from colorama import Fore
import colorama
import yaml

colorama.init(autoreset=True)

with open('SRC/Config/config.yml', 'r') as ymlfile:
   config = yaml.load(ymlfile, Loader=yaml.SafeLoader)


@ui.page("/sign_up")
def sign_up() -> None:
   pass


# background tasks
# @background_tasks.await_on_startup
# def clear_storage() -> None:
#    app.storage.user.clear()
#    print('app starting, clearing storage...')

@ui.page("/login")
def login() -> None:
   def attmept_login() -> None:
         # authentication check
         if username == "" or password == "":
            ui.notify('Wrong username or password', color='negative')
         else:
            if Authentication.auth_login(username.value, password.value):
               app.storage.user.update({'username': username.value, 'authenticated': True})
               ui.navigate.to('/the_mystical_auxilary')
               if config['debug']['debug_mode']:
                  ui.notify('login successful')
                  print(f"stored username: {app.storage.user.get('username')}")
                  print(f"Authenticated: {app.storage.user.get('authenticated')}")
            else:
               ui.notify('login failed')

   # page ui
   ui.add_scss('SRC/css/style.scss')
   ui.label(text=config['title']['normal']).classes('title')
   ui.label(text='Created by dogmoore').classes('absolute-bottom-right')
   
   with ui.grid(columns=1).classes('absolute-center'):
      username = ui.input(label='Username').on('keydown.enter', attmept_login)
      password = ui.input(label='password').on('keydown.enter', attmept_login)
      ui.button(text='Submit', on_click=attmept_login)
      if config['debug']['debug_mode']:
         if config['debug']['flags']['bypass_login_button']:
            ui.button(text='Bypass Login', on_click=lambda: ui.navigate.to('/the_mystical_auxilary'))
         ui.label(text='DEBUG MODE ENABLED')


# auto-fill username if authenticated
   if app.storage.user.get('authenticated', False):
      Debug.info('username was auto-filled due to debug mode', console=False, notify=True)
      username.set_value(app.storage.user.get('username'))


@ui.page('/the_mystical_auxilary')
async def the_mystical_auxilary() -> None:
   await Introduction.main(app.storage.user.get('username'))


@ui.page("/")
def main_page() -> None: # redirect main page to login page
   
   app.storage.user.clear()
   start_up_color= {
      'flag enabled': Fore.GREEN,
      'flag disabled': Fore.RED
      }

   # console start up message
   print('')
   Debug.info('Debug Flags')
   if config['debug']['debug_mode']:
      Debug.info(f'Debug Mode          | {start_up_color['flag enabled']}True')
   else:
      Debug.info(f'Debug Mode          | {start_up_color['flag disabled']}False')
   if config['debug']['flags']['bypass_login']:
      Debug.info(f'Bypass Login        | {start_up_color['flag enabled']}True')
   else:
      Debug.info(f'Bypass Login        | {start_up_color['flag disabled']}False')
   if config['debug']['flags']['bypass_login_button']:
      Debug.info(f'Bypass Login Button | {start_up_color['flag enabled']}True')
   else:
      Debug.info(f'Bypass Login Button | {start_up_color['flag disabled']}False')
   if config['debug']['flags']['disable_intro']:
      Debug.info(f'Bypass Intro        | {start_up_color['flag enabled']}True')
   else:
      Debug.info(f'Bypass Intro        | {start_up_color['flag disabled']}False')
   print('')


   if not config['debug']['flags']['bypass_login']:
      ui.navigate.to('/login')
   else:
      app.storage.user.update({'username': 'dogmoore', 'authenticated': True})
      ui.navigate.to('/the_mystical_auxilary')

# nicegui setup
if config['debug']['debug_mode']: # setup flags
   port = config['port']['debug']
   token = config['token']['debug']
   title = config['title']['debug']
else:
   port = config['port']['normal']
   token = config['token']['normal']
   title = config['title']['normal']


# app starts
ui.run(
   storage_secret=token,
   port=port,
   show=True,
   reload=True,
   title=title,
   dark=True,
   on_air=False # provides a linkie valid for 1 hour
)
