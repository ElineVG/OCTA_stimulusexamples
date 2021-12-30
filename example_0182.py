"""
OCTA toolbox example stimuli
Example stimulus 182
created by Eline Van Geert
based on Wilson & Chatterjee (2005)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0182"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 7, x_margin = [0,0], y_margin = [0, 85], background_color = "none")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [0,41,41,32,
                                                      180,137,185], 
                                                 y = [10,30,65,100,
                                                      0,25,40])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (50,50),(30,30),(20,20),(45,45),
                                                         (45,45),(35,35),(25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")