"""
OCTA toolbox example stimuli
Example stimulus 141
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0141"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 2, x_margin = 10, y_margin = 10, col_spacing = 180, row_spacing = 320, background_color = 'none')

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (170,320) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0138.svg'), Image('svg/example_0139.svg') ] )

# Add mirrorvalues for the elements
stim.mirrorvalues = GridPattern.RepeatAcrossElements( [ "none", "vertical" ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")