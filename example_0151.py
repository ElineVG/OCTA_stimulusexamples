"""
OCTA toolbox example stimuli
Example stimulus 151
created by Eline Van Geert
Gabor created with: https://www.cogsci.nl/gabor-generator
gabor-gaussian--45.00-96-12.00-0.10-0.00-255-255-255-255-255-255-0-0-0
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image
import random

# Define stimulus name
stimname = "example_0151"

# Set seed
random.seed(7897)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, size = (250,250))

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('img/gabor.png') ] )

# Add orientations for the elements
stim.orientations = GridPattern.GradientAcrossElements(-100,-80).RandomizeAcrossElements()
stim.set_element_orientations(10, n_changes = 1)

# Save stimulus
stim.Show()
random.seed(7897)
stim.SaveSVG(stimname, folder = "svg")
random.seed(7897)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(7897)
stim.SaveJSON(stimname, folder = "json")
random.seed(7897)
stim.SavePNG(stimname, folder = "png")
random.seed(7897)
stim.SavePNG(stimname, scale = 10, folder = "png10")