"""
OCTA toolbox example stimuli
Example stimulus 129
created by Eline Van Geert
based on Kimchi & Palmer (1982), Exp. 1 (http://dx.doi.org/10.1037/0096-1523.8.4.521)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Triangle

# Define stimulus name
stimname = "example_0129"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 6, x_margin = 5, y_margin = 5, row_spacing = 33, col_spacing = 33, background_color = 'none')

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = Pattern([50/3,150/3,250/3,100/3,200/3,150/3]).RepeatPatternToSize(10).pattern, 
                                                 y = Pattern([200/3,200/3,200/3,100/3,100/3,0]).pattern)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (100/3,100/3) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ '#54C4D0' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, scale = 2.4, folder = "svg")
stim.SaveSVG(stimname, scale = 1, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")