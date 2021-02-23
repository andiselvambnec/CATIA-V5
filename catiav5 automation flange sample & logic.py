# import python modules
from tkinter import *
import os
from win32com.client import Dispatch

print("opening CAtia...........................")
# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')
# optional CATIA visibility
CATIA.Visible = True

print("CATIA opened.......")
'''
D2 = float(input("flange dia D2="))
D2 = (D2 / 2)

tf = float(input("thickness of flange tf="))

D0 = float(input("diameter of hub D0="))
D0 = (D0 / 2)

L0 = float(input("length of hub L0="))

D1 = float(input("pitch of flange bolt D1"))
D1 = (D1 / 2)

d0 = float(input("diameter of bolt d0="))

n0 = int(input("no of bolt="))
a0 =(360 / n0)

ds = float(input("shaft dia ds="))
ds = (ds / 2)

L1 = float(input("length of shaft L1 ="))

p = float(input("enter a power="))
n = float(input("enter speed="))
t = float(input("enter shear stress"))
'''
root=Tk()

root.title("ANDISELVAM PROJECT")
root.geometry("1280x780")
root.resizable(width=False,height=False)




def flange():
    p = float(box1.get())
    n = float(box2.get())
    t = float(box3.get())
    

    

    mt = ((p * 60)/(2 * 3.14 * n))
    mt = mt * 1000

    ds = (((mt * 16)/(3.14 * t)) ** (1/3))
    ds = round(ds)

    D0 = (2 * ds)   #dia of hub

    D1 = (3 * ds)    # pitch dia of flange bolt

    D2 = (4 * ds)   #outside dia of flange

    L0 = (1.5 * ds) # length of hub

    tf = (0.5 * ds)  #thickness of flange

    L1 = (3 * ds)  ########lenth of shaft

    if(ds < 56):
         n0 = 4
    elif(55 < ds < 151):
         n0 = 6
    elif(150 < ds < 231):
        n0 = 8
    elif(230 < ds < 391):
        n0 = 10
    else:
        n0 = 12


    d0 = (((mt * 4 * 2)/(3.14 * t * n0 * D1)) ** (1/2))
    d0 = round(d0)

    a0 =(360 / n0)

    #for radius and diameter confussion
    D2 = (D2 / 2)
    D0 = (D0 / 2)
    D1 = (D1 / 2)
    ds = (ds / 2)




    

    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneYZ
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = 0.000000
    arrayOfVariantOfDouble1[4] = 1.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = 0.000000
    arrayOfVariantOfDouble1[8] = 1.000000
    sketch1.SetAbsoluteAxisData(arrayOfVariantOfDouble1)
    part1.InWorkObject = sketch1
    factory2D1 = sketch1.OpenEdition()
    geometricElements1 = sketch1.GeometricElements
    axis2D1 = geometricElements1.Item('AbsoluteAxis')
    line2D1 = axis2D1.GetItem('HDirection')
    line2D1.ReportName = 1
    line2D2 = axis2D1.GetItem('VDirection')
    line2D2.ReportName = 2
    circle2D1 = factory2D1.CreateClosedCircle(0.000000, 0.000000, D2)     #D2 flane dia
    point2D1 = axis2D1.GetItem('Origin')
    circle2D1.CenterPoint = point2D1
    circle2D1.ReportName = 3
    point2D2 = factory2D1.CreatePoint(0.000000, D2)
    point2D2.ReportName = 4
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(circle2D1)
    reference3 = part1.CreateReferenceFromObject(point2D2)
    #constraint1 = constraints1.AddBiEltCst(catCstTypeOn, reference2, reference3)
    #constraint1.Mode = catCstModeDrivingDimension
    reference4 = part1.CreateReferenceFromObject(point2D2)
    reference5 = part1.CreateReferenceFromObject(line2D2)
    #constraint2 = constraints1.AddBiEltCst(catCstTypeOn, reference4, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference6 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference6, 20.000000)
    reference7 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference7)
    limit1 = pad1.FirstLimit
    length1 = limit1.Dimension
    length1.Value = tf       #thickness of flange
    part1.Update()
    sketches2 = body1.Sketches
    sketch2 = sketches2.Add(reference1)
    arrayOfVariantOfDouble2=[0,0,0,0,0,0,0,0,0]
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
    factory2D2 = sketch2.OpenEdition()
    geometricElements2 = sketch2.GeometricElements
    axis2D2 = geometricElements2.Item('AbsoluteAxis')
    line2D3 = axis2D2.GetItem('HDirection')
    line2D3.ReportName = 1
    line2D4 = axis2D2.GetItem('VDirection')
    line2D4.ReportName = 2
    circle2D2 = factory2D2.CreateClosedCircle(0.000000, 0.000000, D0)   #D0 hub dia
    point2D3 = axis2D2.GetItem('Origin')
    circle2D2.CenterPoint = point2D3
    circle2D2.ReportName = 3
    point2D4 = factory2D2.CreatePoint(0.000000, D0)
    point2D4.ReportName = 4
    constraints2 = sketch2.Constraints
    reference8 = part1.CreateReferenceFromObject(circle2D2)
    reference9 = part1.CreateReferenceFromObject(point2D4)
    #constraint3 = constraints2.AddBiEltCst(catCstTypeOn, reference8, reference9)
    #constraint3.Mode = catCstModeDrivingDimension
    reference10 = part1.CreateReferenceFromObject(point2D4)
    reference11 = part1.CreateReferenceFromObject(line2D4)
    #constraint4 = constraints2.AddBiEltCst(catCstTypeOn, reference10, reference11)
    #constraint4.Mode = catCstModeDrivingDimension
    sketch2.CloseEdition()
    part1.InWorkObject = sketch2
    part1.Update()
    reference12 = part1.CreateReferenceFromName('')
    pad2 = shapeFactory1.AddNewPadFromRef(reference12, 25.000000)
    reference13 = part1.CreateReferenceFromObject(sketch2)
    pad2.SetProfileElement(reference13)
    limit2 = pad2.FirstLimit
    length2 = limit2.Dimension
    length2.Value = L0           #L0 length of hub
    part1.Update()
    sketch3 = sketches2.Add(reference1)
    arrayOfVariantOfDouble3=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble3[0] = 0.000000
    arrayOfVariantOfDouble3[1] = 0.000000
    arrayOfVariantOfDouble3[2] = 0.000000
    arrayOfVariantOfDouble3[3] = 0.000000
    arrayOfVariantOfDouble3[4] = 1.000000
    arrayOfVariantOfDouble3[5] = 0.000000
    arrayOfVariantOfDouble3[6] = 0.000000
    arrayOfVariantOfDouble3[7] = 0.000000
    arrayOfVariantOfDouble3[8] = 1.000000
    sketch3.SetAbsoluteAxisData(arrayOfVariantOfDouble3)
    part1.InWorkObject = sketch3
    factory2D3 = sketch3.OpenEdition()
    geometricElements3 = sketch3.GeometricElements
    axis2D3 = geometricElements3.Item('AbsoluteAxis')
    line2D5 = axis2D3.GetItem('HDirection')
    line2D5.ReportName = 1
    line2D6 = axis2D3.GetItem('VDirection')
    line2D6.ReportName = 2
    point2D5 = factory2D3.CreatePoint(0.000000, D1)
    point2D5.ReportName = 3
    line2D7 = factory2D3.CreateLine(0.000000, 0.000000, 0.000000, D1)    #bolt pitch
    line2D7.ReportName = 4
    point2D6 = axis2D3.GetItem('Origin')
    line2D7.StartPoint = point2D6
    line2D7.EndPoint = point2D5
    constraints3 = sketch3.Constraints
    reference14 = part1.CreateReferenceFromObject(line2D7)
    reference15 = part1.CreateReferenceFromObject(line2D6)
    #constraint5 = constraints3.AddBiEltCst(catCstTypeVerticality, reference14, reference15)
    #constraint5.Mode = catCstModeDrivingDimension
    circle2D3 = factory2D3.CreateClosedCircle(0.000000, D1, d0)    #D1 pitch dia ,bolt dia
    circle2D3.CenterPoint = point2D5
    circle2D3.ReportName = 5
    sketch3.CenterLine = line2D7
    sketch3.CloseEdition()
    part1.InWorkObject = sketch3
    part1.Update()
    reference16 = part1.CreateReferenceFromName('')
    pocket1 = shapeFactory1.AddNewPocketFromRef(reference16, 75.000000)
    reference17 = part1.CreateReferenceFromObject(sketch3)
    pocket1.SetProfileElement(reference17)
    limit3 = pocket1.FirstLimit
    length3 = limit3.Dimension
    length3.Value = - L0       #length of hub
    part1.Update()
    reference18 = originElements1.PlaneZX
    sketch4 = sketches2.Add(reference18)
    arrayOfVariantOfDouble4=[0,0,0,0,0,0,0,0,0]
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
    factory2D4 = sketch4.OpenEdition()
    geometricElements4 = sketch4.GeometricElements
    axis2D4 = geometricElements4.Item('AbsoluteAxis')
    line2D8 = axis2D4.GetItem('HDirection')
    line2D8.ReportName = 1
    line2D9 = axis2D4.GetItem('VDirection')
    line2D9.ReportName = 2
    point2D7 = factory2D4.CreatePoint(57.475517, 0.000000)
    point2D7.ReportName = 3
    point2D8 = factory2D4.CreatePoint(- 127.680511, 0.000000)
    point2D8.ReportName = 4
    line2D10 = factory2D4.CreateLine(57.475517, 0.000000, - 127.680511, 0.000000)
    line2D10.ReportName = 5
    line2D10.StartPoint = point2D7
    line2D10.EndPoint = point2D8
    constraints4 = sketch4.Constraints
    reference19 = part1.CreateReferenceFromObject(point2D7)
    reference20 = part1.CreateReferenceFromObject(line2D8)
    #constraint6 = constraints4.AddBiEltCst(catCstTypeOn, reference19, reference20)
    #constraint6.Mode = catCstModeDrivingDimension
    reference21 = part1.CreateReferenceFromObject(line2D10)
    reference22 = part1.CreateReferenceFromObject(line2D8)
    #constraint7 = constraints4.AddBiEltCst(catCstTypeHorizontality, reference21, reference22)
    #constraint7.Mode = catCstModeDrivingDimension
    sketch4.CloseEdition()
    part1.InWorkObject = sketch4
    part1.Update()
    reference23 = part1.CreateReferenceFromName('')
    reference24 = part1.CreateReferenceFromName('')
    circPattern1 = shapeFactory1.AddNewCircPattern(None, 1, 2, 20.000000, 45.000000, 1, 1, reference23, reference24, True, 0.000000, True)
    #circPattern1.CircularPatternParameters = catInstancesandAngularSpacing
    #circPattern1.CircularPatternParameters = catInstancesandAngularSpacing
    angularRepartition1 = circPattern1.AngularRepartition
    intParam1 = angularRepartition1.InstancesCount
    intParam1.Value = 6
    angularRepartition2 = circPattern1.AngularRepartition
    angle1 = angularRepartition2.AngularSpacing
    angle1.Value = 45.000000
    intParam1.Value = 6
    angle1.Value = 60.000000
    angle1.Value = a0                      #angle of circular pattern
    intParam1.Value = n0                     #number of bolt
    reference25 = part1.CreateReferenceFromBRepName('WireREdge:(Wire:(Brp:(Sketch.4;5);None:(Limits1:();Limits2:());Cf11:());WithTemporaryBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR15)', sketch4)
    circPattern1.SetRotationAxis(reference25)
    circPattern1.ItemToCopy = pocket1
    part1.Update()
    sketch5 = sketches2.Add(reference1)
    arrayOfVariantOfDouble5=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble5[0] = 0.000000
    arrayOfVariantOfDouble5[1] = 0.000000
    arrayOfVariantOfDouble5[2] = 0.000000
    arrayOfVariantOfDouble5[3] = 0.000000
    arrayOfVariantOfDouble5[4] = 1.000000
    arrayOfVariantOfDouble5[5] = 0.000000
    arrayOfVariantOfDouble5[6] = 0.000000
    arrayOfVariantOfDouble5[7] = 0.000000
    arrayOfVariantOfDouble5[8] = 1.000000
    sketch5.SetAbsoluteAxisData(arrayOfVariantOfDouble5)
    part1.InWorkObject = sketch5
    factory2D5 = sketch5.OpenEdition()
    geometricElements5 = sketch5.GeometricElements
    axis2D5 = geometricElements5.Item('AbsoluteAxis')
    line2D11 = axis2D5.GetItem('HDirection')
    line2D11.ReportName = 1
    line2D12 = axis2D5.GetItem('VDirection')
    line2D12.ReportName = 2
    circle2D4 = factory2D5.CreateClosedCircle(0.000000, 0.000000, ds)    #shaft dia
    point2D9 = axis2D5.GetItem('Origin')
    circle2D4.CenterPoint = point2D9
    circle2D4.ReportName = 3
    sketch5.CloseEdition()
    part1.InWorkObject = sketch5
    part1.Update()
    reference26 = part1.CreateReferenceFromName('')
    pocket2 = shapeFactory1.AddNewPocketFromRef(reference26, - 25.000000)
    limit4 = pocket2.FirstLimit
    length4 = limit4.Dimension
    length4.Value = - L0         #hub length
    reference27 = part1.CreateReferenceFromObject(sketch5)
    pocket2.SetProfileElement(reference27)
    part1.Update()
    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    sketches2 = sketch4.Parent
    bSTR1 = sketch4.Name
    selection1.Add(sketch4)
    visPropertySet1 = visPropertySet1.Parent
    bSTR2 = visPropertySet1.Name
    bSTR3 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    reference28 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
    mirror1 = shapeFactory1.AddNewMirror(reference28)
    part1.Update()
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    body2 = bodies1.Add()
    part1.Update()
    sketches3 = body2.Sketches
    sketch6 = sketches3.Add(reference1)
    arrayOfVariantOfDouble6=[0,0,0,0,0,0,0,0,0]
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
    factory2D6 = sketch6.OpenEdition()
    geometricElements6 = sketch6.GeometricElements
    axis2D6 = geometricElements6.Item('AbsoluteAxis')
    line2D13 = axis2D6.GetItem('HDirection')
    line2D13.ReportName = 1
    line2D14 = axis2D6.GetItem('VDirection')
    line2D14.ReportName = 2
    circle2D5 = factory2D6.CreateClosedCircle(0.000000, 0.000000, ds)     #shaft dia
    point2D10 = axis2D6.GetItem('Origin')
    circle2D5.CenterPoint = point2D10
    circle2D5.ReportName = 3
    sketch6.CloseEdition()
    part1.InWorkObject = sketch6
    part1.Update()
    reference29 = part1.CreateReferenceFromName('')
    pad3 = shapeFactory1.AddNewPadFromRef(reference29, - 75.000000)
    reference30 = part1.CreateReferenceFromObject(sketch6)
    pad3.SetProfileElement(reference30)
    limit5 = pad3.FirstLimit
    length5 = limit5.Dimension
    length5.Value = L1     #length of shaft
    pad3.IsSymmetric = True
    part1.Update()

mylabel1 = Label(root,text="power(w): ",font="Verdana 32 bold italic")

mylabel2 = Label(root,text="speed(rpm): ",font="Verdana 32 bold italic")
mylabel5 = Label(root,text="stress(rpm): ",font="Verdana 32 bold italic")
mylabel3 = Label(root,text="              ")
mylabel4 = Label(root,text="              ")
mylabel4 = Label(root,text="              ")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=2,column=0)
mylabel3.grid(row=1,column=0)
mylabel4.grid(row=3,column=0)
mylabel5.grid(row=4,column=0)

#to create input box
box1=Entry(root,width=50,borderwidth=5,font="Verdana 18 bold italic")
box2=Entry(root,width=50,borderwidth=5,font="Verdana 18 bold italic")
box3=Entry(root,width=50,borderwidth=5,font="Verdana 18 bold italic")

box1.grid(row=0,column=1)
box2.grid(row=2,column=1)
box3.grid(row=4,column=1)

mybutton = Button(root,text="calculate",command=flange)

mybutton.grid(row=5,column=1)

mainloop()



