"""
OCTA toolbox example stimuli
Example stimulus 122
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle
import random

# Define stimulus name
stimname = "example_0122"

# Set seed
random.seed(1635413196)

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 2, x_margin = [0,-60], y_margin = [0,-60], background_color = 'white')

# Change element positions
stim.positions = Positions.CreateCustomPositions( x = [0, 62.5], y = [0, 62.5] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250), (125,125) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse, Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ '#5EA1D8' , 'white' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")