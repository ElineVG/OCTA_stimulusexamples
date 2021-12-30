"""
OCTA toolbox example stimuli
Example stimulus 132
created by Eline Van Geert
based on Kimchi & Palmer (1982), Exp. 2 (http://dx.doi.org/10.1037/0096-1523.8.4.521)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Triangle

# Define stimulus name
stimname = "example_0132"

# Define stimulus
stim = Grid(n_rows = 2, n_cols = 2, row_spacing = 120, col_spacing = 120, background_color = 'none', size = (250,250))

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [60, 60, 0, 120], 
                                                  y = [0, 0, 120, 120])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (110,110) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ None, Triangle, Triangle, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")