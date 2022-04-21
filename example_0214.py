"""
OCTA toolbox example stimuli
Example stimulus 214
created by Eline Van Geert
Image used: fox by Horoofi from Pixabay
https://pixabay.com/illustrations/fox-animal-cartoon-drawing-sketch-3823023/

Frieze pattern 5 (translation, glide reflection, & 180° rotation)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0214"

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

# Define stimulus
stim = Grid(n_rows = 1, n_cols = n_translations, row_spacing = baseheight, col_spacing = basewidth, size = figsize)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.MirrorAcrossElements([basesize])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([baseshape])

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossColumns([0, 0, 180, 180])

# Add mirror values for the elements
stim.mirrorvalues = GridPattern.RepeatAcrossColumns(["none", "vertical", "vertical", "none"])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
