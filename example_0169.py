"""
OCTA toolbox example stimuli
Example stimulus 169
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0169"

# Define stimulus
stim = Grid(n_rows = 2, n_cols = 2, x_margin = 5, y_margin = 5, row_spacing = 130, col_spacing = 130, background_color = "white")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (120,120) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0157.svg'),  Image('svg/example_0158.svg'), 
                                                  Image('svg/example_0159.svg'),  Image('svg/example_0160.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")