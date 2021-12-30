"""
DIY Disney Magic Band
---------------------

Project to demonstrate how one could use near-field communication
technology with RFIDs similar to Disney World parks and resorts.

Hardware
--------
- Raspberry Pi Pico
- Neopixels
- RFID Reader (RC-522)
- USB Micro Cable (data)

Casing
------
I 3d printed part of this project (https://www.thingiverse.com/thing:4460759) for 
demonstrating. There seems to be fitting issues. But if you don't have a 3d printer
one could easily mock something up with old cardboard boxes and wax/parchment paper.

Software
--------
- Python (MicroPython) see: https://micropython.org
- mfrc522 module
- neopixel module (https://github.com/blaz-r/pi_pico_neopixel)
"""

from mfrc522 import MFRC522
import utime
import time
import neopixel

TOTAL_PIXELS = 19
LAST_LED = 0
COLORS = {
    "red": (0, 255, 0),
    "electricred": (228, 3, 3),
    "orange": (255, 165, 0),
    "dark orange": (255, 140, 0),
    "yellow": (255, 255, 0),
    "canaryyellow": (255, 237, 0),
    "green": (255, 0, 0),
    "lasallegreen": (0, 128, 38),
    "blue": (0, 0, 255),
    "patriarch": (117, 7, 135),
    "lightblue": (153, 204, 255),
    "white": (255, 255, 255),
    "purple": (0, 153, 153),
    "gray": (128, 128, 128),
    "stitch": (0, 39, 144),
    "rainbow": (0, 0, 0),
    "pride": (0, 0, 1),
}

pixels = neopixel.Neopixel(TOTAL_PIXELS, 0, 18, "RGB")
reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)


def action_led_fill(color, brightness=50, sleep=0):
    """Utility to fill without"""
    pixels.fill(color)
    pixels.show()
    time.sleep(sleep)


def action_led_color(index, color, brightness=50, sleep=0):
    """Utility to fill without"""
    pixels.set_pixel(index, color)
    pixels.brightness(brightness)
    pixels.show()
    time.sleep(sleep)


def action_led_off(sleep=0):
    """Turn off whatever action back to black"""
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(sleep)


def loading_step(LAST_LED):
    """Idle animation - seen when no tag is present
    
    This needs to be interupted when comes in contact with a tag.
    """
    if LAST_LED >= TOTAL_PIXELS:
        action_led_off()
        action_led_color(0, COLORS["white"])
        return 1
    else:
        action_led_color(LAST_LED, COLORS["white"])
        return LAST_LED + 1


def success_animation(state="default"):
    """LED animation triggered by an id found in the `good_ids` store"""
    clock_wise_steps = [i for i in range(TOTAL_PIXELS - 1)][::-1]
    if state == "default":
        for i in clock_wise_steps:
            action_led_color(i, COLORS["lasallegreen"], brightness=100, sleep=0.05)
        action_led_off()
        for i in clock_wise_steps:
            action_led_color(i, COLORS["lasallegreen"], brightness=100, sleep=0.05)
        action_led_off()


def fail_animation():
    pixels.fill(COLORS["red"])
    pixels.show()
    utime.sleep(2)
    pixels.fill((0, 0, 0))
    pixels.show()


def do_lights_on(color, TOTAL_PIXELS):
    for i in range(TOTAL_PIXELS - 1):
        pixels.set_pixel(i, color)
    pixels.show()


print("\nPlace magicband on reader\n")


good_ids = [[0x51, 0x50, 0xA3, 0x1A]]

try:
    while True:
        reader.init()
        LAST_LED = loading_step(LAST_LED)
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                pixels.fill((0, 0, 0))
                pixels.show()
                print(
                    "Band Dectected: {}  uid={}".format(
                        hex(int.from_bytes(bytes(uid), "little", False)).upper(),
                        reader.tohexstring(uid),
                    )
                )
                if uid in good_ids:
                    print(f"*** {uid} PASSING ***")
                    success_animation()
                else:
                    print(f"---{uid} FAIL---")
                    fail_animation()
        else:
            pass
        utime.sleep_ms(50)

except KeyboardInterrupt:
    print("Close")
