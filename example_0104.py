"""
OCTA toolbox example stimuli
Example stimulus 104
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Triangle, Ellipse

# Define stimulus name
stimname = "example_0104"

# Define stimulus
stim = Outline(n_elements = 24, shape_boundingbox = (100,100), size = (250,250), background_color = "none", 
               stim_orientation = ['animate', '0', '360', "dur='10s', repeatCount = 'indefinite', additive='sum'"])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20), (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Triangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements( start_value = 'limegreen', end_value = 'steelblue' )

# Add orientations for the elements
stim.orientations = GridPattern.MirrorAcrossElements( [ -90, -45, 0, 45, 90 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")