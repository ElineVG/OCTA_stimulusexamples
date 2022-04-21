"""
OCTA toolbox example stimuli
Example stimulus 240
created by Eline Van Geert

Wallpaper patterns: P6M
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid, Concentric
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Image
import numpy as np

# Define stimulus name
stimname = "example_0240"

# Define template parameters
baseshape = Image("svg/example_0222.svg")
basesize = (200,(1/3)*200*np.sqrt(3))
basewidth = basesize[0]
baseheight = basesize[1]

# Create template tile
stimulus = Concentric(n_elements = 12, background_color = "none", size = (200,(1/3)*400*np.sqrt(3)))
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.orientations = GridPattern.RepeatAcrossElements([0, 60, 120, 180, 240, 300])
stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["none","none","none","none","none","none",
                                                          "vertical","vertical","vertical","vertical","vertical","vertical"])
stimulus.SaveSVG(stimname + "_template", folder = "svg")

# Define stimulus parameters
## Number of translations should be an even number!
n_translations_x = 8
n_translations_y = 8

## Translation distance
x_translation = 200
y_translation = int((1/2)*200*np.sqrt(3))

x_shift = -200/2

## Background color
background = "#5EA1D8" #"none"

## Template shape and size
structureshape = Image("svg/" + stimname + "_template.svg")
structuresize = (200,(1/3)*400*np.sqrt(3))

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
