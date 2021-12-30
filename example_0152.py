"""
OCTA toolbox example stimuli
Example stimulus 152
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0152"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 150, col_spacing = 150)

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = stim.positions.x, 
                                              y = [0, 0, 0, 0, 0, 0,
                                                   150, 150, 150, 150, 150, 150,
                                                   300, 300, 300, 295, 300, 300,
                                                   450, 450, 450, 450, 450, 450,
                                                   600, 600, 600, 600, 600, 600,
                                                   750, 750, 750, 750, 750, 750])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(93.63, 122.88)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image("img/locked.svg") ] )

# Add deviations
stim.set_element_shape(15, shape_value = Image("img/unlocked.svg"))
stim.set_element_boundingbox(15, boundingbox_value = (93.63*1.075, 122.88*1.075))

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, scale = 0.25, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")