"""
OCTA toolbox example stimuli
Example stimulus 114
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Triangle, Rectangle, Polygon, RegularPolygon

# Define stimulus name
stimname = "example_0114"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns( [ Ellipse, Triangle, Rectangle, RegularPolygon(5), Polygon(8) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossRows( [ 'orange', 'dodgerblue' ] )

# Add opacities for the elements
stim.opacities = GridPattern.MirrorAcrossElements([
    0.1,0.25,0.5,0.75,1,
    1, 0.75, 0.5, 0.25, 0.1,
    ['set', 0.1, 'to = 1, begin = "click", dur = "2s"'],
    ['animate', 1, 'values = ".8;.6;.4;.2;0;.2;.4;.6;.8;1", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
    ['animate', 1, 'values = ".8;.6;.4;.2;0;.2;.4;.6;.8;1", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"']
])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")