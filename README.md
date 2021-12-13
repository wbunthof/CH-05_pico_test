# pico-micropython-pycharm-template
## Template for MicroPython on Raspberry Pi Pico on PyCharm

The steps for using this template are in this order.

1. [Copy this repo as a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) or [using the command line:](https://stackoverflow.com/questions/62630485/is-it-possible-to-create-a-new-git-repository-from-a-template-only-using-the-com)
   - git clone \<link> 
   - remove the .git folder
   - git init .
   - git add .
   - git commit -m "Commit from template"
   - git push -u origin master
   

2. If the MicroPython plugin for PyCharm is not installed, install it.
   - Go to File &#8594; Settings &#8594; Plugins &#8594; Marketplace
   - Search for MicroPython and install it.


3. Download the MicroPython UF2 file for the pico from Raspberry Pi [downloadable UF2](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2). This can also be found in this project.<br>
**Note, that the file in this project might not be the newest version.**


4. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is connected.


5. It will mount as a Mass Storage Device called RPI-RP2.


6. Drag and drop the MicroPython UF2 file onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython.


7. Now enable the MicroPython plugin
   - Go to File &#8594; Settings &#8594; Languages & Frameworks &#8594; MicroPython
   - **&#9745; Enable MicroPython support**
   - Set Device type &#8594; **Pyboard**
   - Set Device path: COM_<br> 
     _Example: COM1_
   - Press **OK** to confirm.


8. On the top of the main.py script is a yellow notice some packages are required. Press **Missing required MicroPython packages** to install.


9. Start programming! <br>
   _Example:_
 ``` python
 from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    print('Hello World')
    led(1)
    time.sleep(1)
    led(0)
    time.sleep(1)
 ```

10. Flash the code to the Pico
    - Right-click on the root folder or the single file and press **Run 'Flash xxx'**
    - The console shows progression and completion or fails.
    - **Note, when directly cloning this repo make sure that unnecessary files aren't flashed to the pico as it fills up precious space.**


11. If you want to see the results such as ``print()`` in your console go to:
    - Tools &#8594; MicroPython &#8594; MicroPython REPL
    - If nothing is showed press ctrl+D the soft restart the program.
    - **Note, flashing is only possible when MicroPython REPL is not active.**







## Useful links
[MicroPython](http://www.MicroPython.org/) <br>
[MicroPython - Quick reference for the PR2 (Raspberry Pico)](https://docs.MicroPython.org/en/latest/rp2/quickref.html) <br>
[MicroPython - Docs](https://docs.MicroPython.org/en/latest/index.html) <br>
[Adafruit - Welcome to MicroPython]() <br>
