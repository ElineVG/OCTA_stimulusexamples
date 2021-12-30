"""
OCTA toolbox example stimuli
Example stimulus 177
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0177"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 3, x_margin = [0,0], y_margin = [10,0], background_color = "white")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [0,-55,55], y = [0,120,120] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (120,120) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0149.svg'),  Image('svg/example_0147.svg'), 
                                                  Image('svg/example_0148.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")