"""
OCTA toolbox example stimuli
Example stimulus 217
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Text

# Define stimulus name
stimname = "example_0217"

# Define stimulus
stim = Concentric(n_elements = 2, background_color = "#5EA1D8", size = (100,100))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(100,100), (70,70)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Rectangle, Text("L")])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(["#5EA1D8", "lightgrey"])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
