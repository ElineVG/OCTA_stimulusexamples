"""
OCTA toolbox example stimuli
Example stimulus 18
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse
import random

# Define stimulus name
stimname = "example_0018"

# Set random seed
random.seed(23449870)

# Define stimulus
stim = Grid(n_rows = 9, n_cols = 9, size = (250,250))

# Define element positions
stim.positions = Positions.CreateRandomPositions(n_elements = 160, width = 200, height = 200, min_distance = 10, max_iterations = 10)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossColumns( start_value = 'limegreen', end_value = 'steelblue' )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")