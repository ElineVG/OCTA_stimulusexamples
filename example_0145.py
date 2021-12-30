"""
OCTA toolbox example stimuli
Example stimulus 145
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0145"

# Define stimulus
stim = Grid(n_rows = 18, n_cols = 18, row_spacing = 12, col_spacing = 12, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.GradientAcrossLayers( (6,6), (10,10) )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossLayers( "red", "steelblue" )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")