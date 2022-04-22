"""
OCTA toolbox example stimuli
Example stimulus 210
created by Eline Van Geert
Image used: fox by Horoofi from Pixabay
https://pixabay.com/illustrations/fox-animal-cartoon-drawing-sketch-3823023/

Frieze pattern 1: p111 (translation only)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0210"

# Info starting shape
baseshape = Image("img/fox.jpg")
basesize = (100,100)
x_translation_distance = basesize[0] + 0

# Number of translations should be an even number!
n_translations = 8

# Stimulus parameters 
figsize = ((x_translation_distance*n_translations)+x_translation_distance/2, (basesize[1]*2)+basesize[1]/2)
background = "white"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = n_translations, 
            row_spacing = basesize[1], col_spacing = x_translation_distance, size = figsize)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.MirrorAcrossElements([basesize])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([baseshape])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
