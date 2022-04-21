"""
OCTA toolbox example stimuli
Example stimulus 223
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Triangle, Text
import numpy as np

# Define stimulus name
stimname = "example_0223"

# Define stimulus
stim = Concentric(n_elements = 2, background_color = "none", x_margin = [0,-15], y_margin = [0,(1/6)*200*np.sqrt(3)-15])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(200,(1/2)*200*np.sqrt(3)), (70,70)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Triangle, Text("L")])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(["#5EA1D8", "lightgrey"])

# Change element positions
stim.positions.SetPositionDeviations(element_id = [0,1], x_offset = [0,15], y_offset = [0,15])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
