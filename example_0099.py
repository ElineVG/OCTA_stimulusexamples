"""
OCTA toolbox example stimuli
Example stimulus 99
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import PathSvg

# Define stimulus name
stimname = "example_0099"

# Define stimulus
stim = Outline(n_elements = 52, background_color = "#ECFAF9", shape = "img/flower-svgrepo.svg", 
               shape_boundingbox = (200,200), size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ PathSvg("img/flower-svgrepo.svg") ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements([ 
    ['animate', "#1b9fd8", 
     'values = "#1b9fd8;#6dd6ff;#006ca1;#6dd6ff;#1b9fd8", begin = "click", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'] 
])

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([
    ['animate', '0', '360', "begin = 'click', dur='3s', additive='sum'"]
])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")