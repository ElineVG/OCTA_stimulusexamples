"""
OCTA toolbox example stimuli
Example stimulus 59
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle
import random

# Define stimulus name
stimname = "example_0059"

# Set random seed
random.seed(23449870)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossRows( [ (25,25), (20,20) ] )

# Add shapes for the elements
stim.shapes = GridPattern.ElementRepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossElements( [ "#1b9fd8" ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 0 ] ).AddUniformJitter( min_val = -30, max_val = 30 )

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