#!/usr/bin/jython
# target: -Dpython.path=/Development/pdfbox-2.0.6/app/target/pdfbox-app-2.0.6.jar
# -*- coding: utf-8 -*-

import org.apache.pdfbox.examples.util.PrintTextLocations as PrintTextLocations
import java.io.ByteArrayOutputStream as ByteArrayOutputStream
import java.io.File
import java.io.IOException as IOException
import java.io.OutputStreamWriter as OutputStreamWriter
import java.io.Writer
import java.util.List
import java.awt.geom.Rectangle2D.Float as r2df
import org.apache.pdfbox.pdmodel.PDDocument as PDDocument
import org.apache.pdfbox.text.PDFTextStripper as PDFTextStripper
import org.apache.pdfbox.text.PDFTextStripperByArea as PDFTextStripperByArea
import org.apache.pdfbox.text.TextPosition as TextPosition


#Open document and load as PDF object
with open("Attempt3.pdf","rb") as f:
    basicpdf = f.read()
document = PDDocument.load( basicpdf )

#Instantiate PrintTextLocations stripper for identifying location of characters
#PrintTextLocations is a subclass of PDFTextStripper
stripper = PrintTextLocations()
stripper.setSortByPosition( true )
stripper.setStartPage( 0 )
stripper.setEndPage( document.getNumberOfPages() )
dummy = OutputStreamWriter(ByteArrayOutputStream())
#The writeText method is overriden in PrintTextLocations
# String[0.0,792.0 fs=12.0 xscale=12.0 height=7.1400003 space=3.3360004 width=7.332]T
stripper.writeText(document, dummy)

#Instantiate the PDFTextStripperByArea class   
stripperbyarea = PDFTextStripperByArea()

#Create Coordinates - using the Explicit identification of coordinates
# String[0.0,792.0 fs=12.0 xscale=12.0 height=7.1400003 space=3.3360004 width=7.332]T
#use the Rectangle2D.Float to instantiate a rectangle that can take a float.
# r2df(x,y,w,h)
box1 = r2df(0.0,792.0,140.0,12.0)
box2 = r2df(120.0,792.0,120.0,12.0)

stripperbyarea.addRegion("left_text",box1)
stripperbyarea.addRegion("right_text",box2)
page = document.getPage(0)
stripperbyarea.extractRegions(page)
new_box = []
    for area in stripperbyarea.getRegions():
        new_box.append((area, stripperbyarea.getTextForRegion(area)))

def region_map(stripper=None):
	"iterator for region items"
	# usage: dict(x for x in region_map(stripperbyarea))
    for area in stripper.getRegions():
        yield (area, stripper.getTextForRegion(area))