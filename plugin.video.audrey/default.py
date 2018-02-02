from lib import audrey

"""
If you want to create your own addon using Audrey you just need to require it in the addon.xml and then pass your feed and feed type to the feedme() function

feedme(string feed, string type)

feed (string) Path or URL to json file
type (string) Either "file" or "url" depending on where the file is located

Commented example below, will call Audrey with a local file stored in the addons main folder
"""
#import os, xbmcaddon
#addon=xbmcaddon.Addon()
#home=xbmc.translatePath(addon.getAddonInfo('path'))
#audrey.feedme(os.path.join(home, '', "sites.json"), "file")

audrey.feedme()