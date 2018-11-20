"""Default settings and configuration for audio reactive LED strip"""
from __future__ import print_function
from __future__ import division
import os

use_defaults = {"configuration": True,                              # See notes below for detailed explanation
                "GUI_opts": False,
                "devices": False,
                "mic_config": False}

settings = {                                                        # All settings are stored in this dict
    "configuration":{  # Program configuration
                     'USE_GUI': True,                               # Whether to display the GUI
                     'DISPLAY_FPS': False,                          # Whether to print the FPS when running (can reduce performance)
                     'FPS': 60,                                     # Desired refresh rate of the visualization (frames per second)
                     'MAX_BRIGHTNESS': 100,                         # Max brightness sent to LED strip
                     'N_ROLLING_HISTORY': 4,                        # Number of past audio frames to include in the rolling window
                     'MIN_VOLUME_THRESHOLD': 0.001                  # No music visualization displayed if recorded audio volume below threshold
                    #'LOGARITHMIC_SCALING': True,                   # Scale frequencies logarithmically to match perceived pitch of human ear
                     },

    "GUI_opts":{"Graphs":True,                                      # Which parts of the gui to show
                "Reactive Effect Buttons":True,
                "Non Reactive Effect Buttons":True,
                "Frequency Range":True,
                "Effect Options":True,
                "Maximized Window":True,
                "Window Size X":640,
                "Window Size Y":480,
                "Window Position X":640,
                "Window Position Y":480},

    # DO NOT MANUALLY ADD STUFF BELOW HERE UNLESS YOU KNOW WHAT YOU ARE DOING.
    # These dicts are generated by the program at runtime, usually from settings.ini

    # All devices and their respective settings.
    "devices":{},
    # mic settings
    "mic_config":{},
}

colour_manager = {
    # DON'T FIDDLE WITH THIS EITHER
    # saved colours
    "default_colours":{},
    # saved colours
    "default_gradients":{},
    # saved colours
    "user_colours":{},
    # saved gradients
    "user_gradients":{}
}

# Required config used by GUI to generate add board interface
device_req_config = { "ESP8266"    : {"AUTO_DETECT": ["Auto Detect",
                                      "Automatically detect device on network using MAC address",
                                      "checkbox",
                                      False],
                      "MAC_ADDR"   : ["Mac Address",
                                      "Hardware address of device, used for auto-detection",
                                      "textbox",
                                      "aa-bb-cc-dd-ee-ff"],
                      "UDP_IP"     : ["IP Address",
                                      "IP address of device, used if auto-detection isn't active",
                                      "textbox",
                                      "192.168.0.201"],
                      "UDP_PORT"   : ["Port",
                                      "Port used to communicate with device",
                                      "textbox-int",
                                      "7778"]},
                     "Stripless"   : None, # duh
                     "BlinkStick"  : None,
                     "DotStar"     : None,
                     "RaspberryPi" : {"LED_PIN"    : ["LED Pin",
                                                      "GPIO pin connected to the LED strip RaspberryPi (must support PWM)",
                                                      "textbox-int",
                                                      "10"],
                                      "LED_FREQ_HZ": ["LED Frequency",
                                                      "LED signal frequency in Hz",
                                                      "textbox-int",
                                                      "800000"],
                                      "LED_DMA"    : ["DMA Channel",
                                                      "DMA channel used for generating PWM signal",
                                                      "textbox-int",
                                                      "5"],
                                      "LED_INVERT" : ["Invert LEDs",
                                                      "Set True if using an inverting logic level converter",
                                                      "checkbox",
                                                      True]},
                     "Fadecandy"   : {"SERVER"     : ["Server Address",
                                                      "Address of Fadecandy server",
                                                      "textbox",
                                                      "localhost:7890"]}
                     }

