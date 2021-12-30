"""
OCTA toolbox example stimuli
Example stimulus 188
created by Eline Van Geert
based on Gollwitzer et al. (2017)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Triangle

# Define stimulus name
stimname = "example_0188"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 8, col_spacing = 18, x_margin = [5,5], y_margin = [75,75], background_color = "none")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [(30,17)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'none' ] )

# Add borderwidths for the elements
stim.borderwidths = GridPattern.RepeatAcrossElements( [ 1 ] )

# Add bordercolors for the elements
stim.bordercolors = GridPattern.RepeatAcrossElements( [ 'grey' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 90 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")