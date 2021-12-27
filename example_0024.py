"""
OCTA toolbox example stimuli
Example stimulus 24
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import PathSvg

# Define stimulus name
stimname = "example_0024"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, background_color = "none", row_spacing = 40, col_spacing = 40, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30), (35,35), (25,25) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns( [ PathSvg('img/flower2-svgrepo.svg') ] )

# Add fillcolors for the elements
colors_to_use = [ "#1b9fd8", "#6dd6ff", "#006ca1" ]
stim.fillcolors = GridPattern.RepeatAcrossColumns( colors_to_use )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossRightDiagonal( [
    ['animate', '0', '360', "begin = '0s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '1s', dur='8s',  additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '2s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '3s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '4s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '5s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '6s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '7s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '8s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '9s', dur='8s', additive='sum', repeatCount='indefinite'"],
    
    ['animate', '0', '360', "begin = '10s', dur='8s', additive='sum', repeatCount='indefinite'"]
] )

# Add borderwidths for the elements
stim.borderwidths = GridPattern.RepeatAcrossElements( [ 10 ] )

# Add bordercolors for the elements
colors_to_use = [ "#006ca1", "#1b9fd8", "#6dd6ff" ]
stim.bordercolors = GridPattern.RepeatAcrossColumns(colors_to_use)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")