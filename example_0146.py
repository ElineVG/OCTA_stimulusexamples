"""
OCTA toolbox example stimuli
Example stimulus 146
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import RegularPolygon

# Define stimulus name
stimname = "example_0146"

# Define stimulus
stim = Grid(n_rows = 18, n_cols = 18, row_spacing = 15, col_spacing = 15, x_margin = 0, y_margin = 0, background_shape = "Triangle", background_color = "#F8F8F8")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.GradientAcrossLayers( (8,8), (14,14) )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossRightDiagonal( [ RegularPolygon(3) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRows( "red", "steelblue" )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossRows( [0,180] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")