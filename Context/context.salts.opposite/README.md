From library

Single click do opposite of salts default autoplay setting. 
When activated on a salts movie or episode library item do opposite of salts default autoplay.

When autoplay enabled - select source
When autoplay disabled - autoplay

There's already a item for this in SALTS Context Tools
This is the same thing without a menu to reduce the amount of clicks, cause... lazyness 

My prefer method of activating it is from a key
http://kodi.wiki/view/Keymap

Putting this in keymap.xml will activate the script when you press ctrl, shift + enter on a library item.
<keymap>
    <videos>
        <keyboard>
            <return mod="ctrl, shift">runscript(context.salts.opposite)</return>
        </keyboard>
    </videos>
</keymap>

Code is taken from SALTS Context Tools and all credits go to TKnorris
