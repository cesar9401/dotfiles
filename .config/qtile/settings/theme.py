#
# cesar31
# https://github.com/cesar9401
#

from os import path, chdir, listdir
from .path import qtile_path
import json
import random

# set theme
def load_theme():
    theme = getTheme()
    theme_file = path.join(qtile_path, "themes", theme)
    with open(theme_file) as jsonfile:
        return json.load(jsonfile)

# get a theme randomly
def getTheme():
    themes = []
    for file in listdir(path.join(qtile_path, "themes")):
        themes.append(file)

    item = random.choice(tuple(themes))
    return item
