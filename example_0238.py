"""
OCTA toolbox example stimuli
Example stimulus 238
created by Eline Van Geert

Wallpaper patterns: P31M
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid, Concentric
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Image
import numpy as np

# Define stimulus name
stimname = "example_0238"

# Define template1 parameters
baseshape = Image("svg/example_0221.svg")
basesize = (200,(1/3)*200*np.sqrt(3))
basewidth = basesize[0]
baseheight = basesize[1]

# Create template1 tile
stimulus = Concentric(n_elements = 3, background_color = "none", x_margin = 0, y_margin = [(1/6)*200*np.sqrt(3),0])
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.orientations = GridPattern.RepeatAcrossElements([0,120,240])
stimulus.SaveSVG(stimname + "_template", folder = "svg")

# Define template2 parameters
baseshape = Image("svg/"+stimname + "_template"+".svg")
basesize = (200,(1/2)*200*np.sqrt(3))
basewidth = basesize[0]
baseheight = basesize[1]

# Create template2 tile
stimulus = Grid(n_rows = 2, n_cols = 1, background_color = "none", row_spacing = int((1/2)*200*np.sqrt(3)), x_margin = 0, y_margin = 0)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "horizontal"])
stimulus.SaveSVG(stimname + "_template2", folder = "svg")

# Define stimulus parameters
## Number of translations should be an even number!
n_translations_x = 8
n_translations_y = 8

## Translation distance
x_translation = 200
y_translation = int(100*np.sqrt(3))

x_shift = -200/2

## Background color
background = "#5EA1D8" #"none"

## Template shape and size
structureshape = Image("svg/" + stimname + "_template2.svg")
structuresize = (200,200*np.sqrt(3))

# Define stimulus
stim = Grid(n_cols = n_translations_x, n_rows = n_translations_y,
            col_spacing = x_translation, row_spacing = y_translation, 
            background_color = background, background_shape = "Rectangle", size = (1200,1200))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([structuresize])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([structureshape])

# Change element positions (to hexagonal lattice)
x = Pattern(list(range(0, n_translations_x * x_translation, x_translation)))
new_x = x.RepeatPattern(n_translations_x).pattern
y = Pattern(list(range(0, n_translations_y * y_translation, y_translation)))
new_y = y.RepeatElements(n_translations_y).pattern 

x_mod = Pattern([x_shift,0]).RepeatElements(int(n_translations_x))
x_mod = x_mod.RepeatPattern(int(n_translations_y/2)).pattern

stim.positions = Positions.CreateCustomPositions(x = np.array(new_x) + np.array(x_mod), y = new_y)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
