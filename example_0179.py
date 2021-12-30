"""
OCTA toolbox example stimuli
Example stimulus 179
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0179"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 3, x_margin = -40, y_margin = 0, background_color = "white")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [-55,55,0], y = [0,0,110] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (100,100), (100,100), (200,100) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0161.svg'),  Image('svg/example_0162.svg'), 
                                                  Image('svg/example_0163.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")