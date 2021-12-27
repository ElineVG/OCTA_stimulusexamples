"""
OCTA toolbox example stimuli
Example stimulus 23
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0023"

# Define stimulus
stim = Grid(n_rows = 3, n_cols = 3, row_spacing = 45, col_spacing= 45, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossColumns( [ (35,35), (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( ['#1b9fd8']  )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")