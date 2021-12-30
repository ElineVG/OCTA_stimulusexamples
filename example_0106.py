"""
OCTA toolbox example stimuli
Example stimulus 106
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import PathSvg

# Define stimulus name
stimname = "example_0106"

# Define stimulus
stim = Concentric( n_elements = 1, background_color = "none", size = (150,250) )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (150,250) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ PathSvg('img/blob.svg') ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'red' ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")