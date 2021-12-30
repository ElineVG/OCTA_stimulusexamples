"""
OCTA toolbox example stimuli
Example stimulus 175
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0175"

# Define stimulus
stim = Grid(n_rows = 2, n_cols = 2, x_margin = 5, y_margin = 5, row_spacing = 120, col_spacing = 120, background_color = "white")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (100,100) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0123.svg'),  Image('svg/example_0124.svg'), 
                                                  Image('svg/example_0125.svg'),  Image('svg/example_0126.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")