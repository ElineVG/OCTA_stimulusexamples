"""
OCTA toolbox example stimuli
Example stimulus 41
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse
import random

# Define stimulus name
stimname = "example_0041"

# Set seed to make reproducible and get same stimulus every time (!)
# this specific seed example is different from the one in the publication
random.seed(23131240)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add position deviations
stim.positions = stim.positions.SetPositionJitter(distribution = "normal", axis = 'xy', mu = 0, std = 10)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossColumns(["#6dd6ff", "#1b9fd8", "#006ca1"])

# Save stimulus
stim.Show()
random.seed(23131240)
stim.SaveSVG(stimname, folder = "svg")
random.seed(23131240)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(23131240)
stim.SaveJSON(stimname, folder = "json")
random.seed(23131240)
stim.SavePNG(stimname, folder = "png")
random.seed(23131240)
stim.SavePNG(stimname, scale = 10, folder = "png10")