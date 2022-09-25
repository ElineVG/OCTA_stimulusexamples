"""
OCTA toolbox example stimuli
Example stimulus 119
created by Eline Van Geert
inspired by Julesz (1981), doi: 10.1038/290091a0
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Triangle
import random

# Define stimulus name
stimname = "example_0119"

# Set seed
random.seed(1635413196)

# Define stimulus
stim = Grid(n_rows = 12, n_cols = 12, row_spacing = 20, col_spacing = 20, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (10,10) ])

# Add shapes for the elements
stim.shapes = GridPattern.ElementRepeatAcrossRightDiagonal( [ Ellipse, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.ElementRepeatAcrossRightDiagonal( [ '#5EA1D8', '#5EA1D8', '#54C4D0' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossRows([15]).AddUniformJitter(min_val = -180, max_val = 180)

# Save stimulus
stim.Show()
random.seed(1635413196)
stim.SaveSVG(stimname, folder = "svg")
random.seed(1635413196)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(1635413196)
stim.SaveJSON(stimname, folder = "json")
random.seed(1635413196)
stim.SavePNG(stimname, folder = "png")
random.seed(1635413196)
stim.SavePNG(stimname, scale = 10, folder = "png10")