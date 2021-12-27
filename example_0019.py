"""
OCTA toolbox example stimuli
Example stimulus 19
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse

# Define stimulus name
stimname = "example_0019"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (35,35) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossRows( [ Rectangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossRows( ['#1b9fd8', '#6dd6ff', '#006ca1']  )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")