# General config used by GUI to generate add board interface
device_gen_config = {"NAME"         : ["Name",
                                       "Name of LED strip",
                                       "textbox",
                                       "HalcyonCeilingIllumination01"],
                     "N_PIXELS"     : ["No. of LEDs",
                                       "Number of LEDs on this strip",
                                       "textbox-int",
                                       "120"],
                     "N_FFT_BINS"   : ["No. of FFT Bins",
                                       "Number of frequency bins to use when transforming audio to frequency domain",
                                       "textbox-int",
                                       "24"],
                     "MIN_FREQUENCY": ["Min Frequency",
                                       "Frequencies below this value will be removed during audio processing",
                                       "textbox-int",
                                       "20"],
                     "MAX_FREQUENCY": ["Max Frequency",
                                       "Frequencies above this value will be removed during audio processing",
                                       "textbox-int",
                                       "18000"]
                     }

# Default general config for any new device
default_general_config = {"N_PIXELS": 120,                            # Number of pixels in the LED strip (must match ESP8266 firmware)
                          "N_FFT_BINS": 24,                           # Number of frequency bins to use when transforming audio to frequency domain
                          "MIN_FREQUENCY": 20,                        # Frequencies below this value will be removed during audio processing
                          "MAX_FREQUENCY": 18000,                     # Frequencies above this value will be removed during audio processing
                          "current_effect": "Scroll"}                 # Currently selected effect for this board, used as default when program launches

# Default effect opts for any new device
default_effect_opts = {"Energy":    {"blur": 1,                       # Amount of blur to apply
                                     "scale":0.9,                     # Width of effect on strip
                                     "r_multiplier": 1.0,             # How much red
                                     "mirror": True,                  # Reflect output down centre of strip
                                     "g_multiplier": 1.0,             # How much green
                                     "b_multiplier": 1.0},            # How much blue
                       "Wave":      {"color_wave": "Red",             # Colour of moving bit
                                     "color_flash": "White",          # Colour of flashy bit
                                     "wipe_len":5,                    # Initial length of colour bit after beat
                                     "decay": 0.7,                    # How quickly the flash fades away 
                                     "wipe_speed":2},                 # Number of pixels added to colour bit every frame
                       "Spectrum":  {"r_multiplier": 1.0,             # How much red
                                     "g_multiplier": 1.0,             # How much green
                                     "b_multiplier": 1.0},            # How much blue
                       "Wavelength":{"roll_speed": 0,                 # How fast (if at all) to cycle colour overlay across strip
                                     "color_mode": "Spectral",        # Colour gradient to display
                                     "mirror": False,                 # Reflect output down centre of strip
                                     "reverse_grad": False,           # Flip (LR) gradient
                                     "reverse_roll": False,           # Reverse movement of gradient roll
                                     "blur": 3.0,                     # Amount of blur to apply
                                     "flip_lr":False},                # Flip output left-right
                       "Scroll":    {"lows_color": "Red",             # Colour of low frequencies
                                     "mids_color": "Green",           # Colour of mid frequencies
                                     "high_color": "Blue",            # Colour of high frequencies
                                     "decay": 0.995,                  # How quickly the colour fades away as it moves
                                     "speed": 4,                      # Speed of scroll
                                     "mirror": True,                  # Reflect output down centre of strip
                                     "r_multiplier": 1.0,             # How much red
                                     "g_multiplier": 1.0,             # How much green
                                     "b_multiplier": 1.0,             # How much blue
                                     "blur": 0.2},                    # Amount of blur to apply
                       "Power":     {"color_mode": "Spectral",        # Colour gradient to display
                                     "s_count": 20,                   # Initial number of sparks
                                     "s_color": "White",              # Color of sparks
                                     "mirror": True,                  # Mirror output down central axis
                                     "flip_lr":False},                # Flip output left-right
                       "Pulse":     {"bar_color": "Purple",        # Colour gradient to display
                                      "bar_speed": 5,                   # Initial number of sparks
                                      "bar_length": 5,              # Color of sparks
                                      "color_mode": "Spectral"},                # Flip output left-right
                       "Single":    {"color": "Purple"},              # Static color to show
                       "Beat":      {"color": "Red",                  # Colour of beat flash
                                     "decay": 0.7},                   # How quickly the flash fades away
                       "Bars":      {"resolution":4,                  # Number of "bars"
                                     "color_mode":"Spectral",         # Multicolour mode to use
                                     "roll_speed":0,                  # How fast (if at all) to cycle colour colours across strip
                                     "mirror": False,                 # Mirror down centre of strip
                                     "reverse_roll": False,           # Reverse movement of gradient roll
                                     "flip_lr":False},                # Flip output left-right
                       "Gradient":  {"color_mode":"Spectral",         # Colour gradient to display
                                     "roll_speed": 0,                 # How fast (if at all) to cycle colour colours across strip
                                     "mirror": False,                 # Mirror gradient down central axis
                                     "reverse": False},               # Reverse movement of gradient
                       "Fade":      {"color_mode":"Spectral",         # Colour gradient to fade through
                                     "blur": 3.0,                     # Amount of blur to apply
                                     "roll_speed": 1,                 # How fast (if at all) to fade through colours
                                     "mirror": False,
                                     "reverse": False},               # Reverse "direction" of fade (r->g->b or r<-g<-b)
                       "Calibration":{"r": 100,                       # Red value
                                      "g": 100,                       # Green value
                                      "b": 100}                       # Blue value
                       }
