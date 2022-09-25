"""
OCTA toolbox example stimuli
Example stimulus 32
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse
import random

# Define stimulus name
stimname = "example_0032"

# Set seed to make reproducible and get same stimulus every time (!)
# this specific seed example is different from the one in the publication
random.seed(5)

# Define stimulus
stim = Grid(n_rows = 9, n_cols = 9, row_spacing = 24, col_spacing= 24, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RandomPattern( [ 'limegreen', '#41AFBA', 'steelblue' ] )

# Save stimulus
stim.Show()
random.seed(5)
stim.SaveSVG(stimname, folder = "svg")
random.seed(5)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(5)
stim.SaveJSON(stimname, folder = "json")
random.seed(5)
stim.SavePNG(stimname, folder = "png")
random.seed(5)
stim.SavePNG(stimname, scale = 10, folder = "png10")