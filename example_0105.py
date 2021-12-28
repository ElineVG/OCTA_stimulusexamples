"""
OCTA toolbox example stimuli
Example stimulus 105
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0105"

# Define stimulus
stim = Concentric( n_elements = 1,  size = (250,250),
                   stim_orientation = ['animate', '0', '360', "dur='10s', repeatCount = 'indefinite', additive='sum'"])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (150,200) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"'] ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")