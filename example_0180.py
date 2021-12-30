"""
OCTA toolbox example stimuli
Example stimulus 180
created by Eline Van Geert
based on Chipman & Mendelson (1979)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0180"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing=40, col_spacing=40,
            x_margin = 0, y_margin = 0, background_color = "none")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (40.5,40.5) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossLayers(['white', 'white', 'black', 'black' ])
stim.set_element_fillcolors(element_id = [2,3,12,18,17,23,32,33], fillcolor_value = "white")

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")