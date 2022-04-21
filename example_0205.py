"""
OCTA toolbox example stimuli
Example stimulus 205
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0205"

# Define stimulus
stim = Grid(n_rows = 2, n_cols = 2, row_spacing = 125, col_spacing = 125, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (125,125) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("svg/example_0186.svg"), Image("svg/example_0188.svg"),
                                                Image("svg/example_0187.svg"), Image("svg/example_0189.svg") ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
