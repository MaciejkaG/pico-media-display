from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
import select
import sys
import time
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
screenSize = 16

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
i = 0


poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

while True:
    poll_results = poll_obj.poll(1)
    if poll_results:
        data = sys.stdin.readline().strip()
        data = data.split("\\\\")
        try:
            album_title = data[0]
            title = data[1]
            album_artist = data[2]
        except:
            pass
        else:
            title = title + " @ " + album_title
            titleParts = [title[i:i+screenSize] for i in range(0, len(title), screenSize)]
            artistParts = [album_artist[i:i+screenSize] for i in range(0, len(album_artist), screenSize)]
            for x in range(max(len(titleParts), len(artistParts))):
                lcd.clear()
                try:
                    str1 = titleParts[x]
                except IndexError:
                    str1 = titleParts[-1]
                try:
                    str2 = artistParts[x]
                except IndexError:
                    str2 = artistParts[-1]
                if str1==titleParts[-1]:
                    lcd.putstr(str1+" "*(screenSize-len(str1))+str2)
                else:
                    lcd.putstr(str1+"\n"+str2)
                sleep(2)
        lcd.clear()
    else:
        lcd.clear()
        lcd.putstr("Oczekiwanie na  dane")
        sleep(3)
