import xbmcaddon
import xbmcgui
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

os.system('pactl load-module module-udev-detect')
os.system('amixer cset numid=3 1')
# Set a string variable to use
line1 = "Bluetooth Audio auf Line out gestartet"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)