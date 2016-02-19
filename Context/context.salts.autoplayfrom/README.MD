Figured some people might find this useful if your internet is sometimes throttled like mine.
This is a context menu item that will let you select the maximum quality to start autoplaying from for a library item, then start autoplaying, If activated from not a movie or episode it will just open SALTS settings
 
Choosing quality just once should automatically set the max quality back to what you had it as before.

Choosing quality always will keep the change

http://i.imgur.com/kPF5saw.jpg

You can also activate it straight from a key by editing your keymap.xml
http://kodi.wiki/view/Keymap

Putting this in keymap.xml will activate the script when you press ctrl+enter on a library item.
<keymap>
    <videos>
        <keyboard>
            <return mod="ctrl">runscript(context.salts.autoplayfrom)</return>
        </keyboard>
    </videos>
</keymap>

SALTS has a setting for max mv and ep quality, this just sets it to whatever then start autoplay.
timeout in addon.py is the time untill it sets the quality back to normal when selecting just once.
The script will create a small file in kodi cache, just to backup the normal salts settings incase the script is launched more than once in 40 seconds.
if it normaly takes you longer than 40 seconds before autoplay starts change timeout to something longer
