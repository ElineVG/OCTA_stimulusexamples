"""
OCTA toolbox example stimuli
Example stimulus 191
created by Eline Van Geert
based on Gollwitzer et al. (2017)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, RegularPolygon

# Define stimulus name
stimname = "example_0191"

# Define stimulus
stim = Grid(n_rows = 3, n_cols = 4, background_color = "none", size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [(40,40)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )
stim.set_element_shape(element_id = 6, shape_value = RegularPolygon(5))

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'none' ] )

# Add borderwidths for the elements
stim.borderwidths = GridPattern.RepeatAcrossElements( [ 1 ] )

# Add bordercolors for the elements
stim.bordercolors = GridPattern.RepeatAcrossElements( [ 'grey' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")