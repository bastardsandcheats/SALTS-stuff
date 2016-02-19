import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import time

# Change this if it takes longer to scrape and autoplay
# Timeout until revert to normal max quality
timeout = 40
tempfile = 'special://temp/context.salt.autoplayfrom.bac'
SALTS = xbmcaddon.Addon('plugin.video.salts')

line = xbmcvfs.File(xbmc.getInfoLabel('ListItem.FileNameAndPath')).read()
if 'plugin.video.salts' in line:
    epqul = 'Episode_quality'
    mvqul = 'Movie_quality'

    if xbmcvfs.exists(tempfile):                        # backup file should have got deleted after settings were reset
        f = xbmcvfs.File(tempfile, 'r')                 # since its there the values didn't get changed back
        backupepqul, backupmvqul = f.read().split()     # script must have been run twice before timeout
        SALTS.setSetting(epqul, ('%s' % backupepqul))   # lets set the values back and delete the file
        SALTS.setSetting(mvqul, ('%s' % backupmvqul))   # before starting
        f.close()
        xbmcvfs.delete(tempfile)

    line = line.replace('mode=get_sources', 'mode=autoplay')
    Quls = (
            '1080P just once',
            '720P just once',
            'High just once',
            'Medium just once',
            'Low just once',
            '1080P always',
            '720P always',
            'High always',
            'Medium always',
            'Low always'
            )

    selqul = xbmcgui.Dialog().select('Autoplay starting from', Quls)
    if selqul > -1:
        if selqul < 5:
            curepqul = SALTS.getSetting(epqul)
            curmvqul = SALTS.getSetting(mvqul)
            f = xbmcvfs.File(tempfile, 'w')
            f.write('%s %s' % (curepqul, curmvqul))
            f.close()
            SALTS.setSetting(epqul, ('%s' % selqul))
            SALTS.setSetting(mvqul, ('%s' % selqul))
            xbmc.executebuiltin('XBMC.Notification(SALTS trying autoplay,Seting max quality to %s, 5000,)' % Quls[selqul])
            xbmc.executebuiltin('playmedia(%s)' % line)

            if (xbmc.Player().isPlayingVideo()):
                time.sleep(timeout)

            else:
                t = time.time()
                time.sleep(5)
                while time.time() <= t + timeout:
                    if (xbmc.Player().isPlayingVideo()):
                        break

                    else:
                        time.sleep(1)

            SALTS.setSetting(epqul, curepqul)
            SALTS.setSetting(mvqul, curmvqul)
            xbmcvfs.delete(tempfile)

        else:
            selqul -= 5
            SALTS.setSetting(epqul, ('%s' % selqul))
            SALTS.setSetting(mvqul, ('%s' % selqul))
            selqul += 5
            xbmc.executebuiltin('XBMC.Notification(SALTS trying autoplay ,Seting max quality to %s, 5000, )' % Quls[selqul])
            xbmc.executebuiltin('playmedia(%s)' % line)

    else:
        xbmc.executebuiltin('XBMC.Notification(User exited selection, not changing anything, 1000, )')

else:
    xbmc.executebuiltin('XBMC.Notification(Not a salts library item, Opening SALTS settings, 1000, )')
    xbmc.executebuiltin('Addon.OpenSettings(plugin.video.salts)')
