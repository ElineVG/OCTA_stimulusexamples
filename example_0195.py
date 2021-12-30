"""
OCTA toolbox example stimuli
Example stimulus 195
created by Eline Van Geert
inspired by FlexTiles software
Image used: tile by Jorge Carrillo from the Noun Project
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import PathSvg

# Define stimulus name
stimname = "example_0195"

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, background_color = "none", size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (45,45) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ PathSvg('img/tile1.svg') ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ ["diagonal", "dodgerblue", "white"] ] )

# Add orientations for the elements
stim.orientations = GridPattern.TiledGrid(GridPattern.RepeatAcrossElements([0,90,270,180],2,2), tile_multiplier=3)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")