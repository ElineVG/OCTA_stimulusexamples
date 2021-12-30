"""
OCTA toolbox example stimuli
Example stimulus 139
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse
import random

# Define stimulus name
stimname = "example_0139"

# Set seed
random.seed(145132)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, x_margin = 0, y_margin = 0, background_color = 'none')

# Change element positions
px = [130, 55, 10, 97, 98, 81, 111, 96, 6, 121, 65, 82, 142, 133, 23, 59, 133, 101, 133, 34,
      19, 113, 4, 46, 38, 11, 50, 102, 79, 16, 73, 68, 96, 1, 131, 11]
px2 = [35, 55, 10, 97, 98, 81, 111, 96, 6, 121, 65, 82, 142, 133, 23, 59, 133, 101, 133, 34,
       19, 113, 4, 46, 38, 11, 50, 102, 79, 16, 73, 68, 96, 1, 131, 11]
py = [103, 153, 232, 97, 52, 132, 218, 198, 73, 74, 213, 73, 7, 262, 179, 106, 58, 26, 174,
      201, 119, 140, 170, 278, 16, 150, 250, 274, 22, 5, 54, 173, 243, 96, 33, 275]
py2 = [50, 153, 232, 97, 52, 132, 218, 198, 73, 74, 213, 73, 7, 262, 179, 106, 58, 26, 174,
       201, 119, 140, 170, 278, 16, 150, 250, 274, 22, 5, 54, 173, 243, 96, 33, 275]

stim.positions = Positions.CreateCustomPositions(x = px2, y = py2)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.4, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")