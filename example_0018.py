"""
OCTA toolbox example stimuli
Example stimulus 18
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0018"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 40, col_spacing= 40, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLeftDiagonal( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossLeftDiagonal( ['#1b9fd8', '#6dd6ff', '#006ca1']  )

# Add fillcolors for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [0]  )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")