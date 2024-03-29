"""
OCTA toolbox example stimuli
Example stimulus 58
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle
from octa.measurements import Order
import random

# Define stimulus name
stimname = "example_0058"

# Set random seed
random.seed(23449870)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossRows( [ (25,25), (20,20) ] ).AddNormalJitter(mu = 0, std = 5, axis = "x=y")

# Add shapes for the elements
stim.shapes = GridPattern.ElementRepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossElements( [ "#1b9fd8" ] )

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

# Calculate number of pattern deviants
print( Order.CalculatePatternDeviants(stim) )