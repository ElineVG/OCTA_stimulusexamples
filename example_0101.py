"""
OCTA toolbox example stimuli
Example stimulus 101
created by Eline Van Geert

Recreated based on the official IAEA 2021 logo: https://twitter.com/IAEALondon2021/photo
Image used: IAEA logo from https://www.science-of-aesthetics.org/
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle, Text, Image
import random

# Define stimulus name
stimname = "example_0101"

random.seed(5)

# Define stimulus
stim = Concentric(31, background_color = "white", x_margin = (-115,-110), y_margin = (-57,-40), 
                  stim_orientation = ['animate', '0', '360', "begin = 'click', dur='3s', additive='sum'"])

# Change element positions
stim.positions = Positions.CreateCustomPositions( [0, 0, 0, 0, 0, -120, -90, -65, -45, -25, 5, 40, 65, 90, 115,
                                                  -80, -73, -68, -60, -52, -45, -40, -20, -8, 4, 14, 26, 40, 54, 66, 78],
                                                  [0, 0, 0, -60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  44, 40, 40, 44, 44, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 44] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(350,350), (320,320), (220,220), (120,150), (350, 50),
                                                       (20,20), (20,20), (20,20), (20,20), (20,20), (20,20),
                                                       (20,20), (20,20), (20,20), (20,20), (12,12), (10,10), (10,10),
                                                       (12,12), (12,12), (10,10), (10,10), (12,12), (12,12), (12,12),
                                                       (12,12), (12,12), (12,12), (12,12), (12,12), (12,12) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns([ Ellipse, Ellipse, Ellipse, Ellipse, Rectangle,
                                                Text('O'), Text('N'), Text('L'), Text('I'), Text('N'), Text('E'),
                                                Text('2'), Text('0'), Text('2'), Text('1'),
                                                Text('1'), Text('s'), Text('t'), Text('-'), Text('3'),
                                                Text('r'), Text('d'), Text('S'), Text('e'), Text('p'), 
                                                Text('t'), Text('e'), Text('m'), Text('b'), Text('e'), Text('r') ])

stim.set_element_shapes(shape_value = Image('img/IAEA.png'), element_id = 3)

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(['#FDFF00', "red",  "white", "white", "#2F5596",
                                                    "#FDFF00", "#FDFF00", "#FDFF00", "#FDFF00",  "#FDFF00", "#FDFF00",
                                                    "#FDFF00", "#FDFF00",  "#FDFF00", "#FDFF00",
                                                    "black", "black", "black", "black", "black", "black", "black",
                                                    "black", "black", "black", "black", "black", "black", "black", "black", "black"])


# Save stimulus
stim.Show()
stim.SaveSVG(stimname, scale = 0.4, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")