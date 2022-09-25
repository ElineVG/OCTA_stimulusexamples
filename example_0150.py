"""
OCTA toolbox example stimuli
Example stimulus 150
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle
import random

# Define stimulus name
stimname = "example_0150"

# Set seed
random.seed(15)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (3,30) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add orientations for the elements
stim.orientations = GridPattern.GradientAcrossElements(15, 30).RandomizeAcrossElements()
stim.set_element_orientations(-30, n_changes = 1)

# Save stimulus
stim.Show()
random.seed(15)
stim.SaveSVG(stimname, folder = "svg")
random.seed(15)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(15)
stim.SaveJSON(stimname, folder = "json")
random.seed(15)
stim.SavePNG(stimname, folder = "png")
random.seed(15)
stim.SavePNG(stimname, scale = 10, folder = "png10")