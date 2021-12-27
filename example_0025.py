"""
OCTA toolbox example stimuli
Example stimulus 25
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import PathSvg, Ellipse
import random

# Define stimulus name
stimname = "example_0025"

# Set seed 
random.seed(5)

# Define stimulus
stim = Grid( n_rows = 18, n_cols = 18, background_color = "none", row_spacing = 12, col_spacing = 12, size = (250,250))

# Change element positions
stim.positions = Positions.CreateSineGrid( n_rows = 18, n_cols = 18, axis = "xy", A = 8, f = .1,
                                           row_spacing = 12, col_spacing = 12 )
stim.positions = stim.positions.SetPositionJitter(distribution = "uniform", axis = 'xy', min_val = -2, max_val = 2)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (8,8), (10,10), (6,6) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLayers( [ PathSvg('img/flower-svgrepo.svg'), Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossLayers( "purple", "red" )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")