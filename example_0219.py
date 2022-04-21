"""
OCTA toolbox example stimuli
Example stimulus 219
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Triangle, Text

# Define stimulus name
stimname = "example_0219"

# Define stimulus
stim = Concentric(n_elements = 2, background_color = "none", x_margin = [-100,-25], y_margin = [0,-10])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(200,100), (35,35)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Triangle, Text("L")])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(["#5EA1D8", "lightgrey"])

# Change element positions
stim.positions.SetPositionDeviations(element_id = [0,1], x_offset = [0,25], y_offset = [0,10])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
