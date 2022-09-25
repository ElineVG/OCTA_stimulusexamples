"""
OCTA toolbox example stimuli
Example stimulus 200
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Rectangle
import random

# Define stimulus name
stimname = "example_0200"

# Set seed to make reproducible and get same stimulus every time (!)
random.seed(23131240)

# Define stimulus
stim = Grid(n_rows = 9, n_cols = 9, size = (250,250))

# Define element positions
stim.positions = Positions.CreateSineGrid(n_rows = 9, n_cols = 9, row_spacing = 25, col_spacing = 25,
                                          A = 15, f = .1, axis = "xy")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] ).AddUniformJitter(min_val = -5, max_val = 5)

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossLayers( start_value = 'limegreen', end_value = 'steelblue' )

# Save stimulus
stim.Show()
random.seed(23131240)
stim.SaveSVG(stimname, folder = "svg")
random.seed(23131240)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(23131240)
stim.SaveJSON(stimname, folder = "json")
random.seed(23131240)
stim.SavePNG(stimname, folder = "png")
random.seed(23131240)
stim.SavePNG(stimname, scale = 10, folder = "png10")