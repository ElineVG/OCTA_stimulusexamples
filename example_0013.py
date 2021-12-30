"""
OCTA toolbox example stimuli
Example stimulus 13
created by Eline Van Geert
Using butterfly image from the Auckland Optotypes (Hamm et al., 2018)
https://github.com/dakinlab/OpenOptotypes
https://doi.org/10.1167/18.3.13
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse

# Define stimulus name
stimname = "example_0013"

# Define stimulus
stim = Outline(n_elements = 30, shape = "img/butterfly.svg", shape_boundingbox = (200,200), size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements( start_value = 'limegreen', end_value = 'steelblue' )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")