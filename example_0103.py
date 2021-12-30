"""
OCTA toolbox example stimuli
Example stimulus 103
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Triangle, Rectangle, Polygon, RegularPolygon, Image, FitImage, Path, PathSvg, Text

# Define stimulus name
stimname = "example_0103"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (35,35) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse, Triangle, RegularPolygon(3), Rectangle, RegularPolygon(4),
                                                  Polygon(5), RegularPolygon(5), Polygon(6), RegularPolygon(6), RegularPolygon(8),
                                                  PathSvg("img/checkmark.svg"), Text("O"), Text("C"), Text("T"), Text("A"),
                                                  Image("png10/example_0106.png"), FitImage("png10/example_0106.png"), 
                                                  Image("svg/example_0106.svg"), PathSvg('img/blob.svg'),
                                                  Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288),
                                                  Image('img/butterfly.svg'), Image('https://github.com/ElineVG/OCTA_stimulusexamples/blob/main/svg/example_0107.svg?raw=true'), Image('img/Lunaria annua 1.jpg'), Image('svg/example_0104.svg'), Image('svg/example_0108.svg')
                                                 
                                                 ])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossColumns( ['#1b9fd8', '#6dd6ff', '#006ca1']  )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")