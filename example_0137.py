"""
OCTA toolbox example stimuli
Example stimulus 137
created by Eline Van Geert
based on stimuli used to test the global precedence hypothesis (Navon, 1977)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0137"

# Define stimulus
stim = Outline(n_elements = 12, background_color = 'none', size = (250,250))

# Change element positions
stim.positions = Positions.CreateShape(src = 'svg/example_0135.svg', n_elements = 12, width = 200, height = 200)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")