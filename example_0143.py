"""
OCTA toolbox example stimuli
Example stimulus 143
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, RegularPolygon

# Define stimulus name
stimname = "example_0143"

# Define stimulus
stim = Grid(n_rows = 12, n_cols = 12, row_spacing = 20, col_spacing = 20, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ])

# Add shapes for the elements
stim.shapes = GridPattern.MirrorAcrossColumns( [ Rectangle, Ellipse, RegularPolygon(4) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.MirrorAcrossColumns( [ "steelblue", "limegreen" ] )

# Add orientations for the elements
stim.set_element_orientation(element_id = 33, orientation_value = 45)
stim.set_element_orientation(element_id = 44, orientation_value = 45)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")