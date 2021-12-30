"""
OCTA toolbox example stimuli
Example stimulus 166
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse

# Define stimulus name
stimname = "example_0166"

# Define stimulus
stim = Outline(n_elements = 12, x_margin = 0, y_margin = 0, shape_boundingbox = (60,60), background_color = "none", 
                  stim_orientation =  ['animate', '360', '0', "dur='20s', repeatCount='indefinite'"])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ "limegreen", "steelblue" ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ ['animate', '0', '360', "dur='20s', repeatCount='indefinite'"] ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")