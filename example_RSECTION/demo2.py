#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')


from RSECTION.initModel import Model
from RSECTION.BasicObjects.material import Material
from RSECTION.BasicObjects.section import Section
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.opening import Opening
from RSECTION.BasicObjects.element import Element
from RSECTION.enums import ElementArcAlphaAdjustmentTarget, LineArcAlphaAdjustmentTarget, PointReferenceType

if __name__ == '__main__':

    Model(True, "Demo2") # crete new model called Demo

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    # Section(1, 'IPE 200')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    # Element(1, '7 8', 0.5)
    # Element.SingleLine(2, '6 7', 0.5, [True, 0.49])
    # Element.Arc(3, [9, 10], [0.5303,0.5303], ElementArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, 0.5)
    # Element.Circle(4, [0,0], 0.75, 0.5)
    Element.Ellipse(5, [8, 6], [0.45, 0.45], 0.25)


    Model.clientModel.service.finish_modification()

