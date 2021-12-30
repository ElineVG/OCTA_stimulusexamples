"""
OCTA toolbox example stimuli
Example stimulus 160
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle, Triangle
import random

# Define stimulus name
stimname = "example_0160"

# Set seed
random.seed(12563)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (35,35) ] ).AddUniformJitter(-20,5, 'x=y')

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse, Rectangle, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossColumns( "limegreen", "steelblue" )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([0]).AddUniformJitter(-15,15)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")