"""
OCTA toolbox example stimuli
Example stimulus 144
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle, Triangle

# Define stimulus name
stimname = "example_0144"

# Define stimulus
stim = Grid(n_rows = 18, n_cols = 18, background_color = 'none', size = (250,250))

# Change element positions
stim.positions = Positions.CreateSineGrid(18, 18, row_spacing = 12, col_spacing = 12, A = 12, f = 0.05, axis = 'xy')

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (6,6), (10,10) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLayers( [ Ellipse, Rectangle, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossLayers( "limegreen", "steelblue" )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")