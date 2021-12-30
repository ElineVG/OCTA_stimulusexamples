"""
OCTA toolbox example stimuli
Example stimulus 183
created by Eline Van Geert
based on Hübner & Fillinger (2016)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import RegularPolygon

# Define stimulus name
stimname = "example_0183"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 7, x_margin = [85,0], y_margin = [0, 103], background_color = "none")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [150,105,185,
                                                      192, 185, 160, 170], 
                                                 y = [20,12,40,
                                                      8, 22, 62, 77])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (45,45),(35,35),(25,25),(12,12),(8,8),(20,20), (6,6) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ RegularPolygon(6) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 90 ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")