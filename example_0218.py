"""
OCTA toolbox example stimuli
Example stimulus 218
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Polygon, Text
import numpy as np

# Define stimulus name
stimname = "example_0218"

# Define stimulus
stim = Concentric(n_elements = 2, background_color = "none", x_margin = [200,0], y_margin = [100*np.sqrt(3),100*np.sqrt(3)])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(200,200*np.sqrt(3)), (70,70)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Polygon(4), Text("L")])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(["#5EA1D8", "lightgrey"])

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([0,120])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
