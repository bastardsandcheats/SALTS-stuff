"""
    Code is taken from SALTS Context Menu tools
    All credits tknorris
    https://forums.tvaddons.ag/tknorris-release-repository/
"""

import xbmc
import xbmcaddon
import xbmcvfs

line = xbmcvfs.File(xbmc.getInfoLabel('ListItem.FileNameAndPath')).read()
salts = 'plugin.video.salts'
addon = xbmcaddon.Addon(salts)

if salts in line:
    if addon.getSetting('auto-play') == 'true':
        line = line.replace('mode=get_sources', 'mode=select_source')
        msg = 'XBMC.Notification(SALTS Autoplay is enabled:, Opening source selection dialog, 5000, )'

    else:
        line = line.replace('mode=get_sources', 'mode=autoplay')
        msg = 'XBMC.Notification(SALTS Autoplay is disabled:, Trying autoplay, 7000, )'
    xbmc.executebuiltin(msg)
    xbmc.executebuiltin('playmedia(%s)' % line)

else:
    xbmc.executebuiltin('XBMC.Notification(Not a salts library item, Can not play from here, 2000, )')
