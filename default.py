import sys
import urllib.parse
import urllib.request
import json
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

# The full add-on URL is passed as sys.argv[0]
addon_url = sys.argv[0]

# Extract the handle from the URL
# The handle is typically the integer part of the URL before the '?'

try:
    addon_handle = int(sys.argv[1])
except (IndexError, ValueError):
    xbmc.log("Error: Add-on handle not provided for script. Exiting.")
    exit()

# Parse the URL to get the query parameters
original_url = str(sys.argv[2]).replace('?url=', '')

# Rewrite the URL based on your logic
# This is where you'd put your custom code
    
rewritten_url = original_url

if 'player.stv.tv' in original_url:
    response = urllib.request.urlopen('https://player.api.stv.tv/v1/streams/stv/')
    data = response.read()

    try:
        data = json.loads(data)

        if data['success']:
            original_url = data['results']['streamUrl']
            rewritten_url = original_url
    except Exception as e:
        pass

# Create a list item and set the URL
list_item = xbmcgui.ListItem(path=rewritten_url)

# Play the rewritten URL
xbmcplugin.setResolvedUrl(addon_handle, True, listitem=list_item)
