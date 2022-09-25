"""
OCTA toolbox example stimuli
Example stimulus 76
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse
from octa.measurements import Complexity
import random

# Define stimulus name
stimname = "example_0076"

# Set random seed
random.seed(23449876)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 35, col_spacing= 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossColumns( [ (22,22) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ "#1b9fd8" ] )

# Remove random elements
stim.remove_elements(3)

# Save stimulus
stim.Show()
random.seed(23449876)
stim.SaveSVG(stimname, folder = "svg")
random.seed(23449876)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(23449876)
stim.SaveJSON(stimname, folder = "json")
random.seed(23449876)
stim.SavePNG(stimname, folder = "png")
random.seed(23449876)
stim.SavePNG(stimname, scale = 10, folder = "png10")

# Calculate number of elements
print( Complexity.CalculateElementsN(stim) )