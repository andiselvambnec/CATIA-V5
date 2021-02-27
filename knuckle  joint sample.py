# import python modules
import os
from win32com.client import Dispatch
# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')
# optional CATIA visibility
CATIA.Visible = True
'''
a=31.25
b=68.75
c=55
d=50
e=25
f=175
g=60
h=25
'''

a=60
b=130
c=110
d=100
e=50
f=350
g=120
h=50

def knuckle():
    arrayOfVariantOfDouble1=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble3=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble4=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble5=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble6=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble7=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble8=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble9=[0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneXY
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = 1.000000
    arrayOfVariantOfDouble1[8] = 0.000000
    sketch1.SetAbsoluteAxisData(arrayOfVariantOfDouble1)
    part1.InWorkObject = sketch1
    factory2D1 = sketch1.OpenEdition()                                  #sketch 1 start(2circle ,2line)
    geometricElements1 = sketch1.GeometricElements
    axis2D1 = geometricElements1.Item('AbsoluteAxis')
    line2D1 = axis2D1.GetItem('HDirection')
    line2D1.ReportName = 3
    line2D2 = axis2D1.GetItem('VDirection')
    line2D2.ReportName = 4
    point2D1 = factory2D1.CreatePoint(0.000000, - a)
    point2D1.ReportName = 5
    point2D2 = factory2D1.CreatePoint(0.000000, a)
    point2D2.ReportName = 6
    circle2D1 = factory2D1.CreateCircle(0.000000, 0.000000, a, 4.712389, 7.853982)     #inner circle (a=radius of inner)
    point2D3 = axis2D1.GetItem('Origin')
    circle2D1.CenterPoint = point2D3
    circle2D1.ReportName = 7
    circle2D1.StartPoint = point2D1
    circle2D1.EndPoint = point2D2
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(circle2D1)
    #constraint1 = constraints1.AddMonoEltCst(catCstTypeRadius, reference2)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 31.250000
    point2D4 = factory2D1.CreatePoint(0.000000, - b)
    point2D4.ReportName = 8
    point2D5 = factory2D1.CreatePoint(0.000000, b)
    point2D5.ReportName = 9
    circle2D2 = factory2D1.CreateCircle(0.000000, 0.000000, b, 4.712389, 7.853982)    #outer circle (b=radius of outer circle)
    circle2D2.CenterPoint = point2D3
    circle2D2.ReportName = 10
    circle2D2.StartPoint = point2D4
    circle2D2.EndPoint = point2D5
    reference3 = part1.CreateReferenceFromObject(circle2D2)
    #constraint2 = constraints1.AddMonoEltCst(catCstTypeRadius, reference3)
    #constraint2.Mode = catCstModeDrivingDimension
    #length2 = constraint2.Dimension
    #length2.Value = 68.750000
    line2D3 = factory2D1.CreateLine(0.000000, b, 0.000000, a)
    line2D3.ReportName = 11
    line2D3.StartPoint = point2D5
    line2D3.EndPoint = point2D2
    reference4 = part1.CreateReferenceFromObject(point2D5)
    reference5 = part1.CreateReferenceFromObject(line2D2)
    #constraint3 = constraints1.AddBiEltCst(catCstTypeOn, reference4, reference5)
    #constraint3.Mode = catCstModeDrivingDimension
    reference6 = part1.CreateReferenceFromObject(line2D3)
    reference7 = part1.CreateReferenceFromObject(line2D2)
    #constraint4 = constraints1.AddBiEltCst(catCstTypeVerticality, reference6, reference7)
    #constraint4.Mode = catCstModeDrivingDimension
    line2D4 = factory2D1.CreateLine(0.000000, - a, 0.000000, - b)
    line2D4.ReportName = 12
    line2D4.StartPoint = point2D1
    line2D4.EndPoint = point2D4
    reference8 = part1.CreateReferenceFromObject(point2D1)
    reference9 = part1.CreateReferenceFromObject(line2D2)
    #constraint5 = constraints1.AddBiEltCst(catCstTypeOn, reference8, reference9)
    #constraint5.Mode = catCstModeDrivingDimension
    reference10 = part1.CreateReferenceFromObject(line2D4)
    reference11 = part1.CreateReferenceFromObject(line2D2)
    #constraint6 = constraints1.AddBiEltCst(catCstTypeVerticality, reference10, reference11)
    #constraint6.Mode = catCstModeDrivingDimension
    sketch1.CloseEdition()                                                                                                   #sketch 1 closed 
    part1.InWorkObject = hybridBody1
    part1.Update()

    
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference12 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference12, 20.000000)
    reference13 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference13)
    limit1 = pad1.FirstLimit
    length3 = limit1.Dimension
    length3.Value = c                                                                            #pad1 (thickness c is 1.1d)
    part1.Update()
    
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    sketches2 = body1.Sketches
    reference14 = originElements1.PlaneYZ
    sketch2 = sketches2.Add(reference14)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = 0.000000
    arrayOfVariantOfDouble2[4] = 1.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = 0.000000
    arrayOfVariantOfDouble2[8] = 1.000000
    sketch2.SetAbsoluteAxisData(arrayOfVariantOfDouble2)
    part1.InWorkObject = sketch2
    factory2D2 = sketch2.OpenEdition()                                                            #sketch 2 opened 
    geometricElements2 = sketch2.GeometricElements
    axis2D2 = geometricElements2.Item('AbsoluteAxis')
    line2D5 = axis2D2.GetItem('HDirection')
    line2D5.ReportName = 1
    line2D6 = axis2D2.GetItem('VDirection')
    line2D6.ReportName = 2
    reference15 = part1.CreateReferenceFromBRepName('RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;11)));None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MonoFond;MFBRepVersion_CXR15)', pad1)
    geometricElements3 = factory2D2.CreateProjections(reference15)
    reference16 = part1.CreateReferenceFromBRepName('RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MonoFond;MFBRepVersion_CXR15)', pad1)
    geometricElements4 = factory2D2.CreateProjections(reference16)
    sketch2.CloseEdition()                                                                      #sketch 2 closed
    part1.InWorkObject = sketch2
    part1.Update()
    pad2 = shapeFactory1.AddNewPad(sketch2, 55.000000)
    limit2 = pad2.FirstLimit
    length4 = limit2.Dimension
    length4.Value = - d                                                                             #pad2 (length is kd/2)
    part1.Update()

    
    reference17 = originElements1.PlaneZX
    sketch3 = sketches2.Add(reference17)
    arrayOfVariantOfDouble3[0] = 0.000000
    arrayOfVariantOfDouble3[1] = 0.000000
    arrayOfVariantOfDouble3[2] = 0.000000
    arrayOfVariantOfDouble3[3] = - 1.000000
    arrayOfVariantOfDouble3[4] = 0.000000
    arrayOfVariantOfDouble3[5] = 0.000000
    arrayOfVariantOfDouble3[6] = 0.000000
    arrayOfVariantOfDouble3[7] = - 0.000000
    arrayOfVariantOfDouble3[8] = 1.000000
    sketch3.SetAbsoluteAxisData(arrayOfVariantOfDouble3)
    part1.InWorkObject = sketch3
    factory2D3 = sketch3.OpenEdition()                                                              #sketch 3 opened
    geometricElements5 = sketch3.GeometricElements
    axis2D3 = geometricElements5.Item('AbsoluteAxis')
    line2D7 = axis2D3.GetItem('HDirection')
    line2D7.ReportName = 1
    line2D8 = axis2D3.GetItem('VDirection')
    line2D8.ReportName = 2
    reference18 = part1.CreateReferenceFromBRepName('REdge:(Edge:(Face:(Brp:(Pad.2;2);None:();Cf11:());Face:(Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.1;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;10)));Brp:(Pad.1;0:(Brp:(Sketch.1;11)))))))))));None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MonoFond;MFBRepVersion_CXR15)', pad2)
    geometricElements6 = factory2D3.CreateProjections(reference18)
    geometry2D1 = geometricElements6.Item('Mark.1')
    geometry2D1.Construction = True
    point2D6 = factory2D3.CreatePoint(d, 0.000000)
    point2D6.ReportName = 3
    point2D6.Construction = True
    point2D7 = factory2D3.CreatePoint(d, c)
    point2D7.ReportName = 4
    point2D7.Construction = True
    point2D8 = factory2D3.CreatePoint(d, (c/2))
    point2D8.ReportName = 5
    circle2D3 = factory2D3.CreateClosedCircle(d, (c/2), d)
    circle2D3.CenterPoint = point2D8
    circle2D3.ReportName = 6
    constraints2 = sketch3.Constraints
    reference19 = part1.CreateReferenceFromObject(point2D8)
    reference20 = part1.CreateReferenceFromObject(geometry2D1)
    #constraint7 = constraints2.AddBiEltCst(catCstTypeMidPoint, reference19, reference20)
    #constraint7.Mode = catCstModeDrivingDimension
    reference21 = part1.CreateReferenceFromObject(circle2D3)
    #constraint8 = constraints2.AddMonoEltCst(catCstTypeRadius, reference21)
    #constraint8.Mode = catCstModeDrivingDimension
    #length5 = constraint8.Dimension
    #length5.Value = 50.000000
    sketch3.CloseEdition()                                                                          #sketch 3 closed
    part1.InWorkObject = sketch3
    part1.Update()
    reference22 = part1.CreateReferenceFromName('')
    pad3 = shapeFactory1.AddNewPadFromRef(reference22, - 50.000000)
    reference23 = part1.CreateReferenceFromObject(sketch3)
    pad3.SetProfileElement(reference23)
    pad3.IsSymmetric = True
    limit3 = pad3.FirstLimit
    length6 = limit3.Dimension
    length6.Value = b                                                                           #pad3 (l=b)
    part1.Update()

    
    sketch4 = sketches2.Add(reference17)
    arrayOfVariantOfDouble4[0] = 0.000000
    arrayOfVariantOfDouble4[1] = 0.000000
    arrayOfVariantOfDouble4[2] = 0.000000
    arrayOfVariantOfDouble4[3] = - 1.000000
    arrayOfVariantOfDouble4[4] = 0.000000
    arrayOfVariantOfDouble4[5] = 0.000000
    arrayOfVariantOfDouble4[6] = 0.000000
    arrayOfVariantOfDouble4[7] = - 0.000000
    arrayOfVariantOfDouble4[8] = 1.000000
    sketch4.SetAbsoluteAxisData(arrayOfVariantOfDouble4)
    part1.InWorkObject = sketch4
    factory2D4 = sketch4.OpenEdition()                                                    #sketch 4 opened 
    geometricElements7 = sketch4.GeometricElements
    axis2D4 = geometricElements7.Item('AbsoluteAxis')
    line2D9 = axis2D4.GetItem('HDirection')
    line2D9.ReportName = 1
    line2D10 = axis2D4.GetItem('VDirection')
    line2D10.ReportName = 2
    reference24 = part1.CreateReferenceFromBRepName('REdge:(Edge:(Face:(Brp:(Pad.3;0:(Brp:(Sketch.3;6)));None:();Cf11:());Face:(Brp:((Brp:(Pad.3;2);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.1;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;10)));Brp:(Pad.1;0:(Brp:(Sketch.1;11)))))))))))));None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MonoFond;MFBRepVersion_CXR15)', pad3)
    geometricElements8 = factory2D4.CreateProjections(reference24)
    geometry2D2 = geometricElements8.Item('Mark.1')
    geometry2D2.Construction = True
    #point2D9 = factory2D4.CreatePoint(8.241767, 0.000000)
    #point2D9.ReportName = 3
    #point2D9.Construction = True
    #point2D10 = factory2D4.CreatePoint(8.241767, 55.000000)
    #point2D10.ReportName = 4
    #point2D10.Construction = True
    point2D11 = factory2D4.CreatePoint(d, (c/2))
    point2D11.ReportName = 5
    circle2D4 = factory2D4.CreateClosedCircle(d, (c/2), e)
    circle2D4.CenterPoint = point2D11
    circle2D4.ReportName = 6
    constraints3 = sketch4.Constraints
    reference25 = part1.CreateReferenceFromObject(point2D11)
    reference26 = part1.CreateReferenceFromObject(geometry2D2)
    #constraint9 = constraints3.AddBiEltCst(catCstTypeConcentricity, reference25, reference26)
    #constraint9.Mode = catCstModeDrivingDimension
    reference27 = part1.CreateReferenceFromObject(circle2D4)
    #constraint10 = constraints3.AddMonoEltCst(catCstTypeRadius, reference27)
    #constraint10.Mode = catCstModeDrivingDimension
    #length7 = constraint10.Dimension
    #length7.Value = 25.000000
    sketch4.CloseEdition()                                                                 #sketch 4 closed
    part1.InWorkObject = sketch4
    part1.Update()
    reference28 = part1.CreateReferenceFromName('')
    pocket1 = shapeFactory1.AddNewPocketFromRef(reference28, b)                          #pocket 1(l=b)
    pocket1.IsSymmetric = True
    reference29 = part1.CreateReferenceFromObject(sketch4)
    pocket1.SetProfileElement(reference29)
    part1.Update()

    
    sketch5 = sketches2.Add(reference17)
    arrayOfVariantOfDouble5[0] = 0.000000
    arrayOfVariantOfDouble5[1] = 0.000000
    arrayOfVariantOfDouble5[2] = 0.000000
    arrayOfVariantOfDouble5[3] = - 1.000000
    arrayOfVariantOfDouble5[4] = 0.000000
    arrayOfVariantOfDouble5[5] = 0.000000
    arrayOfVariantOfDouble5[6] = 0.000000
    arrayOfVariantOfDouble5[7] = - 0.000000
    arrayOfVariantOfDouble5[8] = 1.000000
    sketch5.SetAbsoluteAxisData(arrayOfVariantOfDouble5)
    part1.InWorkObject = sketch5
    factory2D5 = sketch5.OpenEdition()                                                           #sketch 5 open
    geometricElements9 = sketch5.GeometricElements
    axis2D5 = geometricElements9.Item('AbsoluteAxis')
    line2D11 = axis2D5.GetItem('HDirection')
    line2D11.ReportName = 1
    line2D12 = axis2D5.GetItem('VDirection')
    line2D12.ReportName = 2
    reference30 = part1.CreateReferenceFromBRepName('REdge:(Edge:(Face:(Brp:((Brp:(Pad.3;2);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.1;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;10)));Brp:(Pad.1;0:(Brp:(Sketch.1;11)))))))))))));None:();Cf11:());Face:(Brp:(Pocket.1;0:(Brp:(Sketch.4;6)));None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MonoFond;MFBRepVersion_CXR15)', pocket1)
    geometricElements10 = factory2D5.CreateProjections(reference30)
    geometry2D3 = geometricElements10.Item('Mark.1')
    geometry2D3.Construction = True
    point2D12 = factory2D5.CreatePoint(d, (c/2))
    point2D12.ReportName = 3
    circle2D5 = factory2D5.CreateClosedCircle(d, (c/2), d)
    circle2D5.CenterPoint = point2D12
    circle2D5.ReportName = 4
    constraints4 = sketch5.Constraints
    reference31 = part1.CreateReferenceFromObject(point2D12)
    reference32 = part1.CreateReferenceFromObject(geometry2D3)
    #constraint11 = constraints4.AddBiEltCst(catCstTypeConcentricity, reference31, reference32)
    #constraint11.Mode = catCstModeDrivingDimension
    reference33 = part1.CreateReferenceFromObject(circle2D5)
    #constraint12 = constraints4.AddMonoEltCst(catCstTypeRadius, reference33)
    #constraint12.Mode = catCstModeDrivingDimension
    #length8 = constraint12.Dimension
    #length8.Value = 50.000000
    sketch5.CloseEdition()                                                                         #sketch 5 closed
    part1.InWorkObject = sketch5
    part1.Update()
    reference34 = part1.CreateReferenceFromName('')
    pocket2 = shapeFactory1.AddNewPocketFromRef(reference34, 68.750000)
    reference35 = part1.CreateReferenceFromObject(sketch5)
    pocket2.SetProfileElement(reference35)
    pocket2.IsSymmetric = True
    limit4 = pocket2.FirstLimit
    length9 = limit4.Dimension
    length9.Value = a                                                 #pocket 2 (l=a)
    part1.Update()

    
    sketch6 = sketches2.Add(reference14)
    arrayOfVariantOfDouble6[0] = 0.000000
    arrayOfVariantOfDouble6[1] = 0.000000
    arrayOfVariantOfDouble6[2] = 0.000000
    arrayOfVariantOfDouble6[3] = 0.000000
    arrayOfVariantOfDouble6[4] = 1.000000
    arrayOfVariantOfDouble6[5] = 0.000000
    arrayOfVariantOfDouble6[6] = 0.000000
    arrayOfVariantOfDouble6[7] = 0.000000
    arrayOfVariantOfDouble6[8] = 1.000000
    sketch6.SetAbsoluteAxisData(arrayOfVariantOfDouble6)
    part1.InWorkObject = sketch6
    factory2D6 = sketch6.OpenEdition()                                                              #sketch 6 opened
    geometricElements11 = sketch6.GeometricElements
    axis2D6 = geometricElements11.Item('AbsoluteAxis')
    line2D13 = axis2D6.GetItem('HDirection')
    line2D13.ReportName = 1
    line2D14 = axis2D6.GetItem('VDirection')
    line2D14.ReportName = 2
    point2D13 = factory2D6.CreatePoint((c/2), 0.000000)
    point2D13.ReportName = 3
    line2D15 = factory2D6.CreateLine(0.000000, 0.000000, (c/2), 0.000000)
    line2D15.ReportName = 4
    point2D14 = axis2D6.GetItem('Origin')
    line2D15.StartPoint = point2D14
    line2D15.EndPoint = point2D13
    constraints5 = sketch6.Constraints
    reference36 = part1.CreateReferenceFromObject(line2D15)
    reference37 = part1.CreateReferenceFromObject(line2D13)
    #constraint13 = constraints5.AddBiEltCst(catCstTypeHorizontality, reference36, reference37)
    #constraint13.Mode = catCstModeDrivingDimension
    reference38 = part1.CreateReferenceFromObject(line2D15)
    #constraint14 = constraints5.AddMonoEltCst(catCstTypeLength, reference38)
    #constraint14.Mode = catCstModeDrivingDimension
    #length10 = constraint14.Dimension
    #length10.Value = 27.500000
    point2D15 = factory2D6.CreatePoint((c/2), c)
    point2D15.ReportName = 5
    line2D16 = factory2D6.CreateLine((c/2), 0, (c/2), c)
    line2D16.ReportName = 6
    line2D16.StartPoint = point2D13
    line2D16.EndPoint = point2D15
    reference39 = part1.CreateReferenceFromObject(line2D16)
    reference40 = part1.CreateReferenceFromObject(line2D14)
    #constraint15 = constraints5.AddBiEltCst(catCstTypeVerticality, reference39, reference40)
    #constraint15.Mode = catCstModeDrivingDimension
    reference41 = part1.CreateReferenceFromObject(line2D16)
    #constraint16 = constraints5.AddMonoEltCst(catCstTypeLength, reference41)
    #constraint16.Mode = catCstModeDrivingDimension
    #length11 = constraint16.Dimension
    #length11.Value = 55.000000
    point2D16 = factory2D6.CreatePoint(- (c/2), c)
    point2D16.ReportName = 7
    line2D17 = factory2D6.CreateLine((c/2), c, - (c/2), c)
    line2D17.ReportName = 8
    line2D17.StartPoint = point2D15
    line2D17.EndPoint = point2D16
    reference42 = part1.CreateReferenceFromObject(line2D17)
    reference43 = part1.CreateReferenceFromObject(line2D13)
    #constraint17 = constraints5.AddBiEltCst(catCstTypeHorizontality, reference42, reference43)
    #constraint17.Mode = catCstModeDrivingDimension
    reference44 = part1.CreateReferenceFromObject(line2D17)
    #constraint18 = constraints5.AddMonoEltCst(catCstTypeLength, reference44)
    #constraint18.Mode = catCstModeDrivingDimension
    #length12 = constraint18.Dimension
    #length12.Value = 55.000000
    point2D17 = factory2D6.CreatePoint(- (c/2), 0.000000)
    point2D17.ReportName = 9
    line2D18 = factory2D6.CreateLine(- (c/2), c, - (c/2), 0)
    line2D18.ReportName = 10
    line2D18.StartPoint = point2D16
    line2D18.EndPoint = point2D17
    reference45 = part1.CreateReferenceFromObject(line2D18)
    reference46 = part1.CreateReferenceFromObject(line2D14)
    #constraint19 = constraints5.AddBiEltCst(catCstTypeVerticality, reference45, reference46)
    #constraint19.Mode = catCstModeDrivingDimension
    reference47 = part1.CreateReferenceFromObject(line2D18)
    #constraint20 = constraints5.AddMonoEltCst(catCstTypeLength, reference47)
    #constraint20.Mode = catCstModeDrivingDimension
    #length13 = constraint20.Dimension
    #length13.Value = 55.000000
    point2D18 = factory2D6.CreatePoint(0.000000, 0.000000)
    point2D18.ReportName = 11
    line2D19 = factory2D6.CreateLine(- (c/2), 0, 0, 0)
    line2D19.ReportName = 12
    line2D19.StartPoint = point2D17
    line2D19.EndPoint = point2D18
    reference48 = part1.CreateReferenceFromObject(line2D19)
    reference49 = part1.CreateReferenceFromObject(line2D13)
    #constraint21 = constraints5.AddBiEltCst(catCstTypeHorizontality, reference48, reference49)
    #constraint21.Mode = catCstModeDrivingDimension
    reference50 = part1.CreateReferenceFromObject(line2D19)
    #constraint22 = constraints5.AddMonoEltCst(catCstTypeLength, reference50)
    #constraint22.Mode = catCstModeDrivingDimension
    #length14 = constraint22.Dimension
    #length14.Value = 27.500000
    sketch6.CloseEdition()                                                               #sketch 6 closed
    part1.InWorkObject = sketch6
    part1.Update()
    reference51 = part1.CreateReferenceFromName('')
    pad4 = shapeFactory1.AddNewPadFromRef(reference51, 31.250000)
    reference52 = part1.CreateReferenceFromObject(sketch6)
    pad4.SetProfileElement(reference52)
    limit5 = pad4.FirstLimit
    length15 = limit5.Dimension
    length15.Value = f
    part1.Update()

    
    sketch7 = sketches2.Add(reference1)
    arrayOfVariantOfDouble7[0] = 0.000000
    arrayOfVariantOfDouble7[1] = 0.000000
    arrayOfVariantOfDouble7[2] = 0.000000
    arrayOfVariantOfDouble7[3] = 1.000000
    arrayOfVariantOfDouble7[4] = 0.000000
    arrayOfVariantOfDouble7[5] = 0.000000
    arrayOfVariantOfDouble7[6] = 0.000000
    arrayOfVariantOfDouble7[7] = 1.000000
    arrayOfVariantOfDouble7[8] = 0.000000
    sketch7.SetAbsoluteAxisData(arrayOfVariantOfDouble7)
    part1.InWorkObject = sketch7
    factory2D7 = sketch7.OpenEdition()                                                      #sketch 7 opened
    geometricElements12 = sketch7.GeometricElements
    axis2D7 = geometricElements12.Item('AbsoluteAxis')
    line2D20 = axis2D7.GetItem('HDirection')
    line2D20.ReportName = 1
    line2D21 = axis2D7.GetItem('VDirection')
    line2D21.ReportName = 2
    circle2D6 = factory2D7.CreateClosedCircle(0.000000, 0.000000, a)
    point2D19 = axis2D7.GetItem('Origin')
    circle2D6.CenterPoint = point2D19
    circle2D6.ReportName = 3
    constraints6 = sketch7.Constraints
    reference53 = part1.CreateReferenceFromObject(circle2D6)
    #constraint23 = constraints6.AddMonoEltCst(catCstTypeRadius, reference53)
    #constraint23.Mode = catCstModeDrivingDimension
    #length16 = constraint23.Dimension
    #length16.Value = 31.250000
    sketch7.CloseEdition()                                                              #sketch 7 closed
    part1.InWorkObject = sketch7
    part1.Update()
    reference54 = part1.CreateReferenceFromName('')
    pocket3 = shapeFactory1.AddNewPocketFromRef(reference54, 175.000000)
    reference55 = part1.CreateReferenceFromObject(sketch7)
    pocket3.SetProfileElement(reference55)
    limit6 = pocket3.FirstLimit
    length17 = limit6.Dimension
    length17.Value = - c                                                             #pocket 3(l=c)
    part1.Update()

    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    reference56 = part1.CreateReferenceFromName('Selection_RSur:(Face:(Brp:(Pad.4;2);None:();Cf11:());Pocket.3_ResultOUT;Z0;G3563)')
    sketch8 = sketches2.Add(reference56)
    arrayOfVariantOfDouble8[0] = f
    arrayOfVariantOfDouble8[1] = 0.000000
    arrayOfVariantOfDouble8[2] = 0.000000
    arrayOfVariantOfDouble8[3] = 0.000000
    arrayOfVariantOfDouble8[4] = 1.000000
    arrayOfVariantOfDouble8[5] = 0.000000
    arrayOfVariantOfDouble8[6] = 0.000000
    arrayOfVariantOfDouble8[7] = 0.000000
    arrayOfVariantOfDouble8[8] = 1.000000
    sketch8.SetAbsoluteAxisData(arrayOfVariantOfDouble8)
    part1.InWorkObject = sketch8
    factory2D8 = sketch8.OpenEdition()                                               #sketch 8 opened
    geometricElements13 = sketch8.GeometricElements
    axis2D8 = geometricElements13.Item('AbsoluteAxis')
    line2D22 = axis2D8.GetItem('HDirection')
    line2D22.ReportName = 3
    line2D23 = axis2D8.GetItem('VDirection')
    line2D23.ReportName = 4
    point2D20 = factory2D8.CreatePoint((c/2), 0.000000)
    point2D20.ReportName = 5
    point2D21 = factory2D8.CreatePoint((c/2), (c/4))
    point2D21.ReportName = 6
    line2D24 = factory2D8.CreateLine((c/2), 0.000000, (c/2), (c/4))
    line2D24.ReportName = 1
    line2D24.StartPoint = point2D20
    line2D24.EndPoint = point2D21
    constraints7 = sketch8.Constraints
    reference57 = part1.CreateReferenceFromObject(point2D20)
    reference58 = part1.CreateReferenceFromObject(line2D23)
    #constraint24 = constraints7.AddBiEltCst(catCstTypeDistance, reference57, reference58)
    #constraint24.Mode = catCstModeDrivingDimension
    #length18 = constraint24.Dimension
    #length18.Value = 27.500000
    reference59 = part1.CreateReferenceFromObject(point2D20)
    reference60 = part1.CreateReferenceFromObject(line2D22)
    #constraint25 = constraints7.AddBiEltCst(catCstTypeDistance, reference59, reference60)
    #constraint25.Mode = catCstModeDrivingDimension
    #length19 = constraint25.Dimension
    #length19.Value = 0.000000
    reference61 = part1.CreateReferenceFromObject(point2D21)
    reference62 = part1.CreateReferenceFromObject(line2D23)
    #constraint26 = constraints7.AddBiEltCst(catCstTypeDistance, reference61, reference62)
    #constraint26.Mode = catCstModeDrivingDimension
    #length20 = constraint26.Dimension
    #length20.Value = 27.500000
    reference63 = part1.CreateReferenceFromObject(point2D21)
    reference64 = part1.CreateReferenceFromObject(line2D22)
    #constraint27 = constraints7.AddBiEltCst(catCstTypeDistance, reference63, reference64)
    #constraint27.Mode = catCstModeDrivingDimension
    #length21 = constraint27.Dimension
    #length21.Value = 13.750000
    point2D22 = factory2D8.CreatePoint((c/2), 0.000000)
    point2D22.ReportName = 7
    point2D23 = factory2D8.CreatePoint((c/4), 0.000000)
    point2D23.ReportName = 8
    line2D25 = factory2D8.CreateLine((c/2), 0.000000, (c/4), 0.000000)
    line2D25.ReportName = 2
    line2D25.StartPoint = point2D22
    line2D25.EndPoint = point2D23
    reference65 = part1.CreateReferenceFromObject(point2D22)
    reference66 = part1.CreateReferenceFromObject(line2D23)
    #constraint28 = constraints7.AddBiEltCst(catCstTypeDistance, reference65, reference66)
    #constraint28.Mode = catCstModeDrivingDimension
    #length22 = constraint28.Dimension
    #length22.Value = 27.500000
    reference67 = part1.CreateReferenceFromObject(point2D22)
    reference68 = part1.CreateReferenceFromObject(line2D22)
    #constraint29 = constraints7.AddBiEltCst(catCstTypeDistance, reference67, reference68)
    #constraint29.Mode = catCstModeDrivingDimension
    #length23 = constraint29.Dimension
    #length23.Value = 0.000000
    reference69 = part1.CreateReferenceFromObject(point2D23)
    reference70 = part1.CreateReferenceFromObject(line2D23)
    #constraint30 = constraints7.AddBiEltCst(catCstTypeDistance, reference69, reference70)
    #constraint30.Mode = catCstModeDrivingDimension
    #length24 = constraint30.Dimension
    #length24.Value = 13.750000
    reference71 = part1.CreateReferenceFromObject(point2D23)
    reference72 = part1.CreateReferenceFromObject(line2D22)
    #constraint31 = constraints7.AddBiEltCst(catCstTypeDistance, reference71, reference72)
    #constraint31.Mode = catCstModeDrivingDimension
    #length25 = constraint31.Dimension
    #length25.Value = 0.000000
    point2D24 = factory2D8.CreatePoint((c/2), c)
    point2D24.ReportName = 9
    point2D25 = factory2D8.CreatePoint((c/4), c)
    point2D25.ReportName = 10
    line2D26 = factory2D8.CreateLine((c/2), c, (c/4), c)
    line2D26.ReportName = 11
    line2D26.StartPoint = point2D24
    line2D26.EndPoint = point2D25
    reference73 = part1.CreateReferenceFromObject(point2D24)
    reference74 = part1.CreateReferenceFromObject(line2D23)
    #constraint32 = constraints7.AddBiEltCst(catCstTypeDistance, reference73, reference74)
    #constraint32.Mode = catCstModeDrivingDimension
    #length26 = constraint32.Dimension
    #length26.Value = 27.500000
    reference75 = part1.CreateReferenceFromObject(point2D24)
    reference76 = part1.CreateReferenceFromObject(line2D22)
    #constraint33 = constraints7.AddBiEltCst(catCstTypeDistance, reference75, reference76)
    #constraint33.Mode = catCstModeDrivingDimension
    #length27 = constraint33.Dimension
    #length27.Value = 55.000000
    reference77 = part1.CreateReferenceFromObject(point2D25)
    reference78 = part1.CreateReferenceFromObject(line2D23)
    #constraint34 = constraints7.AddBiEltCst(catCstTypeDistance, reference77, reference78)
    #constraint34.Mode = catCstModeDrivingDimension
    #length28 = constraint34.Dimension
    #length28.Value = 13.750000
    reference79 = part1.CreateReferenceFromObject(point2D25)
    reference80 = part1.CreateReferenceFromObject(line2D22)
    #constraint35 = constraints7.AddBiEltCst(catCstTypeDistance, reference79, reference80)
    #constraint35.Mode = catCstModeDrivingDimension
    #length29 = constraint35.Dimension
    #length29.Value = 55.000000
    point2D26 = factory2D8.CreatePoint((c/2), c)
    point2D26.ReportName = 12
    point2D27 = factory2D8.CreatePoint((c/2), ((3*c)/4))
    point2D27.ReportName = 13
    line2D27 = factory2D8.CreateLine((c/2), c, (c/2), ((3*c)/4))
    line2D27.ReportName = 14
    line2D27.StartPoint = point2D26
    line2D27.EndPoint = point2D27
    reference81 = part1.CreateReferenceFromObject(point2D26)
    reference82 = part1.CreateReferenceFromObject(line2D23)
    #constraint36 = constraints7.AddBiEltCst(catCstTypeDistance, reference81, reference82)
    #constraint36.Mode = catCstModeDrivingDimension
    #length30 = constraint36.Dimension
    #length30.Value = 27.500000
    reference83 = part1.CreateReferenceFromObject(point2D26)
    reference84 = part1.CreateReferenceFromObject(line2D22)
    #constraint37 = constraints7.AddBiEltCst(catCstTypeDistance, reference83, reference84)
    #constraint37.Mode = catCstModeDrivingDimension
    #length31 = constraint37.Dimension
    #length31.Value = 55.000000
    reference85 = part1.CreateReferenceFromObject(point2D27)
    reference86 = part1.CreateReferenceFromObject(line2D23)
    #constraint38 = constraints7.AddBiEltCst(catCstTypeDistance, reference85, reference86)
    #constraint38.Mode = catCstModeDrivingDimension
    #length32 = constraint38.Dimension
    #length32.Value = 27.500000
    reference87 = part1.CreateReferenceFromObject(point2D27)
    reference88 = part1.CreateReferenceFromObject(line2D22)
    #constraint39 = constraints7.AddBiEltCst(catCstTypeDistance, reference87, reference88)
    #length33 = constraint39.Dimension
    #length33.Value = 41.250000
    point2D28 = factory2D8.CreatePoint(- (c/2), 0.000000)
    point2D28.ReportName = 15
    point2D29 = factory2D8.CreatePoint(- (c/2), (c/4))
    point2D29.ReportName = 16
    line2D28 = factory2D8.CreateLine(- (c/2), 0.000000, - (c/2), (c/4))
    line2D28.ReportName = 17
    line2D28.StartPoint = point2D28
    line2D28.EndPoint = point2D29
    reference89 = part1.CreateReferenceFromObject(point2D28)
    reference90 = part1.CreateReferenceFromObject(line2D23)
    #constraint40 = constraints7.AddBiEltCst(catCstTypeDistance, reference89, reference90)
    #constraint40.Mode = catCstModeDrivingDimension
    #length34 = constraint40.Dimension
    #length34.Value = 27.500000
    reference91 = part1.CreateReferenceFromObject(point2D28)
    reference92 = part1.CreateReferenceFromObject(line2D22)
    #constraint41 = constraints7.AddBiEltCst(catCstTypeDistance, reference91, reference92)
    #constraint41.Mode = catCstModeDrivingDimension
    #length35 = constraint41.Dimension
    #length35.Value = 0.000000
    reference93 = part1.CreateReferenceFromObject(point2D29)
    reference94 = part1.CreateReferenceFromObject(line2D23)
    #constraint42 = constraints7.AddBiEltCst(catCstTypeDistance, reference93, reference94)
    #constraint42.Mode = catCstModeDrivingDimension
    #length36 = constraint42.Dimension
    #length36.Value = 27.500000
    reference95 = part1.CreateReferenceFromObject(point2D29)
    reference96 = part1.CreateReferenceFromObject(line2D22)
    #constraint43 = constraints7.AddBiEltCst(catCstTypeDistance, reference95, reference96)
    #constraint43.Mode = catCstModeDrivingDimension
    #length37 = constraint43.Dimension
    #length37.Value = 13.750000
    point2D30 = factory2D8.CreatePoint(- (c/2), 0.000000)
    point2D30.ReportName = 18
    point2D31 = factory2D8.CreatePoint(- (c/4), 0.000000)
    point2D31.ReportName = 19
    line2D29 = factory2D8.CreateLine(- (c/2), 0.000000, - (c/4), 0.000000)
    line2D29.ReportName = 20
    line2D29.StartPoint = point2D30
    line2D29.EndPoint = point2D31
    reference97 = part1.CreateReferenceFromObject(point2D30)
    reference98 = part1.CreateReferenceFromObject(line2D23)
    #constraint44 = constraints7.AddBiEltCst(catCstTypeDistance, reference97, reference98)
    #constraint44.Mode = catCstModeDrivingDimension
    #length38 = constraint44.Dimension
    #length38.Value = 27.500000
    reference99 = part1.CreateReferenceFromObject(point2D30)
    reference100 = part1.CreateReferenceFromObject(line2D22)
    #constraint45 = constraints7.AddBiEltCst(catCstTypeDistance, reference99, reference100)
    #constraint45.Mode = catCstModeDrivingDimension
    #length39 = constraint45.Dimension
    #length39.Value = 0.000000
    reference101 = part1.CreateReferenceFromObject(point2D31)
    reference102 = part1.CreateReferenceFromObject(line2D23)
    #constraint46 = constraints7.AddBiEltCst(catCstTypeDistance, reference101, reference102)
    #constraint46.Mode = catCstModeDrivingDimension
    #length40 = constraint46.Dimension
    #length40.Value = 13.750000
    reference103 = part1.CreateReferenceFromObject(point2D31)
    reference104 = part1.CreateReferenceFromObject(line2D22)
    #constraint47 = constraints7.AddBiEltCst(catCstTypeDistance, reference103, reference104)
    #constraint47.Mode = catCstModeDrivingDimension
    #length41 = constraint47.Dimension
    #length41.Value = 0.000000
    point2D32 = factory2D8.CreatePoint(- (c/2), c)
    point2D32.ReportName = 21
    point2D33 = factory2D8.CreatePoint(- (c/4), c)
    point2D33.ReportName = 22
    line2D30 = factory2D8.CreateLine(- (c/2), c, - (c/4), c)
    line2D30.ReportName = 23
    line2D30.StartPoint = point2D32
    line2D30.EndPoint = point2D33
    reference105 = part1.CreateReferenceFromObject(point2D32)
    reference106 = part1.CreateReferenceFromObject(line2D23)
    #constraint48 = constraints7.AddBiEltCst(catCstTypeDistance, reference105, reference106)
    #constraint48.Mode = catCstModeDrivingDimension
    #length42 = constraint48.Dimension
    #length42.Value = 27.500000
    reference107 = part1.CreateReferenceFromObject(point2D32)
    reference108 = part1.CreateReferenceFromObject(line2D22)
    #constraint49 = constraints7.AddBiEltCst(catCstTypeDistance, reference107, reference108)
    #constraint49.Mode = catCstModeDrivingDimension
    #length43 = constraint49.Dimension
    #length43.Value = 55.000000
    reference109 = part1.CreateReferenceFromObject(point2D33)
    reference110 = part1.CreateReferenceFromObject(line2D23)
    #constraint50 = constraints7.AddBiEltCst(catCstTypeDistance, reference109, reference110)
    #constraint50.Mode = catCstModeDrivingDimension
    #length44 = constraint50.Dimension
    #length44.Value = 13.750000
    reference111 = part1.CreateReferenceFromObject(point2D33)
    reference112 = part1.CreateReferenceFromObject(line2D22)
    #constraint51 = constraints7.AddBiEltCst(catCstTypeDistance, reference111, reference112)
    #constraint51.Mode = catCstModeDrivingDimension
    #length45 = constraint51.Dimension
    #length45.Value = 55.000000
    point2D34 = factory2D8.CreatePoint(- (c/2), ((3*c)/4))
    point2D34.ReportName = 24
    line2D31 = factory2D8.CreateLine(- (c/2), c, - (c/2), ((3*c)/4))
    line2D31.ReportName = 25
    line2D31.StartPoint = point2D32
    line2D31.EndPoint = point2D34
    reference113 = part1.CreateReferenceFromObject(point2D34)
    reference114 = part1.CreateReferenceFromObject(line2D23)
    #constraint52 = constraints7.AddBiEltCst(catCstTypeDistance, reference113, reference114)
    #constraint52.Mode = catCstModeDrivingDimension
    #length46 = constraint52.Dimension
    #length46.Value = 27.500000
    reference115 = part1.CreateReferenceFromObject(point2D34)
    reference116 = part1.CreateReferenceFromObject(line2D22)
    #constraint53 = constraints7.AddBiEltCst(catCstTypeDistance, reference115, reference116)
    #constraint53.Mode = catCstModeDrivingDimension
    #length47 = constraint53.Dimension
    #length47.Value = 41.250000
    line2D32 = factory2D8.CreateLine((c/4), - 0.000000, (c/2), (c/4))
    line2D32.ReportName = 26
    line2D32.StartPoint = point2D23
    line2D32.EndPoint = point2D21
    line2D33 = factory2D8.CreateLine((c/4), c, (c/2), ((3*c)/4))
    line2D33.ReportName = 27
    line2D33.StartPoint = point2D25
    line2D33.EndPoint = point2D27
    line2D34 = factory2D8.CreateLine(- (c/4), - 0.000000, - (c/2), (c/4))
    line2D34.ReportName = 28
    line2D34.StartPoint = point2D31
    line2D34.EndPoint = point2D29
    point2D35 = factory2D8.CreatePoint(- (c/4), c)
    point2D35.ReportName = 29
    point2D36 = factory2D8.CreatePoint(- (c/2), ((3*c)/4))
    point2D36.ReportName = 30
    line2D35 = factory2D8.CreateLine(- (c/4), c, - (c/2), ((3*c)/4))
    line2D35.ReportName = 31
    line2D35.StartPoint = point2D35
    line2D35.EndPoint = point2D36
    sketch8.CloseEdition()                                                         #sketch 8 closed
    part1.InWorkObject = sketch8
    part1.Update()
    viewer3D1.ZoomOut()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    pocket4 = shapeFactory1.AddNewPocket(sketch8, - 55.000000)
    limit7 = pocket4.FirstLimit
    length48 = limit7.Dimension
    length48.Value = g                                                     #pocket 4 (l=1.2d1)
    part1.Update()

     
    reference117 = part1.CreateReferenceFromName('Selection_RSur:(Face:(Brp:(Pad.4;2);None:();Cf11:());Pocket.4_ResultOUT;Z0;G3563)')
    sketch9 = sketches2.Add(reference117)
    arrayOfVariantOfDouble9[0] = f
    arrayOfVariantOfDouble9[1] = 0.000000
    arrayOfVariantOfDouble9[2] = 0.000000
    arrayOfVariantOfDouble9[3] = 0.000000
    arrayOfVariantOfDouble9[4] = 1.000000
    arrayOfVariantOfDouble9[5] = 0.000000
    arrayOfVariantOfDouble9[6] = 0.000000
    arrayOfVariantOfDouble9[7] = 0.000000
    arrayOfVariantOfDouble9[8] = 1.000000
    sketch9.SetAbsoluteAxisData(arrayOfVariantOfDouble9)
    part1.InWorkObject = sketch9
    factory2D9 = sketch9.OpenEdition()                            #sketch 9 opened
    geometricElements14 = sketch9.GeometricElements
    axis2D9 = geometricElements14.Item('AbsoluteAxis')
    line2D36 = axis2D9.GetItem('HDirection')
    line2D36.ReportName = 1
    line2D37 = axis2D9.GetItem('VDirection')
    line2D37.ReportName = 2
    point2D37 = factory2D9.CreatePoint(0.000000, (c/2))
    point2D37.ReportName = 3
    line2D38 = factory2D9.CreateLine(0.000000, 0.000000, 0.000000, (c/2))
    line2D38.ReportName = 4
    point2D38 = axis2D9.GetItem('Origin')
    line2D38.StartPoint = point2D38
    line2D38.EndPoint = point2D37
    constraints8 = sketch9.Constraints
    reference118 = part1.CreateReferenceFromObject(line2D38)
    reference119 = part1.CreateReferenceFromObject(line2D37)
    #constraint54 = constraints8.AddBiEltCst(catCstTypeVerticality, reference118, reference119)
    #constraint54.Mode = catCstModeDrivingDimension
    reference120 = part1.CreateReferenceFromObject(line2D38)
    #constraint55 = constraints8.AddMonoEltCst(catCstTypeLength, reference120)
    #constraint55.Mode = catCstModeDrivingDimension
    #length49 = constraint55.Dimension
    #length49.Value = 27.500000
    circle2D7 = factory2D9.CreateClosedCircle(0.000000, (c/2), h)
    circle2D7.CenterPoint = point2D37
    circle2D7.ReportName = 5
    reference121 = part1.CreateReferenceFromObject(circle2D7)
    #constraint56 = constraints8.AddMonoEltCst(catCstTypeRadius, reference121)
    #constraint56.Mode = catCstModeDrivingDimension
    #length50 = constraint56.Dimension
    #length50.Value = 25.000000
    sketch9.CenterLine = line2D38
    sketch9.CloseEdition()
    part1.InWorkObject = sketch9
    part1.Update()
    pad5 = shapeFactory1.AddNewPad(sketch9, g)
    
    
    part1.Update()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    

knuckle()
