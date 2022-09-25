"""
OCTA toolbox example stimuli
Example stimulus 55
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, Triangle
import random

# Define stimulus name
stimname = "example_0055"

# Set random seed
random.seed(23449870)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.ElementRepeatAcrossColumns( [ Rectangle, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossColumns( [ "#6dd6ff", "#1b9fd8", "#006ca1" ] ).RandomizeAcrossElements()

# Save stimulus
stim.Show()
random.seed(23449870)
stim.SaveSVG(stimname, folder = "svg")
random.seed(23449870)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(23449870)
stim.SaveJSON(stimname, folder = "json")
random.seed(23449870)
stim.SavePNG(stimname, folder = "png")
random.seed(23449870)
stim.SavePNG(stimname, scale = 10, folder = "png10")