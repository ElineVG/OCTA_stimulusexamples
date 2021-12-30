"""
OCTA toolbox example stimuli
Example stimulus 173
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0173"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 3, x_margin = 5, y_margin = 5, background_color = "none")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [0,-65,65], y = [0,115,115] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (100,100) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0130.svg'),  Image('svg/example_0131.svg'), 
                                                  Image('svg/example_0132.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")