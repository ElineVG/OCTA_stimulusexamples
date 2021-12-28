"""
OCTA toolbox example stimuli
Example stimulus 111
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0111"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (5,40) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRows(start_value = 'limegreen', end_value = 'steelblue')

# Add orientations for the elements
stim.orientations = GridPattern.MirrorAcrossElements([
    -45, -30, 0, 30, 45,
    -60, -75, 90, 75, 60,
    ['animate', '0', '360', "begin = 'click', dur='4s', additive='sum'"],
    ['animate', '0', '360', "dur='4s', repeatCount='indefinite'"],
    ['animate', '360', '0', "dur='8s', repeatCount='indefinite'"]
])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")