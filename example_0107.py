"""
OCTA toolbox example stimuli
Example stimulus 107
created by Eline Van Geert
Using butterfly image from the Auckland Optotypes (Hamm et al., 2018)
https://github.com/dakinlab/OpenOptotypes
https://doi.org/10.1167/18.3.13
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import PathSvg

# Define stimulus name
stimname = "example_0107"

# Define stimulus
stim = Concentric( n_elements = 1, background_color = "none", size = (250,250), 
                   stim_orientation = ['animate', '0', '360', "dur='10s', repeatCount = 'indefinite', additive='sum'"] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ PathSvg('img/butterfly.svg') ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ '#6dd6ff' ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")