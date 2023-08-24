# Pico Media Display
Basically the ``sendInfo.py`` file is supposed to run on the PC connected through USB to a Pico running ``pico.py`` script (but it should be named ``main.py`` in order to run automatically on Pico's startup).<br>
**The script also formats and animates the text when it's longer than the defined screen size.**
### Important notes
- The ``pico.py`` script is written using [T-622/RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD) package so you need it for the program to work.
- The program uses serial communication so it's important that you have Thonny or any other program using it too disabled.
- The program is designed to run on a Raspberry Pi Pico running MicroPython with an I2C 16x2 LCD but can be used with other 2-line displays, just change the ``screenSize`` variable in ``pico.py`` to your display's width.
- Currently the program only shows media from Spotify as it's the most common media service and different services use the Windows media API in a different way.
