import xbmc

# Credit to tonywagner
# https://forum.kodi.tv/showthread.php?tid=262745&pid=3193408#pid3193408

path='plugin://plugin.video.mlbtv/?mode=111'
xbmc.executebuiltin(f'PlayMedia({path})')
