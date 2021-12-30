"""
OCTA toolbox example stimuli
Example stimulus 185
created by Eline Van Geert
based on Gollwitzer et al. (2017)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0185"

# Define stimulus
stim = Outline(n_elements = 8, background_color = "none", shape_boundingbox = (80,80))

# Add position deviations
stim.positions = stim.positions.SetPositionDeviations( element_id = [ 7 ], x_offset = [30], y_offset = [-30] )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'grey' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 90 ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")