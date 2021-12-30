"""
OCTA toolbox example stimuli
Example stimulus 126
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0126"

# Define stimulus
stim = Grid(n_rows = 2, n_cols = 2, row_spacing = 160, col_spacing = 160, background_color = 'white', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (80,80) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image("svg/example_0122.svg") ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 180, 90, 270, 0 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")