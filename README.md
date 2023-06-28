# Pico Media Display
NOTE: The program is designed to use on a Raspberry Pi Pico running MicroPython with an I2C 16x2 LCD but can be used with other 2-line displays, just change the ``screenSize`` variable in ``pico.py`` to your display's width.<br>
Basically the ``sendInfo.py`` file is supposed to run on the PC connected through USB to a Pico running ``pico.py`` script (but it should be named ``main.py`` in order to run automatically on Pico's startup).<br>
**The script also formats and animates the text when it's longer than 16.**
## The ``pico.py`` script is written using [T-622/RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD) package so you need it for the program to work.
