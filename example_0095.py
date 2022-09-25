"""
OCTA toolbox example stimuli
Example stimulus 95
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, Triangle
import random

# Define stimulus name
stimname = "example_0095"

# Set random seed
random.seed(10)

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (35,35) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns( [ Rectangle, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossColumns( ['#1b9fd8', '#6dd6ff', '#006ca1']  )

# Swap elements
stim.swap_distinct_elements(n_swap_pairs=2)

# Save stimulus
stim.Show()
random.seed(10)
stim.SaveSVG(stimname, folder = "svg")
random.seed(10)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(10)
stim.SaveJSON(stimname, folder = "json")
random.seed(10)
stim.SavePNG(stimname, folder = "png")
random.seed(10)
stim.SavePNG(stimname, scale = 10, folder = "png10")