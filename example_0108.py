"""
OCTA toolbox example stimuli
Example stimulus 108
created by Eline Van Geert
Natural flower image used: CC by Hůla and Flegr (2016)
https://doi.org/10.7717/peerj.2106
https://figshare.com/s/7306f12659f68f7f3d9d
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0108"

# Define stimulus
stim = Concentric( n_elements = 1,  size = (250,250), background_shape = 'Ellipse',
                   stim_orientation = ['animate', '0', '360', "dur='10s', repeatCount = 'indefinite', additive='sum'"] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (250,250) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Image('img/Lunaria annua 1.jpg') ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")