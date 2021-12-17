"""
OCTA toolbox example stimuli
Example stimulus 68
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, Triangle
from octa.measurements import Order

# Define stimulus name
stimname = "example_0068"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossRightDiagonal( [ (25,25), (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossRightDiagonal( [ Rectangle, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossRightDiagonal( [ "#6dd6ff", "#1b9fd8", "#006ca1" ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

# Calculate pattern direction congruency
print( Order.GetPatterns(stim) )
print( Order.CalculatePatternDirectionCongruency(stim, features = ['shapes', 'boundingboxes', 'fillcolors']))