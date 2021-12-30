"""
OCTA toolbox example stimuli
Example stimulus 168
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0168"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 3, x_margin = 5, y_margin = 5, background_color = "none")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [0,-62.5,62.5], y = [0,125,125] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (120,120) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0146.svg'),  Image('svg/example_0144.svg'), 
                                                  Image('svg/example_0145.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")