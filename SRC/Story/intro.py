from Utils.debug import Debug
from Utils.delays import Delays
from nicegui import ui, app
from Utils.inventory_check import item_fetch
from Utils.rng import Dice

import yaml

with open("SRC/Config/config.yml", "r") as ymlfile:
  config = yaml.load(ymlfile, Loader=yaml.FullLoader)

with open("SRC/Config/character_names.yml", "r") as ymlfile:
  names = yaml.load(ymlfile, Loader=yaml.FullLoader)

with open("SRC/Config/items.yml", "r") as ymlfile:
  items = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Introduction:
  def class_selection(profession: str) -> None:
    ui.notify(f'You chose {profession}')
    app.storage.user.update({"class": profession})
    # ui.chat_message(text=profession, sent=True)

  def gender_selection(gender: str) -> None:
    ui.notify(gender)
    app.storage.user.update({"gender": gender})
  
  def race_selection(race: str) -> None:
    ui.notify(race)
    app.storage.user.update({'race': race})

  async def main(username:str) -> None:
    ui.button(text='Logout', on_click=lambda: ui.navigate.to('/login'))
    if username == None: username = 'Default_User_1' # checks for blank username

    if not config['debug']['flags']['disable_intro']:
      ui.chat_message(name=names['narrator'], text=[f'welcome {username} to Mo\'kin', 'A Realm of knights and magic'])
      await Delays.medium_delay() # check debug flags
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
        with ui.grid(columns=3): # race selection
          ui.button(text='Human', on_click=lambda: Introduction.race_selection('Human'))
          ui.button(text='Aasimar', on_click=lambda: Introduction.race_selection('Aasimar'))
          ui.button(text='Dragonborn', on_click=lambda: Introduction.race_selection('Dragonborn'))
          ui.button(text='Dawrf', on_click=lambda: Introduction.race_selection('Dwarf'))
          ui.button(text='Elf', on_click=lambda: Introduction.race_selection('Elf'))
          ui.button(text='Gnome', on_click=lambda: Introduction.race_selection('Gnome'))
          ui.button(text='Orc', on_click=lambda: Introduction.race_selection('Orc'))
          ui.button(text='Tiefling', on_click=lambda: Introduction.race_selection('Tiefling'))
          ui.button(text='Halfing', on_click=lambda: Introduction.race_selection('halfing'))
      ui.button(text='Complete Character', on_click=lambda: character_building_default())
      ui.button(text='check inventory', on_click=lambda: item_fetch.fetch_item('Warlock_staff'))
      async def character_building_default():

        # building inventory
        match(app.storage.user.get("class")):
          case "Warrior":
            pass
          case "Bard":
            pass
          case "Cleric":
            pass
          case "Druid":
            pass
          case "Fighter":
            pass
          case "Monk":
            pass
          case "Paladin":
            pass
          case "ranger":
            pass
          case "Rogue":
            pass
          case "Sorcerer":
            pass
          case "Warlock":
            pass
          case "Wizard":
            starter = {'inventory': items['Leather Armor']}

        app.storage.user.update(starter)

        # building stats
        '''
        27 points total

        attributes
          strength
          dexterity
          constitution
          intelligence
          wisdom
          charisma
        '''
        match(app.storage.user.get('race')): # let player define?
          case 'Human':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Aasimar':
              app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Dragonborn':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Dwarf':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Elf':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Gnome':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Orc':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Tiefling':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

          case 'Halfing':
            app.storage.user.update({
              'strength': 10,
              'dexterity': 10,
              'constitution': 10,
              'intelligence': 10,
              'wisdom': 10,
              'charisma': 10
            })

      intro_selection = Dice.roll_d3(debug=True)
      if intro_selection == 1: # tavern
        pass
      elif intro_selection == 2: # kidnapping
        pass
      elif intro_selection == 3: # TBD
        pass
      
      # print(f'wisdom: {app.storage.user.get('wisdom')}')

    else:
      ui.label('Intro is disabled via flags')
