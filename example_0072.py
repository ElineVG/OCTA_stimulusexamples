"""
OCTA toolbox example stimuli
Example stimulus 72
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0072"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossRightDiagonal( [ (22,22) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossRightDiagonal( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossColumns( [ "#6dd6ff", "#1b9fd8", "#006ca1" ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")