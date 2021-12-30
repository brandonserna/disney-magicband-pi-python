# Disney Magic Bands

A project to demonstrate how someone could use near-field communication technology with RFIDs similar to the Disney World parks and resorts. No sound yet just the reader and LEDs. The core of this project can be built for about $10 in parts.

![](./magicband.gif)

## Hardware

- Raspberry Pi Pico
- Neopixels
- RFID Reader (RC-522)
- USB Micro Cable (data)

## Software

* Micropython
* Attached modules

Firmware is in the `code.py` file. It's not the cleanest but if I get more time I will do something better about the led class.

## Tools

- Adhesive for leds and whatever casing you use
- Thin wires (jumper wire or other 22-28 gauge to connect)
- Soldering iron (unless you can find versions with the header pins pre-soldered and led connector clips for the LEDs)

## Notes

__3D Print__ the design linked below seems to not fit properly from the clear mickey ring to the back panel. I considered trying to sand or cut down the back panel to make it fit but since the cut is so intricate any sanding or cutting by hand wouldn't work. It seems like it's ~1mm-2mm too large. New design or fix current stl. Also for the light to show up transpearant filament is best I tried PETG for the outter ring and mickey ring. 


__RFID Identifiers__ if you don't know the ids for your bands you could run [this script](https://github.com/kevinmcaleer/pico-rfid/blob/main/ndef_read.py) to store them for reference


## References

I wouldn't have been able to get this far without these great projects, a huge thank you for the work they've done 👏

[foolishmortalbuilders](https://github.com/foolishmortalbuilders/magicbandreader)

[pico neopixel module](https://github.com/blaz-r/pi_pico_neopixel)

[Disney World MagicBand reader v2 thingiverse design](https://www.thingiverse.com/thing:4460759)

[Kevin McAleer RFID Pico video](https://youtu.be/hV9GTqXLMpg)
