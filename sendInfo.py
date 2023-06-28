import asyncio
import serial
from time import sleep
from anyascii import anyascii

import winsdk.windows.media as win
from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def getMediaInfo():
    sessions = await MediaManager.request_async()

    current_session = sessions.get_current_session()
    if current_session:
        info = await current_session.try_get_media_properties_async()

        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

        info_dict['genres'] = list(info_dict['genres'])

        return info_dict

def sendData(data : str):
    s = serial.Serial("COM3", 115200, timeout=5)
    s.flush()
    s.write(anyascii(data+"\n").encode('ascii'))
    s.read_until()

if __name__ == '__main__':
    while True:
        currentMediaInfo = asyncio.run(getMediaInfo())
        try:
            if currentMediaInfo and currentMediaInfo['playback_type']==win.MediaPlaybackType.MUSIC:
                sendData(f"{currentMediaInfo['album_title']}\\\\{currentMediaInfo['title']}\\\\{currentMediaInfo['album_artist']}")
        except:
            sleep(3)
            pass
