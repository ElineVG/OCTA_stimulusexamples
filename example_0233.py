"""
OCTA toolbox example stimuli
Example stimulus 233
created by Eline Van Geert

Wallpaper patterns: P4
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0233"

# Define stimulus parameters
baseshape = Image("svg/example_0217.svg")
basesize = (100,100)
basewidth = basesize[0]
baseheight = basesize[1]

## Number of translations should be an even number!
n_translations_x = 8
n_translations_y = 8

## Translation distance
x_translation = 100
y_translation = 100

## Background color
background = "#5EA1D8" #"none"

# Define stimulus
stim = Grid(n_cols = n_translations_x, n_rows = n_translations_y,
            col_spacing = x_translation, row_spacing = y_translation, 
            background_color = background, x_margin = 0, y_margin = 0)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([basesize])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([baseshape])

# Add orientations for the elements
stim.orientations = GridPattern.TiledGrid(GridPattern.RepeatAcrossElements([0, 90, 270, 180],2,2),4)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
