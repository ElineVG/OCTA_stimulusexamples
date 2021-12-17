# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:14:46 2021

@author: u0090621
"""
from html2image import Html2Image
from base64 import b64encode

img1 = b64encode(open("svg/example_0006.svg", "rb").read())

img2 = b64encode(open("svg/example_0007.svg", "rb").read())

img3 = b64encode(open("svg/example_0008.svg", "rb").read())

hti = Html2Image()

hti.screenshot(
    html_file='test.html', 
    save_as='test.png',
    size=(600, 400)
)