# Lapymod

This is a simple wrapper for the Labymod API.

## Installation

```pip install lapymod```

## Usage

```
import lapymod

#This creates a user that lets you query and update their data.
user = lapymod.User('34e57efa578346c7a9fc890296aaba1f') #(The uuid of LabyStudio -- an admin for Labymod)

#Returns all emotes for the user into a list.
emotes = user.getEmotes()

#Returns all cosmetics for the user into a list.
cosmetics = user.getCosmetics()

#Returns all stickers for the user into a list.
stickers = user.getStickers()

#Returns all roles for the user into a list.
roles = user.getRoles()

#Returns all of the above functions in one nice easy to use dictionary.
all_data = user.getAllData()

#You can change the user while you go.
user.setUser('32645503-0d51-4fc6-8e4a-28b03714db5e') #(The uuid of LabyMarco -- another admin for Labymod)

#When you either want new data for the user or want to change the data with a new supplied user, update it!
user.update()

#Returns True/False if the module is able to connect to the Labymod API.
api_status = lapymod.getStatus()

#Returns the current daily shop emotes in a list.
shop_emotes = lapymod.getShopEmotes()
```
