"""
OCTA toolbox example stimuli
Example stimulus 216
created by Eline Van Geert
Image used: fox by Horoofi from Pixabay
https://pixabay.com/illustrations/fox-animal-cartoon-drawing-sketch-3823023/

Frieze pattern 7 (translation, horizontal and vertical reflection, & 180° rotation)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0216"

# Info starting shape
baseshape = Image("img/fox.jpg")
basesize = (100,100)
basewidth = basesize[0]
baseheight = basesize[1]

# Number of translations should be an even number!
n_translations = 8

# Stimulus parameters 
figsize = ((basewidth*n_translations)+basewidth/2, (baseheight*2)+baseheight/2)
background = "white"

## Create template tile
stimulus = Grid(n_cols = 2, n_rows = 2,
                col_spacing = basewidth, row_spacing = baseheight, 
                background_color = background, size = (2*basewidth, 2*baseheight))
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "vertical", "horizontal", "horizontalvertical"])
stimulus.SaveSVG(stimname + "_template", folder = "svg")

# Define stimulus
stim = Grid(n_rows = 1, n_cols = int(n_translations/2), row_spacing = 2*baseheight, col_spacing = 2*basewidth, size = figsize)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.MirrorAcrossElements([(2*basewidth, 2*baseheight)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("svg/" + stimname + "_template.svg")])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
