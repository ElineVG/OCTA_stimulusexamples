"""
OCTA toolbox example stimuli
Example stimulus 181
created by Eline Van Geert
based on Locher et al. (1998)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0181"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 9, x_margin = [10,20], y_margin = [10,37], background_color = "none")

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = [78,100,121,15,0,
                                                      150,160,95,85], 
                                                 y = [5,0,10,60,76,
                                                      75,92,120,143])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30),(15,15),(30,30),
                                                         (15,15),(30,30),
                                                         (15,15),(25,25),
                                                         (25,25),(25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")