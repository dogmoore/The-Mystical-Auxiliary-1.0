from nicegui import ui, app, background_tasks, Client
from nicegui.page import page
from Utils.authentication import Authentication, Sign_Up
from Story.intro import Introduction
from Utils.events import Events
from Utils.debug import Debug
from fastapi import Request, Response
from colorama import Fore
import colorama
import colorama
import yaml

colorama.init(autoreset=True)

with open('SRC/Config/config.yml', 'r') as ymlfile:
   config = yaml.load(ymlfile, Loader=yaml.SafeLoader)


# exception handling
@app.exception_handler(500)
async def expection_handler_500(request: Request, expection: Exception) -> Response:
   ui.navigate.to('/500')

@ui.page('/500')
def error_500() -> None:
   auth = app.storage.user.get('authenticated', False)
   def return_home():
      if auth:
         ui.navigate.to('/the_mystical_auxiliary')
      else:
         ui.navigate.to('/login')
   ui.label(text='Something went wrong!')
   ui.label(text='please contact the system administrator')
   ui.label(text=Exception)
   ui.button(text='Return', on_click=lambda: return_home())

@app.exception_handler(404) # error 404 handling
async def exception_handler_404(request: Request, exception: Exception) -> Response: # route error 404 to 404 page then login or game page
   auth = app.storage.user.get('authenticated', False)
   with Client(page(''), request=request) as client:
      ui.navigate.to('/404')
   Debug.error(exception)
   return client.build_response(request, 404)

@ui.page('/404')
def error_404() -> None:
   ui.label(text='Something went wrong!')
   ui.label(text='Please contact the system administrator')
   ui.button(text='Return', on_click=lambda: return_home())
   auth = app.storage.user.get('authenticated', False)
   def return_home():
      if auth:
         ui.navigate.to('/the_mystical_auxiliary')
      else:
         ui.navigate.to('/login')
# end exception handling

@ui.page("/sign_up")
def sign_up() -> None:
   Sign_Up.sign_up()


@ui.page("/login")
def login() -> None:
   def attmept_login() -> None:
         # authentication check
         if username == "" or password == "":
            ui.notify('Wrong username or password', color='negative')
         else:
            if Authentication.auth_login(username.value, password.value):
               app.storage.user.update({'username': username.value, 'authenticated': True})
               ui.navigate.to('/the_mystical_auxiliary')
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
      ui.button(text='Sign Up', on_click=lambda: ui.navigate.to('/sign_up'))
      if config['debug']['debug_mode']:
         if config['debug']['flags']['bypass_login_button']:
            ui.button(text='Bypass Login', on_click=lambda: ui.navigate.to('/the_mystical_auxiliary'), color='yellow')
         ui.label(text='DEBUG MODE ENABLED')


# auto-fill username if authenticated
   if app.storage.user.get('authenticated', False):
      Debug.info('username was auto-filled due to debug mode', console=False, notify=True)
      username.set_value(app.storage.user.get('username'))


@ui.page('/the_mystical_auxiliary')
async def the_mystical_auxiliary() -> None:
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
      ui.navigate.to('/the_mystical_auxiliary')

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
