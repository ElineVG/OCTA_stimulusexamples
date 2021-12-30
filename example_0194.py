"""
OCTA toolbox example stimuli
Example stimulus 194
created by Eline Van Geert
based on Jacobsen & Höfel (2002)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Image

# Define stimulus name
stimname = "example_0194"

# Define stimulus
stim = Concentric(n_elements = 2, x_margin = 0, y_margin = 0, background_color = "white", size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250), (160,160) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse, Image('svg/example_0193.svg') ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ -45 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")