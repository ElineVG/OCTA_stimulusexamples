"""
OCTA toolbox example stimuli
Example stimulus 121
created by Eline Van Geert
inspired by Julesz (1981), doi: 10.1038/290091a0
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Triangle, Rectangle
import random

# Define stimulus name
stimname = "example_0121"

# Set seed
random.seed(1635413196)

# Define stimulus
stim = Grid(n_rows = 12, n_cols = 12, row_spacing = 20, col_spacing = 20, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (10,10) ])

# Add shapes for the elements
stim.shapes = GridPattern.TiledElementGrid( 
    GridPattern.ElementRepeatAcrossRightDiagonal( [Triangle, Rectangle, Triangle, Rectangle], 4, 4), 
    tile_multiplier = 3)

# Add fillcolors for the elements
stim.fillcolors = GridPattern.TiledElementGrid( 
    GridPattern.ElementRepeatAcrossRightDiagonal( ['#F39130', '#54C4D0', '#B2D135', '#5EA1D8'], 4, 4), 
    tile_multiplier = 3)

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossRows([15]).AddUniformJitter(min_val = -180, max_val = 180)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")