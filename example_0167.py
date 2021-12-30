"""
OCTA toolbox example stimuli
Example stimulus 167
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0167"

# Define stimulus
stim = Concentric(n_elements = 3, x_margin = 10, y_margin = 10, background_color = "none")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250), (150,150), (50,50) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('svg/example_0165.svg'),  Image('svg/example_0166.svg'), 
                                                  Image('svg/example_0164.svg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")