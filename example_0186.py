"""
OCTA toolbox example stimuli
Example stimulus 186
created by Eline Van Geert
based on Gollwitzer et al. (2017)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0186"

# Define stimulus
stim = Concentric(n_elements = 3, background_color = "none")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [(45,45), (85,85), (125,125)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'none' ] )

# Add borderwidths for the elements
stim.borderwidths = GridPattern.RepeatAcrossElements( [ 10 ] )

# Add bordercolors for the elements
stim.bordercolors = GridPattern.RepeatAcrossElements( [ 'grey' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")