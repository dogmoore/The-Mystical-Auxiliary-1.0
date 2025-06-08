from Utils.debug import Debug
from Story.delays import Delays
from nicegui import ui, app
from Utils.inventory_check import item_fetch
from Utils.rng import Dice

import yaml

with open("SRC/Config/config.yml", "r") as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.FullLoader)

with open("SRC/Config/character_names.yml", "r") as ymlfile:
  names = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Introduction:
  def class_selection(profession: str) -> None:
    ui.notify(f'You chose {profession}')
    app.storage.user.update({"class": profession})
    ui.chat_message(text=profession, sent=True)

  def gender_selection(gender: str) -> None:
    ui.notify(gender)
    app.storage.user.update({"gender": gender})


  async def main(username:str) -> None:
    ui.button(text='Logout', on_click=lambda: ui.navigate.to('/login'))
    if username == None: username = 'Default_User_1' # checks for blank username

    if not config['debug']['flags']['disable_intro']:
      ui.chat_message(name=names['narrator'], text=[f'welcome {username} to Mo\'kin', 'A Realm of knights and magic'])
      # await Delays.medium_delay()
      with ui.chat_message():
        ui.chat_message(text=f'Lets get you started in this world, what is your profession?')
        
        # character creation
        with ui.grid(columns=4): # class selection
          ui.button(text='Warrior', on_click=lambda: Introduction.class_selection('Warrior'))
          ui.button(text='Bard', on_click=lambda: Introduction.class_selection("Bard"))
          ui.button(text="Cleric", on_click=lambda: Introduction.class_selection("Cleric"))
          ui.button(text="Druid", on_click=lambda: Introduction.class_selection("Druid"))
          ui.button(text='Fighter', on_click=lambda: Introduction.class_selection('FIghter'))
          ui.button(text="Monk", on_click=lambda: Introduction.class_selection("Monk"))
          ui.button(text="Paladin", on_click=lambda: Introduction.class_selection("Paladin"))
          ui.button(text="Ranger", on_click=lambda: Introduction.class_selection("Ranger"))
          ui.button(text="Rogue", on_click=lambda: Introduction.class_selection("Rogue"))
          ui.button(text="Sorcerer", on_click=lambda: Introduction.class_selection("Sorcerer"))
          ui.button(text="Warlock", on_click=lambda: Introduction.class_selection("Warlock"))
          ui.button(text='Wizard', on_click=lambda: Introduction.class_selection('Wizard'))

      with ui.chat_message():
        ui.label('And now what\'s your gender?')
        with ui.row(): # gender selction
          ui.button(text='Male', on_click=lambda: Introduction.gender_selection('Male'))
          ui.button(text='Female', on_click=lambda: Introduction.gender_selection('Female'))

      with ui.chat_message():
        with ui.row(): # race selection
          ui.button(text='Human')

      ui.button(text='check inventory', on_click=lambda: item_fetch.fetch_item('Warlock_staff'))

      # building inventory
      profession = app.storage.user.get("class")
      if profession == "Warrior":
        pass
      elif profession == 'Bard':
        pass
      elif profession == 'Cleric':
        pass
      elif profession == 'Warlock':
        app.storage.user.update({'inventory' 'Warlock_boots': True, "Warlock_staff": True})
    

      intro_selection = Dice.roll_d3()
      if intro_selection == 1: # tavern
        pass
      elif intro_selection == 2: # kidnapping
        pass
      elif intro_selection == 3: # TBD
        pass

    else:
      ui.label('Intro is disabled via flags')
