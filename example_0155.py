"""
OCTA toolbox example stimuli
Example stimulus 155
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0155"

# Define stimulus
stim = Grid(n_rows = 16, n_cols = 16, background_shape = Ellipse(boundingbox = (500,500)), row_spacing = 35, col_spacing = 65, size = (500,500),
         stim_orientation = 30)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossColumns( [ "limegreen", "steelblue" ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, scale = 0.5, folder = "svg")
stim.SaveSVG(stimname, scale = 0.3, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")