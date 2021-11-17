"""
OCTA toolbox example stimuli
Example stimulus 52
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, Triangle, Polygon
import random

# Define stimulus name
stimname = "example_0052"

# Set random seed
random.seed(23449870)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.ElementRepeatAcrossColumns( [ Rectangle, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossColumns( [ "#6dd6ff", "#1b9fd8", "#006ca1" ] )

# Change feature values
random_element1 = random.sample(range(36), 1)[0]
random_element2 = random.sample(range(36), 1)[0]
random_element3 = random.sample(range(36), 1)[0]
stim.set_element_fillcolor( random_element1, "red" )
stim.set_element_shape( random_element2, Polygon(5) )
stim.set_element_fillcolor( random_element3, "green" )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")