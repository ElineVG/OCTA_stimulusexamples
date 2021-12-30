"""
OCTA toolbox example stimuli
Example stimulus 193
created by Eline Van Geert
based on Jacobsen & Höfel (2002)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import RegularPolygon

# Define stimulus name
stimname = "example_0193"

# Define stimulus
stim = Grid(n_rows = 3, n_cols = 4, row_spacing=45, col_spacing=45, x_margin = 0, y_margin = 0, background_color = "white")

# Change element positions
stim.positions = Positions.CreateCustomPositions(
  x = [0, 65, 110, 175, 0, 65, 110, 175, 0, 65, 110, 87.5],
  y = [25, 0, 0, 25, 70, 70, 70, 70, 140, 140, 140, 180])
# s = Concentric(2, x_margin = 0, y_margin = 0)
# s.shapes = GridPattern.RepeatAcrossElements([Ellipse, Image("img/jacobseninside1.svg")])
# s.boundingboxes = GridPattern.RepeatAcrossElements([(80,80), (50,50)])
# s.orientations =GridPattern.RepeatAcrossElements([-45])
# s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ RegularPolygon(4) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'black' ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 90 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")