import yaml
from nicegui import ui, app
from typing import Optional

with open('SRC/Config/save_file_format.yml', 'r') as ymlfile:
    SFF = yaml.load(ymlfile, Loader=yaml.SafeLoader)

class item_fetch():
    def fetch_item(item: Optional[str] = ''):
        # item_list = app.storage.user.get()
        item_list = [{'Warlock_staff':True, 'Warlock_boots':True}]
        if item == '' or item == None:
            ui.notify('item was empty')
        else:
            for item_dict in item_list:
                if item_dict.get(item): # .get uses key to fetch
                    ui.notify('inv pass')