# Configurations for dynamic ui generation. Effect options can be changed by widgets created at runtime,
# meaning that you don't need to worry about the user interface - it's all done for you. All you need to
# do is add items to this dict below.
#
# First line of code below explained (as an example):
#   "Energy" is the visualization we're doing options for
#   "blur" is the key in the options dict (config.settings["devices"][self.board]["effect_opts"]["Energy"]["blur"])
#   "Blur" is the string we show on the GUI next to the slider
#   "float_slider" is the GUI element we want to use
#   (0.1,4.0,0.1) is a tuple containing all the details for setting up the slider (see above)
#
# Each effect key points to a list. Each list contains lists giving config for each option.
# Syntax: effect:[key, label_text, ui_element, opts]
#   effect     - the effect which you want to change options for. MUST have a key in config.settings["devices"][board]["effect_opts"]
#   key        - the key of thing you want to be changed. MUST be in config.settings["devices"][board]["effect_opts"][effect], otherwise it won't work.
#   label      - the text displayed on the ui
#   ui_element - how you want the variable to be changed
#   opts       - options for the ui element. check below for what each ui element needs.
# UI Elements + opts:
#   slider, (min, max, interval)                   (for integer values in a given range)
#   float_slider, (min, max, interval)             (for floating point values in a given range)
#   checkbox, *leave blank*                        (for True/False values)
#   dropdown, (dict, list, "colours"/"gradients")  (dict/list, example see below. Keys will be displayed in the dropdown if dict, otherwise just list items. "colours" or "gradients" will handle colour/grad selection for you
#
# Hope this clears things up a bit for you! GUI has never been easier..? The reason for doing this is
# 1 - To make it easy to add options to your effects for the user
# 2 - To give a consistent GUI for the user. If every options page was set out differently it would all be a mess
dynamic_effects_config = {"Energy":[["blur", "Blur", "float_slider", (0.1,4.0,0.1)],
                                    ["scale", "Scale", "float_slider", (0.4,1.0,0.05)],
                                    ["r_multiplier", "Red", "float_slider", (0.05,1.0,0.05)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["g_multiplier", "Green", "float_slider", (0.05,1.0,0.05)],
                                    ["b_multiplier", "Blue", "float_slider", (0.05,1.0,0.05)]],
                            "Wave":[["color_flash", "Flash Color", "dropdown", "colours"],
                                    ["color_wave", "Wave Color", "dropdown", "colours"],
                                    ["wipe_len", "Wave Start Length", "slider", (0,50,1)],
                                    #["wipe_len", "Wave Start Length", "slider", (0,config.settings["devices"][self.board]["configuration"]["N_PIXELS"]//4,1)],
                                    ["wipe_speed", "Wave Speed", "slider", (1,10,1)],
                                    ["decay", "Flash Decay", "float_slider", (0.1,1.0,0.05)]],
                        "Spectrum":[["r_multiplier", "Red", "float_slider", (0.05,1.0,0.05)],
                                    ["g_multiplier", "Green", "float_slider", (0.05,1.0,0.05)],
                                    ["b_multiplier", "Blue", "float_slider", (0.05,1.0,0.05)]],
                      "Wavelength":[["color_mode", "Color Mode", "dropdown", "gradients"],
                                    ["roll_speed", "Roll Speed", "slider", (0,8,1)],
                                    ["blur", "Blur", "float_slider", (0.1,4.0,0.1)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["reverse_grad", "Reverse Gradient", "checkbox"],
                                    ["reverse_roll", "Reverse Roll", "checkbox"],
                                    ["flip_lr", "Flip LR", "checkbox"]],
                          "Scroll":[["lows_color", "Lows Color", "dropdown", "colours"],
                                    ["mids_color", "Mids Color", "dropdown", "colours"],
                                    ["high_color", "Highs Color", "dropdown", "colours"],
                                    ["blur", "Blur", "float_slider", (0.05,4.0,0.05)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["decay", "Decay", "float_slider", (0.97,1.0,0.0005)],
                                    ["speed", "Speed", "slider", (1,5,1)]],
                           "Power":[["color_mode", "Color Mode", "dropdown", "gradients"],
                                    ["s_color", "Spark Color ", "dropdown", "colours"],
                                    ["s_count", "Spark Amount", "slider", (0,20,1)],
                                    #["s_count", "Spark Amount", "slider", (0,config.settings["devices"][self.board]["configuration"]["N_PIXELS"]//6,1)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["flip_lr", "Flip LR", "checkbox"]],
                            "Pulse":[["bar_color", "Bar Color", "dropdown", "colours"],
                                    ["bar_speed", "Bar Speed", "slider", (0,9,1)],
                                    ["bar_length", "Bar Length", "slider", (0,20,1)],
                                    ["color_mode", "Color Mode", "dropdown", "gradients"]],
                          "Single":[["color", "Color", "dropdown", "colours"]],
                            "Beat":[["color", "Color", "dropdown", "colours"],
                                    ["decay", "Flash Decay", "float_slider", (0.3,0.98,0.005)]],
                            "Bars":[["color_mode", "Color Mode", "dropdown", "gradients"],
                                    ["resolution", "Resolution", "slider", (1, 24, 1)],
                                    #["resolution", "Resolution", "slider", (1, config.settings["devices"][self.board]["configuration"]["N_FFT_BINS"], 1)],
                                    ["roll_speed", "Roll Speed", "slider", (0,8,1)],
                                    ["flip_lr", "Flip LR", "checkbox"],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["reverse_roll", "Reverse Roll", "checkbox"]],
                        "Gradient":[["color_mode", "Color Mode", "dropdown", "gradients"],
                                    ["roll_speed", "Roll Speed", "slider", (0,8,1)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["reverse", "Reverse", "checkbox"]],
                            "Fade":[["color_mode", "Color Mode", "dropdown", "gradients"],
                                    ["blur", "Blur", "float_slider", (0.1,4.0,0.1)],
                                    ["roll_speed", "Fade Speed", "slider", (1,60,1)],
                                    ["mirror", "Mirror", "checkbox"],
                                    ["reverse", "Reverse", "checkbox"]],
                     "Calibration":[["r", "Red value", "slider", (0,255,1)],
                                    ["g", "Green value", "slider", (0,255,1)],
                                    ["b", "Blue value", "slider", (0,255,1)]]}

default_colours = {"Red":(255,0,0),
                   "Orange":(255,40,0),
                   "Yellow":(255,255,0),
                   "Green":(0,255,0),
                   "Blue":(0,0,255),
                   "Light blue":(0,247,161),
                   "Purple":(255,0,200),
                   "Pink":(255,0,178),
                   "White":(255,255,255),
                   "Black":(0,0,0)}

default_gradients = {"Spectral": [(255, 0, 0), (255, 40, 0), (255, 255, 0), (0, 255, 0), (0, 247, 161), (0, 0, 255), (255, 0, 200), (255, 0, 178)],
                     "Dancefloor": [(255, 0, 0), (255, 0, 178), (255, 0, 200), (0, 0, 255)],
                     "Sunset": [(255, 0, 0), (255, 40, 0), (255, 255, 0)],
                     "Ocean": [(0, 255, 0), (0, 247, 161), (0, 0, 255)],
                     "Jungle": [(0, 255, 0), (255, 0, 0), (255, 40, 0)],
                     "Sunny": [(255, 255, 0), (0, 247, 161), (255, 40, 0), (0, 0, 255)],
                     "Fruity": [(255, 40, 0), (0, 0, 255)],
                     "Peach": [(255, 40, 0), (255, 0, 178)],
                     "Rust": [(255, 40, 0), (255, 0, 0)],
                     "Good Night": [(200,00,0), (240, 0, 0), (220, 40, 0), (240, 30, 0), (250,15,0), (255,10,0)]
                     }
key_frames = { "breathing": [
  # Rising
  20, 21, 22, 24, 26, 28, 31, 34, 38, 41, 45, 50, 55, 60, 66, 73, 80, 87, 95,
  103, 112, 121, 131, 141, 151, 161, 172, 182, 192, 202, 211, 220, 228, 236,
  242, 247, 251, 254, 255,

  # Falling
  254, 251, 247, 242, 236, 228, 220, 211, 202, 192, 182, 172, 161, 151, 141,
  131, 121, 112, 103, 95, 87, 80, 73, 66, 60, 55, 50, 45, 41, 38, 34, 31, 28,
  26, 24, 22, 21, 20,
  20, 20, 20, 20, 20, 20, 20, 20, 20, 20,]
}

# plz ignore
# default_gradients = {"Spectral"  : ["Red", "Orange", "Yellow", "Green", "Light blue", "Blue", "Purple", "Pink"],
#                      "Dancefloor": ["Red", "Pink", "Purple", "Blue"],
#                      "Sunset"    : ["Red", "Orange", "Yellow"],
#                      "Ocean"     : ["Green", "Light blue", "Blue"],
#                      "Jungle"    : ["Green", "Red", "Orange"],
#                      "Sunny"     : ["Yellow", "Light blue", "Orange", "Blue"],
#                      "Fruity"    : ["Orange", "Blue"],
#                      "Peach"     : ["Orange", "Pink"],
#                      "Rust"      : ["Orange", "Red"]}
# 
# for gradient in default_gradients:
#   colours = []
#   for colour in default_gradients[gradient]:
#     colours.append(default_colours[colour])
#   print("\""+gradient+"\":", colours)

"""
    ~~ NOTES ~~
[use_defaults]
For any dicts in this file (config.py), you can add them into the use_defaults
dict to force the program to use these values over any stored in settings.ini
that you would have set using the GUI. At runtime, settings.ini is used to update
the above dicts with custom set values. 
If you're running a headless RPi, you may want to edit settings in this file, then
specify to use the dict you wrote, rather than have the program overwrite from 
settings.ini at runtime. You could also run the program with the gui, set the 
settings that you want, then disable the gui and the custom settings will still
be loaded. Basically it works as you would expect it to.
[DEVICE TYPE]
Device used to control LED strip.
'ESP8266' means that you are using an ESP8266 module to control the LED strip
and commands will be sent to the ESP8266 over WiFi. You can have as many of 
these as your computer is able to handle.
'RaspberryPi' means that you are using a Raspberry Pi as a standalone unit to process
audio input and control the LED strip directly.
'BlinkStick' means that a BlinkstickPro is connected to this PC which will be used
to control the leds connected to it.
'Fadecandy' means that a Fadecandy server is running on your computer and is connected
via usb to a Fadecandy board connected to LEDs
'DotStar' creates an APA102-based output device. LMK if you have any success 
getting this to work becuase i have no clue if it will.
'Stripless' means that the program will run without sending data to a strip.
Useful for development etc, but doesn't look half as good ;)
[REQUIRED CONFIGURATION KEYS]
===== 'ESP8266'
 "AUTO_DETECT"            # Set this true if you're using windows hotspot to connect (see below for more info)
 "MAC_ADDR"               # MAC address of the ESP8266. Only used if AUTO_DETECT is True
 "UDP_IP"                 # IP address of the ESP8266. Must match IP in ws2812_controller.ino
 "UDP_PORT"               # Port number used for socket communication between Python and ESP8266
===== 'RaspberryPi'
 "LED_PIN"                # GPIO pin connected to the LED strip pixels (must support PWM)
 "LED_FREQ_HZ"            # LED signal frequency in Hz (usually 800kHz)
 "LED_DMA"                # DMA channel used for generating PWM signal (try 5)
 "BRIGHTNESS"             # Brightness of LED strip between 0 and 255
 "LED_INVERT"             # Set True if using an inverting logic level converter
===== 'BlinkStick'
 No required configuration keys
===== 'Fadecandy'
 "SERVER"                 # Address of Fadecandy server. (usually 'localhost:7890')
===== 'DotStar'
 No required configuration keys
===== 'Stripless'
 No required configuration keys (heh)
[AUTO_DETECT]
Set to true if the ip address of the device changes. This is the case if it's connecting
through windows hotspot, for instance. If so, give the mac address of the device. This 
allows windows to look for the device's IP using "arp -a" and finding the matching
mac address. I haven't tested this on Linux or macOS.
[FPS]
FPS indicates the desired refresh rate, or frames-per-second, of the audio
visualization. The actual refresh rate may be lower if the computer cannot keep
up with desired FPS value.
Higher framerates improve "responsiveness" and reduce the latency of the
visualization but are more computationally expensive.
Low framerates are less computationally expensive, but the visualization may
appear "sluggish" or out of sync with the audio being played if it is too low.
The FPS should not exceed the maximum refresh rate of the LED strip, which
depends on how long the LED strip is.
[N_FFT_BINS]
Fast Fourier transforms are used to transform time-domain audio data to the
frequency domain. The frequencies present in the audio signal are assigned
to their respective frequency bins. This value indicates the number of
frequency bins to use.
A small number of bins reduces the frequency resolution of the visualization
but improves amplitude resolution. The opposite is true when using a large
number of bins. More bins is not always better!
There is no point using more bins than there are pixels on the LED strip.

Left in for manual device control
"TYPE": "ESP8266",                           # Device type (see below for all supported boards)
"AUTO_DETECT": True,                         # Set this true if you're using windows hotspot to connect (see below for more info)
"MAC_ADDR": "192.168.137.86",                # MAC address of the ESP8266. Only used if AUTO_DETECT is True
"UDP_IP": "YOUR IP HERE",                    # IP address of the ESP8266. Must match IP in ws2812_controller.ino
"UDP_PORT": 7778,                            # Port number used for socket communication between Python and ESP8266
"MAX_BRIGHTNESS": 250,                       # Max brightness of output (0-255) (my strip sometimes bugs out with high brightness)
"N_PIXELS": 100,                             # Number of pixels in the LED strip (must match ESP8266 firmware)
"N_FFT_BINS": 24,                            # Number of frequency bins to use when transforming audio to frequency domain
"MIN_FREQUENCY": 20,                         # Frequencies below this value will be removed during audio processing
"MAX_FREQUENCY": 18000,                      # Frequencies above this value will be removed during audio processing
"current_effect": "Scroll"                   # Currently selected effect for this board, used as default when program launches

"""

for board in settings["devices"]:
    if settings["devices"][board]["configuration"]["TYPE"] == 'ESP8266':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = False
        # Set to False because the firmware handles gamma correction + dither
    elif settings["devices"][board]["configuration"]["TYPE"] == 'RaspberryPi':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = True
        # Set to True because Raspberry Pi doesn't use hardware dithering
    elif settings["devices"][board]["configuration"]["TYPE"] == 'BlinkStick':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = True
    elif settings["devices"][board]["configuration"]["TYPE"] == 'DotStar':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = False
    elif settings["devices"][board]["configuration"]["TYPE"] == 'Fadecandy':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = False
    elif settings["devices"][board]["configuration"]["TYPE"] == 'Stripless':
        settings["devices"][board]["configuration"]["SOFTWARE_GAMMA_CORRECTION"] = False
    else:
        raise ValueError("Invalid device selected. Device {} not known.".format(settings["devices"][board]["configuration"]["TYPE"]))
    # Cheeky lil fix in case the user sets an odd number of LEDs
    if settings["devices"][board]["configuration"]["N_PIXELS"] % 2:
        settings["devices"][board]["configuration"]["N_PIXELS"] -= 1

# Ignore these
# settings["configuration"]['_max_led_FPS'] = int(((settings["configuration"]["N_PIXELS"] * 30e-6) + 50e-6)**-1.0)