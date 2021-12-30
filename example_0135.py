"""
OCTA toolbox example stimuli
Example stimulus 135
created by Eline Van Geert
based on stimuli used to test the global precedence hypothesis (Navon, 1977)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import RegularPolygon

# Define stimulus name
stimname = "example_0135"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 1, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ RegularPolygon(4) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")