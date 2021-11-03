"""
OCTA toolbox example stimuli
Example stimulus 7
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern

# Define stimulus name
stimname = "example_0007"

# Define stimulus
stim = Outline(n_elements = 24, shape_boundingbox = (100,100), size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")