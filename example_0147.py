"""
OCTA toolbox example stimuli
Example stimulus 147
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0147"

# Create custom positions
pos = Positions.CreateCircle(n_elements = 6, radius = 70)
px = pos.x
py = pos.y
px.append(0)
py.append(0)

# Define stimulus
stim = Outline(n_elements = 7, size = (250,250))

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = px, y = py)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (60,60) ] )
stim.set_element_boundingbox(6, (40,40))

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.set_element_fillcolor(6, "orange")

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")