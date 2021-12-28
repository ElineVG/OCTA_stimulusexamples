"""
OCTA toolbox example stimuli
Example stimulus 8
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
# from octa.shapes import Rectangle, Triangle

# Define stimulus name
stimname = "example_0108"

# Define stimulus
stim = Concentric(n_elements = 7, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.GradientAcrossElements( start_value = (230,230), end_value = (10,10) )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")