# import python modules
from tkinter import *
import random
from time import strftime
from tkinter import ttk
from tkinter import messagebox
import os
from win32com.client import Dispatch
# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')

'''
line     name                       

59        knuckle joint function start

131        knuckle pin design

280        knuckle collar

431        knuckle single eye

1151        knuckle double eye

2010       knuckle assembly

4709        knuckle joint function end

4724       gib joint function start

4796        fork end

 5523       rod end

5927        cotter pin

6201        gib pin

6603        gib joint assembly

8466        unit conversion function

8578        GUI tkinter
'''

'''
a=31.25
b=68.75
c=55
d=50
e=25
f=175
g=60
h=25
m=200
u=37.5
v=200
w=25
'''

def knuckle():
    print(kp)
    print(kt)
    foldername = str(box_3.get())
    #materia = materials_list.get()

    
    #making folder for storing files using input folder name
    mainpath="C:/"
    path=os.path.join(mainpath,foldername)
    os.mkdir(path)
    
    #getting input from tkinter entrys
    '''
    kp = float(box1.get())
    kt = float(box2.get())
    na = na +".CATPart"
    '''
    # optional CATIA visibility
    CATIA.Visible = True



    #kp = float(input("power transmitted="))
    #kt = float(input("tensile stress="))
    
   


    #dimension calculations
    kd0 = (((4*kp)/(3.14*kt))**(1/2))    #dia of rod
    kd0 = round(kd0)

    kd1 = (kd0)                       #dia of pin

    kd2 = (2*(kd0))               #outer dia of the eye

    kd3 = (1.5*(kd0))           #dia of pin head
    
    kt0 = (1.25*(kd0))           #thickness of eye

    kt1 = (0.75*(kd0))          #thickness of fork

    kt2 = (0.5*(kd0))            #thickness of pin head

    knuckleloc = ("C:\\%s\\dimensions.txt" %(foldername))
    knucklepdf = open(knuckleloc,"w+")

    knucklepdf.write("Diameter of Rod (d0): %s mm \n" %(kd0))
    knucklepdf.write("Diameter of pin (d1): %s mm \n" %(kd1))
    knucklepdf.write("Outer Diameter of eye (d2) : %s mm \n" %(kd2))
    knucklepdf.write("Diameter of pin head (d3): %s mm \n" %(kd3))
    knucklepdf.write("thickness of eye (t0): %s mm \n" %(kt0))
    knucklepdf.write("thickness of fork (t1): %s mm \n" %(kt1))
    knucklepdf.write("thickness of pin head (t2): %s mm \n" %(kt2))
    knucklepdf.close()

    
    #which is used for reference (a,b,c,d,e,f,g,h,m)
    a = (kt0)/2
    b = ((kt0)+(2*(kt1)))/2
    c = 1.1 * (kd1)
    d = (kd2)/2
    e = (kd1)/2
    f = (4.5*(kd0))- d
    g = 1.2 * (kd1)
    h = (kd0)/2
    m = 4 * (kd0)
    u = (kd3 / 2)
    v = (2*b)+(2 * kt2)+(0.5 * kt2)
    w = kt2
    

    '''
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(m)
    '''
    #knuckle pin design...............................................................................................................
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
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
    circle2D1 = factory2D1.CreateClosedCircle(0.000000, 0.000000, e)
    point2D1 = axis2D1.GetItem('Origin')
    circle2D1.CenterPoint = point2D1
    circle2D1.ReportName = 3
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(circle2D1)
    #constraint1 = constraints1.AddMonoEltCst(catCstTypeRadius, reference2)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 25.000000
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference3 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference3, 20.000000)
    reference4 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference4)
    limit1 = pad1.FirstLimit
    length2 = limit1.Dimension
    length2.Value = v
    part1.Update()
    sketches2 = body1.Sketches
    sketch2 = sketches2.Add(reference1)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = - 1.000000
    arrayOfVariantOfDouble2[4] = 0.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = - 0.000000
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
    circle2D2 = factory2D2.CreateClosedCircle(0.000000, 0.000000, u)
    point2D2 = axis2D2.GetItem('Origin')
    circle2D2.CenterPoint = point2D2
    circle2D2.ReportName = 3
    constraints2 = sketch2.Constraints
    reference5 = part1.CreateReferenceFromObject(circle2D2)
    #constraint2 = constraints2.AddMonoEltCst(catCstTypeRadius, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    #length3 = constraint2.Dimension
    #length3.Value = 37.500000
    sketch2.CloseEdition()
    part1.InWorkObject = sketch2
    part1.Update()
    pad2 = shapeFactory1.AddNewPad(sketch2, 200.000000)
    limit2 = pad2.FirstLimit
    length4 = limit2.Dimension
    length4.Value = w
    part1.Update()
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("China Blue")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()


    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\knuckle_pin.CATPart' %(foldername))


    #knuckle pin collar design.....................................................................................................................
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0]
    
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
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
    circle2D1 = factory2D1.CreateClosedCircle(0.000000, 0.000000, u)
    point2D1 = axis2D1.GetItem('Origin')
    circle2D1.CenterPoint = point2D1
    circle2D1.ReportName = 3
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(circle2D1)
    #constraint1 = constraints1.AddMonoEltCst(catCstTypeRadius, reference2)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 37.500000
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference3 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference3, 20.000000)
    reference4 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference4)
    limit1 = pad1.FirstLimit
    length2 = limit1.Dimension
    length2.Value = w
    part1.Update()
    sketches2 = body1.Sketches
    sketch2 = sketches2.Add(reference1)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = - 1.000000
    arrayOfVariantOfDouble2[4] = 0.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = - 0.000000
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
    circle2D2 = factory2D2.CreateClosedCircle(0.000000, 0.000000, e)
    point2D2 = axis2D2.GetItem('Origin')
    circle2D2.CenterPoint = point2D2
    circle2D2.ReportName = 3
    constraints2 = sketch2.Constraints
    reference5 = part1.CreateReferenceFromObject(circle2D2)
    #constraint2 = constraints2.AddMonoEltCst(catCstTypeRadius, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    #length3 = constraint2.Dimension
    #length3.Value = 25.000000
    sketch2.CloseEdition()
    part1.InWorkObject = sketch2
    part1.Update()
    reference6 = part1.CreateReferenceFromName('')
    pocket1 = shapeFactory1.AddNewPocketFromRef(reference6, 25.000000)
    reference7 = part1.CreateReferenceFromObject(sketch2)
    pocket1.SetProfileElement(reference7)
    limit2 = pocket1.FirstLimit
    length4 = limit2.Dimension
    length4.Value = - w
    part1.Update()

    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()

    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    #hide a plane
    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''

    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("Light Green")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\knuckle_pin_collar.CATPart' %(foldername))
    
    #single eye design start..............................................................................................................
    arrayOfVariantOfDouble1=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble3=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble4=[0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble5=[0,0,0,0,0,0,0,0,0]
    
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
    arrayOfVariantOfDouble1[8] = 1.000000
    sketch1.SetAbsoluteAxisData(arrayOfVariantOfDouble1)
    part1.InWorkObject = sketch1
    factory2D1 = sketch1.OpenEdition()                                   #sketch 1 opened
    geometricElements1 = sketch1.GeometricElements
    axis2D1 = geometricElements1.Item('AbsoluteAxis')
    line2D1 = axis2D1.GetItem('HDirection')
    line2D1.ReportName = 1
    line2D2 = axis2D1.GetItem('VDirection')
    line2D2.ReportName = 2
    point2D1 = factory2D1.CreatePoint(0, 0)
    point2D1.ReportName = 3
    circle2D1 = factory2D1.CreateClosedCircle(0.000000, 0, d)     #diameter of outer(d)
    circle2D1.CenterPoint = point2D1
    circle2D1.ReportName = 4
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(point2D1)
    reference3 = part1.CreateReferenceFromObject(line2D2)
    #onstraint1 = constraints1.AddBiEltCst(catCstTypeOn, reference2, reference3)
    #constraint1.Mode = catCstModeDrivingDimension
    point2D2 = factory2D1.CreatePoint(d, 0.000000)
    point2D2.ReportName = 5
    reference4 = part1.CreateReferenceFromObject(circle2D1)
    reference5 = part1.CreateReferenceFromObject(point2D2)
    #constraint2 = constraints1.AddBiEltCst(catCstTypeOn, reference4, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    reference6 = part1.CreateReferenceFromObject(point2D2)
    reference7 = part1.CreateReferenceFromObject(line2D1)
    #constraint3 = constraints1.AddBiEltCst(catCstTypeOn, reference6, reference7)
    #constraint3.Mode = catCstModeDrivingDimension
    sketch1.CloseEdition()                                                        #sketch 1 closed
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference8 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference8, 20.000000)
    reference9 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference9)
    pad1.IsSymmetric = True
    limit1 = pad1.FirstLimit
    length1 = limit1.Dimension
    length1.Value = a
    part1.Update()

    
    sketches2 = body1.Sketches
    sketch2 = sketches2.Add(reference1)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = - 1.000000
    arrayOfVariantOfDouble2[4] = 0.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = - 0.000000
    arrayOfVariantOfDouble2[8] = 1.000000
    sketch2.SetAbsoluteAxisData(arrayOfVariantOfDouble2)
    part1.InWorkObject = sketch2
    factory2D2 = sketch2.OpenEdition()                                               #sketch 2 opened
    geometricElements2 = sketch2.GeometricElements
    axis2D2 = geometricElements2.Item('AbsoluteAxis')
    line2D3 = axis2D2.GetItem('HDirection')
    line2D3.ReportName = 1
    line2D4 = axis2D2.GetItem('VDirection')
    line2D4.ReportName = 2
    point2D3 = factory2D2.CreatePoint(0.000000, 0.000000)
    point2D3.ReportName = 3
    point2D4 = factory2D2.CreatePoint(0.000000, (c/2))
    point2D4.ReportName = 4
    line2D5 = factory2D2.CreateLine(0.000000, 0.000000, 0.000000, (c/2))
    line2D5.ReportName = 5
    line2D5.StartPoint = point2D3
    line2D5.EndPoint = point2D4
    constraints2 = sketch2.Constraints
    reference10 = part1.CreateReferenceFromObject(point2D3)
    reference11 = part1.CreateReferenceFromObject(line2D4)
    #constraint4 = constraints2.AddBiEltCst(catCstTypeDistance, reference10, reference11)
    #constraint4.Mode = catCstModeDrivingDimension
    #length2 = constraint4.Dimension
    #length2.Value = 0.000000
    reference12 = part1.CreateReferenceFromObject(point2D3)
    reference13 = part1.CreateReferenceFromObject(line2D3)
    #constraint5 = constraints2.AddBiEltCst(catCstTypeDistance, reference12, reference13)
    #constraint5.Mode = catCstModeDrivingDimension
    #length3 = constraint5.Dimension
    #length3.Value = 0.000000
    reference14 = part1.CreateReferenceFromObject(point2D4)
    reference15 = part1.CreateReferenceFromObject(line2D4)
    #constraint6 = constraints2.AddBiEltCst(catCstTypeDistance, reference14, reference15)
    #constraint6.Mode = catCstModeDrivingDimension
    #length4 = constraint6.Dimension
    #length4.Value = 0.000000
    reference16 = part1.CreateReferenceFromObject(point2D4)
    reference17 = part1.CreateReferenceFromObject(line2D3)
    #constraint7 = constraints2.AddBiEltCst(catCstTypeDistance, reference16, reference17)
    #constraint7.Mode = catCstModeDrivingDimension
    #length5 = constraint7.Dimension
    #length5.Value = 27.500000
    point2D5 = factory2D2.CreatePoint(0.000000, (c/2))
    point2D5.ReportName = 6
    point2D6 = factory2D2.CreatePoint(m, (c/2))           #m is a 4.5kd
    point2D6.ReportName = 7
    line2D6 = factory2D2.CreateLine(0.000000, (c/2), m, (c/2))
    line2D6.ReportName = 8
    line2D6.StartPoint = point2D5
    line2D6.EndPoint = point2D6
    reference18 = part1.CreateReferenceFromObject(point2D5)
    reference19 = part1.CreateReferenceFromObject(line2D4)
    #constraint8 = constraints2.AddBiEltCst(catCstTypeDistance, reference18, reference19)
    #constraint8.Mode = catCstModeDrivingDimension
    #length6 = constraint8.Dimension
    #length6.Value = 0.000000
    reference20 = part1.CreateReferenceFromObject(point2D5)
    reference21 = part1.CreateReferenceFromObject(line2D3)
    #constraint9 = constraints2.AddBiEltCst(catCstTypeDistance, reference20, reference21)
    #constraint9.Mode = catCstModeDrivingDimension
    #length7 = constraint9.Dimension
    #length7.Value = 27.500000
    reference22 = part1.CreateReferenceFromObject(point2D6)
    reference23 = part1.CreateReferenceFromObject(line2D4)
    #constraint10 = constraints2.AddBiEltCst(catCstTypeDistance, reference22, reference23)
    #constraint10.Mode = catCstModeDrivingDimension
    #length8 = constraint10.Dimension
    #length8.Value = 225.000000
    reference24 = part1.CreateReferenceFromObject(point2D6)
    reference25 = part1.CreateReferenceFromObject(line2D3)
    #constraint11 = constraints2.AddBiEltCst(catCstTypeDistance, reference24, reference25)
    #constraint11.Mode = catCstModeDrivingDimension
    #length9 = constraint11.Dimension
    #length9.Value = 27.500000
    point2D7 = factory2D2.CreatePoint(m, (c/2))
    point2D7.ReportName = 9
    point2D8 = factory2D2.CreatePoint(m, - (c/2))
    point2D8.ReportName = 10
    line2D7 = factory2D2.CreateLine(m, (c/2), m, - (c/2))
    line2D7.ReportName = 11
    line2D7.StartPoint = point2D7
    line2D7.EndPoint = point2D8
    reference26 = part1.CreateReferenceFromObject(point2D7)
    reference27 = part1.CreateReferenceFromObject(line2D4)
    #constraint12 = constraints2.AddBiEltCst(catCstTypeDistance, reference26, reference27)
    #constraint12.Mode = catCstModeDrivingDimension
    #length10 = constraint12.Dimension
    #length10.Value = 225.000000
    reference28 = part1.CreateReferenceFromObject(point2D7)
    reference29 = part1.CreateReferenceFromObject(line2D3)
    #constraint13 = constraints2.AddBiEltCst(catCstTypeDistance, reference28, reference29)
    #constraint13.Mode = catCstModeDrivingDimension
    #length11 = constraint13.Dimension
    #length11.Value = 27.500000
    reference30 = part1.CreateReferenceFromObject(point2D8)
    reference31 = part1.CreateReferenceFromObject(line2D4)
    #constraint14 = constraints2.AddBiEltCst(catCstTypeDistance, reference30, reference31)
    #constraint14.Mode = catCstModeDrivingDimension
    #length12 = constraint14.Dimension
    #length12.Value = 225.000000
    reference32 = part1.CreateReferenceFromObject(point2D8)
    reference33 = part1.CreateReferenceFromObject(line2D3)
    #constraint15 = constraints2.AddBiEltCst(catCstTypeDistance, reference32, reference33)
    #constraint15.Mode = catCstModeDrivingDimension
    #length13 = constraint15.Dimension
    #length13.Value = 27.500000
    point2D9 = factory2D2.CreatePoint(m, - (c/2))
    point2D9.ReportName = 12
    point2D10 = factory2D2.CreatePoint(0.000000, - (c/2))
    point2D10.ReportName = 13
    line2D8 = factory2D2.CreateLine(m, - (c/2), 0.000000, - (c/2))
    line2D8.ReportName = 14
    line2D8.StartPoint = point2D9
    line2D8.EndPoint = point2D10
    reference34 = part1.CreateReferenceFromObject(point2D9)
    reference35 = part1.CreateReferenceFromObject(line2D4)
    #constraint16 = constraints2.AddBiEltCst(catCstTypeDistance, reference34, reference35)
    #constraint16.Mode = catCstModeDrivingDimension
    #length14 = constraint16.Dimension
    #length14.Value = 225.000000
    reference36 = part1.CreateReferenceFromObject(point2D9)
    reference37 = part1.CreateReferenceFromObject(line2D3)
    #constraint17 = constraints2.AddBiEltCst(catCstTypeDistance, reference36, reference37)
    #constraint17.Mode = catCstModeDrivingDimension
    #length15 = constraint17.Dimension
    #length15.Value = 27.500000
    reference38 = part1.CreateReferenceFromObject(point2D10)
    reference39 = part1.CreateReferenceFromObject(line2D4)
    #constraint18 = constraints2.AddBiEltCst(catCstTypeDistance, reference38, reference39)
    #constraint18.Mode = catCstModeDrivingDimension
    #length16 = constraint18.Dimension
    #length16.Value = 0.000000
    reference40 = part1.CreateReferenceFromObject(point2D10)
    reference41 = part1.CreateReferenceFromObject(line2D3)
    #constraint19 = constraints2.AddBiEltCst(catCstTypeDistance, reference40, reference41)
    #constraint19.Mode = catCstModeDrivingDimension
    #length17 = constraint19.Dimension
    #length17.Value = 27.500000
    point2D11 = factory2D2.CreatePoint(0.000000, - (c/2))
    point2D11.ReportName = 15
    point2D12 = factory2D2.CreatePoint(0.000000, 0.000000)
    point2D12.ReportName = 16
    line2D9 = factory2D2.CreateLine(0.000000, - (c/2), 0.000000, 0.000000)
    line2D9.ReportName = 17
    line2D9.StartPoint = point2D11
    line2D9.EndPoint = point2D12
    reference42 = part1.CreateReferenceFromObject(point2D11)
    reference43 = part1.CreateReferenceFromObject(line2D4)
    #constraint20 = constraints2.AddBiEltCst(catCstTypeDistance, reference42, reference43)
    #constraint20.Mode = catCstModeDrivingDimension
    #length18 = constraint20.Dimension
    #length18.Value = 0.000000
    reference44 = part1.CreateReferenceFromObject(point2D11)
    reference45 = part1.CreateReferenceFromObject(line2D3)
    #constraint21 = constraints2.AddBiEltCst(catCstTypeDistance, reference44, reference45)
    #constraint21.Mode = catCstModeDrivingDimension
    #length19 = constraint21.Dimension
    #length19.Value = 27.500000
    reference46 = part1.CreateReferenceFromObject(point2D12)
    reference47 = part1.CreateReferenceFromObject(line2D4)
    #constraint22 = constraints2.AddBiEltCst(catCstTypeDistance, reference46, reference47)
    #constraint22.Mode = catCstModeDrivingDimension
    #length20 = constraint22.Dimension
    #length20.Value = 0.000000
    reference48 = part1.CreateReferenceFromObject(point2D12)
    reference49 = part1.CreateReferenceFromObject(line2D3)
    #constraint23 = constraints2.AddBiEltCst(catCstTypeDistance, reference48, reference49)
    #constraint23.Mode = catCstModeDrivingDimension
    #length21 = constraint23.Dimension
    #length21.Value = 0.000000
    sketch2.CloseEdition()                                                                         #sketch 2 closed
    part1.InWorkObject = sketch2
    part1.Update()
    reference50 = part1.CreateReferenceFromName('')
    pad2 = shapeFactory1.AddNewPadFromRef(reference50, 31.250000)
    reference51 = part1.CreateReferenceFromObject(sketch2)
    pad2.SetProfileElement(reference51)
    pad2.IsSymmetric = True
    limit2 = pad2.FirstLimit
    length22 = limit2.Dimension
    length22.Value = (c/2)                                                         #c=1.1kd1
    part1.Update()
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D

    
    reference52 = part1.CreateReferenceFromName('Selection_RSur:(Face:(Brp:(Pad.2;0:(Brp:(Sketch.2;11)));None:();Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    sketch3 = sketches2.Add(reference52)
    arrayOfVariantOfDouble3[0] = - m
    arrayOfVariantOfDouble3[1] = 0.000000
    arrayOfVariantOfDouble3[2] = 0.000000
    arrayOfVariantOfDouble3[3] = 0.000000
    arrayOfVariantOfDouble3[4] = - 1.000000
    arrayOfVariantOfDouble3[5] = 0.000000
    arrayOfVariantOfDouble3[6] = 0.000000
    arrayOfVariantOfDouble3[7] = 0.000000
    arrayOfVariantOfDouble3[8] = 1.000000
    sketch3.SetAbsoluteAxisData(arrayOfVariantOfDouble3)
    part1.InWorkObject = sketch3
    factory2D3 = sketch3.OpenEdition()                                                             #sketch 3 opened
    geometricElements3 = sketch3.GeometricElements
    axis2D3 = geometricElements3.Item('AbsoluteAxis')
    line2D10 = axis2D3.GetItem('HDirection')
    line2D10.ReportName = 1
    line2D11 = axis2D3.GetItem('VDirection')
    line2D11.ReportName = 2
    point2D13 = factory2D3.CreatePoint((c/2), (c/2))
    point2D13.ReportName = 3
    point2D14 = factory2D3.CreatePoint((c/2), (c/4))
    point2D14.ReportName = 4
    line2D12 = factory2D3.CreateLine((c/2), (c/2), (c/2), (c/4))
    line2D12.ReportName = 5
    line2D12.StartPoint = point2D13
    line2D12.EndPoint = point2D14
    constraints3 = sketch3.Constraints
    reference53 = part1.CreateReferenceFromObject(point2D13)
    reference54 = part1.CreateReferenceFromObject(line2D11)
    #constraint24 = constraints3.AddBiEltCst(catCstTypeDistance, reference53, reference54)
    #constraint24.Mode = catCstModeDrivingDimension
    #length23 = constraint24.Dimension
    #length23.Value = 27.500000
    reference55 = part1.CreateReferenceFromObject(point2D13)
    reference56 = part1.CreateReferenceFromObject(line2D10)
    #constraint25 = constraints3.AddBiEltCst(catCstTypeDistance, reference55, reference56)
    #constraint25.Mode = catCstModeDrivingDimension
    #length24 = constraint25.Dimension
    #length24.Value = 27.500000
    reference57 = part1.CreateReferenceFromObject(point2D14)
    reference58 = part1.CreateReferenceFromObject(line2D11)
    #constraint26 = constraints3.AddBiEltCst(catCstTypeDistance, reference57, reference58)
    #constraint26.Mode = catCstModeDrivingDimension
    #length25 = constraint26.Dimension
    #length25.Value = 27.500000
    reference59 = part1.CreateReferenceFromObject(point2D14)
    reference60 = part1.CreateReferenceFromObject(line2D10)
    #constraint27 = constraints3.AddBiEltCst(catCstTypeDistance, reference59, reference60)
    #constraint27.Mode = catCstModeDrivingDimension
    #length26 = constraint27.Dimension
    #length26.Value = 13.750000
    point2D15 = factory2D3.CreatePoint((c/2), (c/2))
    point2D15.ReportName = 6
    point2D16 = factory2D3.CreatePoint((c/4), (c/2))
    point2D16.ReportName = 7
    line2D13 = factory2D3.CreateLine((c/2), (c/2), (c/4), (c/2))
    line2D13.ReportName = 8
    line2D13.StartPoint = point2D15
    line2D13.EndPoint = point2D16
    reference61 = part1.CreateReferenceFromObject(point2D15)
    reference62 = part1.CreateReferenceFromObject(line2D11)
    #constraint28 = constraints3.AddBiEltCst(catCstTypeDistance, reference61, reference62)
    #constraint28.Mode = catCstModeDrivingDimension
    #length27 = constraint28.Dimension
    #length27.Value = 27.500000
    reference63 = part1.CreateReferenceFromObject(point2D15)
    reference64 = part1.CreateReferenceFromObject(line2D10)
    #constraint29 = constraints3.AddBiEltCst(catCstTypeDistance, reference63, reference64)
    #constraint29.Mode = catCstModeDrivingDimension
    #length28 = constraint29.Dimension
    #length28.Value = 27.500000
    reference65 = part1.CreateReferenceFromObject(point2D16)
    reference66 = part1.CreateReferenceFromObject(line2D11)
    #constraint30 = constraints3.AddBiEltCst(catCstTypeDistance, reference65, reference66)
    #constraint30.Mode = catCstModeDrivingDimension
    #length29 = constraint30.Dimension
    #length29.Value = 13.750000
    reference67 = part1.CreateReferenceFromObject(point2D16)
    reference68 = part1.CreateReferenceFromObject(line2D10)
    #constraint31 = constraints3.AddBiEltCst(catCstTypeDistance, reference67, reference68)
    #constraint31.Mode = catCstModeDrivingDimension
    #length30 = constraint31.Dimension
    #length30.Value = 27.500000
    point2D17 = factory2D3.CreatePoint(- (c/2), (c/2))
    point2D17.ReportName = 9
    point2D18 = factory2D3.CreatePoint(- (c/2), (c/4))
    point2D18.ReportName = 10
    line2D14 = factory2D3.CreateLine(- (c/2), (c/2), - (c/2), (c/4))
    line2D14.ReportName = 11
    line2D14.StartPoint = point2D17
    line2D14.EndPoint = point2D18
    reference69 = part1.CreateReferenceFromObject(point2D17)
    reference70 = part1.CreateReferenceFromObject(line2D11)
    #constraint32 = constraints3.AddBiEltCst(catCstTypeDistance, reference69, reference70)
    #constraint32.Mode = catCstModeDrivingDimension
    #length31 = constraint32.Dimension
    #length31.Value = 27.500000
    reference71 = part1.CreateReferenceFromObject(point2D17)
    reference72 = part1.CreateReferenceFromObject(line2D10)
    #constraint33 = constraints3.AddBiEltCst(catCstTypeDistance, reference71, reference72)
    #constraint33.Mode = catCstModeDrivingDimension
    #length32 = constraint33.Dimension
    #length32.Value = 27.500000
    reference73 = part1.CreateReferenceFromObject(point2D18)
    reference74 = part1.CreateReferenceFromObject(line2D11)
    #constraint34 = constraints3.AddBiEltCst(catCstTypeDistance, reference73, reference74)
    #constraint34.Mode = catCstModeDrivingDimension
    #length33 = constraint34.Dimension
    #length33.Value = 27.500000
    reference75 = part1.CreateReferenceFromObject(point2D18)
    reference76 = part1.CreateReferenceFromObject(line2D10)
    #constraint35 = constraints3.AddBiEltCst(catCstTypeDistance, reference75, reference76)
    #constraint35.Mode = catCstModeDrivingDimension
    #length34 = constraint35.Dimension
    #length34.Value = 13.750000
    point2D19 = factory2D3.CreatePoint(- (c/2), (c/2))
    point2D19.ReportName = 12
    point2D20 = factory2D3.CreatePoint(- (c/4), (c/2))
    point2D20.ReportName = 13
    line2D15 = factory2D3.CreateLine(- (c/2), (c/2), - (c/4), (c/2))
    line2D15.ReportName = 14
    line2D15.StartPoint = point2D19
    line2D15.EndPoint = point2D20
    reference77 = part1.CreateReferenceFromObject(point2D19)
    reference78 = part1.CreateReferenceFromObject(line2D11)
    #constraint36 = constraints3.AddBiEltCst(catCstTypeDistance, reference77, reference78)
    #constraint36.Mode = catCstModeDrivingDimension
    #length35 = constraint36.Dimension
    #length35.Value = 27.500000
    reference79 = part1.CreateReferenceFromObject(point2D19)
    reference80 = part1.CreateReferenceFromObject(line2D10)
    #constraint37 = constraints3.AddBiEltCst(catCstTypeDistance, reference79, reference80)
    #constraint37.Mode = catCstModeDrivingDimension
    #length36 = constraint37.Dimension
    #length36.Value = 27.500000
    reference81 = part1.CreateReferenceFromObject(point2D20)
    reference82 = part1.CreateReferenceFromObject(line2D11)
    #constraint38 = constraints3.AddBiEltCst(catCstTypeDistance, reference81, reference82)
    #constraint38.Mode = catCstModeDrivingDimension
    #length37 = constraint38.Dimension
    #length37.Value = 13.750000
    reference83 = part1.CreateReferenceFromObject(point2D20)
    reference84 = part1.CreateReferenceFromObject(line2D10)
    #constraint39 = constraints3.AddBiEltCst(catCstTypeDistance, reference83, reference84)
    #constraint39.Mode = catCstModeDrivingDimension
    #length38 = constraint39.Dimension
    #length38.Value = 27.500000
    point2D21 = factory2D3.CreatePoint(- (c/2), - (c/2))
    point2D21.ReportName = 15
    point2D22 = factory2D3.CreatePoint(- (c/2), - (c/4))
    point2D22.ReportName = 16
    line2D16 = factory2D3.CreateLine(- (c/2), - (c/2), - (c/2), - (c/4))
    line2D16.ReportName = 17
    line2D16.StartPoint = point2D21
    line2D16.EndPoint = point2D22
    reference85 = part1.CreateReferenceFromObject(point2D21)
    reference86 = part1.CreateReferenceFromObject(line2D11)
    #constraint40 = constraints3.AddBiEltCst(catCstTypeDistance, reference85, reference86)
    #constraint40.Mode = catCstModeDrivingDimension
    #length39 = constraint40.Dimension
    #length39.Value = 27.500000
    reference87 = part1.CreateReferenceFromObject(point2D21)
    reference88 = part1.CreateReferenceFromObject(line2D10)
    #constraint41 = constraints3.AddBiEltCst(catCstTypeDistance, reference87, reference88)
    #constraint41.Mode = catCstModeDrivingDimension
    #length40 = constraint41.Dimension
    #length40.Value = 27.500000
    reference89 = part1.CreateReferenceFromObject(point2D22)
    reference90 = part1.CreateReferenceFromObject(line2D11)
    #constraint42 = constraints3.AddBiEltCst(catCstTypeDistance, reference89, reference90)
    #constraint42.Mode = catCstModeDrivingDimension
    #length41 = constraint42.Dimension
    #length41.Value = 27.500000
    reference91 = part1.CreateReferenceFromObject(point2D22)
    reference92 = part1.CreateReferenceFromObject(line2D10)
    #constraint43 = constraints3.AddBiEltCst(catCstTypeDistance, reference91, reference92)
    #constraint43.Mode = catCstModeDrivingDimension
    #length42 = constraint43.Dimension
    #length42.Value = 13.750000
    point2D23 = factory2D3.CreatePoint(- (c/2), - (c/2))
    point2D23.ReportName = 18
    point2D24 = factory2D3.CreatePoint(- (c/4), - (c/2))
    point2D24.ReportName = 19
    line2D17 = factory2D3.CreateLine(- (c/2), - (c/2), - (c/4), - (c/2))
    line2D17.ReportName = 20
    line2D17.StartPoint = point2D23
    line2D17.EndPoint = point2D24
    reference93 = part1.CreateReferenceFromObject(point2D23)
    reference94 = part1.CreateReferenceFromObject(line2D11)
    #constraint44 = constraints3.AddBiEltCst(catCstTypeDistance, reference93, reference94)
    #constraint44.Mode = catCstModeDrivingDimension
    #length43 = constraint44.Dimension
    #length43.Value = 27.500000
    reference95 = part1.CreateReferenceFromObject(point2D23)
    reference96 = part1.CreateReferenceFromObject(line2D10)
    #constraint45 = constraints3.AddBiEltCst(catCstTypeDistance, reference95, reference96)
    #constraint45.Mode = catCstModeDrivingDimension
    #length44 = constraint45.Dimension
    #length44.Value = 27.500000
    reference97 = part1.CreateReferenceFromObject(point2D24)
    reference98 = part1.CreateReferenceFromObject(line2D11)
    #constraint46 = constraints3.AddBiEltCst(catCstTypeDistance, reference97, reference98)
    #constraint46.Mode = catCstModeDrivingDimension
    #length45 = constraint46.Dimension
    #length45.Value = 13.750000
    reference99 = part1.CreateReferenceFromObject(point2D24)
    reference100 = part1.CreateReferenceFromObject(line2D10)
    #constraint47 = constraints3.AddBiEltCst(catCstTypeDistance, reference99, reference100)
    #constraint47.Mode = catCstModeDrivingDimension
    #length46 = constraint47.Dimension
    #length46.Value = 27.500000

    
    point2D25 = factory2D3.CreatePoint((c/2), - (c/2))
    point2D25.ReportName = 21
    point2D26 = factory2D3.CreatePoint((c/2), - (c/4))
    point2D26.ReportName = 22
    line2D18 = factory2D3.CreateLine((c/2), - (c/2), (c/2), - (c/4))
    line2D18.ReportName = 23
    line2D18.StartPoint = point2D25
    line2D18.EndPoint = point2D26
    reference101 = part1.CreateReferenceFromObject(point2D25)
    reference102 = part1.CreateReferenceFromObject(line2D11)
    #constraint48 = constraints3.AddBiEltCst(catCstTypeDistance, reference101, reference102)
    #constraint48.Mode = catCstModeDrivingDimension
    #length47 = constraint48.Dimension
    #length47.Value = 27.500000
    reference103 = part1.CreateReferenceFromObject(point2D25)
    reference104 = part1.CreateReferenceFromObject(line2D10)
    #constraint49 = constraints3.AddBiEltCst(catCstTypeDistance, reference103, reference104)
    #constraint49.Mode = catCstModeDrivingDimension
    #length48 = constraint49.Dimension
    #length48.Value = 27.500000
    reference105 = part1.CreateReferenceFromObject(point2D26)
    reference106 = part1.CreateReferenceFromObject(line2D11)
    #constraint50 = constraints3.AddBiEltCst(catCstTypeDistance, reference105, reference106)
    #constraint50.Mode = catCstModeDrivingDimension
    #length49 = constraint50.Dimension
    #length49.Value = 27.500000
    reference107 = part1.CreateReferenceFromObject(point2D26)
    reference108 = part1.CreateReferenceFromObject(line2D10)
    #constraint51 = constraints3.AddBiEltCst(catCstTypeDistance, reference107, reference108)
    #constraint51.Mode = catCstModeDrivingDimension
    #length50 = constraint51.Dimension
    #length50.Value = 13.750000
    point2D27 = factory2D3.CreatePoint((c/2), - (c/2))
    point2D27.ReportName = 24
    point2D28 = factory2D3.CreatePoint((c/4), - (c/2))
    point2D28.ReportName = 25
    line2D19 = factory2D3.CreateLine((c/2), - (c/2), (c/4), - (c/2))
    line2D19.ReportName = 26
    line2D19.StartPoint = point2D27
    line2D19.EndPoint = point2D28
    reference109 = part1.CreateReferenceFromObject(point2D27)
    reference110 = part1.CreateReferenceFromObject(line2D11)
    #constraint52 = constraints3.AddBiEltCst(catCstTypeDistance, reference109, reference110)
    #constraint52.Mode = catCstModeDrivingDimension
    #length51 = constraint52.Dimension
    #length51.Value = 27.500000
    reference111 = part1.CreateReferenceFromObject(point2D27)
    reference112 = part1.CreateReferenceFromObject(line2D10)
    #constraint53 = constraints3.AddBiEltCst(catCstTypeDistance, reference111, reference112)
    #constraint53.Mode = catCstModeDrivingDimension
    #length52 = constraint53.Dimension
    #length52.Value = 27.500000
    reference113 = part1.CreateReferenceFromObject(point2D28)
    reference114 = part1.CreateReferenceFromObject(line2D11)
    #constraint54 = constraints3.AddBiEltCst(catCstTypeDistance, reference113, reference114)
    #constraint54.Mode = catCstModeDrivingDimension
    #length53 = constraint54.Dimension
    #length53.Value = 13.750000
    reference115 = part1.CreateReferenceFromObject(point2D28)
    reference116 = part1.CreateReferenceFromObject(line2D10)
    #constraint55 = constraints3.AddBiEltCst(catCstTypeDistance, reference115, reference116)
    #constraint55.Mode = catCstModeDrivingDimension
    #length54 = constraint55.Dimension
    #length54.Value = 27.500000
    line2D20 = factory2D3.CreateLine((c/4), (c/2), (c/2), (c/4))
    line2D20.ReportName = 27
    line2D20.StartPoint = point2D16
    line2D20.EndPoint = point2D14
    line2D21 = factory2D3.CreateLine(- (c/2), (c/4), - (c/4), (c/2))
    line2D21.ReportName = 28
    line2D21.StartPoint = point2D18
    line2D21.EndPoint = point2D20
    line2D22 = factory2D3.CreateLine(- (c/2), - (c/4), - (c/4), - (c/2))
    line2D22.ReportName = 29
    line2D22.StartPoint = point2D22
    line2D22.EndPoint = point2D24
    line2D23 = factory2D3.CreateLine((c/4), - (c/2), (c/2), - (c/4))
    line2D23.ReportName = 30
    line2D23.StartPoint = point2D28
    line2D23.EndPoint = point2D26
    
    sketch3.CloseEdition()
    part1.InWorkObject = sketch3
    part1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    pocket1 = shapeFactory1.AddNewPocket(sketch3, 27.500000)
    limit3 = pocket1.FirstLimit
    length55 = limit3.Dimension
    length55.Value = g                                                     #g is 1.2kd1
    part1.Update()

    
    
    reference117 = part1.CreateReferenceFromName('Selection_RSur:(Face:(Brp:(Pad.1;2);None:();Cf11:());Pocket.1_ResultOUT;Z0;G3563)')
    sketch4 = sketches2.Add(reference117)
    arrayOfVariantOfDouble4[0] = 0.000000
    arrayOfVariantOfDouble4[1] = a
    arrayOfVariantOfDouble4[2] = 0.000000
    arrayOfVariantOfDouble4[3] = - 1.000000
    arrayOfVariantOfDouble4[4] = 0.000000
    arrayOfVariantOfDouble4[5] = 0.000000
    arrayOfVariantOfDouble4[6] = 0.000000
    arrayOfVariantOfDouble4[7] = 0.000000
    arrayOfVariantOfDouble4[8] = 1.000000
    sketch4.SetAbsoluteAxisData(arrayOfVariantOfDouble4)
    part1.InWorkObject = sketch4
    factory2D4 = sketch4.OpenEdition()                                        #sketch 4 open
    geometricElements4 = sketch4.GeometricElements
    axis2D4 = geometricElements4.Item('AbsoluteAxis')
    line2D24 = axis2D4.GetItem('HDirection')
    line2D24.ReportName = 1
    line2D25 = axis2D4.GetItem('VDirection')
    line2D25.ReportName = 2
    circle2D2 = factory2D4.CreateClosedCircle(0.000000, 0.000000, e)
    point2D29 = axis2D4.GetItem('Origin')
    circle2D2.CenterPoint = point2D29
    circle2D2.ReportName = 3
    constraints4 = sketch4.Constraints
    reference118 = part1.CreateReferenceFromObject(circle2D2)
    #constraint56 = constraints4.AddMonoEltCst(catCstTypeRadius, reference118)
    #constraint56.Mode = catCstModeDrivingDimension
    #length56 = constraint56.Dimension
    #length56.Value = 25.000000
    sketch4.CloseEdition()                                                      #sketch 4 closed
    part1.InWorkObject = sketch4
    part1.Update()
    reference119 = part1.CreateReferenceFromName('')
    pocket2 = shapeFactory1.AddNewPocketFromRef(reference119, 60.000000)
    reference120 = part1.CreateReferenceFromObject(sketch4)
    pocket2.SetProfileElement(reference120)
    limit4 = pocket2.FirstLimit
    length57 = limit4.Dimension
    length57.Value = (2*a)                                             #pad
    part1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    reference121 = part1.CreateReferenceFromName('Selection_RSur:(Face:(Brp:(Pad.2;0:(Brp:(Sketch.2;11)));None:();Cf11:());Pocket.2_ResultOUT;Z0;G3563)')
    sketch5 = sketches2.Add(reference121)
    arrayOfVariantOfDouble5[0] = - m
    arrayOfVariantOfDouble5[1] = 0.000000
    arrayOfVariantOfDouble5[2] = 0.000000
    arrayOfVariantOfDouble5[3] = 0.000000
    arrayOfVariantOfDouble5[4] = - 1.000000
    arrayOfVariantOfDouble5[5] = 0.000000
    arrayOfVariantOfDouble5[6] = 0.000000
    arrayOfVariantOfDouble5[7] = 0.000000
    arrayOfVariantOfDouble5[8] = 1.000000
    sketch5.SetAbsoluteAxisData(arrayOfVariantOfDouble5)
    part1.InWorkObject = sketch5
    factory2D5 = sketch5.OpenEdition()
    geometricElements5 = sketch5.GeometricElements
    axis2D5 = geometricElements5.Item('AbsoluteAxis')
    line2D26 = axis2D5.GetItem('HDirection')
    line2D26.ReportName = 1
    line2D27 = axis2D5.GetItem('VDirection')
    line2D27.ReportName = 2
    circle2D3 = factory2D5.CreateClosedCircle(0.000000, 0.000000, h)
    point2D30 = axis2D5.GetItem('Origin')
    circle2D3.CenterPoint = point2D30
    circle2D3.ReportName = 3
    constraints5 = sketch5.Constraints
    reference122 = part1.CreateReferenceFromObject(circle2D3)
    #constraint57 = constraints5.AddMonoEltCst(catCstTypeRadius, reference122)
    #constraint57.Mode = catCstModeDrivingDimension
    #length58 = constraint57.Dimension
    #length58.Value = 25.000000
    sketch5.CloseEdition()
    part1.InWorkObject = sketch5
    part1.Update()
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    pad3 = shapeFactory1.AddNewPad(sketch5, 62.500000)
    limit5 = pad3.FirstLimit
    length59 = limit5.Dimension
    length59.Value = g

    
    part1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    #hide a plane
    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()

    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''

    
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("Gold Metal")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    
    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\knuckle_single_eye.CATPart' %(foldername))

    

    #single eye design end
    #...............................................................................................................................#
    #...................................................................................................................................#
    #double eye design start
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
    #hide a plane
    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("DS Red")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\knuckle_double_eye.CATPart' %(foldername))

    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''assembly start''''''''''''''''''''''''''''''''''''''''''''''''#
    
    
    arrayOfVariantOfBSTR1 = [0,0,0,0,0,0,0,0,0,0,0]
    
    arrayOfVariantOfBSTR2 = [0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfBSTR3 = [0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfBSTR4 = [0,0,0,0,0,0,0,0,0,0,0]

    catCstTypeOn = 2
    catCstTypeSurfContact = 20
    

    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble3 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble4 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble5 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble6 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble7 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble8 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble9 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble10 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble11 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble12 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble13 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble14 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble15 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble16 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble17 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble18 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble19 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble20 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble21 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble22 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble23 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble24 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble25 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble26 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble27 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble28 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble29 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble30 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble31 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble32 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble33 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble34 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble35 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble36 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble37 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble38 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble39 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble40 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble41 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble42 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble43 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble44 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble45 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble46 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble47 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble48 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble49 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble50 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble51 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble52 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble53 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble54 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble55 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble56 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble57 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble58 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble59 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble60 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble61 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble62 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble63 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble64 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble65 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble66 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble67 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble68 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble69 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble70 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble71 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble72 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble73 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble74 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble75 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble76 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble77 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble78 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble79 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble80 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble81 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble82 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble83 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble84 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble85 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble86 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble87 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble88 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble89 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble90 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble91 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble92 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble93 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble94 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble95 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble96 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble97 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble98 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble99 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble100 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble101 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble102 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble103 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble104 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble105 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble106 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble107 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble108 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble109 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble110 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble111 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble112 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble113 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble114 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble115 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble116 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble117 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble118 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble119 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble120 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble121 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble122 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble123 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble124 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble125 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble126 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble127 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble128 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble129 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble130 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble131 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble132 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble133 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble134 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble135 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble136 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble137 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble138 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble139 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble140 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble141 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble142 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble143 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble144 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble145 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble146 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble147 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble148 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble149 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble150 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble151 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble152 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble153 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble154 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble155 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble156 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble157 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble158 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble159 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble160 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble161 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble162 = [0,0,0,0,0,0,0,0,0,0,0,0]



    #arrayOfVariantOfBSTR4 = vbObjectInitialize((0,), Variant)

    #bSTR1 = Variant()

    #bSTR2 = Variant()
    documents1 = CATIA.Documents
    productDocument1 = documents1.Add('Product')
    product1 = productDocument1.Product
    products1 = product1.Products
    arrayOfVariantOfBSTR1[0] = ('C:\\%s\\knuckle_double_eye.CATPart' %(foldername))

    #('C:\\%s\\knuckle_double_eye.CATPart' %(foldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR1, 'All')
    constraints1 = product1.Connections('CATIAConstraints')
    reference1 = product1.CreateReferenceFromName('Product1/Part4.1/!Product1/Part4.1/')
    #constraint1 = constraints1.AddMonoEltCst(catCstTypeReference, reference1)
    arrayOfVariantOfBSTR2[0] = ('C:\\%s\\knuckle_single_eye.CATPart' %(foldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR2, 'All')
    product2 = products1.Item('Part3.1')
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble1[0] = 1.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = 0.000000
    arrayOfVariantOfDouble1[4] = 1.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = 0.000000
    arrayOfVariantOfDouble1[8] = 1.000000
    arrayOfVariantOfDouble1[9] = 0.000000
    arrayOfVariantOfDouble1[10] = 4.627248
    arrayOfVariantOfDouble1[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble1)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble2[0] = 1.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = 0.000000
    arrayOfVariantOfDouble2[4] = 1.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = 0.000000
    arrayOfVariantOfDouble2[8] = 1.000000
    arrayOfVariantOfDouble2[9] = 0.000000
    arrayOfVariantOfDouble2[10] = 10.506613
    arrayOfVariantOfDouble2[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble2)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble3[0] = 1.000000
    arrayOfVariantOfDouble3[1] = 0.000000
    arrayOfVariantOfDouble3[2] = 0.000000
    arrayOfVariantOfDouble3[3] = 0.000000
    arrayOfVariantOfDouble3[4] = 1.000000
    arrayOfVariantOfDouble3[5] = 0.000000
    arrayOfVariantOfDouble3[6] = 0.000000
    arrayOfVariantOfDouble3[7] = 0.000000
    arrayOfVariantOfDouble3[8] = 1.000000
    arrayOfVariantOfDouble3[9] = 0.000000
    arrayOfVariantOfDouble3[10] = 10.506617
    arrayOfVariantOfDouble3[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble3)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble4[0] = 1.000000
    arrayOfVariantOfDouble4[1] = 0.000000
    arrayOfVariantOfDouble4[2] = 0.000000
    arrayOfVariantOfDouble4[3] = 0.000000
    arrayOfVariantOfDouble4[4] = 1.000000
    arrayOfVariantOfDouble4[5] = 0.000000
    arrayOfVariantOfDouble4[6] = 0.000000
    arrayOfVariantOfDouble4[7] = 0.000000
    arrayOfVariantOfDouble4[8] = 1.000000
    arrayOfVariantOfDouble4[9] = 0.000000
    arrayOfVariantOfDouble4[10] = 13.632911
    arrayOfVariantOfDouble4[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble4)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble5[0] = 1.000000
    arrayOfVariantOfDouble5[1] = 0.000000
    arrayOfVariantOfDouble5[2] = 0.000000
    arrayOfVariantOfDouble5[3] = 0.000000
    arrayOfVariantOfDouble5[4] = 1.000000
    arrayOfVariantOfDouble5[5] = 0.000000
    arrayOfVariantOfDouble5[6] = 0.000000
    arrayOfVariantOfDouble5[7] = 0.000000
    arrayOfVariantOfDouble5[8] = 1.000000
    arrayOfVariantOfDouble5[9] = 0.000000
    arrayOfVariantOfDouble5[10] = 10.865327
    arrayOfVariantOfDouble5[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble5)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble6[0] = 1.000000
    arrayOfVariantOfDouble6[1] = 0.000000
    arrayOfVariantOfDouble6[2] = 0.000000
    arrayOfVariantOfDouble6[3] = 0.000000
    arrayOfVariantOfDouble6[4] = 1.000000
    arrayOfVariantOfDouble6[5] = 0.000000
    arrayOfVariantOfDouble6[6] = 0.000000
    arrayOfVariantOfDouble6[7] = 0.000000
    arrayOfVariantOfDouble6[8] = 1.000000
    arrayOfVariantOfDouble6[9] = 0.000000
    arrayOfVariantOfDouble6[10] = 22.294467
    arrayOfVariantOfDouble6[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble6)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble7[0] = 1.000000
    arrayOfVariantOfDouble7[1] = 0.000000
    arrayOfVariantOfDouble7[2] = 0.000000
    arrayOfVariantOfDouble7[3] = 0.000000
    arrayOfVariantOfDouble7[4] = 1.000000
    arrayOfVariantOfDouble7[5] = 0.000000
    arrayOfVariantOfDouble7[6] = 0.000000
    arrayOfVariantOfDouble7[7] = 0.000000
    arrayOfVariantOfDouble7[8] = 1.000000
    arrayOfVariantOfDouble7[9] = 0.000000
    arrayOfVariantOfDouble7[10] = 8.482200
    arrayOfVariantOfDouble7[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble7)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble8[0] = 1.000000
    arrayOfVariantOfDouble8[1] = 0.000000
    arrayOfVariantOfDouble8[2] = 0.000000
    arrayOfVariantOfDouble8[3] = 0.000000
    arrayOfVariantOfDouble8[4] = 1.000000
    arrayOfVariantOfDouble8[5] = 0.000000
    arrayOfVariantOfDouble8[6] = 0.000000
    arrayOfVariantOfDouble8[7] = 0.000000
    arrayOfVariantOfDouble8[8] = 1.000000
    arrayOfVariantOfDouble8[9] = 0.000000
    arrayOfVariantOfDouble8[10] = 8.661537
    arrayOfVariantOfDouble8[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble8)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble9[0] = 1.000000
    arrayOfVariantOfDouble9[1] = 0.000000
    arrayOfVariantOfDouble9[2] = 0.000000
    arrayOfVariantOfDouble9[3] = 0.000000
    arrayOfVariantOfDouble9[4] = 1.000000
    arrayOfVariantOfDouble9[5] = 0.000000
    arrayOfVariantOfDouble9[6] = 0.000000
    arrayOfVariantOfDouble9[7] = 0.000000
    arrayOfVariantOfDouble9[8] = 1.000000
    arrayOfVariantOfDouble9[9] = 0.000000
    arrayOfVariantOfDouble9[10] = 7.738994
    arrayOfVariantOfDouble9[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble9)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble10[0] = 1.000000
    arrayOfVariantOfDouble10[1] = 0.000000
    arrayOfVariantOfDouble10[2] = 0.000000
    arrayOfVariantOfDouble10[3] = 0.000000
    arrayOfVariantOfDouble10[4] = 1.000000
    arrayOfVariantOfDouble10[5] = 0.000000
    arrayOfVariantOfDouble10[6] = 0.000000
    arrayOfVariantOfDouble10[7] = 0.000000
    arrayOfVariantOfDouble10[8] = 1.000000
    arrayOfVariantOfDouble10[9] = 0.000000
    arrayOfVariantOfDouble10[10] = 7.354514
    arrayOfVariantOfDouble10[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble10)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble11[0] = 1.000000
    arrayOfVariantOfDouble11[1] = 0.000000
    arrayOfVariantOfDouble11[2] = 0.000000
    arrayOfVariantOfDouble11[3] = 0.000000
    arrayOfVariantOfDouble11[4] = 1.000000
    arrayOfVariantOfDouble11[5] = 0.000000
    arrayOfVariantOfDouble11[6] = 0.000000
    arrayOfVariantOfDouble11[7] = 0.000000
    arrayOfVariantOfDouble11[8] = 1.000000
    arrayOfVariantOfDouble11[9] = 0.000000
    arrayOfVariantOfDouble11[10] = 14.376126
    arrayOfVariantOfDouble11[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble11)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble12[0] = 1.000000
    arrayOfVariantOfDouble12[1] = 0.000000
    arrayOfVariantOfDouble12[2] = 0.000000
    arrayOfVariantOfDouble12[3] = 0.000000
    arrayOfVariantOfDouble12[4] = 1.000000
    arrayOfVariantOfDouble12[5] = 0.000000
    arrayOfVariantOfDouble12[6] = 0.000000
    arrayOfVariantOfDouble12[7] = 0.000000
    arrayOfVariantOfDouble12[8] = 1.000000
    arrayOfVariantOfDouble12[9] = 0.000000
    arrayOfVariantOfDouble12[10] = 3.690146
    arrayOfVariantOfDouble12[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble12)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble13[0] = 1.000000
    arrayOfVariantOfDouble13[1] = 0.000000
    arrayOfVariantOfDouble13[2] = 0.000000
    arrayOfVariantOfDouble13[3] = 0.000000
    arrayOfVariantOfDouble13[4] = 1.000000
    arrayOfVariantOfDouble13[5] = 0.000000
    arrayOfVariantOfDouble13[6] = 0.000000
    arrayOfVariantOfDouble13[7] = 0.000000
    arrayOfVariantOfDouble13[8] = 1.000000
    arrayOfVariantOfDouble13[9] = 0.000000
    arrayOfVariantOfDouble13[10] = 4.971391
    arrayOfVariantOfDouble13[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble13)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble14[0] = 1.000000
    arrayOfVariantOfDouble14[1] = 0.000000
    arrayOfVariantOfDouble14[2] = 0.000000
    arrayOfVariantOfDouble14[3] = 0.000000
    arrayOfVariantOfDouble14[4] = 1.000000
    arrayOfVariantOfDouble14[5] = 0.000000
    arrayOfVariantOfDouble14[6] = 0.000000
    arrayOfVariantOfDouble14[7] = 0.000000
    arrayOfVariantOfDouble14[8] = 1.000000
    arrayOfVariantOfDouble14[9] = 0.000000
    arrayOfVariantOfDouble14[10] = 6.995812
    arrayOfVariantOfDouble14[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble14)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble15[0] = 1.000000
    arrayOfVariantOfDouble15[1] = 0.000000
    arrayOfVariantOfDouble15[2] = 0.000000
    arrayOfVariantOfDouble15[3] = 0.000000
    arrayOfVariantOfDouble15[4] = 1.000000
    arrayOfVariantOfDouble15[5] = 0.000000
    arrayOfVariantOfDouble15[6] = 0.000000
    arrayOfVariantOfDouble15[7] = 0.000000
    arrayOfVariantOfDouble15[8] = 1.000000
    arrayOfVariantOfDouble15[9] = 0.000000
    arrayOfVariantOfDouble15[10] = 2.024422
    arrayOfVariantOfDouble15[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble15)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble16[0] = 1.000000
    arrayOfVariantOfDouble16[1] = 0.000000
    arrayOfVariantOfDouble16[2] = 0.000000
    arrayOfVariantOfDouble16[3] = 0.000000
    arrayOfVariantOfDouble16[4] = 1.000000
    arrayOfVariantOfDouble16[5] = 0.000000
    arrayOfVariantOfDouble16[6] = 0.000000
    arrayOfVariantOfDouble16[7] = 0.000000
    arrayOfVariantOfDouble16[8] = 1.000000
    arrayOfVariantOfDouble16[9] = 0.000000
    arrayOfVariantOfDouble16[10] = 2.767624
    arrayOfVariantOfDouble16[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble16)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble17[0] = 1.000000
    arrayOfVariantOfDouble17[1] = 0.000000
    arrayOfVariantOfDouble17[2] = 0.000000
    arrayOfVariantOfDouble17[3] = 0.000000
    arrayOfVariantOfDouble17[4] = 1.000000
    arrayOfVariantOfDouble17[5] = 0.000000
    arrayOfVariantOfDouble17[6] = 0.000000
    arrayOfVariantOfDouble17[7] = 0.000000
    arrayOfVariantOfDouble17[8] = 1.000000
    arrayOfVariantOfDouble17[9] = 0.000000
    arrayOfVariantOfDouble17[10] = 3.869496
    arrayOfVariantOfDouble17[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble17)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble18[0] = 1.000000
    arrayOfVariantOfDouble18[1] = 0.000000
    arrayOfVariantOfDouble18[2] = 0.000000
    arrayOfVariantOfDouble18[3] = 0.000000
    arrayOfVariantOfDouble18[4] = 1.000000
    arrayOfVariantOfDouble18[5] = 0.000000
    arrayOfVariantOfDouble18[6] = 0.000000
    arrayOfVariantOfDouble18[7] = 0.000000
    arrayOfVariantOfDouble18[8] = 1.000000
    arrayOfVariantOfDouble18[9] = 0.000000
    arrayOfVariantOfDouble18[10] = 2.767607
    arrayOfVariantOfDouble18[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble18)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble19[0] = 1.000000
    arrayOfVariantOfDouble19[1] = 0.000000
    arrayOfVariantOfDouble19[2] = 0.000000
    arrayOfVariantOfDouble19[3] = 0.000000
    arrayOfVariantOfDouble19[4] = 1.000000
    arrayOfVariantOfDouble19[5] = 0.000000
    arrayOfVariantOfDouble19[6] = 0.000000
    arrayOfVariantOfDouble19[7] = 0.000000
    arrayOfVariantOfDouble19[8] = 1.000000
    arrayOfVariantOfDouble19[9] = 0.000000
    arrayOfVariantOfDouble19[10] = 2.767632
    arrayOfVariantOfDouble19[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble19)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble20[0] = 1.000000
    arrayOfVariantOfDouble20[1] = 0.000000
    arrayOfVariantOfDouble20[2] = 0.000000
    arrayOfVariantOfDouble20[3] = 0.000000
    arrayOfVariantOfDouble20[4] = 1.000000
    arrayOfVariantOfDouble20[5] = 0.000000
    arrayOfVariantOfDouble20[6] = 0.000000
    arrayOfVariantOfDouble20[7] = 0.000000
    arrayOfVariantOfDouble20[8] = 1.000000
    arrayOfVariantOfDouble20[9] = 0.000000
    arrayOfVariantOfDouble20[10] = 2.203762
    arrayOfVariantOfDouble20[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble20)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble21[0] = 1.000000
    arrayOfVariantOfDouble21[1] = 0.000000
    arrayOfVariantOfDouble21[2] = 0.000000
    arrayOfVariantOfDouble21[3] = 0.000000
    arrayOfVariantOfDouble21[4] = 1.000000
    arrayOfVariantOfDouble21[5] = 0.000000
    arrayOfVariantOfDouble21[6] = 0.000000
    arrayOfVariantOfDouble21[7] = 0.000000
    arrayOfVariantOfDouble21[8] = 1.000000
    arrayOfVariantOfDouble21[9] = 0.000000
    arrayOfVariantOfDouble21[10] = 4.612682
    arrayOfVariantOfDouble21[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble21)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble22[0] = 1.000000
    arrayOfVariantOfDouble22[1] = 0.000000
    arrayOfVariantOfDouble22[2] = 0.000000
    arrayOfVariantOfDouble22[3] = 0.000000
    arrayOfVariantOfDouble22[4] = 1.000000
    arrayOfVariantOfDouble22[5] = 0.000000
    arrayOfVariantOfDouble22[6] = 0.000000
    arrayOfVariantOfDouble22[7] = 0.000000
    arrayOfVariantOfDouble22[8] = 1.000000
    arrayOfVariantOfDouble22[9] = 0.000000
    arrayOfVariantOfDouble22[10] = 4.792053
    arrayOfVariantOfDouble22[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble22)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble23[0] = 1.000000
    arrayOfVariantOfDouble23[1] = 0.000000
    arrayOfVariantOfDouble23[2] = 0.000000
    arrayOfVariantOfDouble23[3] = 0.000000
    arrayOfVariantOfDouble23[4] = 1.000000
    arrayOfVariantOfDouble23[5] = 0.000000
    arrayOfVariantOfDouble23[6] = 0.000000
    arrayOfVariantOfDouble23[7] = 0.000000
    arrayOfVariantOfDouble23[8] = 1.000000
    arrayOfVariantOfDouble23[9] = 0.000000
    arrayOfVariantOfDouble23[10] = 1.845074
    arrayOfVariantOfDouble23[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble23)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble24[0] = 1.000000
    arrayOfVariantOfDouble24[1] = 0.000000
    arrayOfVariantOfDouble24[2] = 0.000000
    arrayOfVariantOfDouble24[3] = 0.000000
    arrayOfVariantOfDouble24[4] = 1.000000
    arrayOfVariantOfDouble24[5] = 0.000000
    arrayOfVariantOfDouble24[6] = 0.000000
    arrayOfVariantOfDouble24[7] = 0.000000
    arrayOfVariantOfDouble24[8] = 1.000000
    arrayOfVariantOfDouble24[9] = 0.000000
    arrayOfVariantOfDouble24[10] = 5.535210
    arrayOfVariantOfDouble24[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble24)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble25[0] = 1.000000
    arrayOfVariantOfDouble25[1] = 0.000000
    arrayOfVariantOfDouble25[2] = 0.000000
    arrayOfVariantOfDouble25[3] = 0.000000
    arrayOfVariantOfDouble25[4] = 1.000000
    arrayOfVariantOfDouble25[5] = 0.000000
    arrayOfVariantOfDouble25[6] = 0.000000
    arrayOfVariantOfDouble25[7] = 0.000000
    arrayOfVariantOfDouble25[8] = 1.000000
    arrayOfVariantOfDouble25[9] = 0.000000
    arrayOfVariantOfDouble25[10] = 6.457787
    arrayOfVariantOfDouble25[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble25)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble26[0] = 1.000000
    arrayOfVariantOfDouble26[1] = 0.000000
    arrayOfVariantOfDouble26[2] = 0.000000
    arrayOfVariantOfDouble26[3] = 0.000000
    arrayOfVariantOfDouble26[4] = 1.000000
    arrayOfVariantOfDouble26[5] = 0.000000
    arrayOfVariantOfDouble26[6] = 0.000000
    arrayOfVariantOfDouble26[7] = 0.000000
    arrayOfVariantOfDouble26[8] = 1.000000
    arrayOfVariantOfDouble26[9] = 0.000000
    arrayOfVariantOfDouble26[10] = 2.767614
    arrayOfVariantOfDouble26[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble26)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble27[0] = 1.000000
    arrayOfVariantOfDouble27[1] = 0.000000
    arrayOfVariantOfDouble27[2] = 0.000000
    arrayOfVariantOfDouble27[3] = 0.000000
    arrayOfVariantOfDouble27[4] = 1.000000
    arrayOfVariantOfDouble27[5] = 0.000000
    arrayOfVariantOfDouble27[6] = 0.000000
    arrayOfVariantOfDouble27[7] = 0.000000
    arrayOfVariantOfDouble27[8] = 1.000000
    arrayOfVariantOfDouble27[9] = 0.000000
    arrayOfVariantOfDouble27[10] = 1.101884
    arrayOfVariantOfDouble27[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble27)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble28[0] = 1.000000
    arrayOfVariantOfDouble28[1] = 0.000000
    arrayOfVariantOfDouble28[2] = 0.000000
    arrayOfVariantOfDouble28[3] = 0.000000
    arrayOfVariantOfDouble28[4] = 1.000000
    arrayOfVariantOfDouble28[5] = 0.000000
    arrayOfVariantOfDouble28[6] = 0.000000
    arrayOfVariantOfDouble28[7] = 0.000000
    arrayOfVariantOfDouble28[8] = 1.000000
    arrayOfVariantOfDouble28[9] = 0.000000
    arrayOfVariantOfDouble28[10] = 3.690156
    arrayOfVariantOfDouble28[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble28)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble29[0] = 1.000000
    arrayOfVariantOfDouble29[1] = 0.000000
    arrayOfVariantOfDouble29[2] = 0.000000
    arrayOfVariantOfDouble29[3] = 0.000000
    arrayOfVariantOfDouble29[4] = 1.000000
    arrayOfVariantOfDouble29[5] = 0.000000
    arrayOfVariantOfDouble29[6] = 0.000000
    arrayOfVariantOfDouble29[7] = 0.000000
    arrayOfVariantOfDouble29[8] = 1.000000
    arrayOfVariantOfDouble29[9] = 0.000000
    arrayOfVariantOfDouble29[10] = 1.845054
    arrayOfVariantOfDouble29[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble29)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble30[0] = 1.000000
    arrayOfVariantOfDouble30[1] = 0.000000
    arrayOfVariantOfDouble30[2] = 0.000000
    arrayOfVariantOfDouble30[3] = 0.000000
    arrayOfVariantOfDouble30[4] = 1.000000
    arrayOfVariantOfDouble30[5] = 0.000000
    arrayOfVariantOfDouble30[6] = 0.000000
    arrayOfVariantOfDouble30[7] = 0.000000
    arrayOfVariantOfDouble30[8] = 1.000000
    arrayOfVariantOfDouble30[9] = 0.000000
    arrayOfVariantOfDouble30[10] = 3.126316
    arrayOfVariantOfDouble30[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble30)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble31[0] = 1.000000
    arrayOfVariantOfDouble31[1] = 0.000000
    arrayOfVariantOfDouble31[2] = 0.000000
    arrayOfVariantOfDouble31[3] = 0.000000
    arrayOfVariantOfDouble31[4] = 1.000000
    arrayOfVariantOfDouble31[5] = 0.000000
    arrayOfVariantOfDouble31[6] = 0.000000
    arrayOfVariantOfDouble31[7] = 0.000000
    arrayOfVariantOfDouble31[8] = 1.000000
    arrayOfVariantOfDouble31[9] = 0.000000
    arrayOfVariantOfDouble31[10] = 4.612694
    arrayOfVariantOfDouble31[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble31)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble32[0] = 1.000000
    arrayOfVariantOfDouble32[1] = 0.000000
    arrayOfVariantOfDouble32[2] = 0.000000
    arrayOfVariantOfDouble32[3] = 0.000000
    arrayOfVariantOfDouble32[4] = 1.000000
    arrayOfVariantOfDouble32[5] = 0.000000
    arrayOfVariantOfDouble32[6] = 0.000000
    arrayOfVariantOfDouble32[7] = 0.000000
    arrayOfVariantOfDouble32[8] = 1.000000
    arrayOfVariantOfDouble32[9] = 0.000000
    arrayOfVariantOfDouble32[10] = 1.460586
    arrayOfVariantOfDouble32[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble32)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble33[0] = 1.000000
    arrayOfVariantOfDouble33[1] = 0.000000
    arrayOfVariantOfDouble33[2] = 0.000000
    arrayOfVariantOfDouble33[3] = 0.000000
    arrayOfVariantOfDouble33[4] = 1.000000
    arrayOfVariantOfDouble33[5] = 0.000000
    arrayOfVariantOfDouble33[6] = 0.000000
    arrayOfVariantOfDouble33[7] = 0.000000
    arrayOfVariantOfDouble33[8] = 1.000000
    arrayOfVariantOfDouble33[9] = 0.000000
    arrayOfVariantOfDouble33[10] = 2.767605
    arrayOfVariantOfDouble33[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble33)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble34[0] = 1.000000
    arrayOfVariantOfDouble34[1] = 0.000000
    arrayOfVariantOfDouble34[2] = 0.000000
    arrayOfVariantOfDouble34[3] = 0.000000
    arrayOfVariantOfDouble34[4] = 1.000000
    arrayOfVariantOfDouble34[5] = 0.000000
    arrayOfVariantOfDouble34[6] = 0.000000
    arrayOfVariantOfDouble34[7] = 0.000000
    arrayOfVariantOfDouble34[8] = 1.000000
    arrayOfVariantOfDouble34[9] = 0.000000
    arrayOfVariantOfDouble34[10] = 2.946962
    arrayOfVariantOfDouble34[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble34)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble35[0] = 1.000000
    arrayOfVariantOfDouble35[1] = 0.000000
    arrayOfVariantOfDouble35[2] = 0.000000
    arrayOfVariantOfDouble35[3] = 0.000000
    arrayOfVariantOfDouble35[4] = 1.000000
    arrayOfVariantOfDouble35[5] = 0.000000
    arrayOfVariantOfDouble35[6] = 0.000000
    arrayOfVariantOfDouble35[7] = 0.000000
    arrayOfVariantOfDouble35[8] = 1.000000
    arrayOfVariantOfDouble35[9] = 0.000000
    arrayOfVariantOfDouble35[10] = 1.845082
    arrayOfVariantOfDouble35[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble35)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble36[0] = 1.000000
    arrayOfVariantOfDouble36[1] = 0.000000
    arrayOfVariantOfDouble36[2] = 0.000000
    arrayOfVariantOfDouble36[3] = 0.000000
    arrayOfVariantOfDouble36[4] = 1.000000
    arrayOfVariantOfDouble36[5] = 0.000000
    arrayOfVariantOfDouble36[6] = 0.000000
    arrayOfVariantOfDouble36[7] = 0.000000
    arrayOfVariantOfDouble36[8] = 1.000000
    arrayOfVariantOfDouble36[9] = 0.000000
    arrayOfVariantOfDouble36[10] = 4.792045
    arrayOfVariantOfDouble36[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble36)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble37[0] = 1.000000
    arrayOfVariantOfDouble37[1] = 0.000000
    arrayOfVariantOfDouble37[2] = 0.000000
    arrayOfVariantOfDouble37[3] = 0.000000
    arrayOfVariantOfDouble37[4] = 1.000000
    arrayOfVariantOfDouble37[5] = 0.000000
    arrayOfVariantOfDouble37[6] = 0.000000
    arrayOfVariantOfDouble37[7] = 0.000000
    arrayOfVariantOfDouble37[8] = 1.000000
    arrayOfVariantOfDouble37[9] = 0.000000
    arrayOfVariantOfDouble37[10] = 1.845093
    arrayOfVariantOfDouble37[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble37)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble38[0] = 1.000000
    arrayOfVariantOfDouble38[1] = 0.000000
    arrayOfVariantOfDouble38[2] = 0.000000
    arrayOfVariantOfDouble38[3] = 0.000000
    arrayOfVariantOfDouble38[4] = 1.000000
    arrayOfVariantOfDouble38[5] = 0.000000
    arrayOfVariantOfDouble38[6] = 0.000000
    arrayOfVariantOfDouble38[7] = 0.000000
    arrayOfVariantOfDouble38[8] = 1.000000
    arrayOfVariantOfDouble38[9] = 0.000000
    arrayOfVariantOfDouble38[10] = 2.767610
    arrayOfVariantOfDouble38[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble38)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble39[0] = 1.000000
    arrayOfVariantOfDouble39[1] = 0.000000
    arrayOfVariantOfDouble39[2] = 0.000000
    arrayOfVariantOfDouble39[3] = 0.000000
    arrayOfVariantOfDouble39[4] = 1.000000
    arrayOfVariantOfDouble39[5] = 0.000000
    arrayOfVariantOfDouble39[6] = 0.000000
    arrayOfVariantOfDouble39[7] = 0.000000
    arrayOfVariantOfDouble39[8] = 1.000000
    arrayOfVariantOfDouble39[9] = 0.000000
    arrayOfVariantOfDouble39[10] = 2.024405
    arrayOfVariantOfDouble39[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble39)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble40[0] = 1.000000
    arrayOfVariantOfDouble40[1] = 0.000000
    arrayOfVariantOfDouble40[2] = 0.000000
    arrayOfVariantOfDouble40[3] = 0.000000
    arrayOfVariantOfDouble40[4] = 1.000000
    arrayOfVariantOfDouble40[5] = 0.000000
    arrayOfVariantOfDouble40[6] = 0.000000
    arrayOfVariantOfDouble40[7] = 0.000000
    arrayOfVariantOfDouble40[8] = 1.000000
    arrayOfVariantOfDouble40[9] = 0.000000
    arrayOfVariantOfDouble40[10] = 4.612693
    arrayOfVariantOfDouble40[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble40)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble41[0] = 1.000000
    arrayOfVariantOfDouble41[1] = 0.000000
    arrayOfVariantOfDouble41[2] = 0.000000
    arrayOfVariantOfDouble41[3] = 0.000000
    arrayOfVariantOfDouble41[4] = 1.000000
    arrayOfVariantOfDouble41[5] = 0.000000
    arrayOfVariantOfDouble41[6] = 0.000000
    arrayOfVariantOfDouble41[7] = 0.000000
    arrayOfVariantOfDouble41[8] = 1.000000
    arrayOfVariantOfDouble41[9] = 0.000000
    arrayOfVariantOfDouble41[10] = 4.048877
    arrayOfVariantOfDouble41[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble41)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble42[0] = 1.000000
    arrayOfVariantOfDouble42[1] = 0.000000
    arrayOfVariantOfDouble42[2] = 0.000000
    arrayOfVariantOfDouble42[3] = 0.000000
    arrayOfVariantOfDouble42[4] = 1.000000
    arrayOfVariantOfDouble42[5] = 0.000000
    arrayOfVariantOfDouble42[6] = 0.000000
    arrayOfVariantOfDouble42[7] = 0.000000
    arrayOfVariantOfDouble42[8] = 1.000000
    arrayOfVariantOfDouble42[9] = 0.000000
    arrayOfVariantOfDouble42[10] = 0.922527
    arrayOfVariantOfDouble42[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble42)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble43[0] = 1.000000
    arrayOfVariantOfDouble43[1] = 0.000000
    arrayOfVariantOfDouble43[2] = 0.000000
    arrayOfVariantOfDouble43[3] = 0.000000
    arrayOfVariantOfDouble43[4] = 1.000000
    arrayOfVariantOfDouble43[5] = 0.000000
    arrayOfVariantOfDouble43[6] = 0.000000
    arrayOfVariantOfDouble43[7] = 0.000000
    arrayOfVariantOfDouble43[8] = 1.000000
    arrayOfVariantOfDouble43[9] = 0.000000
    arrayOfVariantOfDouble43[10] = 1.101869
    arrayOfVariantOfDouble43[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble43)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble44[0] = 1.000000
    arrayOfVariantOfDouble44[1] = 0.000000
    arrayOfVariantOfDouble44[2] = 0.000000
    arrayOfVariantOfDouble44[3] = 0.000000
    arrayOfVariantOfDouble44[4] = 1.000000
    arrayOfVariantOfDouble44[5] = 0.000000
    arrayOfVariantOfDouble44[6] = 0.000000
    arrayOfVariantOfDouble44[7] = 0.000000
    arrayOfVariantOfDouble44[8] = 1.000000
    arrayOfVariantOfDouble44[9] = 0.000000
    arrayOfVariantOfDouble44[10] = 4.612704
    arrayOfVariantOfDouble44[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble44)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble45[0] = 1.000000
    arrayOfVariantOfDouble45[1] = 0.000000
    arrayOfVariantOfDouble45[2] = 0.000000
    arrayOfVariantOfDouble45[3] = 0.000000
    arrayOfVariantOfDouble45[4] = 1.000000
    arrayOfVariantOfDouble45[5] = 0.000000
    arrayOfVariantOfDouble45[6] = 0.000000
    arrayOfVariantOfDouble45[7] = 0.000000
    arrayOfVariantOfDouble45[8] = 1.000000
    arrayOfVariantOfDouble45[9] = 0.000000
    arrayOfVariantOfDouble45[10] = 0.922528
    arrayOfVariantOfDouble45[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble45)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble46[0] = 1.000000
    arrayOfVariantOfDouble46[1] = 0.000000
    arrayOfVariantOfDouble46[2] = 0.000000
    arrayOfVariantOfDouble46[3] = 0.000000
    arrayOfVariantOfDouble46[4] = 1.000000
    arrayOfVariantOfDouble46[5] = 0.000000
    arrayOfVariantOfDouble46[6] = 0.000000
    arrayOfVariantOfDouble46[7] = 0.000000
    arrayOfVariantOfDouble46[8] = 1.000000
    arrayOfVariantOfDouble46[9] = 0.000000
    arrayOfVariantOfDouble46[10] = 1.845085
    arrayOfVariantOfDouble46[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble46)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble47[0] = 1.000000
    arrayOfVariantOfDouble47[1] = 0.000000
    arrayOfVariantOfDouble47[2] = 0.000000
    arrayOfVariantOfDouble47[3] = 0.000000
    arrayOfVariantOfDouble47[4] = 1.000000
    arrayOfVariantOfDouble47[5] = 0.000000
    arrayOfVariantOfDouble47[6] = 0.000000
    arrayOfVariantOfDouble47[7] = 0.000000
    arrayOfVariantOfDouble47[8] = 1.000000
    arrayOfVariantOfDouble47[9] = 0.000000
    arrayOfVariantOfDouble47[10] = 0.358697
    arrayOfVariantOfDouble47[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble47)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble48[0] = 1.000000
    arrayOfVariantOfDouble48[1] = 0.000000
    arrayOfVariantOfDouble48[2] = 0.000000
    arrayOfVariantOfDouble48[3] = 0.000000
    arrayOfVariantOfDouble48[4] = 1.000000
    arrayOfVariantOfDouble48[5] = 0.000000
    arrayOfVariantOfDouble48[6] = 0.000000
    arrayOfVariantOfDouble48[7] = 0.000000
    arrayOfVariantOfDouble48[8] = 1.000000
    arrayOfVariantOfDouble48[9] = 0.000000
    arrayOfVariantOfDouble48[10] = 1.845086
    arrayOfVariantOfDouble48[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble48)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble49[0] = 1.000000
    arrayOfVariantOfDouble49[1] = 0.000000
    arrayOfVariantOfDouble49[2] = 0.000000
    arrayOfVariantOfDouble49[3] = 0.000000
    arrayOfVariantOfDouble49[4] = 1.000000
    arrayOfVariantOfDouble49[5] = 0.000000
    arrayOfVariantOfDouble49[6] = 0.000000
    arrayOfVariantOfDouble49[7] = 0.000000
    arrayOfVariantOfDouble49[8] = 1.000000
    arrayOfVariantOfDouble49[9] = 0.000000
    arrayOfVariantOfDouble49[10] = 0.358704
    arrayOfVariantOfDouble49[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble49)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble50[0] = 1.000000
    arrayOfVariantOfDouble50[1] = 0.000000
    arrayOfVariantOfDouble50[2] = 0.000000
    arrayOfVariantOfDouble50[3] = 0.000000
    arrayOfVariantOfDouble50[4] = 1.000000
    arrayOfVariantOfDouble50[5] = 0.000000
    arrayOfVariantOfDouble50[6] = 0.000000
    arrayOfVariantOfDouble50[7] = 0.000000
    arrayOfVariantOfDouble50[8] = 1.000000
    arrayOfVariantOfDouble50[9] = 0.000000
    arrayOfVariantOfDouble50[10] = 1.845047
    arrayOfVariantOfDouble50[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble50)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble51[0] = 1.000000
    arrayOfVariantOfDouble51[1] = 0.000000
    arrayOfVariantOfDouble51[2] = 0.000000
    arrayOfVariantOfDouble51[3] = 0.000000
    arrayOfVariantOfDouble51[4] = 1.000000
    arrayOfVariantOfDouble51[5] = 0.000000
    arrayOfVariantOfDouble51[6] = 0.000000
    arrayOfVariantOfDouble51[7] = 0.000000
    arrayOfVariantOfDouble51[8] = 1.000000
    arrayOfVariantOfDouble51[9] = 0.000000
    arrayOfVariantOfDouble51[10] = 2.767619
    arrayOfVariantOfDouble51[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble51)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble52[0] = 1.000000
    arrayOfVariantOfDouble52[1] = 0.000000
    arrayOfVariantOfDouble52[2] = 0.000000
    arrayOfVariantOfDouble52[3] = 0.000000
    arrayOfVariantOfDouble52[4] = 1.000000
    arrayOfVariantOfDouble52[5] = 0.000000
    arrayOfVariantOfDouble52[6] = 0.000000
    arrayOfVariantOfDouble52[7] = 0.000000
    arrayOfVariantOfDouble52[8] = 1.000000
    arrayOfVariantOfDouble52[9] = 0.000000
    arrayOfVariantOfDouble52[10] = 2.024433
    arrayOfVariantOfDouble52[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble52)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble53[0] = 1.000000
    arrayOfVariantOfDouble53[1] = 0.000000
    arrayOfVariantOfDouble53[2] = 0.000000
    arrayOfVariantOfDouble53[3] = 0.000000
    arrayOfVariantOfDouble53[4] = 1.000000
    arrayOfVariantOfDouble53[5] = 0.000000
    arrayOfVariantOfDouble53[6] = 0.000000
    arrayOfVariantOfDouble53[7] = 0.000000
    arrayOfVariantOfDouble53[8] = 1.000000
    arrayOfVariantOfDouble53[9] = 0.000000
    arrayOfVariantOfDouble53[10] = 0.922548
    arrayOfVariantOfDouble53[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble53)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble54[0] = 1.000000
    arrayOfVariantOfDouble54[1] = 0.000000
    arrayOfVariantOfDouble54[2] = 0.000000
    arrayOfVariantOfDouble54[3] = 0.000000
    arrayOfVariantOfDouble54[4] = 1.000000
    arrayOfVariantOfDouble54[5] = 0.000000
    arrayOfVariantOfDouble54[6] = 0.000000
    arrayOfVariantOfDouble54[7] = 0.000000
    arrayOfVariantOfDouble54[8] = 1.000000
    arrayOfVariantOfDouble54[9] = 0.000000
    arrayOfVariantOfDouble54[10] = 0.922528
    arrayOfVariantOfDouble54[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble54)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble55[0] = 1.000000
    arrayOfVariantOfDouble55[1] = 0.000000
    arrayOfVariantOfDouble55[2] = 0.000000
    arrayOfVariantOfDouble55[3] = 0.000000
    arrayOfVariantOfDouble55[4] = 1.000000
    arrayOfVariantOfDouble55[5] = 0.000000
    arrayOfVariantOfDouble55[6] = 0.000000
    arrayOfVariantOfDouble55[7] = 0.000000
    arrayOfVariantOfDouble55[8] = 1.000000
    arrayOfVariantOfDouble55[9] = 0.000000
    arrayOfVariantOfDouble55[10] = 0.179349
    arrayOfVariantOfDouble55[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble55)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble56[0] = 1.000000
    arrayOfVariantOfDouble56[1] = 0.000000
    arrayOfVariantOfDouble56[2] = 0.000000
    arrayOfVariantOfDouble56[3] = 0.000000
    arrayOfVariantOfDouble56[4] = 1.000000
    arrayOfVariantOfDouble56[5] = 0.000000
    arrayOfVariantOfDouble56[6] = 0.000000
    arrayOfVariantOfDouble56[7] = 0.000000
    arrayOfVariantOfDouble56[8] = 1.000000
    arrayOfVariantOfDouble56[9] = 0.000000
    arrayOfVariantOfDouble56[10] = 0.922528
    arrayOfVariantOfDouble56[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble56)
    arrayOfVariantOfBSTR3[0] = ('C:\\%s\\knuckle_pin.CATPart' %(foldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR3, 'All')
    product3 = products1.Item('Part1.1')
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble57[0] = 1.000000
    arrayOfVariantOfDouble57[1] = 0.000000
    arrayOfVariantOfDouble57[2] = 0.000000
    arrayOfVariantOfDouble57[3] = 0.000000
    arrayOfVariantOfDouble57[4] = 1.000000
    arrayOfVariantOfDouble57[5] = 0.000000
    arrayOfVariantOfDouble57[6] = 0.000000
    arrayOfVariantOfDouble57[7] = 0.000000
    arrayOfVariantOfDouble57[8] = 1.000000
    arrayOfVariantOfDouble57[9] = 0.000000
    arrayOfVariantOfDouble57[10] = - 5.519252
    arrayOfVariantOfDouble57[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble57)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble58[0] = 1.000000
    arrayOfVariantOfDouble58[1] = 0.000000
    arrayOfVariantOfDouble58[2] = 0.000000
    arrayOfVariantOfDouble58[3] = 0.000000
    arrayOfVariantOfDouble58[4] = 1.000000
    arrayOfVariantOfDouble58[5] = 0.000000
    arrayOfVariantOfDouble58[6] = 0.000000
    arrayOfVariantOfDouble58[7] = 0.000000
    arrayOfVariantOfDouble58[8] = 1.000000
    arrayOfVariantOfDouble58[9] = 0.000000
    arrayOfVariantOfDouble58[10] = - 5.728884
    arrayOfVariantOfDouble58[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble58)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble59[0] = 1.000000
    arrayOfVariantOfDouble59[1] = 0.000000
    arrayOfVariantOfDouble59[2] = 0.000000
    arrayOfVariantOfDouble59[3] = 0.000000
    arrayOfVariantOfDouble59[4] = 1.000000
    arrayOfVariantOfDouble59[5] = 0.000000
    arrayOfVariantOfDouble59[6] = 0.000000
    arrayOfVariantOfDouble59[7] = 0.000000
    arrayOfVariantOfDouble59[8] = 1.000000
    arrayOfVariantOfDouble59[9] = 0.000000
    arrayOfVariantOfDouble59[10] = - 11.903247
    arrayOfVariantOfDouble59[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble59)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble60[0] = 1.000000
    arrayOfVariantOfDouble60[1] = 0.000000
    arrayOfVariantOfDouble60[2] = 0.000000
    arrayOfVariantOfDouble60[3] = 0.000000
    arrayOfVariantOfDouble60[4] = 1.000000
    arrayOfVariantOfDouble60[5] = 0.000000
    arrayOfVariantOfDouble60[6] = 0.000000
    arrayOfVariantOfDouble60[7] = 0.000000
    arrayOfVariantOfDouble60[8] = 1.000000
    arrayOfVariantOfDouble60[9] = 0.000000
    arrayOfVariantOfDouble60[10] = - 35.264274
    arrayOfVariantOfDouble60[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble60)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble61[0] = 1.000000
    arrayOfVariantOfDouble61[1] = 0.000000
    arrayOfVariantOfDouble61[2] = 0.000000
    arrayOfVariantOfDouble61[3] = 0.000000
    arrayOfVariantOfDouble61[4] = 1.000000
    arrayOfVariantOfDouble61[5] = 0.000000
    arrayOfVariantOfDouble61[6] = 0.000000
    arrayOfVariantOfDouble61[7] = 0.000000
    arrayOfVariantOfDouble61[8] = 1.000000
    arrayOfVariantOfDouble61[9] = 0.000000
    arrayOfVariantOfDouble61[10] = - 26.766314
    arrayOfVariantOfDouble61[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble61)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble62[0] = 1.000000
    arrayOfVariantOfDouble62[1] = 0.000000
    arrayOfVariantOfDouble62[2] = 0.000000
    arrayOfVariantOfDouble62[3] = 0.000000
    arrayOfVariantOfDouble62[4] = 1.000000
    arrayOfVariantOfDouble62[5] = 0.000000
    arrayOfVariantOfDouble62[6] = 0.000000
    arrayOfVariantOfDouble62[7] = 0.000000
    arrayOfVariantOfDouble62[8] = 1.000000
    arrayOfVariantOfDouble62[9] = 0.000000
    arrayOfVariantOfDouble62[10] = - 27.944118
    arrayOfVariantOfDouble62[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble62)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble63[0] = 1.000000
    arrayOfVariantOfDouble63[1] = 0.000000
    arrayOfVariantOfDouble63[2] = 0.000000
    arrayOfVariantOfDouble63[3] = 0.000000
    arrayOfVariantOfDouble63[4] = 1.000000
    arrayOfVariantOfDouble63[5] = 0.000000
    arrayOfVariantOfDouble63[6] = 0.000000
    arrayOfVariantOfDouble63[7] = 0.000000
    arrayOfVariantOfDouble63[8] = 1.000000
    arrayOfVariantOfDouble63[9] = 0.000000
    arrayOfVariantOfDouble63[10] = - 58.593243
    arrayOfVariantOfDouble63[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble63)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble64[0] = 1.000000
    arrayOfVariantOfDouble64[1] = 0.000000
    arrayOfVariantOfDouble64[2] = 0.000000
    arrayOfVariantOfDouble64[3] = 0.000000
    arrayOfVariantOfDouble64[4] = 1.000000
    arrayOfVariantOfDouble64[5] = 0.000000
    arrayOfVariantOfDouble64[6] = 0.000000
    arrayOfVariantOfDouble64[7] = 0.000000
    arrayOfVariantOfDouble64[8] = 1.000000
    arrayOfVariantOfDouble64[9] = 0.000000
    arrayOfVariantOfDouble64[10] = - 25.397786
    arrayOfVariantOfDouble64[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble64)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble65[0] = 1.000000
    arrayOfVariantOfDouble65[1] = 0.000000
    arrayOfVariantOfDouble65[2] = 0.000000
    arrayOfVariantOfDouble65[3] = 0.000000
    arrayOfVariantOfDouble65[4] = 1.000000
    arrayOfVariantOfDouble65[5] = 0.000000
    arrayOfVariantOfDouble65[6] = 0.000000
    arrayOfVariantOfDouble65[7] = 0.000000
    arrayOfVariantOfDouble65[8] = 1.000000
    arrayOfVariantOfDouble65[9] = 0.000000
    arrayOfVariantOfDouble65[10] = - 31.604196
    arrayOfVariantOfDouble65[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble65)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble66[0] = 1.000000
    arrayOfVariantOfDouble66[1] = 0.000000
    arrayOfVariantOfDouble66[2] = 0.000000
    arrayOfVariantOfDouble66[3] = 0.000000
    arrayOfVariantOfDouble66[4] = 1.000000
    arrayOfVariantOfDouble66[5] = 0.000000
    arrayOfVariantOfDouble66[6] = 0.000000
    arrayOfVariantOfDouble66[7] = 0.000000
    arrayOfVariantOfDouble66[8] = 1.000000
    arrayOfVariantOfDouble66[9] = 0.000000
    arrayOfVariantOfDouble66[10] = - 54.487667
    arrayOfVariantOfDouble66[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble66)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble67[0] = 1.000000
    arrayOfVariantOfDouble67[1] = 0.000000
    arrayOfVariantOfDouble67[2] = 0.000000
    arrayOfVariantOfDouble67[3] = 0.000000
    arrayOfVariantOfDouble67[4] = 1.000000
    arrayOfVariantOfDouble67[5] = 0.000000
    arrayOfVariantOfDouble67[6] = 0.000000
    arrayOfVariantOfDouble67[7] = 0.000000
    arrayOfVariantOfDouble67[8] = 1.000000
    arrayOfVariantOfDouble67[9] = 0.000000
    arrayOfVariantOfDouble67[10] = - 25.652576
    arrayOfVariantOfDouble67[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble67)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble68[0] = 1.000000
    arrayOfVariantOfDouble68[1] = 0.000000
    arrayOfVariantOfDouble68[2] = 0.000000
    arrayOfVariantOfDouble68[3] = 0.000000
    arrayOfVariantOfDouble68[4] = 1.000000
    arrayOfVariantOfDouble68[5] = 0.000000
    arrayOfVariantOfDouble68[6] = 0.000000
    arrayOfVariantOfDouble68[7] = 0.000000
    arrayOfVariantOfDouble68[8] = 1.000000
    arrayOfVariantOfDouble68[9] = 0.000000
    arrayOfVariantOfDouble68[10] = - 13.494518
    arrayOfVariantOfDouble68[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble68)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble69[0] = 1.000000
    arrayOfVariantOfDouble69[1] = 0.000000
    arrayOfVariantOfDouble69[2] = 0.000000
    arrayOfVariantOfDouble69[3] = 0.000000
    arrayOfVariantOfDouble69[4] = 1.000000
    arrayOfVariantOfDouble69[5] = 0.000000
    arrayOfVariantOfDouble69[6] = 0.000000
    arrayOfVariantOfDouble69[7] = 0.000000
    arrayOfVariantOfDouble69[8] = 1.000000
    arrayOfVariantOfDouble69[9] = 0.000000
    arrayOfVariantOfDouble69[10] = - 29.535386
    arrayOfVariantOfDouble69[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble69)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble70[0] = 1.000000
    arrayOfVariantOfDouble70[1] = 0.000000
    arrayOfVariantOfDouble70[2] = 0.000000
    arrayOfVariantOfDouble70[3] = 0.000000
    arrayOfVariantOfDouble70[4] = 1.000000
    arrayOfVariantOfDouble70[5] = 0.000000
    arrayOfVariantOfDouble70[6] = 0.000000
    arrayOfVariantOfDouble70[7] = 0.000000
    arrayOfVariantOfDouble70[8] = 1.000000
    arrayOfVariantOfDouble70[9] = 0.000000
    arrayOfVariantOfDouble70[10] = - 6.397126
    arrayOfVariantOfDouble70[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble70)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble71[0] = 1.000000
    arrayOfVariantOfDouble71[1] = 0.000000
    arrayOfVariantOfDouble71[2] = 0.000000
    arrayOfVariantOfDouble71[3] = 0.000000
    arrayOfVariantOfDouble71[4] = 1.000000
    arrayOfVariantOfDouble71[5] = 0.000000
    arrayOfVariantOfDouble71[6] = 0.000000
    arrayOfVariantOfDouble71[7] = 0.000000
    arrayOfVariantOfDouble71[8] = 1.000000
    arrayOfVariantOfDouble71[9] = 0.000000
    arrayOfVariantOfDouble71[10] = - 8.020426
    arrayOfVariantOfDouble71[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble71)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble72[0] = 1.000000
    arrayOfVariantOfDouble72[1] = 0.000000
    arrayOfVariantOfDouble72[2] = 0.000000
    arrayOfVariantOfDouble72[3] = 0.000000
    arrayOfVariantOfDouble72[4] = 1.000000
    arrayOfVariantOfDouble72[5] = 0.000000
    arrayOfVariantOfDouble72[6] = 0.000000
    arrayOfVariantOfDouble72[7] = 0.000000
    arrayOfVariantOfDouble72[8] = 1.000000
    arrayOfVariantOfDouble72[9] = 0.000000
    arrayOfVariantOfDouble72[10] = - 10.757468
    arrayOfVariantOfDouble72[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble72)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble73[0] = 1.000000
    arrayOfVariantOfDouble73[1] = 0.000000
    arrayOfVariantOfDouble73[2] = 0.000000
    arrayOfVariantOfDouble73[3] = 0.000000
    arrayOfVariantOfDouble73[4] = 1.000000
    arrayOfVariantOfDouble73[5] = 0.000000
    arrayOfVariantOfDouble73[6] = 0.000000
    arrayOfVariantOfDouble73[7] = 0.000000
    arrayOfVariantOfDouble73[8] = 1.000000
    arrayOfVariantOfDouble73[9] = 0.000000
    arrayOfVariantOfDouble73[10] = - 3.660100
    arrayOfVariantOfDouble73[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble73)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble74[0] = 1.000000
    arrayOfVariantOfDouble74[1] = 0.000000
    arrayOfVariantOfDouble74[2] = 0.000000
    arrayOfVariantOfDouble74[3] = 0.000000
    arrayOfVariantOfDouble74[4] = 1.000000
    arrayOfVariantOfDouble74[5] = 0.000000
    arrayOfVariantOfDouble74[6] = 0.000000
    arrayOfVariantOfDouble74[7] = 0.000000
    arrayOfVariantOfDouble74[8] = 1.000000
    arrayOfVariantOfDouble74[9] = 0.000000
    arrayOfVariantOfDouble74[10] = - 2.291533
    arrayOfVariantOfDouble74[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble74)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble75[0] = 1.000000
    arrayOfVariantOfDouble75[1] = 0.000000
    arrayOfVariantOfDouble75[2] = 0.000000
    arrayOfVariantOfDouble75[3] = 0.000000
    arrayOfVariantOfDouble75[4] = 1.000000
    arrayOfVariantOfDouble75[5] = 0.000000
    arrayOfVariantOfDouble75[6] = 0.000000
    arrayOfVariantOfDouble75[7] = 0.000000
    arrayOfVariantOfDouble75[8] = 1.000000
    arrayOfVariantOfDouble75[9] = 0.000000
    arrayOfVariantOfDouble75[10] = - 9.834479
    arrayOfVariantOfDouble75[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble75)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble76[0] = 1.000000
    arrayOfVariantOfDouble76[1] = 0.000000
    arrayOfVariantOfDouble76[2] = 0.000000
    arrayOfVariantOfDouble76[3] = 0.000000
    arrayOfVariantOfDouble76[4] = 1.000000
    arrayOfVariantOfDouble76[5] = 0.000000
    arrayOfVariantOfDouble76[6] = 0.000000
    arrayOfVariantOfDouble76[7] = 0.000000
    arrayOfVariantOfDouble76[8] = 1.000000
    arrayOfVariantOfDouble76[9] = 0.000000
    arrayOfVariantOfDouble76[10] = - 2.291562
    arrayOfVariantOfDouble76[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble76)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble77[0] = 1.000000
    arrayOfVariantOfDouble77[1] = 0.000000
    arrayOfVariantOfDouble77[2] = 0.000000
    arrayOfVariantOfDouble77[3] = 0.000000
    arrayOfVariantOfDouble77[4] = 1.000000
    arrayOfVariantOfDouble77[5] = 0.000000
    arrayOfVariantOfDouble77[6] = 0.000000
    arrayOfVariantOfDouble77[7] = 0.000000
    arrayOfVariantOfDouble77[8] = 1.000000
    arrayOfVariantOfDouble77[9] = 0.000000
    arrayOfVariantOfDouble77[10] = - 4.583093
    arrayOfVariantOfDouble77[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble77)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble78[0] = 1.000000
    arrayOfVariantOfDouble78[1] = 0.000000
    arrayOfVariantOfDouble78[2] = 0.000000
    arrayOfVariantOfDouble78[3] = 0.000000
    arrayOfVariantOfDouble78[4] = 1.000000
    arrayOfVariantOfDouble78[5] = 0.000000
    arrayOfVariantOfDouble78[6] = 0.000000
    arrayOfVariantOfDouble78[7] = 0.000000
    arrayOfVariantOfDouble78[8] = 1.000000
    arrayOfVariantOfDouble78[9] = 0.000000
    arrayOfVariantOfDouble78[10] = - 10.534725
    arrayOfVariantOfDouble78[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble78)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble79[0] = 1.000000
    arrayOfVariantOfDouble79[1] = 0.000000
    arrayOfVariantOfDouble79[2] = 0.000000
    arrayOfVariantOfDouble79[3] = 0.000000
    arrayOfVariantOfDouble79[4] = 1.000000
    arrayOfVariantOfDouble79[5] = 0.000000
    arrayOfVariantOfDouble79[6] = 0.000000
    arrayOfVariantOfDouble79[7] = 0.000000
    arrayOfVariantOfDouble79[8] = 1.000000
    arrayOfVariantOfDouble79[9] = 0.000000
    arrayOfVariantOfDouble79[10] = - 4.583088
    arrayOfVariantOfDouble79[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble79)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble80[0] = 1.000000
    arrayOfVariantOfDouble80[1] = 0.000000
    arrayOfVariantOfDouble80[2] = 0.000000
    arrayOfVariantOfDouble80[3] = 0.000000
    arrayOfVariantOfDouble80[4] = 1.000000
    arrayOfVariantOfDouble80[5] = 0.000000
    arrayOfVariantOfDouble80[6] = 0.000000
    arrayOfVariantOfDouble80[7] = 0.000000
    arrayOfVariantOfDouble80[8] = 1.000000
    arrayOfVariantOfDouble80[9] = 0.000000
    arrayOfVariantOfDouble80[10] = - 6.174380
    arrayOfVariantOfDouble80[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble80)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble81[0] = 1.000000
    arrayOfVariantOfDouble81[1] = 0.000000
    arrayOfVariantOfDouble81[2] = 0.000000
    arrayOfVariantOfDouble81[3] = 0.000000
    arrayOfVariantOfDouble81[4] = 1.000000
    arrayOfVariantOfDouble81[5] = 0.000000
    arrayOfVariantOfDouble81[6] = 0.000000
    arrayOfVariantOfDouble81[7] = 0.000000
    arrayOfVariantOfDouble81[8] = 1.000000
    arrayOfVariantOfDouble81[9] = 0.000000
    arrayOfVariantOfDouble81[10] = - 2.291562
    arrayOfVariantOfDouble81[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble81)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble82[0] = 1.000000
    arrayOfVariantOfDouble82[1] = 0.000000
    arrayOfVariantOfDouble82[2] = 0.000000
    arrayOfVariantOfDouble82[3] = 0.000000
    arrayOfVariantOfDouble82[4] = 1.000000
    arrayOfVariantOfDouble82[5] = 0.000000
    arrayOfVariantOfDouble82[6] = 0.000000
    arrayOfVariantOfDouble82[7] = 0.000000
    arrayOfVariantOfDouble82[8] = 1.000000
    arrayOfVariantOfDouble82[9] = 0.000000
    arrayOfVariantOfDouble82[10] = - 3.437320
    arrayOfVariantOfDouble82[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble82)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble83[0] = 1.000000
    arrayOfVariantOfDouble83[1] = 0.000000
    arrayOfVariantOfDouble83[2] = 0.000000
    arrayOfVariantOfDouble83[3] = 0.000000
    arrayOfVariantOfDouble83[4] = 1.000000
    arrayOfVariantOfDouble83[5] = 0.000000
    arrayOfVariantOfDouble83[6] = 0.000000
    arrayOfVariantOfDouble83[7] = 0.000000
    arrayOfVariantOfDouble83[8] = 1.000000
    arrayOfVariantOfDouble83[9] = 0.000000
    arrayOfVariantOfDouble83[10] = - 5.728866
    arrayOfVariantOfDouble83[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble83)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble84[0] = 1.000000
    arrayOfVariantOfDouble84[1] = 0.000000
    arrayOfVariantOfDouble84[2] = 0.000000
    arrayOfVariantOfDouble84[3] = 0.000000
    arrayOfVariantOfDouble84[4] = 1.000000
    arrayOfVariantOfDouble84[5] = 0.000000
    arrayOfVariantOfDouble84[6] = 0.000000
    arrayOfVariantOfDouble84[7] = 0.000000
    arrayOfVariantOfDouble84[8] = 1.000000
    arrayOfVariantOfDouble84[9] = 0.000000
    arrayOfVariantOfDouble84[10] = - 1.145793
    arrayOfVariantOfDouble84[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble84)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble85[0] = 1.000000
    arrayOfVariantOfDouble85[1] = 0.000000
    arrayOfVariantOfDouble85[2] = 0.000000
    arrayOfVariantOfDouble85[3] = 0.000000
    arrayOfVariantOfDouble85[4] = 1.000000
    arrayOfVariantOfDouble85[5] = 0.000000
    arrayOfVariantOfDouble85[6] = 0.000000
    arrayOfVariantOfDouble85[7] = 0.000000
    arrayOfVariantOfDouble85[8] = 1.000000
    arrayOfVariantOfDouble85[9] = 0.000000
    arrayOfVariantOfDouble85[10] = - 1.145770
    arrayOfVariantOfDouble85[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble85)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble86[0] = 1.000000
    arrayOfVariantOfDouble86[1] = 0.000000
    arrayOfVariantOfDouble86[2] = 0.000000
    arrayOfVariantOfDouble86[3] = 0.000000
    arrayOfVariantOfDouble86[4] = 1.000000
    arrayOfVariantOfDouble86[5] = 0.000000
    arrayOfVariantOfDouble86[6] = 0.000000
    arrayOfVariantOfDouble86[7] = 0.000000
    arrayOfVariantOfDouble86[8] = 1.000000
    arrayOfVariantOfDouble86[9] = 0.000000
    arrayOfVariantOfDouble86[10] = - 1.591283
    arrayOfVariantOfDouble86[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble86)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble87[0] = 1.000000
    arrayOfVariantOfDouble87[1] = 0.000000
    arrayOfVariantOfDouble87[2] = 0.000000
    arrayOfVariantOfDouble87[3] = 0.000000
    arrayOfVariantOfDouble87[4] = 1.000000
    arrayOfVariantOfDouble87[5] = 0.000000
    arrayOfVariantOfDouble87[6] = 0.000000
    arrayOfVariantOfDouble87[7] = 0.000000
    arrayOfVariantOfDouble87[8] = 1.000000
    arrayOfVariantOfDouble87[9] = 0.000000
    arrayOfVariantOfDouble87[10] = - 3.437323
    arrayOfVariantOfDouble87[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble87)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble88[0] = 1.000000
    arrayOfVariantOfDouble88[1] = 0.000000
    arrayOfVariantOfDouble88[2] = 0.000000
    arrayOfVariantOfDouble88[3] = 0.000000
    arrayOfVariantOfDouble88[4] = 1.000000
    arrayOfVariantOfDouble88[5] = 0.000000
    arrayOfVariantOfDouble88[6] = 0.000000
    arrayOfVariantOfDouble88[7] = 0.000000
    arrayOfVariantOfDouble88[8] = 1.000000
    arrayOfVariantOfDouble88[9] = 0.000000
    arrayOfVariantOfDouble88[10] = - 1.368521
    arrayOfVariantOfDouble88[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble88)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble89[0] = 1.000000
    arrayOfVariantOfDouble89[1] = 0.000000
    arrayOfVariantOfDouble89[2] = 0.000000
    arrayOfVariantOfDouble89[3] = 0.000000
    arrayOfVariantOfDouble89[4] = 1.000000
    arrayOfVariantOfDouble89[5] = 0.000000
    arrayOfVariantOfDouble89[6] = 0.000000
    arrayOfVariantOfDouble89[7] = 0.000000
    arrayOfVariantOfDouble89[8] = 1.000000
    arrayOfVariantOfDouble89[9] = 0.000000
    arrayOfVariantOfDouble89[10] = - 3.437318
    arrayOfVariantOfDouble89[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble89)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble90[0] = 1.000000
    arrayOfVariantOfDouble90[1] = 0.000000
    arrayOfVariantOfDouble90[2] = 0.000000
    arrayOfVariantOfDouble90[3] = 0.000000
    arrayOfVariantOfDouble90[4] = 1.000000
    arrayOfVariantOfDouble90[5] = 0.000000
    arrayOfVariantOfDouble90[6] = 0.000000
    arrayOfVariantOfDouble90[7] = 0.000000
    arrayOfVariantOfDouble90[8] = 1.000000
    arrayOfVariantOfDouble90[9] = 0.000000
    arrayOfVariantOfDouble90[10] = - 2.291564
    arrayOfVariantOfDouble90[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble90)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble91[0] = 1.000000
    arrayOfVariantOfDouble91[1] = 0.000000
    arrayOfVariantOfDouble91[2] = 0.000000
    arrayOfVariantOfDouble91[3] = 0.000000
    arrayOfVariantOfDouble91[4] = 1.000000
    arrayOfVariantOfDouble91[5] = 0.000000
    arrayOfVariantOfDouble91[6] = 0.000000
    arrayOfVariantOfDouble91[7] = 0.000000
    arrayOfVariantOfDouble91[8] = 1.000000
    arrayOfVariantOfDouble91[9] = 0.000000
    arrayOfVariantOfDouble91[10] = - 4.583092
    arrayOfVariantOfDouble91[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble91)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble92[0] = 1.000000
    arrayOfVariantOfDouble92[1] = 0.000000
    arrayOfVariantOfDouble92[2] = 0.000000
    arrayOfVariantOfDouble92[3] = 0.000000
    arrayOfVariantOfDouble92[4] = 1.000000
    arrayOfVariantOfDouble92[5] = 0.000000
    arrayOfVariantOfDouble92[6] = 0.000000
    arrayOfVariantOfDouble92[7] = 0.000000
    arrayOfVariantOfDouble92[8] = 1.000000
    arrayOfVariantOfDouble92[9] = 0.000000
    arrayOfVariantOfDouble92[10] = - 3.437356
    arrayOfVariantOfDouble92[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble92)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble93[0] = 1.000000
    arrayOfVariantOfDouble93[1] = 0.000000
    arrayOfVariantOfDouble93[2] = 0.000000
    arrayOfVariantOfDouble93[3] = 0.000000
    arrayOfVariantOfDouble93[4] = 1.000000
    arrayOfVariantOfDouble93[5] = 0.000000
    arrayOfVariantOfDouble93[6] = 0.000000
    arrayOfVariantOfDouble93[7] = 0.000000
    arrayOfVariantOfDouble93[8] = 1.000000
    arrayOfVariantOfDouble93[9] = 0.000000
    arrayOfVariantOfDouble93[10] = - 2.291528
    arrayOfVariantOfDouble93[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble93)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble94[0] = 1.000000
    arrayOfVariantOfDouble94[1] = 0.000000
    arrayOfVariantOfDouble94[2] = 0.000000
    arrayOfVariantOfDouble94[3] = 0.000000
    arrayOfVariantOfDouble94[4] = 1.000000
    arrayOfVariantOfDouble94[5] = 0.000000
    arrayOfVariantOfDouble94[6] = 0.000000
    arrayOfVariantOfDouble94[7] = 0.000000
    arrayOfVariantOfDouble94[8] = 1.000000
    arrayOfVariantOfDouble94[9] = 0.000000
    arrayOfVariantOfDouble94[10] = - 3.882845
    arrayOfVariantOfDouble94[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble94)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble95[0] = 1.000000
    arrayOfVariantOfDouble95[1] = 0.000000
    arrayOfVariantOfDouble95[2] = 0.000000
    arrayOfVariantOfDouble95[3] = 0.000000
    arrayOfVariantOfDouble95[4] = 1.000000
    arrayOfVariantOfDouble95[5] = 0.000000
    arrayOfVariantOfDouble95[6] = 0.000000
    arrayOfVariantOfDouble95[7] = 0.000000
    arrayOfVariantOfDouble95[8] = 1.000000
    arrayOfVariantOfDouble95[9] = 0.000000
    arrayOfVariantOfDouble95[10] = - 3.660049
    arrayOfVariantOfDouble95[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble95)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble96[0] = 1.000000
    arrayOfVariantOfDouble96[1] = 0.000000
    arrayOfVariantOfDouble96[2] = 0.000000
    arrayOfVariantOfDouble96[3] = 0.000000
    arrayOfVariantOfDouble96[4] = 1.000000
    arrayOfVariantOfDouble96[5] = 0.000000
    arrayOfVariantOfDouble96[6] = 0.000000
    arrayOfVariantOfDouble96[7] = 0.000000
    arrayOfVariantOfDouble96[8] = 1.000000
    arrayOfVariantOfDouble96[9] = 0.000000
    arrayOfVariantOfDouble96[10] = - 5.251352
    arrayOfVariantOfDouble96[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble96)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble97[0] = 1.000000
    arrayOfVariantOfDouble97[1] = 0.000000
    arrayOfVariantOfDouble97[2] = 0.000000
    arrayOfVariantOfDouble97[3] = 0.000000
    arrayOfVariantOfDouble97[4] = 1.000000
    arrayOfVariantOfDouble97[5] = 0.000000
    arrayOfVariantOfDouble97[6] = 0.000000
    arrayOfVariantOfDouble97[7] = 0.000000
    arrayOfVariantOfDouble97[8] = 1.000000
    arrayOfVariantOfDouble97[9] = 0.000000
    arrayOfVariantOfDouble97[10] = - 1.145791
    arrayOfVariantOfDouble97[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble97)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble98[0] = 1.000000
    arrayOfVariantOfDouble98[1] = 0.000000
    arrayOfVariantOfDouble98[2] = 0.000000
    arrayOfVariantOfDouble98[3] = 0.000000
    arrayOfVariantOfDouble98[4] = 1.000000
    arrayOfVariantOfDouble98[5] = 0.000000
    arrayOfVariantOfDouble98[6] = 0.000000
    arrayOfVariantOfDouble98[7] = 0.000000
    arrayOfVariantOfDouble98[8] = 1.000000
    arrayOfVariantOfDouble98[9] = 0.000000
    arrayOfVariantOfDouble98[10] = - 1.145772
    arrayOfVariantOfDouble98[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble98)
    arrayOfVariantOfBSTR4[0] = ('C:\\%s\\knuckle_pin_collar.CATPart' %(foldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR4, 'All')
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    product4 = products1.Item('Part2.1')
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble99[0] = 1.000000
    arrayOfVariantOfDouble99[1] = 0.000000
    arrayOfVariantOfDouble99[2] = 0.000000
    arrayOfVariantOfDouble99[3] = 0.000000
    arrayOfVariantOfDouble99[4] = 1.000000
    arrayOfVariantOfDouble99[5] = 0.000000
    arrayOfVariantOfDouble99[6] = 0.000000
    arrayOfVariantOfDouble99[7] = 0.000000
    arrayOfVariantOfDouble99[8] = 1.000000
    arrayOfVariantOfDouble99[9] = 0.000000
    arrayOfVariantOfDouble99[10] = 7.697306
    arrayOfVariantOfDouble99[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble99)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble100[0] = 1.000000
    arrayOfVariantOfDouble100[1] = 0.000000
    arrayOfVariantOfDouble100[2] = 0.000000
    arrayOfVariantOfDouble100[3] = 0.000000
    arrayOfVariantOfDouble100[4] = 1.000000
    arrayOfVariantOfDouble100[5] = 0.000000
    arrayOfVariantOfDouble100[6] = 0.000000
    arrayOfVariantOfDouble100[7] = 0.000000
    arrayOfVariantOfDouble100[8] = 1.000000
    arrayOfVariantOfDouble100[9] = 0.000000
    arrayOfVariantOfDouble100[10] = 6.683900
    arrayOfVariantOfDouble100[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble100)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble101[0] = 1.000000
    arrayOfVariantOfDouble101[1] = 0.000000
    arrayOfVariantOfDouble101[2] = 0.000000
    arrayOfVariantOfDouble101[3] = 0.000000
    arrayOfVariantOfDouble101[4] = 1.000000
    arrayOfVariantOfDouble101[5] = 0.000000
    arrayOfVariantOfDouble101[6] = 0.000000
    arrayOfVariantOfDouble101[7] = 0.000000
    arrayOfVariantOfDouble101[8] = 1.000000
    arrayOfVariantOfDouble101[9] = 0.000000
    arrayOfVariantOfDouble101[10] = 8.171883
    arrayOfVariantOfDouble101[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble101)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble102[0] = 1.000000
    arrayOfVariantOfDouble102[1] = 0.000000
    arrayOfVariantOfDouble102[2] = 0.000000
    arrayOfVariantOfDouble102[3] = 0.000000
    arrayOfVariantOfDouble102[4] = 1.000000
    arrayOfVariantOfDouble102[5] = 0.000000
    arrayOfVariantOfDouble102[6] = 0.000000
    arrayOfVariantOfDouble102[7] = 0.000000
    arrayOfVariantOfDouble102[8] = 1.000000
    arrayOfVariantOfDouble102[9] = 0.000000
    arrayOfVariantOfDouble102[10] = 5.699957
    arrayOfVariantOfDouble102[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble102)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble103[0] = 1.000000
    arrayOfVariantOfDouble103[1] = 0.000000
    arrayOfVariantOfDouble103[2] = 0.000000
    arrayOfVariantOfDouble103[3] = 0.000000
    arrayOfVariantOfDouble103[4] = 1.000000
    arrayOfVariantOfDouble103[5] = 0.000000
    arrayOfVariantOfDouble103[6] = 0.000000
    arrayOfVariantOfDouble103[7] = 0.000000
    arrayOfVariantOfDouble103[8] = 1.000000
    arrayOfVariantOfDouble103[9] = 0.000000
    arrayOfVariantOfDouble103[10] = 9.659880
    arrayOfVariantOfDouble103[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble103)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble104[0] = 1.000000
    arrayOfVariantOfDouble104[1] = 0.000000
    arrayOfVariantOfDouble104[2] = 0.000000
    arrayOfVariantOfDouble104[3] = 0.000000
    arrayOfVariantOfDouble104[4] = 1.000000
    arrayOfVariantOfDouble104[5] = 0.000000
    arrayOfVariantOfDouble104[6] = 0.000000
    arrayOfVariantOfDouble104[7] = 0.000000
    arrayOfVariantOfDouble104[8] = 1.000000
    arrayOfVariantOfDouble104[9] = 0.000000
    arrayOfVariantOfDouble104[10] = 10.643819
    arrayOfVariantOfDouble104[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble104)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble105[0] = 1.000000
    arrayOfVariantOfDouble105[1] = 0.000000
    arrayOfVariantOfDouble105[2] = 0.000000
    arrayOfVariantOfDouble105[3] = 0.000000
    arrayOfVariantOfDouble105[4] = 1.000000
    arrayOfVariantOfDouble105[5] = 0.000000
    arrayOfVariantOfDouble105[6] = 0.000000
    arrayOfVariantOfDouble105[7] = 0.000000
    arrayOfVariantOfDouble105[8] = 1.000000
    arrayOfVariantOfDouble105[9] = 0.000000
    arrayOfVariantOfDouble105[10] = 13.871843
    arrayOfVariantOfDouble105[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble105)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble106[0] = 1.000000
    arrayOfVariantOfDouble106[1] = 0.000000
    arrayOfVariantOfDouble106[2] = 0.000000
    arrayOfVariantOfDouble106[3] = 0.000000
    arrayOfVariantOfDouble106[4] = 1.000000
    arrayOfVariantOfDouble106[5] = 0.000000
    arrayOfVariantOfDouble106[6] = 0.000000
    arrayOfVariantOfDouble106[7] = 0.000000
    arrayOfVariantOfDouble106[8] = 1.000000
    arrayOfVariantOfDouble106[9] = 0.000000
    arrayOfVariantOfDouble106[10] = 9.659853
    arrayOfVariantOfDouble106[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble106)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble107[0] = 1.000000
    arrayOfVariantOfDouble107[1] = 0.000000
    arrayOfVariantOfDouble107[2] = 0.000000
    arrayOfVariantOfDouble107[3] = 0.000000
    arrayOfVariantOfDouble107[4] = 1.000000
    arrayOfVariantOfDouble107[5] = 0.000000
    arrayOfVariantOfDouble107[6] = 0.000000
    arrayOfVariantOfDouble107[7] = 0.000000
    arrayOfVariantOfDouble107[8] = 1.000000
    arrayOfVariantOfDouble107[9] = 0.000000
    arrayOfVariantOfDouble107[10] = 4.463988
    arrayOfVariantOfDouble107[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble107)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble108[0] = 1.000000
    arrayOfVariantOfDouble108[1] = 0.000000
    arrayOfVariantOfDouble108[2] = 0.000000
    arrayOfVariantOfDouble108[3] = 0.000000
    arrayOfVariantOfDouble108[4] = 1.000000
    arrayOfVariantOfDouble108[5] = 0.000000
    arrayOfVariantOfDouble108[6] = 0.000000
    arrayOfVariantOfDouble108[7] = 0.000000
    arrayOfVariantOfDouble108[8] = 1.000000
    arrayOfVariantOfDouble108[9] = 0.000000
    arrayOfVariantOfDouble108[10] = 13.871839
    arrayOfVariantOfDouble108[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble108)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble109[0] = 1.000000
    arrayOfVariantOfDouble109[1] = 0.000000
    arrayOfVariantOfDouble109[2] = 0.000000
    arrayOfVariantOfDouble109[3] = 0.000000
    arrayOfVariantOfDouble109[4] = 1.000000
    arrayOfVariantOfDouble109[5] = 0.000000
    arrayOfVariantOfDouble109[6] = 0.000000
    arrayOfVariantOfDouble109[7] = 0.000000
    arrayOfVariantOfDouble109[8] = 1.000000
    arrayOfVariantOfDouble109[9] = 0.000000
    arrayOfVariantOfDouble109[10] = 4.211956
    arrayOfVariantOfDouble109[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble109)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble110[0] = 1.000000
    arrayOfVariantOfDouble110[1] = 0.000000
    arrayOfVariantOfDouble110[2] = 0.000000
    arrayOfVariantOfDouble110[3] = 0.000000
    arrayOfVariantOfDouble110[4] = 1.000000
    arrayOfVariantOfDouble110[5] = 0.000000
    arrayOfVariantOfDouble110[6] = 0.000000
    arrayOfVariantOfDouble110[7] = 0.000000
    arrayOfVariantOfDouble110[8] = 1.000000
    arrayOfVariantOfDouble110[9] = 0.000000
    arrayOfVariantOfDouble110[10] = 2.723978
    arrayOfVariantOfDouble110[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble110)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble111[0] = 1.000000
    arrayOfVariantOfDouble111[1] = 0.000000
    arrayOfVariantOfDouble111[2] = 0.000000
    arrayOfVariantOfDouble111[3] = 0.000000
    arrayOfVariantOfDouble111[4] = 1.000000
    arrayOfVariantOfDouble111[5] = 0.000000
    arrayOfVariantOfDouble111[6] = 0.000000
    arrayOfVariantOfDouble111[7] = 0.000000
    arrayOfVariantOfDouble111[8] = 1.000000
    arrayOfVariantOfDouble111[9] = 0.000000
    arrayOfVariantOfDouble111[10] = 5.447896
    arrayOfVariantOfDouble111[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble111)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble112[0] = 1.000000
    arrayOfVariantOfDouble112[1] = 0.000000
    arrayOfVariantOfDouble112[2] = 0.000000
    arrayOfVariantOfDouble112[3] = 0.000000
    arrayOfVariantOfDouble112[4] = 1.000000
    arrayOfVariantOfDouble112[5] = 0.000000
    arrayOfVariantOfDouble112[6] = 0.000000
    arrayOfVariantOfDouble112[7] = 0.000000
    arrayOfVariantOfDouble112[8] = 1.000000
    arrayOfVariantOfDouble112[9] = 0.000000
    arrayOfVariantOfDouble112[10] = 6.935918
    arrayOfVariantOfDouble112[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble112)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble113[0] = 1.000000
    arrayOfVariantOfDouble113[1] = 0.000000
    arrayOfVariantOfDouble113[2] = 0.000000
    arrayOfVariantOfDouble113[3] = 0.000000
    arrayOfVariantOfDouble113[4] = 1.000000
    arrayOfVariantOfDouble113[5] = 0.000000
    arrayOfVariantOfDouble113[6] = 0.000000
    arrayOfVariantOfDouble113[7] = 0.000000
    arrayOfVariantOfDouble113[8] = 1.000000
    arrayOfVariantOfDouble113[9] = 0.000000
    arrayOfVariantOfDouble113[10] = 6.683898
    arrayOfVariantOfDouble113[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble113)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble114[0] = 1.000000
    arrayOfVariantOfDouble114[1] = 0.000000
    arrayOfVariantOfDouble114[2] = 0.000000
    arrayOfVariantOfDouble114[3] = 0.000000
    arrayOfVariantOfDouble114[4] = 1.000000
    arrayOfVariantOfDouble114[5] = 0.000000
    arrayOfVariantOfDouble114[6] = 0.000000
    arrayOfVariantOfDouble114[7] = 0.000000
    arrayOfVariantOfDouble114[8] = 1.000000
    arrayOfVariantOfDouble114[9] = 0.000000
    arrayOfVariantOfDouble114[10] = 2.723963
    arrayOfVariantOfDouble114[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble114)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble115[0] = 1.000000
    arrayOfVariantOfDouble115[1] = 0.000000
    arrayOfVariantOfDouble115[2] = 0.000000
    arrayOfVariantOfDouble115[3] = 0.000000
    arrayOfVariantOfDouble115[4] = 1.000000
    arrayOfVariantOfDouble115[5] = 0.000000
    arrayOfVariantOfDouble115[6] = 0.000000
    arrayOfVariantOfDouble115[7] = 0.000000
    arrayOfVariantOfDouble115[8] = 1.000000
    arrayOfVariantOfDouble115[9] = 0.000000
    arrayOfVariantOfDouble115[10] = 1.488012
    arrayOfVariantOfDouble115[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble115)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble116[0] = 1.000000
    arrayOfVariantOfDouble116[1] = 0.000000
    arrayOfVariantOfDouble116[2] = 0.000000
    arrayOfVariantOfDouble116[3] = 0.000000
    arrayOfVariantOfDouble116[4] = 1.000000
    arrayOfVariantOfDouble116[5] = 0.000000
    arrayOfVariantOfDouble116[6] = 0.000000
    arrayOfVariantOfDouble116[7] = 0.000000
    arrayOfVariantOfDouble116[8] = 1.000000
    arrayOfVariantOfDouble116[9] = 0.000000
    arrayOfVariantOfDouble116[10] = 1.235950
    arrayOfVariantOfDouble116[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble116)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble117[0] = 1.000000
    arrayOfVariantOfDouble117[1] = 0.000000
    arrayOfVariantOfDouble117[2] = 0.000000
    arrayOfVariantOfDouble117[3] = 0.000000
    arrayOfVariantOfDouble117[4] = 1.000000
    arrayOfVariantOfDouble117[5] = 0.000000
    arrayOfVariantOfDouble117[6] = 0.000000
    arrayOfVariantOfDouble117[7] = 0.000000
    arrayOfVariantOfDouble117[8] = 1.000000
    arrayOfVariantOfDouble117[9] = 0.000000
    arrayOfVariantOfDouble117[10] = 8.675934
    arrayOfVariantOfDouble117[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble117)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble118[0] = 1.000000
    arrayOfVariantOfDouble118[1] = 0.000000
    arrayOfVariantOfDouble118[2] = 0.000000
    arrayOfVariantOfDouble118[3] = 0.000000
    arrayOfVariantOfDouble118[4] = 1.000000
    arrayOfVariantOfDouble118[5] = 0.000000
    arrayOfVariantOfDouble118[6] = 0.000000
    arrayOfVariantOfDouble118[7] = 0.000000
    arrayOfVariantOfDouble118[8] = 1.000000
    arrayOfVariantOfDouble118[9] = 0.000000
    arrayOfVariantOfDouble118[10] = 5.195905
    arrayOfVariantOfDouble118[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble118)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble119[0] = 1.000000
    arrayOfVariantOfDouble119[1] = 0.000000
    arrayOfVariantOfDouble119[2] = 0.000000
    arrayOfVariantOfDouble119[3] = 0.000000
    arrayOfVariantOfDouble119[4] = 1.000000
    arrayOfVariantOfDouble119[5] = 0.000000
    arrayOfVariantOfDouble119[6] = 0.000000
    arrayOfVariantOfDouble119[7] = 0.000000
    arrayOfVariantOfDouble119[8] = 1.000000
    arrayOfVariantOfDouble119[9] = 0.000000
    arrayOfVariantOfDouble119[10] = 5.699949
    arrayOfVariantOfDouble119[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble119)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble120[0] = 1.000000
    arrayOfVariantOfDouble120[1] = 0.000000
    arrayOfVariantOfDouble120[2] = 0.000000
    arrayOfVariantOfDouble120[3] = 0.000000
    arrayOfVariantOfDouble120[4] = 1.000000
    arrayOfVariantOfDouble120[5] = 0.000000
    arrayOfVariantOfDouble120[6] = 0.000000
    arrayOfVariantOfDouble120[7] = 0.000000
    arrayOfVariantOfDouble120[8] = 1.000000
    arrayOfVariantOfDouble120[9] = 0.000000
    arrayOfVariantOfDouble120[10] = 8.423902
    arrayOfVariantOfDouble120[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble120)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble121[0] = 1.000000
    arrayOfVariantOfDouble121[1] = 0.000000
    arrayOfVariantOfDouble121[2] = 0.000000
    arrayOfVariantOfDouble121[3] = 0.000000
    arrayOfVariantOfDouble121[4] = 1.000000
    arrayOfVariantOfDouble121[5] = 0.000000
    arrayOfVariantOfDouble121[6] = 0.000000
    arrayOfVariantOfDouble121[7] = 0.000000
    arrayOfVariantOfDouble121[8] = 1.000000
    arrayOfVariantOfDouble121[9] = 0.000000
    arrayOfVariantOfDouble121[10] = 5.699974
    arrayOfVariantOfDouble121[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble121)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble122[0] = 1.000000
    arrayOfVariantOfDouble122[1] = 0.000000
    arrayOfVariantOfDouble122[2] = 0.000000
    arrayOfVariantOfDouble122[3] = 0.000000
    arrayOfVariantOfDouble122[4] = 1.000000
    arrayOfVariantOfDouble122[5] = 0.000000
    arrayOfVariantOfDouble122[6] = 0.000000
    arrayOfVariantOfDouble122[7] = 0.000000
    arrayOfVariantOfDouble122[8] = 1.000000
    arrayOfVariantOfDouble122[9] = 0.000000
    arrayOfVariantOfDouble122[10] = 11.147865
    arrayOfVariantOfDouble122[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble122)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble123[0] = 1.000000
    arrayOfVariantOfDouble123[1] = 0.000000
    arrayOfVariantOfDouble123[2] = 0.000000
    arrayOfVariantOfDouble123[3] = 0.000000
    arrayOfVariantOfDouble123[4] = 1.000000
    arrayOfVariantOfDouble123[5] = 0.000000
    arrayOfVariantOfDouble123[6] = 0.000000
    arrayOfVariantOfDouble123[7] = 0.000000
    arrayOfVariantOfDouble123[8] = 1.000000
    arrayOfVariantOfDouble123[9] = 0.000000
    arrayOfVariantOfDouble123[10] = 8.675920
    arrayOfVariantOfDouble123[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble123)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble124[0] = 1.000000
    arrayOfVariantOfDouble124[1] = 0.000000
    arrayOfVariantOfDouble124[2] = 0.000000
    arrayOfVariantOfDouble124[3] = 0.000000
    arrayOfVariantOfDouble124[4] = 1.000000
    arrayOfVariantOfDouble124[5] = 0.000000
    arrayOfVariantOfDouble124[6] = 0.000000
    arrayOfVariantOfDouble124[7] = 0.000000
    arrayOfVariantOfDouble124[8] = 1.000000
    arrayOfVariantOfDouble124[9] = 0.000000
    arrayOfVariantOfDouble124[10] = 9.659891
    arrayOfVariantOfDouble124[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble124)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble125[0] = 1.000000
    arrayOfVariantOfDouble125[1] = 0.000000
    arrayOfVariantOfDouble125[2] = 0.000000
    arrayOfVariantOfDouble125[3] = 0.000000
    arrayOfVariantOfDouble125[4] = 1.000000
    arrayOfVariantOfDouble125[5] = 0.000000
    arrayOfVariantOfDouble125[6] = 0.000000
    arrayOfVariantOfDouble125[7] = 0.000000
    arrayOfVariantOfDouble125[8] = 1.000000
    arrayOfVariantOfDouble125[9] = 0.000000
    arrayOfVariantOfDouble125[10] = 8.171890
    arrayOfVariantOfDouble125[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble125)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble126[0] = 1.000000
    arrayOfVariantOfDouble126[1] = 0.000000
    arrayOfVariantOfDouble126[2] = 0.000000
    arrayOfVariantOfDouble126[3] = 0.000000
    arrayOfVariantOfDouble126[4] = 1.000000
    arrayOfVariantOfDouble126[5] = 0.000000
    arrayOfVariantOfDouble126[6] = 0.000000
    arrayOfVariantOfDouble126[7] = 0.000000
    arrayOfVariantOfDouble126[8] = 1.000000
    arrayOfVariantOfDouble126[9] = 0.000000
    arrayOfVariantOfDouble126[10] = 24.767661
    arrayOfVariantOfDouble126[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble126)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble127[0] = 1.000000
    arrayOfVariantOfDouble127[1] = 0.000000
    arrayOfVariantOfDouble127[2] = 0.000000
    arrayOfVariantOfDouble127[3] = 0.000000
    arrayOfVariantOfDouble127[4] = 1.000000
    arrayOfVariantOfDouble127[5] = 0.000000
    arrayOfVariantOfDouble127[6] = 0.000000
    arrayOfVariantOfDouble127[7] = 0.000000
    arrayOfVariantOfDouble127[8] = 1.000000
    arrayOfVariantOfDouble127[9] = 0.000000
    arrayOfVariantOfDouble127[10] = 12.635867
    arrayOfVariantOfDouble127[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble127)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble128[0] = 1.000000
    arrayOfVariantOfDouble128[1] = 0.000000
    arrayOfVariantOfDouble128[2] = 0.000000
    arrayOfVariantOfDouble128[3] = 0.000000
    arrayOfVariantOfDouble128[4] = 1.000000
    arrayOfVariantOfDouble128[5] = 0.000000
    arrayOfVariantOfDouble128[6] = 0.000000
    arrayOfVariantOfDouble128[7] = 0.000000
    arrayOfVariantOfDouble128[8] = 1.000000
    arrayOfVariantOfDouble128[9] = 0.000000
    arrayOfVariantOfDouble128[10] = 36.899478
    arrayOfVariantOfDouble128[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble128)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble129[0] = 1.000000
    arrayOfVariantOfDouble129[1] = 0.000000
    arrayOfVariantOfDouble129[2] = 0.000000
    arrayOfVariantOfDouble129[3] = 0.000000
    arrayOfVariantOfDouble129[4] = 1.000000
    arrayOfVariantOfDouble129[5] = 0.000000
    arrayOfVariantOfDouble129[6] = 0.000000
    arrayOfVariantOfDouble129[7] = 0.000000
    arrayOfVariantOfDouble129[8] = 1.000000
    arrayOfVariantOfDouble129[9] = 0.000000
    arrayOfVariantOfDouble129[10] = 25.271768
    arrayOfVariantOfDouble129[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble129)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble130[0] = 1.000000
    arrayOfVariantOfDouble130[1] = 0.000000
    arrayOfVariantOfDouble130[2] = 0.000000
    arrayOfVariantOfDouble130[3] = 0.000000
    arrayOfVariantOfDouble130[4] = 1.000000
    arrayOfVariantOfDouble130[5] = 0.000000
    arrayOfVariantOfDouble130[6] = 0.000000
    arrayOfVariantOfDouble130[7] = 0.000000
    arrayOfVariantOfDouble130[8] = 1.000000
    arrayOfVariantOfDouble130[9] = 0.000000
    arrayOfVariantOfDouble130[10] = 16.595776
    arrayOfVariantOfDouble130[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble130)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble131[0] = 1.000000
    arrayOfVariantOfDouble131[1] = 0.000000
    arrayOfVariantOfDouble131[2] = 0.000000
    arrayOfVariantOfDouble131[3] = 0.000000
    arrayOfVariantOfDouble131[4] = 1.000000
    arrayOfVariantOfDouble131[5] = 0.000000
    arrayOfVariantOfDouble131[6] = 0.000000
    arrayOfVariantOfDouble131[7] = 0.000000
    arrayOfVariantOfDouble131[8] = 1.000000
    arrayOfVariantOfDouble131[9] = 0.000000
    arrayOfVariantOfDouble131[10] = 11.147860
    arrayOfVariantOfDouble131[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble131)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble132[0] = 1.000000
    arrayOfVariantOfDouble132[1] = 0.000000
    arrayOfVariantOfDouble132[2] = 0.000000
    arrayOfVariantOfDouble132[3] = 0.000000
    arrayOfVariantOfDouble132[4] = 1.000000
    arrayOfVariantOfDouble132[5] = 0.000000
    arrayOfVariantOfDouble132[6] = 0.000000
    arrayOfVariantOfDouble132[7] = 0.000000
    arrayOfVariantOfDouble132[8] = 1.000000
    arrayOfVariantOfDouble132[9] = 0.000000
    arrayOfVariantOfDouble132[10] = 25.271764
    arrayOfVariantOfDouble132[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble132)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble133[0] = 1.000000
    arrayOfVariantOfDouble133[1] = 0.000000
    arrayOfVariantOfDouble133[2] = 0.000000
    arrayOfVariantOfDouble133[3] = 0.000000
    arrayOfVariantOfDouble133[4] = 1.000000
    arrayOfVariantOfDouble133[5] = 0.000000
    arrayOfVariantOfDouble133[6] = 0.000000
    arrayOfVariantOfDouble133[7] = 0.000000
    arrayOfVariantOfDouble133[8] = 1.000000
    arrayOfVariantOfDouble133[9] = 0.000000
    arrayOfVariantOfDouble133[10] = 9.911884
    arrayOfVariantOfDouble133[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble133)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble134[0] = 1.000000
    arrayOfVariantOfDouble134[1] = 0.000000
    arrayOfVariantOfDouble134[2] = 0.000000
    arrayOfVariantOfDouble134[3] = 0.000000
    arrayOfVariantOfDouble134[4] = 1.000000
    arrayOfVariantOfDouble134[5] = 0.000000
    arrayOfVariantOfDouble134[6] = 0.000000
    arrayOfVariantOfDouble134[7] = 0.000000
    arrayOfVariantOfDouble134[8] = 1.000000
    arrayOfVariantOfDouble134[9] = 0.000000
    arrayOfVariantOfDouble134[10] = 11.147857
    arrayOfVariantOfDouble134[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble134)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble135[0] = 1.000000
    arrayOfVariantOfDouble135[1] = 0.000000
    arrayOfVariantOfDouble135[2] = 0.000000
    arrayOfVariantOfDouble135[3] = 0.000000
    arrayOfVariantOfDouble135[4] = 1.000000
    arrayOfVariantOfDouble135[5] = 0.000000
    arrayOfVariantOfDouble135[6] = 0.000000
    arrayOfVariantOfDouble135[7] = 0.000000
    arrayOfVariantOfDouble135[8] = 1.000000
    arrayOfVariantOfDouble135[9] = 0.000000
    arrayOfVariantOfDouble135[10] = 1.487988
    arrayOfVariantOfDouble135[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble135)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble136[0] = 1.000000
    arrayOfVariantOfDouble136[1] = 0.000000
    arrayOfVariantOfDouble136[2] = 0.000000
    arrayOfVariantOfDouble136[3] = 0.000000
    arrayOfVariantOfDouble136[4] = 1.000000
    arrayOfVariantOfDouble136[5] = 0.000000
    arrayOfVariantOfDouble136[6] = 0.000000
    arrayOfVariantOfDouble136[7] = 0.000000
    arrayOfVariantOfDouble136[8] = 1.000000
    arrayOfVariantOfDouble136[9] = 0.000000
    arrayOfVariantOfDouble136[10] = 4.211977
    arrayOfVariantOfDouble136[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble136)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble137[0] = 1.000000
    arrayOfVariantOfDouble137[1] = 0.000000
    arrayOfVariantOfDouble137[2] = 0.000000
    arrayOfVariantOfDouble137[3] = 0.000000
    arrayOfVariantOfDouble137[4] = 1.000000
    arrayOfVariantOfDouble137[5] = 0.000000
    arrayOfVariantOfDouble137[6] = 0.000000
    arrayOfVariantOfDouble137[7] = 0.000000
    arrayOfVariantOfDouble137[8] = 1.000000
    arrayOfVariantOfDouble137[9] = 0.000000
    arrayOfVariantOfDouble137[10] = 4.211985
    arrayOfVariantOfDouble137[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble137)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble138[0] = 1.000000
    arrayOfVariantOfDouble138[1] = 0.000000
    arrayOfVariantOfDouble138[2] = 0.000000
    arrayOfVariantOfDouble138[3] = 0.000000
    arrayOfVariantOfDouble138[4] = 1.000000
    arrayOfVariantOfDouble138[5] = 0.000000
    arrayOfVariantOfDouble138[6] = 0.000000
    arrayOfVariantOfDouble138[7] = 0.000000
    arrayOfVariantOfDouble138[8] = 1.000000
    arrayOfVariantOfDouble138[9] = 0.000000
    arrayOfVariantOfDouble138[10] = 7.187902
    arrayOfVariantOfDouble138[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble138)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble139[0] = 1.000000
    arrayOfVariantOfDouble139[1] = 0.000000
    arrayOfVariantOfDouble139[2] = 0.000000
    arrayOfVariantOfDouble139[3] = 0.000000
    arrayOfVariantOfDouble139[4] = 1.000000
    arrayOfVariantOfDouble139[5] = 0.000000
    arrayOfVariantOfDouble139[6] = 0.000000
    arrayOfVariantOfDouble139[7] = 0.000000
    arrayOfVariantOfDouble139[8] = 1.000000
    arrayOfVariantOfDouble139[9] = 0.000000
    arrayOfVariantOfDouble139[10] = 6.935913
    arrayOfVariantOfDouble139[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble139)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble140[0] = 1.000000
    arrayOfVariantOfDouble140[1] = 0.000000
    arrayOfVariantOfDouble140[2] = 0.000000
    arrayOfVariantOfDouble140[3] = 0.000000
    arrayOfVariantOfDouble140[4] = 1.000000
    arrayOfVariantOfDouble140[5] = 0.000000
    arrayOfVariantOfDouble140[6] = 0.000000
    arrayOfVariantOfDouble140[7] = 0.000000
    arrayOfVariantOfDouble140[8] = 1.000000
    arrayOfVariantOfDouble140[9] = 0.000000
    arrayOfVariantOfDouble140[10] = 11.147912
    arrayOfVariantOfDouble140[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble140)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble141[0] = 1.000000
    arrayOfVariantOfDouble141[1] = 0.000000
    arrayOfVariantOfDouble141[2] = 0.000000
    arrayOfVariantOfDouble141[3] = 0.000000
    arrayOfVariantOfDouble141[4] = 1.000000
    arrayOfVariantOfDouble141[5] = 0.000000
    arrayOfVariantOfDouble141[6] = 0.000000
    arrayOfVariantOfDouble141[7] = 0.000000
    arrayOfVariantOfDouble141[8] = 1.000000
    arrayOfVariantOfDouble141[9] = 0.000000
    arrayOfVariantOfDouble141[10] = 6.683881
    arrayOfVariantOfDouble141[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble141)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble142[0] = 1.000000
    arrayOfVariantOfDouble142[1] = 0.000000
    arrayOfVariantOfDouble142[2] = 0.000000
    arrayOfVariantOfDouble142[3] = 0.000000
    arrayOfVariantOfDouble142[4] = 1.000000
    arrayOfVariantOfDouble142[5] = 0.000000
    arrayOfVariantOfDouble142[6] = 0.000000
    arrayOfVariantOfDouble142[7] = 0.000000
    arrayOfVariantOfDouble142[8] = 1.000000
    arrayOfVariantOfDouble142[9] = 0.000000
    arrayOfVariantOfDouble142[10] = 33.695615
    arrayOfVariantOfDouble142[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble142)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble143[0] = 1.000000
    arrayOfVariantOfDouble143[1] = 0.000000
    arrayOfVariantOfDouble143[2] = 0.000000
    arrayOfVariantOfDouble143[3] = 0.000000
    arrayOfVariantOfDouble143[4] = 1.000000
    arrayOfVariantOfDouble143[5] = 0.000000
    arrayOfVariantOfDouble143[6] = 0.000000
    arrayOfVariantOfDouble143[7] = 0.000000
    arrayOfVariantOfDouble143[8] = 1.000000
    arrayOfVariantOfDouble143[9] = 0.000000
    arrayOfVariantOfDouble143[10] = 25.271737
    arrayOfVariantOfDouble143[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble143)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble144[0] = 1.000000
    arrayOfVariantOfDouble144[1] = 0.000000
    arrayOfVariantOfDouble144[2] = 0.000000
    arrayOfVariantOfDouble144[3] = 0.000000
    arrayOfVariantOfDouble144[4] = 1.000000
    arrayOfVariantOfDouble144[5] = 0.000000
    arrayOfVariantOfDouble144[6] = 0.000000
    arrayOfVariantOfDouble144[7] = 0.000000
    arrayOfVariantOfDouble144[8] = 1.000000
    arrayOfVariantOfDouble144[9] = 0.000000
    arrayOfVariantOfDouble144[10] = 12.635882
    arrayOfVariantOfDouble144[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble144)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble145[0] = 1.000000
    arrayOfVariantOfDouble145[1] = 0.000000
    arrayOfVariantOfDouble145[2] = 0.000000
    arrayOfVariantOfDouble145[3] = 0.000000
    arrayOfVariantOfDouble145[4] = 1.000000
    arrayOfVariantOfDouble145[5] = 0.000000
    arrayOfVariantOfDouble145[6] = 0.000000
    arrayOfVariantOfDouble145[7] = 0.000000
    arrayOfVariantOfDouble145[8] = 1.000000
    arrayOfVariantOfDouble145[9] = 0.000000
    arrayOfVariantOfDouble145[10] = 27.995654
    arrayOfVariantOfDouble145[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble145)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble146[0] = 1.000000
    arrayOfVariantOfDouble146[1] = 0.000000
    arrayOfVariantOfDouble146[2] = 0.000000
    arrayOfVariantOfDouble146[3] = 0.000000
    arrayOfVariantOfDouble146[4] = 1.000000
    arrayOfVariantOfDouble146[5] = 0.000000
    arrayOfVariantOfDouble146[6] = 0.000000
    arrayOfVariantOfDouble146[7] = 0.000000
    arrayOfVariantOfDouble146[8] = 1.000000
    arrayOfVariantOfDouble146[9] = 0.000000
    arrayOfVariantOfDouble146[10] = 11.147911
    arrayOfVariantOfDouble146[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble146)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble147[0] = 1.000000
    arrayOfVariantOfDouble147[1] = 0.000000
    arrayOfVariantOfDouble147[2] = 0.000000
    arrayOfVariantOfDouble147[3] = 0.000000
    arrayOfVariantOfDouble147[4] = 1.000000
    arrayOfVariantOfDouble147[5] = 0.000000
    arrayOfVariantOfDouble147[6] = 0.000000
    arrayOfVariantOfDouble147[7] = 0.000000
    arrayOfVariantOfDouble147[8] = 1.000000
    arrayOfVariantOfDouble147[9] = 0.000000
    arrayOfVariantOfDouble147[10] = 17.099842
    arrayOfVariantOfDouble147[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble147)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble148[0] = 1.000000
    arrayOfVariantOfDouble148[1] = 0.000000
    arrayOfVariantOfDouble148[2] = 0.000000
    arrayOfVariantOfDouble148[3] = 0.000000
    arrayOfVariantOfDouble148[4] = 1.000000
    arrayOfVariantOfDouble148[5] = 0.000000
    arrayOfVariantOfDouble148[6] = 0.000000
    arrayOfVariantOfDouble148[7] = 0.000000
    arrayOfVariantOfDouble148[8] = 1.000000
    arrayOfVariantOfDouble148[9] = 0.000000
    arrayOfVariantOfDouble148[10] = 10.163922
    arrayOfVariantOfDouble148[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble148)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble149[0] = 1.000000
    arrayOfVariantOfDouble149[1] = 0.000000
    arrayOfVariantOfDouble149[2] = 0.000000
    arrayOfVariantOfDouble149[3] = 0.000000
    arrayOfVariantOfDouble149[4] = 1.000000
    arrayOfVariantOfDouble149[5] = 0.000000
    arrayOfVariantOfDouble149[6] = 0.000000
    arrayOfVariantOfDouble149[7] = 0.000000
    arrayOfVariantOfDouble149[8] = 1.000000
    arrayOfVariantOfDouble149[9] = 0.000000
    arrayOfVariantOfDouble149[10] = 6.935916
    arrayOfVariantOfDouble149[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble149)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble150[0] = 1.000000
    arrayOfVariantOfDouble150[1] = 0.000000
    arrayOfVariantOfDouble150[2] = 0.000000
    arrayOfVariantOfDouble150[3] = 0.000000
    arrayOfVariantOfDouble150[4] = 1.000000
    arrayOfVariantOfDouble150[5] = 0.000000
    arrayOfVariantOfDouble150[6] = 0.000000
    arrayOfVariantOfDouble150[7] = 0.000000
    arrayOfVariantOfDouble150[8] = 1.000000
    arrayOfVariantOfDouble150[9] = 0.000000
    arrayOfVariantOfDouble150[10] = 16.847821
    arrayOfVariantOfDouble150[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble150)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble151[0] = 1.000000
    arrayOfVariantOfDouble151[1] = 0.000000
    arrayOfVariantOfDouble151[2] = 0.000000
    arrayOfVariantOfDouble151[3] = 0.000000
    arrayOfVariantOfDouble151[4] = 1.000000
    arrayOfVariantOfDouble151[5] = 0.000000
    arrayOfVariantOfDouble151[6] = 0.000000
    arrayOfVariantOfDouble151[7] = 0.000000
    arrayOfVariantOfDouble151[8] = 1.000000
    arrayOfVariantOfDouble151[9] = 0.000000
    arrayOfVariantOfDouble151[10] = 7.439988
    arrayOfVariantOfDouble151[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble151)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble152[0] = 1.000000
    arrayOfVariantOfDouble152[1] = 0.000000
    arrayOfVariantOfDouble152[2] = 0.000000
    arrayOfVariantOfDouble152[3] = 0.000000
    arrayOfVariantOfDouble152[4] = 1.000000
    arrayOfVariantOfDouble152[5] = 0.000000
    arrayOfVariantOfDouble152[6] = 0.000000
    arrayOfVariantOfDouble152[7] = 0.000000
    arrayOfVariantOfDouble152[8] = 1.000000
    arrayOfVariantOfDouble152[9] = 0.000000
    arrayOfVariantOfDouble152[10] = 14.123819
    arrayOfVariantOfDouble152[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble152)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble153[0] = 1.000000
    arrayOfVariantOfDouble153[1] = 0.000000
    arrayOfVariantOfDouble153[2] = 0.000000
    arrayOfVariantOfDouble153[3] = 0.000000
    arrayOfVariantOfDouble153[4] = 1.000000
    arrayOfVariantOfDouble153[5] = 0.000000
    arrayOfVariantOfDouble153[6] = 0.000000
    arrayOfVariantOfDouble153[7] = 0.000000
    arrayOfVariantOfDouble153[8] = 1.000000
    arrayOfVariantOfDouble153[9] = 0.000000
    arrayOfVariantOfDouble153[10] = 9.659915
    arrayOfVariantOfDouble153[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble153)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble154[0] = 1.000000
    arrayOfVariantOfDouble154[1] = 0.000000
    arrayOfVariantOfDouble154[2] = 0.000000
    arrayOfVariantOfDouble154[3] = 0.000000
    arrayOfVariantOfDouble154[4] = 1.000000
    arrayOfVariantOfDouble154[5] = 0.000000
    arrayOfVariantOfDouble154[6] = 0.000000
    arrayOfVariantOfDouble154[7] = 0.000000
    arrayOfVariantOfDouble154[8] = 1.000000
    arrayOfVariantOfDouble154[9] = 0.000000
    arrayOfVariantOfDouble154[10] = 17.099851
    arrayOfVariantOfDouble154[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble154)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble155[0] = 1.000000
    arrayOfVariantOfDouble155[1] = 0.000000
    arrayOfVariantOfDouble155[2] = 0.000000
    arrayOfVariantOfDouble155[3] = 0.000000
    arrayOfVariantOfDouble155[4] = 1.000000
    arrayOfVariantOfDouble155[5] = 0.000000
    arrayOfVariantOfDouble155[6] = 0.000000
    arrayOfVariantOfDouble155[7] = 0.000000
    arrayOfVariantOfDouble155[8] = 1.000000
    arrayOfVariantOfDouble155[9] = 0.000000
    arrayOfVariantOfDouble155[10] = 5.951958
    arrayOfVariantOfDouble155[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble155)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble156[0] = 1.000000
    arrayOfVariantOfDouble156[1] = 0.000000
    arrayOfVariantOfDouble156[2] = 0.000000
    arrayOfVariantOfDouble156[3] = 0.000000
    arrayOfVariantOfDouble156[4] = 1.000000
    arrayOfVariantOfDouble156[5] = 0.000000
    arrayOfVariantOfDouble156[6] = 0.000000
    arrayOfVariantOfDouble156[7] = 0.000000
    arrayOfVariantOfDouble156[8] = 1.000000
    arrayOfVariantOfDouble156[9] = 0.000000
    arrayOfVariantOfDouble156[10] = 11.147900
    arrayOfVariantOfDouble156[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble156)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble157[0] = 1.000000
    arrayOfVariantOfDouble157[1] = 0.000000
    arrayOfVariantOfDouble157[2] = 0.000000
    arrayOfVariantOfDouble157[3] = 0.000000
    arrayOfVariantOfDouble157[4] = 1.000000
    arrayOfVariantOfDouble157[5] = 0.000000
    arrayOfVariantOfDouble157[6] = 0.000000
    arrayOfVariantOfDouble157[7] = 0.000000
    arrayOfVariantOfDouble157[8] = 1.000000
    arrayOfVariantOfDouble157[9] = 0.000000
    arrayOfVariantOfDouble157[10] = 14.123802
    arrayOfVariantOfDouble157[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble157)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble158[0] = 1.000000
    arrayOfVariantOfDouble158[1] = 0.000000
    arrayOfVariantOfDouble158[2] = 0.000000
    arrayOfVariantOfDouble158[3] = 0.000000
    arrayOfVariantOfDouble158[4] = 1.000000
    arrayOfVariantOfDouble158[5] = 0.000000
    arrayOfVariantOfDouble158[6] = 0.000000
    arrayOfVariantOfDouble158[7] = 0.000000
    arrayOfVariantOfDouble158[8] = 1.000000
    arrayOfVariantOfDouble158[9] = 0.000000
    arrayOfVariantOfDouble158[10] = 5.699968
    arrayOfVariantOfDouble158[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble158)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble159[0] = 1.000000
    arrayOfVariantOfDouble159[1] = 0.000000
    arrayOfVariantOfDouble159[2] = 0.000000
    arrayOfVariantOfDouble159[3] = 0.000000
    arrayOfVariantOfDouble159[4] = 1.000000
    arrayOfVariantOfDouble159[5] = 0.000000
    arrayOfVariantOfDouble159[6] = 0.000000
    arrayOfVariantOfDouble159[7] = 0.000000
    arrayOfVariantOfDouble159[8] = 1.000000
    arrayOfVariantOfDouble159[9] = 0.000000
    arrayOfVariantOfDouble159[10] = 8.675956
    arrayOfVariantOfDouble159[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble159)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble160[0] = 1.000000
    arrayOfVariantOfDouble160[1] = 0.000000
    arrayOfVariantOfDouble160[2] = 0.000000
    arrayOfVariantOfDouble160[3] = 0.000000
    arrayOfVariantOfDouble160[4] = 1.000000
    arrayOfVariantOfDouble160[5] = 0.000000
    arrayOfVariantOfDouble160[6] = 0.000000
    arrayOfVariantOfDouble160[7] = 0.000000
    arrayOfVariantOfDouble160[8] = 1.000000
    arrayOfVariantOfDouble160[9] = 0.000000
    arrayOfVariantOfDouble160[10] = 1.487979
    arrayOfVariantOfDouble160[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble160)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble161[0] = 1.000000
    arrayOfVariantOfDouble161[1] = 0.000000
    arrayOfVariantOfDouble161[2] = 0.000000
    arrayOfVariantOfDouble161[3] = 0.000000
    arrayOfVariantOfDouble161[4] = 1.000000
    arrayOfVariantOfDouble161[5] = 0.000000
    arrayOfVariantOfDouble161[6] = 0.000000
    arrayOfVariantOfDouble161[7] = 0.000000
    arrayOfVariantOfDouble161[8] = 1.000000
    arrayOfVariantOfDouble161[9] = 0.000000
    arrayOfVariantOfDouble161[10] = 2.723927
    arrayOfVariantOfDouble161[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble161)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble162[0] = 1.000000
    arrayOfVariantOfDouble162[1] = 0.000000
    arrayOfVariantOfDouble162[2] = 0.000000
    arrayOfVariantOfDouble162[3] = 0.000000
    arrayOfVariantOfDouble162[4] = 1.000000
    arrayOfVariantOfDouble162[5] = 0.000000
    arrayOfVariantOfDouble162[6] = 0.000000
    arrayOfVariantOfDouble162[7] = 0.000000
    arrayOfVariantOfDouble162[8] = 1.000000
    arrayOfVariantOfDouble162[9] = 0.000000
    arrayOfVariantOfDouble162[10] = 2.975988
    arrayOfVariantOfDouble162[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble162)
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomIn()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference2 = product1.CreateReferenceFromName('Product1/Part4.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.3;0:(Brp:(Sketch.3;6)));AtLeastOneNoSharedIncluded:(Brp:((Brp:(Pocket.2;2);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.2;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));Brp:(Pad.1;0:(Brp:(Sketch.1;7)))))))))))));Brp:((Brp:(Pad.3;1);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.2;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));Brp:(Pad.1;0:(Brp:(Sketch.1;10))))))))))))));Cf11:());Pad.5_ResultOUT;Z0;G3563))')
    reference3 = product1.CreateReferenceFromName('Product1/Part3.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;4)));None:();Cf11:());Pad.3_ResultOUT;Z0;G3563))')
    constraint2 = constraints1.AddBiEltCst(catCstTypeOn, reference2, reference3)
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference4 = product1.CreateReferenceFromName('Product1/Part4.1/!Selection_RSur:(Face:(Brp:((Brp:(Pocket.2;2);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.2;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));Brp:(Pad.1;0:(Brp:(Sketch.1;7)))))))))))));None:();Cf11:());Pad.5_ResultOUT;Z0;G3563)')
    reference5 = product1.CreateReferenceFromName('Product1/Part3.1/!Selection_RSur:(Face:(Brp:(Pad.1;1);None:();Cf11:());Pad.3_ResultOUT;Z0;G3563)')
    constraint3 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference4, reference5)
    product1.Update()
    constraints1 = product1.Connections('CATIAConstraints')
    reference3 = product1.CreateReferenceFromName('Product1/Part3.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;4)));None:();Cf11:());Pad.3_ResultOUT;Z0;G3563))')
    reference6 = product1.CreateReferenceFromName('Product1/Part1.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;3)));None:();Cf11:());Pad.2_ResultOUT;Z0;G3563))')
    constraint4 = constraints1.AddBiEltCst(catCstTypeOn, reference3, reference6)
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference7 = product1.CreateReferenceFromName('Product1/Part4.1/!Selection_RSur:(Face:(Brp:((Brp:(Pad.3;1);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.2;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));Brp:(Pad.1;0:(Brp:(Sketch.1;10)))))))))))));None:();Cf11:());Pad.5_ResultOUT;Z0;G3563)')
    reference8 = product1.CreateReferenceFromName('Product1/Part1.1/!Selection_RSur:(Face:(Brp:(Pad.2;2);None:();Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    constraint5 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference7, reference8)
    product1.Update()
    constraints1 = product1.Connections('CATIAConstraints')
    reference6 = product1.CreateReferenceFromName('Product1/Part1.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;3)));None:();Cf11:());Pad.2_ResultOUT;Z0;G3563))')
    reference9 = product1.CreateReferenceFromName('Product1/Part2.1/!Axis:(Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;3)));None:();Cf11:());Pocket.1_ResultOUT;Z0;G3563))')
    constraint6 = constraints1.AddBiEltCst(catCstTypeOn, reference6, reference9)
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference10 = product1.CreateReferenceFromName('Product1/Part4.1/!Selection_RSur:(Face:(Brp:((Brp:(Pad.3;2);Brp:(Pad.2;0:(Brp:(Sketch.2;(Brp:(Sketch.2_ProjectedGeomSet.1;(Brp:(FeatureRSUR.1;(Brp:(Pad.1;0:(Brp:(Sketch.1;10)));Brp:(Pad.1;0:(Brp:(Sketch.1;11)))))))))))));None:();Cf11:());Pad.5_ResultOUT;Z0;G3563)')
    reference11 = product1.CreateReferenceFromName('Product1/Part2.1/!Selection_RSur:(Face:(Brp:(Pad.1;1);None:();Cf11:());Pocket.1_ResultOUT;Z0;G3563)')
    constraint7 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference10, reference11)
    product1.Update()


    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    #hide a plane

    productDocument1 = CATIA.ActiveDocument
    productDocument1.SaveAs('C:\\%s\\knuckle_assembly.CATProduct' %(foldername))
        #C:\\Users\\l\\Downloads\\engine\\Product12.CATProduct')


    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''assembly end '''''''''''''''''''''''''''''''''''''''''''''''''''''#
'''
gw = 40
gl1 = 12
gl2 = 35
gl3 = 42
gl4 = 30
gB = 55
gt1 = 13
gt2 = 15
gt = 10
gb1 = 29
gb = 26
'''

def gib():
    CATIA.Visible = True
    '''
    gw = 40
    gl1 = 12
    gl2 = 35
    gl3 = 42
    gl4 = 30
    gB = 55
    gt1 = 13
    gt2 = 15
    gt = 10
    gb1 = 29
    gb = 26
    '''
    '''gf=float(input("transmitting force F(N)="))
    ts=float(input("tensile stress(N/mm2)="))
    ss=float(input("shear stress(N/mm2)="))'''
    '''messagebox.showerror("gf",gf)
    messagebox.showerror("ts",ts)
    messagebox.showerror("ss",ss)'''
    gibfoldername = str(gbox_4.get())
    #messagebox.showerror("name",gibfoldername)
    



    #making folder for storing files using input folder name
    mainpath="C:/"
    path=os.path.join(mainpath,gibfoldername)
    os.mkdir(path)

    gh=((gf / ts)**(1/2))     #overall height of fork end
    gh = round(gh)

    gw = gh

    gt = (0.3 * gh)              #thickness of cotter
    gt = round(gt)

    gB = (gf / (2 * gt * ss))         #length of the hole
    gB = round(gB)

    gb1 = (0.55 * gB)           #width of the gib
    gb = (0.45 * gB)            #width of the cotter

    gt1=(gf / (2  *(gh  -gt) * ts))    #thickness of fork end sleeve
    gt1 = round(gt1)

    gl3 = ( gf / (4 * gt1 * ss))        #length of strap end
    gl3 = round(gl3)

    gl2 = (gf / (2 * gh * ss))         #length of rod end
    gl2 = round(gl2)

    gl1 = gt                     #length of gib extrude portion

    gl4 = ((2/3) * gh)             #length between fork end and l2
    gl4 = round(gl4)

    gt2 = (1.3 * gt)                 #thickness of gib extrude portion
    gt2 = round(gt2)
    gLG=(gh+(2*(gt1+gt2)))      #over all length of gib

    gLG=round(gLG)

    gLC=(4*gh)                   #over all length of cotter

    gLC=round(gLC)
    


    gibloc = ("C:\\%s\\Dimensions.txt" %(gibfoldername))
    gibpdf = open(gibloc,"w+")

    gibpdf.write("Thickness of cotter (t) : %s mm \n" %(gt))
    gibpdf.write("Width of cotter (b) : %s mm \n" %(gb))
    gibpdf.write("Width of gib (b1): %s mm \n" %(gb1))
    gibpdf.write("Thickness of fork end sleeve (t1) : %s mm \n" %(gt1))
    gibpdf.write("Length of strap end (l3) : %s mm \n" %(gl3))
    gibpdf.write("Length of rod end (l2): %s mm \n" %(gl2))
    gibpdf.write("Length of gib extrude portion (l1): %s mm \n" %(gl1))
    gibpdf.write("Thickness of gib extrude portion (t2): %s mm \n" %(gt2))
    gibpdf.write("Overall gib length : %s mm \n" %(gLG))
    gibpdf.write("Cotter length : %s mm \n" %(gLC))
    gibpdf.close()


    

    
    #..............................................................fork end start.................................................................
    
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble3 = [0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
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
    point2D1 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D1.ReportName = 3
    point2D2 = factory2D1.CreatePoint(0.000000, (gw / 2))
    point2D2.ReportName = 4
    line2D3 = factory2D1.CreateLine(0.000000, 0.000000, 0.000000, (gw / 2))
    line2D3.ReportName = 5
    line2D3.StartPoint = point2D1
    line2D3.EndPoint = point2D2
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(point2D1)
    reference3 = part1.CreateReferenceFromObject(line2D2)
    #constraint1 = constraints1.AddBiEltCst(catCstTypeDistance, reference2, reference3)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 0.000000
    reference4 = part1.CreateReferenceFromObject(point2D1)
    reference5 = part1.CreateReferenceFromObject(line2D1)
    #constraint2 = constraints1.AddBiEltCst(catCstTypeDistance, reference4, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    #length2 = constraint2.Dimension
    #length2.Value = 0.000000
    reference6 = part1.CreateReferenceFromObject(point2D2)
    reference7 = part1.CreateReferenceFromObject(line2D2)
    #constraint3 = constraints1.AddBiEltCst(catCstTypeDistance, reference6, reference7)
    #constraint3.Mode = catCstModeDrivingDimension
    #length3 = constraint3.Dimension
    #length3.Value = 0.000000
    reference8 = part1.CreateReferenceFromObject(point2D2)
    reference9 = part1.CreateReferenceFromObject(line2D1)
    #constraint4 = constraints1.AddBiEltCst(catCstTypeDistance, reference8, reference9)
    #constraint4.Mode = catCstModeDrivingDimension
    #length4 = constraint4.Dimension
    #length4.Value = 20.000000
    point2D3 = factory2D1.CreatePoint(0.000000, (gw / 2))
    point2D3.ReportName = 6
    point2D4 = factory2D1.CreatePoint((gl3 + gB + gl2), (gw /2))
    point2D4.ReportName = 7
    line2D4 = factory2D1.CreateLine(0.000000, (gw / 2), (gl3 + gB + gl2), (gw / 2))
    line2D4.ReportName = 8
    line2D4.StartPoint = point2D3
    line2D4.EndPoint = point2D4
    reference10 = part1.CreateReferenceFromObject(point2D3)
    reference11 = part1.CreateReferenceFromObject(line2D2)
    #constraint5 = constraints1.AddBiEltCst(catCstTypeDistance, reference10, reference11)
    #constraint5.Mode = catCstModeDrivingDimension
    #length5 = constraint5.Dimension
    #length5.Value = 0.000000
    reference12 = part1.CreateReferenceFromObject(point2D3)
    reference13 = part1.CreateReferenceFromObject(line2D1)
    #constraint6 = constraints1.AddBiEltCst(catCstTypeDistance, reference12, reference13)
    #constraint6.Mode = catCstModeDrivingDimension
    #length6 = constraint6.Dimension
    #length6.Value = 20.000000
    reference14 = part1.CreateReferenceFromObject(point2D4)
    reference15 = part1.CreateReferenceFromObject(line2D2)
    #constraint7 = constraints1.AddBiEltCst(catCstTypeDistance, reference14, reference15)
    #constraint7.Mode = catCstModeDrivingDimension
    #length7 = constraint7.Dimension
    #length7.Value = 132.000000
    reference16 = part1.CreateReferenceFromObject(point2D4)
    reference17 = part1.CreateReferenceFromObject(line2D1)
    #constraint8 = constraints1.AddBiEltCst(catCstTypeDistance, reference16, reference17)
    #constraint8.Mode = catCstModeDrivingDimension
    #length8 = constraint8.Dimension
    #length8.Value = 20.000000
    point2D5 = factory2D1.CreatePoint((gl3 + gB + gl2), (gw / 2))
    point2D5.ReportName = 9
    point2D6 = factory2D1.CreatePoint((gl3 + gB + gl2), (((gw / 2) + gt1)))
    point2D6.ReportName = 10
    line2D5 = factory2D1.CreateLine((gl3 + gB + gl2), (gw / 2), (gl3 + gB + gl2), (((gw / 2) + gt1)))
    line2D5.ReportName = 11
    line2D5.StartPoint = point2D5
    line2D5.EndPoint = point2D6
    reference18 = part1.CreateReferenceFromObject(point2D5)
    reference19 = part1.CreateReferenceFromObject(line2D2)
    #constraint9 = constraints1.AddBiEltCst(catCstTypeDistance, reference18, reference19)
    #constraint9.Mode = catCstModeDrivingDimension
    #length9 = constraint9.Dimension
    #length9.Value = 132.000000
    reference20 = part1.CreateReferenceFromObject(point2D5)
    reference21 = part1.CreateReferenceFromObject(line2D1)
    #constraint10 = constraints1.AddBiEltCst(catCstTypeDistance, reference20, reference21)
    #constraint10.Mode = catCstModeDrivingDimension
    #length10 = constraint10.Dimension
    #length10.Value = 20.000000
    reference22 = part1.CreateReferenceFromObject(point2D6)
    reference23 = part1.CreateReferenceFromObject(line2D2)
    #constraint11 = constraints1.AddBiEltCst(catCstTypeDistance, reference22, reference23)
    #constraint11.Mode = catCstModeDrivingDimension
    #length11 = constraint11.Dimension
    #length11.Value = 132.000000
    reference24 = part1.CreateReferenceFromObject(point2D6)
    reference25 = part1.CreateReferenceFromObject(line2D1)
    #constraint12 = constraints1.AddBiEltCst(catCstTypeDistance, reference24, reference25)
    #constraint12.Mode = catCstModeDrivingDimension
    #length12 = constraint12.Dimension
    #length12.Value = 33.000000
    point2D7 = factory2D1.CreatePoint((gl3 + gB + gl2), (((gw / 2) + gt1)))
    point2D7.ReportName = 12
    point2D8 = factory2D1.CreatePoint(- gl4, (((gw / 2) + gt1)))
    point2D8.ReportName = 13
    line2D6 = factory2D1.CreateLine((gl3 + gB + gl2), (((gw / 2) + gt1)), - gl4, (((gw / 2) + gt1)))
    line2D6.ReportName = 14
    line2D6.StartPoint = point2D7
    line2D6.EndPoint = point2D8
    reference26 = part1.CreateReferenceFromObject(point2D7)
    reference27 = part1.CreateReferenceFromObject(line2D2)
    #constraint13 = constraints1.AddBiEltCst(catCstTypeDistance, reference26, reference27)
    #constraint13.Mode = catCstModeDrivingDimension
    #length13 = constraint13.Dimension
    #length13.Value = 132.000000
    reference28 = part1.CreateReferenceFromObject(point2D7)
    reference29 = part1.CreateReferenceFromObject(line2D1)
    #constraint14 = constraints1.AddBiEltCst(catCstTypeDistance, reference28, reference29)
    #constraint14.Mode = catCstModeDrivingDimension
    #length14 = constraint14.Dimension
    #length14.Value = 33.000000
    reference30 = part1.CreateReferenceFromObject(point2D8)
    reference31 = part1.CreateReferenceFromObject(line2D2)
    #constraint15 = constraints1.AddBiEltCst(catCstTypeDistance, reference30, reference31)
    #constraint15.Mode = catCstModeDrivingDimension
    #length15 = constraint15.Dimension
    #length15.Value = 30.000000
    reference32 = part1.CreateReferenceFromObject(point2D8)
    reference33 = part1.CreateReferenceFromObject(line2D1)
    #constraint16 = constraints1.AddBiEltCst(catCstTypeDistance, reference32, reference33)
    #constraint16.Mode = catCstModeDrivingDimension
    #length16 = constraint16.Dimension
    #length16.Value = 33.000000
    point2D9 = factory2D1.CreatePoint(- gl4, - (((gw / 2) + gt1)))
    point2D9.ReportName = 15
    point2D10 = factory2D1.CreatePoint(- gl4, (((gw / 2) + gt1)))
    point2D10.ReportName = 16
    line2D7 = factory2D1.CreateLine(- gl4, - (((gw / 2) + gt1)), - gl4, (((gw / 2) + gt1)))
    line2D7.ReportName = 17
    line2D7.StartPoint = point2D9
    line2D7.EndPoint = point2D10
    reference34 = part1.CreateReferenceFromObject(point2D9)
    reference35 = part1.CreateReferenceFromObject(line2D2)
    #constraint17 = constraints1.AddBiEltCst(catCstTypeDistance, reference34, reference35)
    #constraint17.Mode = catCstModeDrivingDimension
    #length17 = constraint17.Dimension
    #length17.Value = 30.000000
    reference36 = part1.CreateReferenceFromObject(point2D9)
    reference37 = part1.CreateReferenceFromObject(line2D1)
    #constraint18 = constraints1.AddBiEltCst(catCstTypeDistance, reference36, reference37)
    #constraint18.Mode = catCstModeDrivingDimension
    #length18 = constraint18.Dimension
    #length18.Value = 33.000000
    reference38 = part1.CreateReferenceFromObject(point2D10)
    reference39 = part1.CreateReferenceFromObject(line2D2)
    #constraint19 = constraints1.AddBiEltCst(catCstTypeDistance, reference38, reference39)
    #constraint19.Mode = catCstModeDrivingDimension
    #length19 = constraint19.Dimension
    #length19.Value = 30.000000
    reference40 = part1.CreateReferenceFromObject(point2D10)
    reference41 = part1.CreateReferenceFromObject(line2D1)
    #constraint20 = constraints1.AddBiEltCst(catCstTypeDistance, reference40, reference41)
    #constraint20.Mode = catCstModeDrivingDimension
    #length20 = constraint20.Dimension
    #length20.Value = 33.000000
    point2D11 = factory2D1.CreatePoint(- gl4, - (((gw / 2) + gt1)))
    point2D11.ReportName = 18
    point2D12 = factory2D1.CreatePoint((gl3 + gB + gl2), - (((gw / 2) + gt1)))
    point2D12.ReportName = 19
    line2D8 = factory2D1.CreateLine(- gl4, - (((gw / 2) + gt1)), (gl3 + gB + gl2), - (((gw / 2) + gt1)))
    line2D8.ReportName = 20
    line2D8.StartPoint = point2D11
    line2D8.EndPoint = point2D12
    reference42 = part1.CreateReferenceFromObject(point2D11)
    reference43 = part1.CreateReferenceFromObject(line2D2)
    #constraint21 = constraints1.AddBiEltCst(catCstTypeDistance, reference42, reference43)
    #constraint21.Mode = catCstModeDrivingDimension
    #length21 = constraint21.Dimension
    #length21.Value = 30.000000
    reference44 = part1.CreateReferenceFromObject(point2D11)
    reference45 = part1.CreateReferenceFromObject(line2D1)
    #constraint22 = constraints1.AddBiEltCst(catCstTypeDistance, reference44, reference45)
    #constraint22.Mode = catCstModeDrivingDimension
    #length22 = constraint22.Dimension
    #length22.Value = 33.000000
    reference46 = part1.CreateReferenceFromObject(point2D12)
    reference47 = part1.CreateReferenceFromObject(line2D2)
    #constraint23 = constraints1.AddBiEltCst(catCstTypeDistance, reference46, reference47)
    #constraint23.Mode = catCstModeDrivingDimension
    #length23 = constraint23.Dimension
    #length23.Value = 132.000000
    reference48 = part1.CreateReferenceFromObject(point2D12)
    reference49 = part1.CreateReferenceFromObject(line2D1)
    #constraint24 = constraints1.AddBiEltCst(catCstTypeDistance, reference48, reference49)
    #constraint24.Mode = catCstModeDrivingDimension
    #length24 = constraint24.Dimension
    #length24.Value = 33.000000
    point2D13 = factory2D1.CreatePoint((gl3 + gB + gl2), - (((gw / 2) + gt1)))
    point2D13.ReportName = 21
    point2D14 = factory2D1.CreatePoint((gl3 + gB + gl2), - (gw / 2))
    point2D14.ReportName = 22
    line2D9 = factory2D1.CreateLine((gl3 + gB + gl2), - (((gw / 2) + gt1)), (gl3 + gB + gl2), - (gw / 2))
    line2D9.ReportName = 23
    line2D9.StartPoint = point2D13
    line2D9.EndPoint = point2D14
    reference50 = part1.CreateReferenceFromObject(point2D13)
    reference51 = part1.CreateReferenceFromObject(line2D2)
    #constraint25 = constraints1.AddBiEltCst(catCstTypeDistance, reference50, reference51)
    #constraint25.Mode = catCstModeDrivingDimension
    #length25 = constraint25.Dimension
    #length25.Value = 132.000000
    reference52 = part1.CreateReferenceFromObject(point2D13)
    reference53 = part1.CreateReferenceFromObject(line2D1)
    #constraint26 = constraints1.AddBiEltCst(catCstTypeDistance, reference52, reference53)
    #constraint26.Mode = catCstModeDrivingDimension
    #length26 = constraint26.Dimension
    #length26.Value = 33.000000
    reference54 = part1.CreateReferenceFromObject(point2D14)
    reference55 = part1.CreateReferenceFromObject(line2D2)
    #constraint27 = constraints1.AddBiEltCst(catCstTypeDistance, reference54, reference55)
    #constraint27.Mode = catCstModeDrivingDimension
    #length27 = constraint27.Dimension
    #length27.Value = 132.000000
    reference56 = part1.CreateReferenceFromObject(point2D14)
    reference57 = part1.CreateReferenceFromObject(line2D1)
    #constraint28 = constraints1.AddBiEltCst(catCstTypeDistance, reference56, reference57)
    #constraint28.Mode = catCstModeDrivingDimension
    #length28 = constraint28.Dimension
    #length28.Value = 20.000000
    point2D15 = factory2D1.CreatePoint((gl3 + gB + gl2), - (gw / 2))
    point2D15.ReportName = 24
    point2D16 = factory2D1.CreatePoint(0.000000, - (gw / 2))
    point2D16.ReportName = 25
    line2D10 = factory2D1.CreateLine((gl3 + gB + gl2), - (gw / 2), 0.000000, - (gw / 2))
    line2D10.ReportName = 26
    line2D10.StartPoint = point2D15
    line2D10.EndPoint = point2D16
    reference58 = part1.CreateReferenceFromObject(point2D15)
    reference59 = part1.CreateReferenceFromObject(line2D2)
    #constraint29 = constraints1.AddBiEltCst(catCstTypeDistance, reference58, reference59)
    #constraint29.Mode = catCstModeDrivingDimension
    #length29 = constraint29.Dimension
    #length29.Value = 132.000000
    reference60 = part1.CreateReferenceFromObject(point2D15)
    reference61 = part1.CreateReferenceFromObject(line2D1)
    #constraint30 = constraints1.AddBiEltCst(catCstTypeDistance, reference60, reference61)
    #constraint30.Mode = catCstModeDrivingDimension
    #length30 = constraint30.Dimension
    #length30.Value = 20.000000
    reference62 = part1.CreateReferenceFromObject(point2D16)
    reference63 = part1.CreateReferenceFromObject(line2D1)
    #constraint31 = constraints1.AddBiEltCst(catCstTypeDistance, reference62, reference63)
    #constraint31.Mode = catCstModeDrivingDimension
    #length31 = constraint31.Dimension
    #length31.Value = 20.000000
    reference64 = part1.CreateReferenceFromObject(point2D16)
    reference65 = part1.CreateReferenceFromObject(line2D2)
    #constraint32 = constraints1.AddBiEltCst(catCstTypeDistance, reference64, reference65)
    #constraint32.Mode = catCstModeDrivingDimension
    #length32 = constraint32.Dimension
    #length32.Value = 0.000000
    point2D17 = factory2D1.CreatePoint(0.000000, - (gw / 2))
    point2D17.ReportName = 27
    point2D18 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D18.ReportName = 28
    line2D11 = factory2D1.CreateLine(0.000000, - (gw / 2), 0.000000, 0.000000)
    line2D11.ReportName = 29
    line2D11.StartPoint = point2D17
    line2D11.EndPoint = point2D18
    reference66 = part1.CreateReferenceFromObject(point2D17)
    reference67 = part1.CreateReferenceFromObject(line2D2)
    #constraint33 = constraints1.AddBiEltCst(catCstTypeDistance, reference66, reference67)
    #constraint33.Mode = catCstModeDrivingDimension
    #length33 = constraint33.Dimension
    #length33.Value = 0.000000
    reference68 = part1.CreateReferenceFromObject(point2D17)
    reference69 = part1.CreateReferenceFromObject(line2D1)
    #constraint34 = constraints1.AddBiEltCst(catCstTypeDistance, reference68, reference69)
    #constraint34.Mode = catCstModeDrivingDimension
    #length34 = constraint34.Dimension
    #length34.Value = 20.000000
    reference70 = part1.CreateReferenceFromObject(point2D18)
    reference71 = part1.CreateReferenceFromObject(line2D2)
    #constraint35 = constraints1.AddBiEltCst(catCstTypeDistance, reference70, reference71)
    #constraint35.Mode = catCstModeDrivingDimension
    #length35 = constraint35.Dimension
    #length35.Value = 0.000000
    reference72 = part1.CreateReferenceFromObject(point2D18)
    reference73 = part1.CreateReferenceFromObject(line2D1)
    #constraint36 = constraints1.AddBiEltCst(catCstTypeDistance, reference72, reference73)
    #constraint36.Mode = catCstModeDrivingDimension
    #length36 = constraint36.Dimension
    #length36.Value = 0.000000
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    reference74 = part1.CreateReferenceFromName('')
    pad1 = shapeFactory1.AddNewPadFromRef(reference74, (gw/2))
    reference75 = part1.CreateReferenceFromObject(sketch1)
    pad1.SetProfileElement(reference75)
    pad1.IsSymmetric = True
    part1.Update()
    sketches2 = body1.Sketches
    reference76 = originElements1.PlaneXY
    sketch2 = sketches2.Add(reference76)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = 1.000000
    arrayOfVariantOfDouble2[4] = 0.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = 1.000000
    arrayOfVariantOfDouble2[8] = 0.000000
    sketch2.SetAbsoluteAxisData(arrayOfVariantOfDouble2)
    part1.InWorkObject = sketch2
    factory2D2 = sketch2.OpenEdition()
    geometricElements2 = sketch2.GeometricElements
    axis2D2 = geometricElements2.Item('AbsoluteAxis')
    line2D12 = axis2D2.GetItem('HDirection')
    line2D12.ReportName = 1
    line2D13 = axis2D2.GetItem('VDirection')
    line2D13.ReportName = 2
    point2D19 = factory2D2.CreatePoint(- gl2, (gt / 2))
    point2D19.ReportName = 3
    point2D20 = factory2D2.CreatePoint(- (gl2 + gB), (gt / 2))
    point2D20.ReportName = 4
    line2D14 = factory2D2.CreateLine(- gl2, (gt / 2), - (gl2 + gB), (gt / 2))
    line2D14.ReportName = 5
    line2D14.StartPoint = point2D19
    line2D14.EndPoint = point2D20
    constraints2 = sketch2.Constraints
    reference77 = part1.CreateReferenceFromObject(point2D19)
    reference78 = part1.CreateReferenceFromObject(line2D13)
    #constraint37 = constraints2.AddBiEltCst(catCstTypeDistance, reference77, reference78)
    #constraint37.Mode = catCstModeDrivingDimension
    #length37 = constraint37.Dimension
    #length37.Value = 35.000000
    reference79 = part1.CreateReferenceFromObject(point2D19)
    reference80 = part1.CreateReferenceFromObject(line2D12)
    #constraint38 = constraints2.AddBiEltCst(catCstTypeDistance, reference79, reference80)
    #constraint38.Mode = catCstModeDrivingDimension
    #length38 = constraint38.Dimension
    #length38.Value = 5.000000
    reference81 = part1.CreateReferenceFromObject(point2D20)
    reference82 = part1.CreateReferenceFromObject(line2D13)
    #constraint39 = constraints2.AddBiEltCst(catCstTypeDistance, reference81, reference82)
    #constraint39.Mode = catCstModeDrivingDimension
    #length39 = constraint39.Dimension
    #length39.Value = 90.000000
    reference83 = part1.CreateReferenceFromObject(point2D20)
    reference84 = part1.CreateReferenceFromObject(line2D12)
    #constraint40 = constraints2.AddBiEltCst(catCstTypeDistance, reference83, reference84)
    #constraint40.Mode = catCstModeDrivingDimension
    #length40 = constraint40.Dimension
    #length40.Value = 5.000000
    point2D21 = factory2D2.CreatePoint(- (gl2 + gB), (gt / 2))
    point2D21.ReportName = 6
    point2D22 = factory2D2.CreatePoint(- (gl2 + gB), - (gt / 2))
    point2D22.ReportName = 7
    line2D15 = factory2D2.CreateLine(- (gl2 + gB), (gt / 2), - (gl2 + gB), - (gt / 2))
    line2D15.ReportName = 8
    line2D15.StartPoint = point2D21
    line2D15.EndPoint = point2D22
    reference85 = part1.CreateReferenceFromObject(point2D21)
    reference86 = part1.CreateReferenceFromObject(line2D13)
    #constraint41 = constraints2.AddBiEltCst(catCstTypeDistance, reference85, reference86)
    #constraint41.Mode = catCstModeDrivingDimension
    #length41 = constraint41.Dimension
    #length41.Value = 90.000000
    reference87 = part1.CreateReferenceFromObject(point2D21)
    reference88 = part1.CreateReferenceFromObject(line2D12)
    #constraint42 = constraints2.AddBiEltCst(catCstTypeDistance, reference87, reference88)
    #constraint42.Mode = catCstModeDrivingDimension
    #length42 = constraint42.Dimension
    #length42.Value = 5.000000
    reference89 = part1.CreateReferenceFromObject(point2D22)
    reference90 = part1.CreateReferenceFromObject(line2D13)
    #constraint43 = constraints2.AddBiEltCst(catCstTypeDistance, reference89, reference90)
    #constraint43.Mode = catCstModeDrivingDimension
    #length43 = constraint43.Dimension
    #length43.Value = 90.000000
    reference91 = part1.CreateReferenceFromObject(point2D22)
    reference92 = part1.CreateReferenceFromObject(line2D12)
    #constraint44 = constraints2.AddBiEltCst(catCstTypeDistance, reference91, reference92)
    #constraint44.Mode = catCstModeDrivingDimension
    #length44 = constraint44.Dimension
    #length44.Value = 5.000000
    point2D23 = factory2D2.CreatePoint(- (gl2 + gB), - (gt / 2))
    point2D23.ReportName = 9
    point2D24 = factory2D2.CreatePoint(- gl2, - (gt / 2))
    point2D24.ReportName = 10
    line2D16 = factory2D2.CreateLine(- (gl2 + gB), - (gt / 2), - gl2, - (gt / 2))
    line2D16.ReportName = 11
    line2D16.StartPoint = point2D23
    line2D16.EndPoint = point2D24
    reference93 = part1.CreateReferenceFromObject(point2D23)
    reference94 = part1.CreateReferenceFromObject(line2D13)
    #constraint45 = constraints2.AddBiEltCst(catCstTypeDistance, reference93, reference94)
    #constraint45.Mode = catCstModeDrivingDimension
    #length45 = constraint45.Dimension
    #length45.Value = 90.000000
    reference95 = part1.CreateReferenceFromObject(point2D23)
    reference96 = part1.CreateReferenceFromObject(line2D12)
    #constraint46 = constraints2.AddBiEltCst(catCstTypeDistance, reference95, reference96)
    #constraint46.Mode = catCstModeDrivingDimension
    #length46 = constraint46.Dimension
    #length46.Value = 5.000000
    reference97 = part1.CreateReferenceFromObject(point2D24)
    reference98 = part1.CreateReferenceFromObject(line2D13)
    #constraint47 = constraints2.AddBiEltCst(catCstTypeDistance, reference97, reference98)
    #constraint47.Mode = catCstModeDrivingDimension
    #length47 = constraint47.Dimension
    #length47.Value = 35.000000
    reference99 = part1.CreateReferenceFromObject(point2D24)
    reference100 = part1.CreateReferenceFromObject(line2D12)
    #constraint48 = constraints2.AddBiEltCst(catCstTypeDistance, reference99, reference100)
    #constraint48.Mode = catCstModeDrivingDimension
    #length48 = constraint48.Dimension
    #length48.Value = 5.000000
    point2D25 = factory2D2.CreatePoint(- gl2, - (gt / 2))
    point2D25.ReportName = 12
    point2D26 = factory2D2.CreatePoint(- gl2, (gt / 2))
    point2D26.ReportName = 13
    line2D17 = factory2D2.CreateLine(- gl2, - (gt / 2), - gl2, (gt / 2))
    line2D17.ReportName = 14
    line2D17.StartPoint = point2D25
    line2D17.EndPoint = point2D26
    reference101 = part1.CreateReferenceFromObject(point2D25)
    reference102 = part1.CreateReferenceFromObject(line2D13)
    #constraint49 = constraints2.AddBiEltCst(catCstTypeDistance, reference101, reference102)
    #constraint49.Mode = catCstModeDrivingDimension
    #length49 = constraint49.Dimension
    #length49.Value = 35.000000
    reference103 = part1.CreateReferenceFromObject(point2D25)
    reference104 = part1.CreateReferenceFromObject(line2D12)
    #constraint50 = constraints2.AddBiEltCst(catCstTypeDistance, reference103, reference104)
    #constraint50.Mode = catCstModeDrivingDimension
    #length50 = constraint50.Dimension
    #length50.Value = 5.000000
    reference105 = part1.CreateReferenceFromObject(point2D26)
    reference106 = part1.CreateReferenceFromObject(line2D13)
    #constraint51 = constraints2.AddBiEltCst(catCstTypeDistance, reference105, reference106)
    #constraint51.Mode = catCstModeDrivingDimension
    #length51 = constraint51.Dimension
    #length51.Value = 35.000000
    reference107 = part1.CreateReferenceFromObject(point2D26)
    reference108 = part1.CreateReferenceFromObject(line2D12)
    #constraint52 = constraints2.AddBiEltCst(catCstTypeDistance, reference107, reference108)
    #constraint52.Mode = catCstModeDrivingDimension
    #length52 = constraint52.Dimension
    #length52.Value = 5.000000
    sketch2.CloseEdition()
    part1.InWorkObject = sketch2
    part1.Update()
    reference109 = part1.CreateReferenceFromName('')
    pocket1 = shapeFactory1.AddNewPocketFromRef(reference109, ((gw / 2) + gt1))
    reference110 = part1.CreateReferenceFromObject(sketch2)
    pocket1.SetProfileElement(reference110)
    pocket1.IsSymmetric = True
    limit1 = pocket1.FirstLimit
    length53 = limit1.Dimension
    length53.Value = ((gw / 2) + gt1)
    part1.Update()
    reference111 = originElements1.PlaneYZ
    sketch3 = sketches2.Add(reference111)
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
    line2D18 = axis2D3.GetItem('HDirection')
    line2D18.ReportName = 1
    line2D19 = axis2D3.GetItem('VDirection')
    line2D19.ReportName = 2
    point2D27 = factory2D3.CreatePoint(- (gw / 2), - (gw / 2))
    point2D27.ReportName = 3
    point2D28 = factory2D3.CreatePoint((gw / 2), - (gw / 2))
    point2D28.ReportName = 4
    line2D20 = factory2D3.CreateLine(- (gw / 2), - (gw / 2), (gw / 2), - (gw / 2))
    line2D20.ReportName = 5
    line2D20.StartPoint = point2D27
    line2D20.EndPoint = point2D28
    constraints3 = sketch3.Constraints
    reference112 = part1.CreateReferenceFromObject(point2D27)
    reference113 = part1.CreateReferenceFromObject(line2D19)
    #constraint53 = constraints3.AddBiEltCst(catCstTypeDistance, reference112, reference113)
    #constraint53.Mode = catCstModeDrivingDimension
    #length54 = constraint53.Dimension
    #length54.Value = 20.000000
    reference114 = part1.CreateReferenceFromObject(point2D27)
    reference115 = part1.CreateReferenceFromObject(line2D18)
    #constraint54 = constraints3.AddBiEltCst(catCstTypeDistance, reference114, reference115)
    #constraint54.Mode = catCstModeDrivingDimension
    #length55 = constraint54.Dimension
    #length55.Value = 20.000000
    reference116 = part1.CreateReferenceFromObject(point2D28)
    reference117 = part1.CreateReferenceFromObject(line2D19)
    #constraint55 = constraints3.AddBiEltCst(catCstTypeDistance, reference116, reference117)
    #constraint55.Mode = catCstModeDrivingDimension
    #length56 = constraint55.Dimension
    #length56.Value = 20.000000
    reference118 = part1.CreateReferenceFromObject(point2D28)
    reference119 = part1.CreateReferenceFromObject(line2D18)
    #constraint56 = constraints3.AddBiEltCst(catCstTypeDistance, reference118, reference119)
    #constraint56.Mode = catCstModeDrivingDimension
    #length57 = constraint56.Dimension
    #length57.Value = 20.000000
    point2D29 = factory2D3.CreatePoint((gw / 2), - (gw / 2))
    point2D29.ReportName = 6
    point2D30 = factory2D3.CreatePoint((gw / 2), (gw / 2))
    point2D30.ReportName = 7
    line2D21 = factory2D3.CreateLine((gw / 2), - (gw / 2), (gw / 2), (gw / 2))
    line2D21.ReportName = 8
    line2D21.StartPoint = point2D29
    line2D21.EndPoint = point2D30
    reference120 = part1.CreateReferenceFromObject(point2D29)
    reference121 = part1.CreateReferenceFromObject(line2D19)
    #constraint57 = constraints3.AddBiEltCst(catCstTypeDistance, reference120, reference121)
    #constraint57.Mode = catCstModeDrivingDimension
    #length58 = constraint57.Dimension
    #length58.Value = 20.000000
    reference122 = part1.CreateReferenceFromObject(point2D29)
    reference123 = part1.CreateReferenceFromObject(line2D18)
    #constraint58 = constraints3.AddBiEltCst(catCstTypeDistance, reference122, reference123)
    #constraint58.Mode = catCstModeDrivingDimension
    #length59 = constraint58.Dimension
    #length59.Value = 20.000000
    reference124 = part1.CreateReferenceFromObject(point2D30)
    reference125 = part1.CreateReferenceFromObject(line2D19)
    #constraint59 = constraints3.AddBiEltCst(catCstTypeDistance, reference124, reference125)
    #constraint59.Mode = catCstModeDrivingDimension
    #length60 = constraint59.Dimension
    #length60.Value = 20.000000
    reference126 = part1.CreateReferenceFromObject(point2D30)
    reference127 = part1.CreateReferenceFromObject(line2D18)
    #constraint60 = constraints3.AddBiEltCst(catCstTypeDistance, reference126, reference127)
    #constraint60.Mode = catCstModeDrivingDimension
    #length61 = constraint60.Dimension
    #length61.Value = 20.000000
    point2D31 = factory2D3.CreatePoint((gw / 2), (gw / 2))
    point2D31.ReportName = 9
    point2D32 = factory2D3.CreatePoint(- (gw / 2), (gw / 2))
    point2D32.ReportName = 10
    line2D22 = factory2D3.CreateLine((gw / 2), (gw / 2), - (gw / 2), (gw / 2))
    line2D22.ReportName = 11
    line2D22.StartPoint = point2D31
    line2D22.EndPoint = point2D32
    reference128 = part1.CreateReferenceFromObject(point2D31)
    reference129 = part1.CreateReferenceFromObject(line2D19)
    #constraint61 = constraints3.AddBiEltCst(catCstTypeDistance, reference128, reference129)
    #constraint61.Mode = catCstModeDrivingDimension
    #length62 = constraint61.Dimension
    #length62.Value = 20.000000
    reference130 = part1.CreateReferenceFromObject(point2D31)
    reference131 = part1.CreateReferenceFromObject(line2D18)
    #constraint62 = constraints3.AddBiEltCst(catCstTypeDistance, reference130, reference131)
    #constraint62.Mode = catCstModeDrivingDimension
    #length63 = constraint62.Dimension
    #length63.Value = 20.000000
    reference132 = part1.CreateReferenceFromObject(point2D32)
    reference133 = part1.CreateReferenceFromObject(line2D19)
    #constraint63 = constraints3.AddBiEltCst(catCstTypeDistance, reference132, reference133)
    #constraint63.Mode = catCstModeDrivingDimension
    #length64 = constraint63.Dimension
    #length64.Value = 20.000000
    reference134 = part1.CreateReferenceFromObject(point2D32)
    reference135 = part1.CreateReferenceFromObject(line2D18)
    #constraint64 = constraints3.AddBiEltCst(catCstTypeDistance, reference134, reference135)
    #constraint64.Mode = catCstModeDrivingDimension
    #length65 = constraint64.Dimension
    #length65.Value = 20.000000
    point2D33 = factory2D3.CreatePoint(- (gw / 2), (gw / 2))
    point2D33.ReportName = 12
    point2D34 = factory2D3.CreatePoint(- (gw / 2), - (gw / 2))
    point2D34.ReportName = 13
    line2D23 = factory2D3.CreateLine(- (gw / 2), (gw / 2), - (gw / 2), - (gw / 2))
    line2D23.ReportName = 14
    line2D23.StartPoint = point2D33
    line2D23.EndPoint = point2D34
    reference136 = part1.CreateReferenceFromObject(point2D33)
    reference137 = part1.CreateReferenceFromObject(line2D19)
    #constraint65 = constraints3.AddBiEltCst(catCstTypeDistance, reference136, reference137)
    #constraint65.Mode = catCstModeDrivingDimension
    #length66 = constraint65.Dimension
    #length66.Value = 20.000000
    reference138 = part1.CreateReferenceFromObject(point2D33)
    reference139 = part1.CreateReferenceFromObject(line2D18)
    #constraint66 = constraints3.AddBiEltCst(catCstTypeDistance, reference138, reference139)
    #constraint66.Mode = catCstModeDrivingDimension
    #length67 = constraint66.Dimension
    #length67.Value = 20.000000
    reference140 = part1.CreateReferenceFromObject(point2D34)
    reference141 = part1.CreateReferenceFromObject(line2D19)
    #constraint67 = constraints3.AddBiEltCst(catCstTypeDistance, reference140, reference141)
    #constraint67.Mode = catCstModeDrivingDimension
    #length68 = constraint67.Dimension
    #length68.Value = 20.000000
    reference142 = part1.CreateReferenceFromObject(point2D34)
    reference143 = part1.CreateReferenceFromObject(line2D18)
    #constraint68 = constraints3.AddBiEltCst(catCstTypeDistance, reference142, reference143)
    #constraint68.Mode = catCstModeDrivingDimension
    #length69 = constraint68.Dimension
    #length69.Value = 20.000000
    sketch3.CloseEdition()
    part1.InWorkObject = sketch3
    part1.Update()
    reference144 = part1.CreateReferenceFromName('')
    pad2 = shapeFactory1.AddNewPadFromRef(reference144, 33.000000)
    reference145 = part1.CreateReferenceFromObject(sketch3)
    pad2.SetProfileElement(reference145)
    limit2 = pad2.FirstLimit
    length70 = limit2.Dimension
    length70.Value = (gl4 + (1.5 * gw))
    part1.Update()

    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''

    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("Fire Red")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    
    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\Fork_end.CATPart' %(gibfoldername))
    
    #.............................................................................fork end end................................................................

    #......................................................................rod start...................................................................
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneYZ
    sketch1 = sketches1.Add(reference1)
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
    factory2D1 = sketch1.OpenEdition()                                                              #sketch 1 is opened..............................................
    geometricElements1 = sketch1.GeometricElements
    axis2D1 = geometricElements1.Item('AbsoluteAxis')
    line2D1 = axis2D1.GetItem('HDirection')
    line2D1.ReportName = 1
    line2D2 = axis2D1.GetItem('VDirection')
    line2D2.ReportName = 2
    point2D1 = factory2D1.CreatePoint(- (gw / 2), - (gw / 2))
    point2D1.ReportName = 3
    point2D2 = factory2D1.CreatePoint((gw / 2), - (gw / 2))
    point2D2.ReportName = 4
    line2D3 = factory2D1.CreateLine(- (gw / 2), - (gw / 2), (gw / 2), - (gw / 2))
    line2D3.ReportName = 5
    line2D3.StartPoint = point2D1
    line2D3.EndPoint = point2D2
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(point2D1)
    reference3 = part1.CreateReferenceFromObject(line2D2)
    #constraint1 = constraints1.AddBiEltCst(catCstTypeDistance, reference2, reference3)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 20.000000
    reference4 = part1.CreateReferenceFromObject(point2D1)
    reference5 = part1.CreateReferenceFromObject(line2D1)
    #constraint2 = constraints1.AddBiEltCst(catCstTypeDistance, reference4, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    #length2 = constraint2.Dimension
    #length2.Value = 20.000000
    reference6 = part1.CreateReferenceFromObject(point2D2)
    reference7 = part1.CreateReferenceFromObject(line2D2)
    #constraint3 = constraints1.AddBiEltCst(catCstTypeDistance, reference6, reference7)
    #constraint3.Mode = catCstModeDrivingDimension
    #length3 = constraint3.Dimension
    #length3.Value = 20.000000
    reference8 = part1.CreateReferenceFromObject(point2D2)
    reference9 = part1.CreateReferenceFromObject(line2D1)
    #constraint4 = constraints1.AddBiEltCst(catCstTypeDistance, reference8, reference9)
    #constraint4.Mode = catCstModeDrivingDimension
    #length4 = constraint4.Dimension
    #length4.Value = 20.000000
    point2D3 = factory2D1.CreatePoint((gw / 2), - (gw / 2))
    point2D3.ReportName = 6
    point2D4 = factory2D1.CreatePoint((gw / 2), (gw / 2))
    point2D4.ReportName = 7
    line2D4 = factory2D1.CreateLine((gw / 2), - (gw / 2), (gw / 2), (gw / 2))
    line2D4.ReportName = 8
    line2D4.StartPoint = point2D3
    line2D4.EndPoint = point2D4
    reference10 = part1.CreateReferenceFromObject(point2D3)
    reference11 = part1.CreateReferenceFromObject(line2D2)
    #constraint5 = constraints1.AddBiEltCst(catCstTypeDistance, reference10, reference11)
    #constraint5.Mode = catCstModeDrivingDimension
    #length5 = constraint5.Dimension
    #length5.Value = 20.000000
    reference12 = part1.CreateReferenceFromObject(point2D3)
    reference13 = part1.CreateReferenceFromObject(line2D1)
    #constraint6 = constraints1.AddBiEltCst(catCstTypeDistance, reference12, reference13)
    #constraint6.Mode = catCstModeDrivingDimension
    #length6 = constraint6.Dimension
    #length6.Value = 20.000000
    reference14 = part1.CreateReferenceFromObject(point2D4)
    reference15 = part1.CreateReferenceFromObject(line2D2)
    #constraint7 = constraints1.AddBiEltCst(catCstTypeDistance, reference14, reference15)
    #constraint7.Mode = catCstModeDrivingDimension
    #length7 = constraint7.Dimension
    #length7.Value = 20.000000
    reference16 = part1.CreateReferenceFromObject(point2D4)
    reference17 = part1.CreateReferenceFromObject(line2D1)
    #constraint8 = constraints1.AddBiEltCst(catCstTypeDistance, reference16, reference17)
    #constraint8.Mode = catCstModeDrivingDimension
    #length8 = constraint8.Dimension
    #length8.Value = 20.000000
    point2D5 = factory2D1.CreatePoint((gw / 2), (gw / 2))
    point2D5.ReportName = 9
    point2D6 = factory2D1.CreatePoint(- (gw / 2), (gw / 2))
    point2D6.ReportName = 10
    line2D5 = factory2D1.CreateLine((gw / 2), (gw / 2), - (gw / 2), (gw / 2))
    line2D5.ReportName = 11
    line2D5.StartPoint = point2D5
    line2D5.EndPoint = point2D6
    reference18 = part1.CreateReferenceFromObject(point2D5)
    reference19 = part1.CreateReferenceFromObject(line2D2)
    #constraint9 = constraints1.AddBiEltCst(catCstTypeDistance, reference18, reference19)
    #constraint9.Mode = catCstModeDrivingDimension
    #length9 = constraint9.Dimension
    #length9.Value = 20.000000
    reference20 = part1.CreateReferenceFromObject(point2D5)
    reference21 = part1.CreateReferenceFromObject(line2D1)
    #constraint10 = constraints1.AddBiEltCst(catCstTypeDistance, reference20, reference21)
    #constraint10.Mode = catCstModeDrivingDimension
    #length10 = constraint10.Dimension
    #length10.Value = 20.000000
    reference22 = part1.CreateReferenceFromObject(point2D6)
    reference23 = part1.CreateReferenceFromObject(line2D2)
    #constraint11 = constraints1.AddBiEltCst(catCstTypeDistance, reference22, reference23)
    #constraint11.Mode = catCstModeDrivingDimension
    #length11 = constraint11.Dimension
    #length11.Value = 20.000000
    reference24 = part1.CreateReferenceFromObject(point2D6)
    reference25 = part1.CreateReferenceFromObject(line2D1)
    #constraint12 = constraints1.AddBiEltCst(catCstTypeDistance, reference24, reference25)
    #constraint12.Mode = catCstModeDrivingDimension
    #length12 = constraint12.Dimension
    #length12.Value = 20.000000
    point2D7 = factory2D1.CreatePoint(- (gw / 2), (gw / 2))
    point2D7.ReportName = 12
    point2D8 = factory2D1.CreatePoint(- (gw / 2), - (gw / 2))
    point2D8.ReportName = 13
    line2D6 = factory2D1.CreateLine(- (gw / 2), (gw / 2), - (gw / 2), - (gw / 2))
    line2D6.ReportName = 14
    line2D6.StartPoint = point2D7
    line2D6.EndPoint = point2D8
    reference26 = part1.CreateReferenceFromObject(point2D7)
    reference27 = part1.CreateReferenceFromObject(line2D2)
    #constraint13 = constraints1.AddBiEltCst(catCstTypeDistance, reference26, reference27)
    #constraint13.Mode = catCstModeDrivingDimension
    #length13 = constraint13.Dimension
    #length13.Value = 20.000000
    reference28 = part1.CreateReferenceFromObject(point2D7)
    reference29 = part1.CreateReferenceFromObject(line2D1)
    #constraint14 = constraints1.AddBiEltCst(catCstTypeDistance, reference28, reference29)
    #constraint14.Mode = catCstModeDrivingDimension
    #length14 = constraint14.Dimension
    #length14.Value = 20.000000
    reference30 = part1.CreateReferenceFromObject(point2D8)
    reference31 = part1.CreateReferenceFromObject(line2D2)
    #constraint15 = constraints1.AddBiEltCst(catCstTypeDistance, reference30, reference31)
    #constraint15.Mode = catCstModeDrivingDimension
    #length15 = constraint15.Dimension
    #length15.Value = 20.000000
    reference32 = part1.CreateReferenceFromObject(point2D8)
    reference33 = part1.CreateReferenceFromObject(line2D1)
    #constraint16 = constraints1.AddBiEltCst(catCstTypeDistance, reference32, reference33)
    #constraint16.Mode = catCstModeDrivingDimension
    #length16 = constraint16.Dimension
    #length16.Value = 20.000000
    sketch1.CloseEdition()                                                                  #sketch 1 is closed................................................
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    pad1 = shapeFactory1.AddNewPad(sketch1, 20.000000)
    limit1 = pad1.FirstLimit
    length17 = limit1.Dimension
    length17.Value = - (gl2 + gB + gl3 + (1.5 * gw))
    part1.Update()
    sketches2 = body1.Sketches
    reference34 = originElements1.PlaneXY
    sketch2 = sketches2.Add(reference34)
    arrayOfVariantOfDouble2[0] = 0.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = 1.000000
    arrayOfVariantOfDouble2[4] = 0.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = 1.000000
    arrayOfVariantOfDouble2[8] = 0.000000
    sketch2.SetAbsoluteAxisData(arrayOfVariantOfDouble2)
    part1.InWorkObject = sketch2
    factory2D2 = sketch2.OpenEdition()                              #sketch 2 is opened.......................................................
    geometricElements2 = sketch2.GeometricElements
    axis2D2 = geometricElements2.Item('AbsoluteAxis')
    line2D7 = axis2D2.GetItem('HDirection')
    line2D7.ReportName = 1
    line2D8 = axis2D2.GetItem('VDirection')
    line2D8.ReportName = 2
    point2D9 = factory2D2.CreatePoint(- gl2, (gt / 2))
    point2D9.ReportName = 3
    point2D10 = factory2D2.CreatePoint(- (gl2 + gB), (gt / 2))
    point2D10.ReportName = 4
    line2D9 = factory2D2.CreateLine(- gl2, (gt / 2), - (gl2 + gB), (gt / 2))
    line2D9.ReportName = 5
    line2D9.StartPoint = point2D9
    line2D9.EndPoint = point2D10
    constraints2 = sketch2.Constraints
    reference35 = part1.CreateReferenceFromObject(point2D9)
    reference36 = part1.CreateReferenceFromObject(line2D8)
    #constraint17 = constraints2.AddBiEltCst(catCstTypeDistance, reference35, reference36)
    #constraint17.Mode = catCstModeDrivingDimension
    #length18 = constraint17.Dimension
    #length18.Value = 35.000000
    reference37 = part1.CreateReferenceFromObject(point2D9)
    reference38 = part1.CreateReferenceFromObject(line2D7)
    #constraint18 = constraints2.AddBiEltCst(catCstTypeDistance, reference37, reference38)
    #constraint18.Mode = catCstModeDrivingDimension
    #length19 = constraint18.Dimension
    #length19.Value = 5.000000
    reference39 = part1.CreateReferenceFromObject(point2D10)
    reference40 = part1.CreateReferenceFromObject(line2D8)
    #constraint19 = constraints2.AddBiEltCst(catCstTypeDistance, reference39, reference40)
    #constraint19.Mode = catCstModeDrivingDimension
    #length20 = constraint19.Dimension
    #length20.Value = 90.000000
    reference41 = part1.CreateReferenceFromObject(point2D10)
    reference42 = part1.CreateReferenceFromObject(line2D7)
    #constraint20 = constraints2.AddBiEltCst(catCstTypeDistance, reference41, reference42)
    #constraint20.Mode = catCstModeDrivingDimension
    #length21 = constraint20.Dimension
    #length21.Value = 5.000000
    point2D11 = factory2D2.CreatePoint(- (gl2 + gB), (gt / 2))
    point2D11.ReportName = 6
    point2D12 = factory2D2.CreatePoint(- (gl2 + gB), - (gt / 2))
    point2D12.ReportName = 7
    line2D10 = factory2D2.CreateLine(- (gl2 + gB), (gt / 2), - (gl2 + gB), - (gt / 2))
    line2D10.ReportName = 8
    line2D10.StartPoint = point2D11
    line2D10.EndPoint = point2D12
    reference43 = part1.CreateReferenceFromObject(point2D11)
    reference44 = part1.CreateReferenceFromObject(line2D8)
    #constraint21 = constraints2.AddBiEltCst(catCstTypeDistance, reference43, reference44)
    #constraint21.Mode = catCstModeDrivingDimension
    #length22 = constraint21.Dimension
    #length22.Value = 90.000000
    reference45 = part1.CreateReferenceFromObject(point2D11)
    reference46 = part1.CreateReferenceFromObject(line2D7)
    #constraint22 = constraints2.AddBiEltCst(catCstTypeDistance, reference45, reference46)
    #constraint22.Mode = catCstModeDrivingDimension
    #length23 = constraint22.Dimension
    #length23.Value = 5.000000
    reference47 = part1.CreateReferenceFromObject(point2D12)
    reference48 = part1.CreateReferenceFromObject(line2D8)
    #constraint23 = constraints2.AddBiEltCst(catCstTypeDistance, reference47, reference48)
    #constraint23.Mode = catCstModeDrivingDimension
    #length24 = constraint23.Dimension
    #length24.Value = 90.000000
    reference49 = part1.CreateReferenceFromObject(point2D12)
    reference50 = part1.CreateReferenceFromObject(line2D7)
    #constraint24 = constraints2.AddBiEltCst(catCstTypeDistance, reference49, reference50)
    #constraint24.Mode = catCstModeDrivingDimension
    #length25 = constraint24.Dimension
    #length25.Value = 5.000000
    point2D13 = factory2D2.CreatePoint(- (gl2 + gB), - (gt / 2))
    point2D13.ReportName = 9
    point2D14 = factory2D2.CreatePoint(- gl2, - (gt / 2))
    point2D14.ReportName = 10
    line2D11 = factory2D2.CreateLine(- (gl2 + gB), - (gt / 2), - gl2, - (gt / 2))
    line2D11.ReportName = 11
    line2D11.StartPoint = point2D13
    line2D11.EndPoint = point2D14
    reference51 = part1.CreateReferenceFromObject(point2D13)
    reference52 = part1.CreateReferenceFromObject(line2D8)
    #constraint25 = constraints2.AddBiEltCst(catCstTypeDistance, reference51, reference52)
    #constraint25.Mode = catCstModeDrivingDimension
    #length26 = constraint25.Dimension
    #length26.Value = 90.000000
    reference53 = part1.CreateReferenceFromObject(point2D13)
    reference54 = part1.CreateReferenceFromObject(line2D7)
    #constraint26 = constraints2.AddBiEltCst(catCstTypeDistance, reference53, reference54)
    #constraint26.Mode = catCstModeDrivingDimension
    #length27 = constraint26.Dimension
    #length27.Value = 5.000000
    reference55 = part1.CreateReferenceFromObject(point2D14)
    reference56 = part1.CreateReferenceFromObject(line2D8)
    #constraint27 = constraints2.AddBiEltCst(catCstTypeDistance, reference55, reference56)
    #constraint27.Mode = catCstModeDrivingDimension
    #length28 = constraint27.Dimension
    #length28.Value = 35.000000
    reference57 = part1.CreateReferenceFromObject(point2D14)
    reference58 = part1.CreateReferenceFromObject(line2D7)
    #constraint28 = constraints2.AddBiEltCst(catCstTypeDistance, reference57, reference58)
    #constraint28.Mode = catCstModeDrivingDimension
    #length29 = constraint28.Dimension
    #length29.Value = 5.000000
    point2D15 = factory2D2.CreatePoint(- gl2, - (gt / 2))
    point2D15.ReportName = 12
    point2D16 = factory2D2.CreatePoint(- gl2, (gt / 2))
    point2D16.ReportName = 13
    line2D12 = factory2D2.CreateLine(- gl2, - (gt / 2), - gl2, (gt / 2))
    line2D12.ReportName = 14
    line2D12.StartPoint = point2D15
    line2D12.EndPoint = point2D16
    reference59 = part1.CreateReferenceFromObject(point2D15)
    reference60 = part1.CreateReferenceFromObject(line2D8)
    #constraint29 = constraints2.AddBiEltCst(catCstTypeDistance, reference59, reference60)
    #constraint29.Mode = catCstModeDrivingDimension
    #length30 = constraint29.Dimension
    #length30.Value = 35.000000
    reference61 = part1.CreateReferenceFromObject(point2D15)
    reference62 = part1.CreateReferenceFromObject(line2D7)
    #constraint30 = constraints2.AddBiEltCst(catCstTypeDistance, reference61, reference62)
    #constraint30.Mode = catCstModeDrivingDimension
    #length31 = constraint30.Dimension
    #length31.Value = 5.000000
    reference63 = part1.CreateReferenceFromObject(point2D16)
    reference64 = part1.CreateReferenceFromObject(line2D8)
    #constraint31 = constraints2.AddBiEltCst(catCstTypeDistance, reference63, reference64)
    #constraint31.Mode = catCstModeDrivingDimension
    #length32 = constraint31.Dimension
    #length32.Value = 35.000000
    reference65 = part1.CreateReferenceFromObject(point2D16)
    reference66 = part1.CreateReferenceFromObject(line2D7)
    #constraint32 = constraints2.AddBiEltCst(catCstTypeDistance, reference65, reference66)
    #constraint32.Mode = catCstModeDrivingDimension
    #length33 = constraint32.Dimension
    #length33.Value = 5.000000
    sketch2.CloseEdition()                                                          #sketch 2 is closed..........................................
    part1.InWorkObject = sketch2
    part1.Update()
    reference67 = part1.CreateReferenceFromName('')
    pocket1 = shapeFactory1.AddNewPocketFromRef(reference67, - 192.000000)
    reference68 = part1.CreateReferenceFromObject(sketch2)
    pocket1.SetProfileElement(reference68)
    pocket1.IsSymmetric = True
    limit2 = pocket1.FirstLimit
    length34 = limit2.Dimension
    length34.Value = (gw / 2)
    part1.Update()

    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()

    '''

    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("Light Green")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\Rod_end.CATPart' %(gibfoldername))
    

    #..........................................................................rod end.......................................................

    #............................................................cotter start...................................................
    
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
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
    point2D1 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D1.ReportName = 3
    point2D2 = factory2D1.CreatePoint(0.000000, (2 * gw))
    point2D2.ReportName = 4
    line2D3 = factory2D1.CreateLine(0.000000, 0.000000, 0.000000, (2 * gw))
    line2D3.ReportName = 5
    line2D3.StartPoint = point2D1
    line2D3.EndPoint = point2D2
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(point2D1)
    reference3 = part1.CreateReferenceFromObject(line2D2)
    #constraint1 = constraints1.AddBiEltCst(catCstTypeDistance, reference2, reference3)
    #constraint1.Mode = catCstModeDrivingDimension
    #length1 = constraint1.Dimension
    #length1.Value = 0.000000
    reference4 = part1.CreateReferenceFromObject(point2D1)
    reference5 = part1.CreateReferenceFromObject(line2D1)
    #constraint2 = constraints1.AddBiEltCst(catCstTypeDistance, reference4, reference5)
    #constraint2.Mode = catCstModeDrivingDimension
    #length2 = constraint2.Dimension
    #length2.Value = 0.000000
    reference6 = part1.CreateReferenceFromObject(point2D2)
    reference7 = part1.CreateReferenceFromObject(line2D2)
    #constraint3 = constraints1.AddBiEltCst(catCstTypeDistance, reference6, reference7)
    #constraint3.Mode = catCstModeDrivingDimension
    #length3 = constraint3.Dimension
    #length3.Value = 0.000000
    reference8 = part1.CreateReferenceFromObject(point2D2)
    reference9 = part1.CreateReferenceFromObject(line2D1)
    #constraint4 = constraints1.AddBiEltCst(catCstTypeDistance, reference8, reference9)
    #constraint4.Mode = catCstModeDrivingDimension
    #length4 = constraint4.Dimension
    #length4.Value = 75.000000
    point2D3 = factory2D1.CreatePoint(0.000000, (2 * gw))
    point2D3.ReportName = 6
    point2D4 = factory2D1.CreatePoint(- (gb + ((2 * gw)/30)), (2 * gw))
    point2D4.ReportName = 7
    line2D4 = factory2D1.CreateLine(0.000000, (2 * gw), - (gb + ((2 * gw)/30)), (2 * gw))
    line2D4.ReportName = 8
    line2D4.StartPoint = point2D3
    line2D4.EndPoint = point2D4
    reference10 = part1.CreateReferenceFromObject(point2D3)
    reference11 = part1.CreateReferenceFromObject(line2D2)
    #constraint5 = constraints1.AddBiEltCst(catCstTypeDistance, reference10, reference11)
    #constraint5.Mode = catCstModeDrivingDimension
    #length5 = constraint5.Dimension
    #length5.Value = 0.000000
    reference12 = part1.CreateReferenceFromObject(point2D3)
    reference13 = part1.CreateReferenceFromObject(line2D1)
    #constraint6 = constraints1.AddBiEltCst(catCstTypeDistance, reference12, reference13)
    #constraint6.Mode = catCstModeDrivingDimension
    #length6 = constraint6.Dimension
    #length6.Value = 75.000000
    reference14 = part1.CreateReferenceFromObject(point2D4)
    reference15 = part1.CreateReferenceFromObject(line2D2)
    #constraint7 = constraints1.AddBiEltCst(catCstTypeDistance, reference14, reference15)
    #constraint7.Mode = catCstModeDrivingDimension
    #length7 = constraint7.Dimension
    #length7.Value = 32.000000
    reference16 = part1.CreateReferenceFromObject(point2D4)
    reference17 = part1.CreateReferenceFromObject(line2D1)
    #constraint8 = constraints1.AddBiEltCst(catCstTypeDistance, reference16, reference17)
    #constraint8.Mode = catCstModeDrivingDimension
    #length8 = constraint8.Dimension
    #length8.Value = 75.000000
    point2D5 = factory2D1.CreatePoint(- (gb + ((2 * gw)/30)), (2 * gw))
    point2D5.ReportName = 9
    point2D6 = factory2D1.CreatePoint(- (gb - ((2 * gw)/30)), - (2 * gw))
    point2D6.ReportName = 10
    line2D5 = factory2D1.CreateLine(- (gb + ((2 * gw)/30)), (2 * gw), - (gb - ((2 * gw)/30)), - (2 * gw))
    line2D5.ReportName = 11
    line2D5.StartPoint = point2D5
    line2D5.EndPoint = point2D6
    reference18 = part1.CreateReferenceFromObject(point2D5)
    reference19 = part1.CreateReferenceFromObject(line2D2)
    #constraint9 = constraints1.AddBiEltCst(catCstTypeDistance, reference18, reference19)
    #constraint9.Mode = catCstModeDrivingDimension
    #length9 = constraint9.Dimension
    #length9.Value = 32.000000
    reference20 = part1.CreateReferenceFromObject(point2D5)
    reference21 = part1.CreateReferenceFromObject(line2D1)
    #constraint10 = constraints1.AddBiEltCst(catCstTypeDistance, reference20, reference21)
    #constraint10.Mode = catCstModeDrivingDimension
    #length10 = constraint10.Dimension
    #length10.Value = 75.000000
    reference22 = part1.CreateReferenceFromObject(point2D6)
    reference23 = part1.CreateReferenceFromObject(line2D2)
    #constraint11 = constraints1.AddBiEltCst(catCstTypeDistance, reference22, reference23)
    #constraint11.Mode = catCstModeDrivingDimension
    #length11 = constraint11.Dimension
    #length11.Value = 20.000000
    reference24 = part1.CreateReferenceFromObject(point2D6)
    reference25 = part1.CreateReferenceFromObject(line2D1)
    #constraint12 = constraints1.AddBiEltCst(catCstTypeDistance, reference24, reference25)
    #constraint12.Mode = catCstModeDrivingDimension
    #length12 = constraint12.Dimension
    #length12.Value = 75.000000
    point2D7 = factory2D1.CreatePoint(- (gb - ((2 * gw)/30)), - (2 * gw))
    point2D7.ReportName = 12
    point2D8 = factory2D1.CreatePoint(0.000000, - (2 * gw))
    point2D8.ReportName = 13
    line2D6 = factory2D1.CreateLine(- (gb - ((2 * gw)/30)), - (2 * gw), 0.000000, - (2 * gw))
    line2D6.ReportName = 14
    line2D6.StartPoint = point2D7
    line2D6.EndPoint = point2D8
    reference26 = part1.CreateReferenceFromObject(point2D7)
    reference27 = part1.CreateReferenceFromObject(line2D2)
    #constraint13 = constraints1.AddBiEltCst(catCstTypeDistance, reference26, reference27)
    #constraint13.Mode = catCstModeDrivingDimension
    #length13 = constraint13.Dimension
    #length13.Value = 20.000000
    reference28 = part1.CreateReferenceFromObject(point2D7)
    reference29 = part1.CreateReferenceFromObject(line2D1)
    #constraint14 = constraints1.AddBiEltCst(catCstTypeDistance, reference28, reference29)
    #constraint14.Mode = catCstModeDrivingDimension
    #length14 = constraint14.Dimension
    #length14.Value = 75.000000
    reference30 = part1.CreateReferenceFromObject(point2D8)
    reference31 = part1.CreateReferenceFromObject(line2D2)
    #constraint15 = constraints1.AddBiEltCst(catCstTypeDistance, reference30, reference31)
    #constraint15.Mode = catCstModeDrivingDimension
    #length15 = constraint15.Dimension
    #length15.Value = 0.000000
    reference32 = part1.CreateReferenceFromObject(point2D8)
    reference33 = part1.CreateReferenceFromObject(line2D1)
    #constraint16 = constraints1.AddBiEltCst(catCstTypeDistance, reference32, reference33)
    #constraint16.Mode = catCstModeDrivingDimension
    #length16 = constraint16.Dimension
    #length16.Value = 75.000000
    point2D9 = factory2D1.CreatePoint(0.000000, - (2 * gw))
    point2D9.ReportName = 15
    point2D10 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D10.ReportName = 16
    line2D7 = factory2D1.CreateLine(0.000000, - (2 * gw), 0.000000, 0.000000)
    line2D7.ReportName = 17
    line2D7.StartPoint = point2D9
    line2D7.EndPoint = point2D10
    reference34 = part1.CreateReferenceFromObject(point2D9)
    reference35 = part1.CreateReferenceFromObject(line2D2)
    #constraint17 = constraints1.AddBiEltCst(catCstTypeDistance, reference34, reference35)
    #constraint17.Mode = catCstModeDrivingDimension
    #length17 = constraint17.Dimension
    #length17.Value = 0.000000
    reference36 = part1.CreateReferenceFromObject(point2D9)
    reference37 = part1.CreateReferenceFromObject(line2D1)
    #constraint18 = constraints1.AddBiEltCst(catCstTypeDistance, reference36, reference37)
    #constraint18.Mode = catCstModeDrivingDimension
    #length18 = constraint18.Dimension
    #length18.Value = 75.000000
    reference38 = part1.CreateReferenceFromObject(point2D10)
    reference39 = part1.CreateReferenceFromObject(line2D2)
    #constraint19 = constraints1.AddBiEltCst(catCstTypeDistance, reference38, reference39)
    #constraint19.Mode = catCstModeDrivingDimension
    #length19 = constraint19.Dimension
    #length19.Value = 0.000000
    reference40 = part1.CreateReferenceFromObject(point2D10)
    reference41 = part1.CreateReferenceFromObject(line2D1)
    #constraint20 = constraints1.AddBiEltCst(catCstTypeDistance, reference40, reference41)
    #constraint20.Mode = catCstModeDrivingDimension
    #length20 = constraint20.Dimension
    #length20.Value = 0.000000
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    pad1 = shapeFactory1.AddNewPad(sketch1, 20.000000)
    pad1.IsSymmetric = True
    limit1 = pad1.FirstLimit
    length21 = limit1.Dimension
    length21.Value = (gt / 2)
    part1.Update()


    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("DS Gold")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()

    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\cotter_pin.CATPart' %(gibfoldername))
    

    #..............................................................cotter end...................................................................

    #............................................................gib start...................................................................

    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0]
    documents1 = CATIA.Documents
    partDocument1 = documents1.Add('Part')
    part1 = partDocument1.Part
    hybridBodies1 = part1.HybridBodies
    hybridBody1 = hybridBodies1.Item('Geometrical Set.1')
    sketches1 = hybridBody1.HybridSketches
    originElements1 = part1.OriginElements
    reference1 = originElements1.PlaneZX
    sketch1 = sketches1.Add(reference1)
    arrayOfVariantOfDouble1[0] = 0.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = - 1.000000
    arrayOfVariantOfDouble1[4] = 0.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = - 0.000000
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
    point2D1 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D1.ReportName = 3
    point2D2 = factory2D1.CreatePoint(0.000000, ((gw / 2) + gt1))
    point2D2.ReportName = 4
    line2D3 = factory2D1.CreateLine(0.000000, 0.000000, 0.000000, ((gw / 2) + gt1))
    line2D3.ReportName = 5
    line2D3.StartPoint = point2D1
    line2D3.EndPoint = point2D2
    constraints1 = sketch1.Constraints
    reference2 = part1.CreateReferenceFromObject(point2D1)
    reference3 = part1.CreateReferenceFromObject(line2D2)
    '''constraint1 = constraints1.AddBiEltCst(catCstTypeDistance, reference2, reference3)
    constraint1.Mode = catCstModeDrivingDimension
    length1 = constraint1.Dimension
    length1.Value = 0.000000'''
    reference4 = part1.CreateReferenceFromObject(point2D1)
    reference5 = part1.CreateReferenceFromObject(line2D1)
    '''constraint2 = constraints1.AddBiEltCst(catCstTypeDistance, reference4, reference5)
    constraint2.Mode = catCstModeDrivingDimension
    length2 = constraint2.Dimension
    length2.Value = 0.000000'''
    reference6 = part1.CreateReferenceFromObject(point2D2)
    reference7 = part1.CreateReferenceFromObject(line2D2)
    '''constraint3 = constraints1.AddBiEltCst(catCstTypeDistance, reference6, reference7)
    constraint3.Mode = catCstModeDrivingDimension
    length3 = constraint3.Dimension
    length3.Value = 0.000000'''
    reference8 = part1.CreateReferenceFromObject(point2D2)
    reference9 = part1.CreateReferenceFromObject(line2D1)
    '''constraint4 = constraints1.AddBiEltCst(catCstTypeDistance, reference8, reference9)
    constraint4.Mode = catCstModeDrivingDimension
    length4 = constraint4.Dimension
    length4.Value = 33.000000'''
    point2D3 = factory2D1.CreatePoint(0.000000, ((gw / 2) + gt1))
    point2D3.ReportName = 6
    point2D4 = factory2D1.CreatePoint(- gl1, 33.000000)
    point2D4.ReportName = 7
    line2D4 = factory2D1.CreateLine(0.000000, ((gw / 2) + gt1), - gl1, ((gw / 2) + gt1))
    line2D4.ReportName = 8
    line2D4.StartPoint = point2D3
    line2D4.EndPoint = point2D4
    reference10 = part1.CreateReferenceFromObject(point2D3)
    reference11 = part1.CreateReferenceFromObject(line2D2)
    '''constraint5 = constraints1.AddBiEltCst(catCstTypeDistance, reference10, reference11)
    constraint5.Mode = catCstModeDrivingDimension
    length5 = constraint5.Dimension
    length5.Value = 0.000000'''
    reference12 = part1.CreateReferenceFromObject(point2D3)
    reference13 = part1.CreateReferenceFromObject(line2D1)
    '''constraint6 = constraints1.AddBiEltCst(catCstTypeDistance, reference12, reference13)
    constraint6.Mode = catCstModeDrivingDimension
    length6 = constraint6.Dimension
    length6.Value = 33.000000'''
    reference14 = part1.CreateReferenceFromObject(point2D4)
    reference15 = part1.CreateReferenceFromObject(line2D2)
    '''constraint7 = constraints1.AddBiEltCst(catCstTypeDistance, reference14, reference15)
    constraint7.Mode = catCstModeDrivingDimension
    length7 = constraint7.Dimension
    length7.Value = 12.000000'''
    reference16 = part1.CreateReferenceFromObject(point2D4)
    reference17 = part1.CreateReferenceFromObject(line2D1)
    '''constraint8 = constraints1.AddBiEltCst(catCstTypeDistance, reference16, reference17)
    constraint8.Mode = catCstModeDrivingDimension
    length8 = constraint8.Dimension
    length8.Value = 33.000000'''
    point2D5 = factory2D1.CreatePoint(- gl1, ((gw / 2) + gt1))
    point2D5.ReportName = 9
    point2D6 = factory2D1.CreatePoint(- gl1, ((gw / 2) + gt1 + gt2))
    point2D6.ReportName = 10
    line2D5 = factory2D1.CreateLine(- gl1, ((gw / 2) + gt1), - gl1, ((gw / 2) + gt1 + gt2))
    line2D5.ReportName = 11
    line2D5.StartPoint = point2D5
    line2D5.EndPoint = point2D6
    reference18 = part1.CreateReferenceFromObject(point2D5)
    reference19 = part1.CreateReferenceFromObject(line2D2)
    '''constraint9 = constraints1.AddBiEltCst(catCstTypeDistance, reference18, reference19)
    constraint9.Mode = catCstModeDrivingDimension
    length9 = constraint9.Dimension
    length9.Value = 12.000000'''
    reference20 = part1.CreateReferenceFromObject(point2D5)
    reference21 = part1.CreateReferenceFromObject(line2D1)
    '''constraint10 = constraints1.AddBiEltCst(catCstTypeDistance, reference20, reference21)
    constraint10.Mode = catCstModeDrivingDimension
    length10 = constraint10.Dimension
    length10.Value = 33.000000'''
    reference22 = part1.CreateReferenceFromObject(point2D6)
    reference23 = part1.CreateReferenceFromObject(line2D2)
    '''constraint11 = constraints1.AddBiEltCst(catCstTypeDistance, reference22, reference23)
    constraint11.Mode = catCstModeDrivingDimension
    length11 = constraint11.Dimension
    length11.Value = 12.000000'''
    reference24 = part1.CreateReferenceFromObject(point2D6)
    reference25 = part1.CreateReferenceFromObject(line2D1)
    '''constraint12 = constraints1.AddBiEltCst(catCstTypeDistance, reference24, reference25)
    constraint12.Mode = catCstModeDrivingDimension
    length12 = constraint12.Dimension
    length12.Value = 48.000000'''
    point2D7 = factory2D1.CreatePoint(- gl1, ((gw / 2) + gt1 + gt2))
    point2D7.ReportName = 12
    point2D8 = factory2D1.CreatePoint((gb1 -((gw / 2) + gt1 + gt2)/30), ((gw / 2) + gt1 + gt2))
    point2D8.ReportName = 13
    line2D6 = factory2D1.CreateLine(- gl1, ((gw / 2) + gt1 + gt2), (gb1 -((gw / 2) + gt1 + gt2)/30), ((gw / 2) + gt1 + gt2))
    line2D6.ReportName = 14
    line2D6.StartPoint = point2D7
    line2D6.EndPoint = point2D8
    reference26 = part1.CreateReferenceFromObject(point2D7)
    reference27 = part1.CreateReferenceFromObject(line2D2)
    '''constraint13 = constraints1.AddBiEltCst(catCstTypeDistance, reference26, reference27)
    constraint13.Mode = catCstModeDrivingDimension
    length13 = constraint13.Dimension
    length13.Value = 12.000000'''
    reference28 = part1.CreateReferenceFromObject(point2D7)
    reference29 = part1.CreateReferenceFromObject(line2D1)
    '''constraint14 = constraints1.AddBiEltCst(catCstTypeDistance, reference28, reference29)
    constraint14.Mode = catCstModeDrivingDimension
    length14 = constraint14.Dimension
    length14.Value = 48.000000'''
    reference30 = part1.CreateReferenceFromObject(point2D8)
    reference31 = part1.CreateReferenceFromObject(line2D2)
    '''constraint15 = constraints1.AddBiEltCst(catCstTypeDistance, reference30, reference31)
    constraint15.Mode = catCstModeDrivingDimension
    length15 = constraint15.Dimension
    length15.Value = 26.000000'''
    reference32 = part1.CreateReferenceFromObject(point2D8)
    reference33 = part1.CreateReferenceFromObject(line2D1)
    '''constraint16 = constraints1.AddBiEltCst(catCstTypeDistance, reference32, reference33)
    constraint16.Mode = catCstModeDrivingDimension
    length16 = constraint16.Dimension
    length16.Value = 48.000000'''
    point2D9 = factory2D1.CreatePoint((gb1 -((gw / 2) + gt1 + gt2)/30), ((gw / 2) + gt1 + gt2))
    point2D9.ReportName = 15
    point2D10 = factory2D1.CreatePoint((gb1 +((gw / 2) + gt1 + gt2)/30), - ((gw / 2) + gt1 + gt2))
    point2D10.ReportName = 16
    line2D7 = factory2D1.CreateLine((gb1 -((gw / 2) + gt1 + gt2)/30), ((gw / 2) + gt1 + gt2), (gb1 +((gw / 2) + gt1 + gt2)/30), - ((gw / 2) + gt1 + gt2))
    line2D7.ReportName = 17
    line2D7.StartPoint = point2D9
    line2D7.EndPoint = point2D10
    reference34 = part1.CreateReferenceFromObject(point2D9)
    reference35 = part1.CreateReferenceFromObject(line2D2)
    '''constraint17 = constraints1.AddBiEltCst(catCstTypeDistance, reference34, reference35)
    constraint17.Mode = catCstModeDrivingDimension
    length17 = constraint17.Dimension
    length17.Value = 26.000000'''
    reference36 = part1.CreateReferenceFromObject(point2D9)
    reference37 = part1.CreateReferenceFromObject(line2D1)
    '''constraint18 = constraints1.AddBiEltCst(catCstTypeDistance, reference36, reference37)
    constraint18.Mode = catCstModeDrivingDimension
    length18 = constraint18.Dimension
    length18.Value = 48.000000'''
    reference38 = part1.CreateReferenceFromObject(point2D10)
    reference39 = part1.CreateReferenceFromObject(line2D2)
    '''constraint19 = constraints1.AddBiEltCst(catCstTypeDistance, reference38, reference39)
    constraint19.Mode = catCstModeDrivingDimension
    length19 = constraint19.Dimension
    length19.Value = 32.000000'''
    reference40 = part1.CreateReferenceFromObject(point2D10)
    reference41 = part1.CreateReferenceFromObject(line2D1)
    '''constraint20 = constraints1.AddBiEltCst(catCstTypeDistance, reference40, reference41)
    constraint20.Mode = catCstModeDrivingDimension
    length20 = constraint20.Dimension
    length20.Value = 48.000000'''
    point2D11 = factory2D1.CreatePoint((gb1 +((gw / 2) + gt1 + gt2)/30), - ((gw / 2) + gt1 + gt2))
    point2D11.ReportName = 18
    point2D12 = factory2D1.CreatePoint(- gl1, - ((gw / 2) + gt1 + gt2))
    point2D12.ReportName = 19
    line2D8 = factory2D1.CreateLine((gb1 +((gw / 2) + gt1 + gt2)/30), - ((gw / 2) + gt1 + gt2), - gl1, - ((gw / 2) + gt1 + gt2))
    line2D8.ReportName = 20
    line2D8.StartPoint = point2D11
    line2D8.EndPoint = point2D12
    reference42 = part1.CreateReferenceFromObject(point2D11)
    reference43 = part1.CreateReferenceFromObject(line2D2)
    '''constraint21 = constraints1.AddBiEltCst(catCstTypeDistance, reference42, reference43)
    constraint21.Mode = catCstModeDrivingDimension
    length21 = constraint21.Dimension
    length21.Value = 32.000000'''
    reference44 = part1.CreateReferenceFromObject(point2D11)
    reference45 = part1.CreateReferenceFromObject(line2D1)
    '''constraint22 = constraints1.AddBiEltCst(catCstTypeDistance, reference44, reference45)
    constraint22.Mode = catCstModeDrivingDimension
    length22 = constraint22.Dimension
    length22.Value = 48.000000'''
    reference46 = part1.CreateReferenceFromObject(point2D12)
    reference47 = part1.CreateReferenceFromObject(line2D2)
    ''''constraint23 = constraints1.AddBiEltCst(catCstTypeDistance, reference46, reference47)
    constraint23.Mode = catCstModeDrivingDimension
    length23 = constraint23.Dimension
    length23.Value = 12.000000'''
    reference48 = part1.CreateReferenceFromObject(point2D12)
    reference49 = part1.CreateReferenceFromObject(line2D1)
    '''constraint24 = constraints1.AddBiEltCst(catCstTypeDistance, reference48, reference49)
    constraint24.Mode = catCstModeDrivingDimension
    length24 = constraint24.Dimension
    length24.Value = 48.000000'''
    point2D13 = factory2D1.CreatePoint(- gl1, - ((gw / 2) + gt1 + gt2))
    point2D13.ReportName = 21
    point2D14 = factory2D1.CreatePoint(- gl1, - ((gw / 2) + gt1))
    point2D14.ReportName = 22
    line2D9 = factory2D1.CreateLine(- gl1, - ((gw / 2) + gt1 + gt2), - gl1, - ((gw / 2) + gt1))
    line2D9.ReportName = 23
    line2D9.StartPoint = point2D13
    line2D9.EndPoint = point2D14
    reference50 = part1.CreateReferenceFromObject(point2D13)
    reference51 = part1.CreateReferenceFromObject(line2D2)
    '''constraint25 = constraints1.AddBiEltCst(catCstTypeDistance, reference50, reference51)
    constraint25.Mode = catCstModeDrivingDimension
    length25 = constraint25.Dimension
    length25.Value = 12.000000'''
    reference52 = part1.CreateReferenceFromObject(point2D13)
    reference53 = part1.CreateReferenceFromObject(line2D1)
    '''constraint26 = constraints1.AddBiEltCst(catCstTypeDistance, reference52, reference53)
    constraint26.Mode = catCstModeDrivingDimension
    length26 = constraint26.Dimension
    length26.Value = 48.000000'''
    reference54 = part1.CreateReferenceFromObject(point2D14)
    reference55 = part1.CreateReferenceFromObject(line2D2)
    '''constraint27 = constraints1.AddBiEltCst(catCstTypeDistance, reference54, reference55)
    constraint27.Mode = catCstModeDrivingDimension
    length27 = constraint27.Dimension
    length27.Value = 12.000000'''
    reference56 = part1.CreateReferenceFromObject(point2D14)
    reference57 = part1.CreateReferenceFromObject(line2D1)
    '''constraint28 = constraints1.AddBiEltCst(catCstTypeDistance, reference56, reference57)
    constraint28.Mode = catCstModeDrivingDimension
    length28 = constraint28.Dimension
    length28.Value = 33.000000'''
    point2D15 = factory2D1.CreatePoint(- gl1, - ((gw / 2) + gt1))
    point2D15.ReportName = 24
    point2D16 = factory2D1.CreatePoint(0.000000, - ((gw / 2) + gt1))
    point2D16.ReportName = 25
    line2D10 = factory2D1.CreateLine(- gl1, - ((gw / 2) + gt1), 0.000000, - ((gw / 2) + gt1))
    line2D10.ReportName = 26
    line2D10.StartPoint = point2D15
    line2D10.EndPoint = point2D16
    reference58 = part1.CreateReferenceFromObject(point2D15)
    reference59 = part1.CreateReferenceFromObject(line2D2)
    '''constraint29 = constraints1.AddBiEltCst(catCstTypeDistance, reference58, reference59)
    constraint29.Mode = catCstModeDrivingDimension
    length29 = constraint29.Dimension
    length29.Value = 12.000000'''
    reference60 = part1.CreateReferenceFromObject(point2D15)
    reference61 = part1.CreateReferenceFromObject(line2D1)
    '''constraint30 = constraints1.AddBiEltCst(catCstTypeDistance, reference60, reference61)
    constraint30.Mode = catCstModeDrivingDimension
    length30 = constraint30.Dimension
    length30.Value = 33.000000'''
    reference62 = part1.CreateReferenceFromObject(point2D16)
    reference63 = part1.CreateReferenceFromObject(line2D2)
    '''constraint31 = constraints1.AddBiEltCst(catCstTypeDistance, reference62, reference63)
    constraint31.Mode = catCstModeDrivingDimension
    length31 = constraint31.Dimension
    length31.Value = 0.000000'''
    reference64 = part1.CreateReferenceFromObject(point2D16)
    reference65 = part1.CreateReferenceFromObject(line2D1)
    '''constraint32 = constraints1.AddBiEltCst(catCstTypeDistance, reference64, reference65)
    constraint32.Mode = catCstModeDrivingDimension
    length32 = constraint32.Dimension
    length32.Value = 33.000000'''
    point2D17 = factory2D1.CreatePoint(0.000000, - ((gw / 2) + gt1))
    point2D17.ReportName = 27
    point2D18 = factory2D1.CreatePoint(0.000000, 0.000000)
    point2D18.ReportName = 28
    line2D11 = factory2D1.CreateLine(0.000000, - ((gw / 2) + gt1), 0.000000, 0.000000)
    line2D11.ReportName = 29
    line2D11.StartPoint = point2D17
    line2D11.EndPoint = point2D18
    reference66 = part1.CreateReferenceFromObject(point2D17)
    reference67 = part1.CreateReferenceFromObject(line2D2)
    '''constraint33 = constraints1.AddBiEltCst(catCstTypeDistance, reference66, reference67)
    constraint33.Mode = catCstModeDrivingDimension
    length33 = constraint33.Dimension
    length33.Value = 0.000000'''
    reference68 = part1.CreateReferenceFromObject(point2D17)
    reference69 = part1.CreateReferenceFromObject(line2D1)
    '''constraint34 = constraints1.AddBiEltCst(catCstTypeDistance, reference68, reference69)
    constraint34.Mode = catCstModeDrivingDimension
    length34 = constraint34.Dimension
    length34.Value = 33.000000'''
    reference70 = part1.CreateReferenceFromObject(point2D18)
    reference71 = part1.CreateReferenceFromObject(line2D1)
    '''constraint35 = constraints1.AddBiEltCst(catCstTypeDistance, reference70, reference71)
    constraint35.Mode = catCstModeDrivingDimension
    length35 = constraint35.Dimension
    length35.Value = 0.000000'''
    reference72 = part1.CreateReferenceFromObject(point2D18)
    reference73 = part1.CreateReferenceFromObject(line2D2)
    '''constraint36 = constraints1.AddBiEltCst(catCstTypeDistance, reference72, reference73)
    constraint36.Mode = catCstModeDrivingDimension
    length36 = constraint36.Dimension
    length36.Value = 0.000000'''
    sketch1.CloseEdition()
    part1.InWorkObject = hybridBody1
    part1.Update()
    bodies1 = part1.Bodies
    body1 = bodies1.Item('PartBody')
    part1.InWorkObject = body1
    part1.InWorkObject = body1
    shapeFactory1 = part1.ShapeFactory
    pad1 = shapeFactory1.AddNewPad(sketch1, 20.000000)
    pad1.IsSymmetric = True
    limit1 = pad1.FirstLimit
    length37 = limit1.Dimension
    length37.Value = (gt / 2)
    part1.Update()

    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomOut()
    
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D

    selection1 = partDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    selection1.Add(hybridShapePlaneExplicit1)
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = visPropertySet1.Name
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()
    selection2 = partDocument1.Selection
    visPropertySet2 = selection2.VisProperties
    hybridShapePlaneExplicit2 = originElements1.PlaneZX
    selection2.Add(hybridShapePlaneExplicit2)
    visPropertySet2 = visPropertySet2.Parent
    bSTR3 = visPropertySet2.Name
    bSTR4 = visPropertySet2.Name
    visPropertySet2.SetShow(1)
    selection2.Clear()
    selection3 = partDocument1.Selection
    visPropertySet3 = selection3.VisProperties
    hybridShapePlaneExplicit3 = originElements1.PlaneXY
    selection3.Add(hybridShapePlaneExplicit3)
    visPropertySet3 = visPropertySet3.Parent
    bSTR5 = visPropertySet3.Name
    bSTR6 = visPropertySet3.Name
    visPropertySet3.SetShow(1)
    selection3.Clear()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Metal").Materials.Item(materia)
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()
    '''
    # Assign Material
    MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
    hk=CATIA.ActiveDocument.Part.MainBody
    systempath= CATIA.SystemService.Environ("CATDocView")
    path= "C:\\Program Files (x86)\\Dassault Systemes\\B20\\intel_a\\startup\\materials\\Catalog.CATMaterial"
    MatDoc=CATIA.Documents.Open(path)
    oMaterial=MatDoc.Families.Item("Painting").Materials.Item("DS Light Blue")
    MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
    MatDoc.Close()
    part1.Update()

    
    partDocument1 = CATIA.ActiveDocument
    #partDocument1.SaveAs('C:\\Users\\l\\Downloads\\engine\\andisamy.CATPart')
    partDocument1.SaveAs('C:\\%s\\gib_pin.CATPart' %(gibfoldername))
    

    #......................................................................gib stop......................................................


    #..............................................................assembly start...............................................................................
    '''arrayOfVariantOfBSTR1 = vbObjectInitialize((0,), Variant)

    arrayOfVariantOfBSTR2 = vbObjectInitialize((0,), Variant)

    arrayOfVariantOfBSTR3 = vbObjectInitialize((0,), Variant)

    arrayOfVariantOfBSTR4 = vbObjectInitialize((0,), Variant)'''

        
    arrayOfVariantOfBSTR1 = [0,0,0,0,0,0,0,0,0,0,0]
    
    arrayOfVariantOfBSTR2 = [0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfBSTR3 = [0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfBSTR4 = [0,0,0,0,0,0,0,0,0,0,0]

    catCstTypeOn = 2
    catCstTypeSurfContact = 20
    catCstTypeReference = 0
    catCstOrientSame=0
    catCstOrientOpposite=1
    '''arrayOfVariantOfDouble1 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble2 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble3 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble4 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble5 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble6 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble7 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble8 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble9 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble10 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble11 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble12 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble13 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble14 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble15 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble16 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble17 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble18 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble19 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble20 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble21 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble22 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble23 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble24 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble25 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble26 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble27 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble28 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble29 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble30 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble31 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble32 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble33 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble34 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble35 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble36 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble37 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble38 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble39 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble40 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble41 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble42 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble43 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble44 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble45 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble46 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble47 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble48 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble49 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble50 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble51 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble52 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble53 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble54 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble55 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble56 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble57 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble58 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble59 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble60 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble61 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble62 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble63 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble64 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble65 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble66 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble67 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble68 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble69 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble70 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble71 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble72 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble73 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble74 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble75 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble76 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble77 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble78 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble79 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble80 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble81 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble82 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble83 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble84 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble85 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble86 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble87 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble88 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble89 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble90 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble91 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble92 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble93 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble94 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble95 = vbObjectInitialize((11,), Variant)

    arrayOfVariantOfDouble96 = vbObjectInitialize((11,), Variant)'''
    arrayOfVariantOfDouble1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble3 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble4 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble5 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble6 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble7 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble8 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble9 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble10 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble11 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble12 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble13 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble14 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble15 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble16 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble17 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble18 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble19 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble20 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble21 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble22 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble23 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble24 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble25 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble26 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble27 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble28 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble29 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble30 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble31 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble32 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble33 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble34 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble35 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble36 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble37 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble38 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble39 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble40 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble41 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble42 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble43 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble44 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble45 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble46 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble47 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble48 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble49 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble50 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble51 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble52 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble53 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble54 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble55 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble56 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble57 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble58 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble59 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble60 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble61 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble62 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble63 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble64 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble65 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble66 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble67 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble68 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble69 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble70 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble71 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble72 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble73 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble74 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble75 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble76 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble77 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble78 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble79 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble80 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble81 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble82 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble83 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble84 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble85 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble86 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble87 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble88 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble89 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble90 = [0,0,0,0,0,0,0,0,0,0,0,0]

    arrayOfVariantOfDouble91 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble92 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble93 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble94 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble95 = [0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfVariantOfDouble96 = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    documents1 = CATIA.Documents
    productDocument1 = documents1.Add('Product')
    product1 = productDocument1.Product
    products1 = product1.Products
    arrayOfVariantOfBSTR1[0] = ('C:\\%s\\Fork_end.CATPart' %(gibfoldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR1, 'All')
    constraints1 = product1.Connections('CATIAConstraints')
    reference1 = product1.CreateReferenceFromName('Product1/Part1.1/!Product1/Part1.1/')
    constraint1 = constraints1.AddMonoEltCst(catCstTypeReference, reference1)
    arrayOfVariantOfBSTR2[0] = ('C:\\%s\\Rod_end.CATPart' %(gibfoldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR2, 'All')
    arrayOfVariantOfBSTR3[0] = ('C:\\%s\\cotter_pin.CATPart' %(gibfoldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR3, 'All')
    arrayOfVariantOfBSTR4[0] = ('C:\\%s\\gib_pin.CATPart' %(gibfoldername))
    products1.AddComponentsFromFiles(arrayOfVariantOfBSTR4, 'All')
    product2 = products1.Item('Part2.1')
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble1[0] = 1.000000
    arrayOfVariantOfDouble1[1] = 0.000000
    arrayOfVariantOfDouble1[2] = 0.000000
    arrayOfVariantOfDouble1[3] = 0.000000
    arrayOfVariantOfDouble1[4] = 1.000000
    arrayOfVariantOfDouble1[5] = 0.000000
    arrayOfVariantOfDouble1[6] = 0.000000
    arrayOfVariantOfDouble1[7] = 0.000000
    arrayOfVariantOfDouble1[8] = 1.000000
    arrayOfVariantOfDouble1[9] = 0.000000
    arrayOfVariantOfDouble1[10] = 3.031415
    arrayOfVariantOfDouble1[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble1)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble2[0] = 1.000000
    arrayOfVariantOfDouble2[1] = 0.000000
    arrayOfVariantOfDouble2[2] = 0.000000
    arrayOfVariantOfDouble2[3] = 0.000000
    arrayOfVariantOfDouble2[4] = 1.000000
    arrayOfVariantOfDouble2[5] = 0.000000
    arrayOfVariantOfDouble2[6] = 0.000000
    arrayOfVariantOfDouble2[7] = 0.000000
    arrayOfVariantOfDouble2[8] = 1.000000
    arrayOfVariantOfDouble2[9] = 0.000000
    arrayOfVariantOfDouble2[10] = 6.320700
    arrayOfVariantOfDouble2[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble2)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble3[0] = 1.000000
    arrayOfVariantOfDouble3[1] = 0.000000
    arrayOfVariantOfDouble3[2] = 0.000000
    arrayOfVariantOfDouble3[3] = 0.000000
    arrayOfVariantOfDouble3[4] = 1.000000
    arrayOfVariantOfDouble3[5] = 0.000000
    arrayOfVariantOfDouble3[6] = 0.000000
    arrayOfVariantOfDouble3[7] = 0.000000
    arrayOfVariantOfDouble3[8] = 1.000000
    arrayOfVariantOfDouble3[9] = 0.000000
    arrayOfVariantOfDouble3[10] = 6.470662
    arrayOfVariantOfDouble3[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble3)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble4[0] = 1.000000
    arrayOfVariantOfDouble4[1] = 0.000000
    arrayOfVariantOfDouble4[2] = 0.000000
    arrayOfVariantOfDouble4[3] = 0.000000
    arrayOfVariantOfDouble4[4] = 1.000000
    arrayOfVariantOfDouble4[5] = 0.000000
    arrayOfVariantOfDouble4[6] = 0.000000
    arrayOfVariantOfDouble4[7] = 0.000000
    arrayOfVariantOfDouble4[8] = 1.000000
    arrayOfVariantOfDouble4[9] = 0.000000
    arrayOfVariantOfDouble4[10] = 6.320710
    arrayOfVariantOfDouble4[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble4)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble5[0] = 1.000000
    arrayOfVariantOfDouble5[1] = 0.000000
    arrayOfVariantOfDouble5[2] = 0.000000
    arrayOfVariantOfDouble5[3] = 0.000000
    arrayOfVariantOfDouble5[4] = 1.000000
    arrayOfVariantOfDouble5[5] = 0.000000
    arrayOfVariantOfDouble5[6] = 0.000000
    arrayOfVariantOfDouble5[7] = 0.000000
    arrayOfVariantOfDouble5[8] = 1.000000
    arrayOfVariantOfDouble5[9] = 0.000000
    arrayOfVariantOfDouble5[10] = 26.504033
    arrayOfVariantOfDouble5[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble5)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble6[0] = 1.000000
    arrayOfVariantOfDouble6[1] = 0.000000
    arrayOfVariantOfDouble6[2] = 0.000000
    arrayOfVariantOfDouble6[3] = 0.000000
    arrayOfVariantOfDouble6[4] = 1.000000
    arrayOfVariantOfDouble6[5] = 0.000000
    arrayOfVariantOfDouble6[6] = 0.000000
    arrayOfVariantOfDouble6[7] = 0.000000
    arrayOfVariantOfDouble6[8] = 1.000000
    arrayOfVariantOfDouble6[9] = 0.000000
    arrayOfVariantOfDouble6[10] = 28.346650
    arrayOfVariantOfDouble6[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble6)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble7[0] = 1.000000
    arrayOfVariantOfDouble7[1] = 0.000000
    arrayOfVariantOfDouble7[2] = 0.000000
    arrayOfVariantOfDouble7[3] = 0.000000
    arrayOfVariantOfDouble7[4] = 1.000000
    arrayOfVariantOfDouble7[5] = 0.000000
    arrayOfVariantOfDouble7[6] = 0.000000
    arrayOfVariantOfDouble7[7] = 0.000000
    arrayOfVariantOfDouble7[8] = 1.000000
    arrayOfVariantOfDouble7[9] = 0.000000
    arrayOfVariantOfDouble7[10] = 39.445369
    arrayOfVariantOfDouble7[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble7)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble8[0] = 1.000000
    arrayOfVariantOfDouble8[1] = 0.000000
    arrayOfVariantOfDouble8[2] = 0.000000
    arrayOfVariantOfDouble8[3] = 0.000000
    arrayOfVariantOfDouble8[4] = 1.000000
    arrayOfVariantOfDouble8[5] = 0.000000
    arrayOfVariantOfDouble8[6] = 0.000000
    arrayOfVariantOfDouble8[7] = 0.000000
    arrayOfVariantOfDouble8[8] = 1.000000
    arrayOfVariantOfDouble8[9] = 0.000000
    arrayOfVariantOfDouble8[10] = 39.123874
    arrayOfVariantOfDouble8[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble8)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble9[0] = 1.000000
    arrayOfVariantOfDouble9[1] = 0.000000
    arrayOfVariantOfDouble9[2] = 0.000000
    arrayOfVariantOfDouble9[3] = 0.000000
    arrayOfVariantOfDouble9[4] = 1.000000
    arrayOfVariantOfDouble9[5] = 0.000000
    arrayOfVariantOfDouble9[6] = 0.000000
    arrayOfVariantOfDouble9[7] = 0.000000
    arrayOfVariantOfDouble9[8] = 1.000000
    arrayOfVariantOfDouble9[9] = 0.000000
    arrayOfVariantOfDouble9[10] = 34.645780
    arrayOfVariantOfDouble9[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble9)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble10[0] = 1.000000
    arrayOfVariantOfDouble10[1] = 0.000000
    arrayOfVariantOfDouble10[2] = 0.000000
    arrayOfVariantOfDouble10[3] = 0.000000
    arrayOfVariantOfDouble10[4] = 1.000000
    arrayOfVariantOfDouble10[5] = 0.000000
    arrayOfVariantOfDouble10[6] = 0.000000
    arrayOfVariantOfDouble10[7] = 0.000000
    arrayOfVariantOfDouble10[8] = 1.000000
    arrayOfVariantOfDouble10[9] = 0.000000
    arrayOfVariantOfDouble10[10] = 20.954677
    arrayOfVariantOfDouble10[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble10)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble11[0] = 1.000000
    arrayOfVariantOfDouble11[1] = 0.000000
    arrayOfVariantOfDouble11[2] = 0.000000
    arrayOfVariantOfDouble11[3] = 0.000000
    arrayOfVariantOfDouble11[4] = 1.000000
    arrayOfVariantOfDouble11[5] = 0.000000
    arrayOfVariantOfDouble11[6] = 0.000000
    arrayOfVariantOfDouble11[7] = 0.000000
    arrayOfVariantOfDouble11[8] = 1.000000
    arrayOfVariantOfDouble11[9] = 0.000000
    arrayOfVariantOfDouble11[10] = 12.941347
    arrayOfVariantOfDouble11[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble11)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble12[0] = 1.000000
    arrayOfVariantOfDouble12[1] = 0.000000
    arrayOfVariantOfDouble12[2] = 0.000000
    arrayOfVariantOfDouble12[3] = 0.000000
    arrayOfVariantOfDouble12[4] = 1.000000
    arrayOfVariantOfDouble12[5] = 0.000000
    arrayOfVariantOfDouble12[6] = 0.000000
    arrayOfVariantOfDouble12[7] = 0.000000
    arrayOfVariantOfDouble12[8] = 1.000000
    arrayOfVariantOfDouble12[9] = 0.000000
    arrayOfVariantOfDouble12[10] = 7.863392
    arrayOfVariantOfDouble12[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble12)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble13[0] = 1.000000
    arrayOfVariantOfDouble13[1] = 0.000000
    arrayOfVariantOfDouble13[2] = 0.000000
    arrayOfVariantOfDouble13[3] = 0.000000
    arrayOfVariantOfDouble13[4] = 1.000000
    arrayOfVariantOfDouble13[5] = 0.000000
    arrayOfVariantOfDouble13[6] = 0.000000
    arrayOfVariantOfDouble13[7] = 0.000000
    arrayOfVariantOfDouble13[8] = 1.000000
    arrayOfVariantOfDouble13[9] = 0.000000
    arrayOfVariantOfDouble13[10] = 6.770583
    arrayOfVariantOfDouble13[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble13)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble14[0] = 1.000000
    arrayOfVariantOfDouble14[1] = 0.000000
    arrayOfVariantOfDouble14[2] = 0.000000
    arrayOfVariantOfDouble14[3] = 0.000000
    arrayOfVariantOfDouble14[4] = 1.000000
    arrayOfVariantOfDouble14[5] = 0.000000
    arrayOfVariantOfDouble14[6] = 0.000000
    arrayOfVariantOfDouble14[7] = 0.000000
    arrayOfVariantOfDouble14[8] = 1.000000
    arrayOfVariantOfDouble14[9] = 0.000000
    arrayOfVariantOfDouble14[10] = 4.927978
    arrayOfVariantOfDouble14[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble14)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble15[0] = 1.000000
    arrayOfVariantOfDouble15[1] = 0.000000
    arrayOfVariantOfDouble15[2] = 0.000000
    arrayOfVariantOfDouble15[3] = 0.000000
    arrayOfVariantOfDouble15[4] = 1.000000
    arrayOfVariantOfDouble15[5] = 0.000000
    arrayOfVariantOfDouble15[6] = 0.000000
    arrayOfVariantOfDouble15[7] = 0.000000
    arrayOfVariantOfDouble15[8] = 1.000000
    arrayOfVariantOfDouble15[9] = 0.000000
    arrayOfVariantOfDouble15[10] = 2.613916
    arrayOfVariantOfDouble15[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble15)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble16[0] = 1.000000
    arrayOfVariantOfDouble16[1] = 0.000000
    arrayOfVariantOfDouble16[2] = 0.000000
    arrayOfVariantOfDouble16[3] = 0.000000
    arrayOfVariantOfDouble16[4] = 1.000000
    arrayOfVariantOfDouble16[5] = 0.000000
    arrayOfVariantOfDouble16[6] = 0.000000
    arrayOfVariantOfDouble16[7] = 0.000000
    arrayOfVariantOfDouble16[8] = 1.000000
    arrayOfVariantOfDouble16[9] = 0.000000
    arrayOfVariantOfDouble16[10] = 4.006690
    arrayOfVariantOfDouble16[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble16)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble17[0] = 1.000000
    arrayOfVariantOfDouble17[1] = 0.000000
    arrayOfVariantOfDouble17[2] = 0.000000
    arrayOfVariantOfDouble17[3] = 0.000000
    arrayOfVariantOfDouble17[4] = 1.000000
    arrayOfVariantOfDouble17[5] = 0.000000
    arrayOfVariantOfDouble17[6] = 0.000000
    arrayOfVariantOfDouble17[7] = 0.000000
    arrayOfVariantOfDouble17[8] = 1.000000
    arrayOfVariantOfDouble17[9] = 0.000000
    arrayOfVariantOfDouble17[10] = 0.771333
    arrayOfVariantOfDouble17[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble17)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble18[0] = 1.000000
    arrayOfVariantOfDouble18[1] = 0.000000
    arrayOfVariantOfDouble18[2] = 0.000000
    arrayOfVariantOfDouble18[3] = 0.000000
    arrayOfVariantOfDouble18[4] = 1.000000
    arrayOfVariantOfDouble18[5] = 0.000000
    arrayOfVariantOfDouble18[6] = 0.000000
    arrayOfVariantOfDouble18[7] = 0.000000
    arrayOfVariantOfDouble18[8] = 1.000000
    arrayOfVariantOfDouble18[9] = 0.000000
    arrayOfVariantOfDouble18[10] = 2.464004
    arrayOfVariantOfDouble18[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble18)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble19[0] = 1.000000
    arrayOfVariantOfDouble19[1] = 0.000000
    arrayOfVariantOfDouble19[2] = 0.000000
    arrayOfVariantOfDouble19[3] = 0.000000
    arrayOfVariantOfDouble19[4] = 1.000000
    arrayOfVariantOfDouble19[5] = 0.000000
    arrayOfVariantOfDouble19[6] = 0.000000
    arrayOfVariantOfDouble19[7] = 0.000000
    arrayOfVariantOfDouble19[8] = 1.000000
    arrayOfVariantOfDouble19[9] = 0.000000
    arrayOfVariantOfDouble19[10] = 0.921289
    arrayOfVariantOfDouble19[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble19)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble20[0] = 1.000000
    arrayOfVariantOfDouble20[1] = 0.000000
    arrayOfVariantOfDouble20[2] = 0.000000
    arrayOfVariantOfDouble20[3] = 0.000000
    arrayOfVariantOfDouble20[4] = 1.000000
    arrayOfVariantOfDouble20[5] = 0.000000
    arrayOfVariantOfDouble20[6] = 0.000000
    arrayOfVariantOfDouble20[7] = 0.000000
    arrayOfVariantOfDouble20[8] = 1.000000
    arrayOfVariantOfDouble20[9] = 0.000000
    arrayOfVariantOfDouble20[10] = 1.692642
    arrayOfVariantOfDouble20[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble20)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble21[0] = 1.000000
    arrayOfVariantOfDouble21[1] = 0.000000
    arrayOfVariantOfDouble21[2] = 0.000000
    arrayOfVariantOfDouble21[3] = 0.000000
    arrayOfVariantOfDouble21[4] = 1.000000
    arrayOfVariantOfDouble21[5] = 0.000000
    arrayOfVariantOfDouble21[6] = 0.000000
    arrayOfVariantOfDouble21[7] = 0.000000
    arrayOfVariantOfDouble21[8] = 1.000000
    arrayOfVariantOfDouble21[9] = 0.000000
    arrayOfVariantOfDouble21[10] = 1.692636
    arrayOfVariantOfDouble21[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble21)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble22[0] = 1.000000
    arrayOfVariantOfDouble22[1] = 0.000000
    arrayOfVariantOfDouble22[2] = 0.000000
    arrayOfVariantOfDouble22[3] = 0.000000
    arrayOfVariantOfDouble22[4] = 1.000000
    arrayOfVariantOfDouble22[5] = 0.000000
    arrayOfVariantOfDouble22[6] = 0.000000
    arrayOfVariantOfDouble22[7] = 0.000000
    arrayOfVariantOfDouble22[8] = 1.000000
    arrayOfVariantOfDouble22[9] = 0.000000
    arrayOfVariantOfDouble22[10] = 0.771361
    arrayOfVariantOfDouble22[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble22)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble23[0] = 1.000000
    arrayOfVariantOfDouble23[1] = 0.000000
    arrayOfVariantOfDouble23[2] = 0.000000
    arrayOfVariantOfDouble23[3] = 0.000000
    arrayOfVariantOfDouble23[4] = 1.000000
    arrayOfVariantOfDouble23[5] = 0.000000
    arrayOfVariantOfDouble23[6] = 0.000000
    arrayOfVariantOfDouble23[7] = 0.000000
    arrayOfVariantOfDouble23[8] = 1.000000
    arrayOfVariantOfDouble23[9] = 0.000000
    arrayOfVariantOfDouble23[10] = 0.921279
    arrayOfVariantOfDouble23[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble23)
    move1 = product2.Move
    move1 = move1.MovableObject
    arrayOfVariantOfDouble24[0] = 1.000000
    arrayOfVariantOfDouble24[1] = 0.000000
    arrayOfVariantOfDouble24[2] = 0.000000
    arrayOfVariantOfDouble24[3] = 0.000000
    arrayOfVariantOfDouble24[4] = 1.000000
    arrayOfVariantOfDouble24[5] = 0.000000
    arrayOfVariantOfDouble24[6] = 0.000000
    arrayOfVariantOfDouble24[7] = 0.000000
    arrayOfVariantOfDouble24[8] = 1.000000
    arrayOfVariantOfDouble24[9] = 0.000000
    arrayOfVariantOfDouble24[10] = 2.314049
    arrayOfVariantOfDouble24[11] = 0.000000
    move1.Apply(arrayOfVariantOfDouble24)
    product3 = products1.Item('Part3.1')
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble25[0] = 1.000000
    arrayOfVariantOfDouble25[1] = 0.000000
    arrayOfVariantOfDouble25[2] = 0.000000
    arrayOfVariantOfDouble25[3] = 0.000000
    arrayOfVariantOfDouble25[4] = 1.000000
    arrayOfVariantOfDouble25[5] = 0.000000
    arrayOfVariantOfDouble25[6] = 0.000000
    arrayOfVariantOfDouble25[7] = 0.000000
    arrayOfVariantOfDouble25[8] = 1.000000
    arrayOfVariantOfDouble25[9] = 0.000000
    arrayOfVariantOfDouble25[10] = - 4.879389
    arrayOfVariantOfDouble25[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble25)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble26[0] = 1.000000
    arrayOfVariantOfDouble26[1] = 0.000000
    arrayOfVariantOfDouble26[2] = 0.000000
    arrayOfVariantOfDouble26[3] = 0.000000
    arrayOfVariantOfDouble26[4] = 1.000000
    arrayOfVariantOfDouble26[5] = 0.000000
    arrayOfVariantOfDouble26[6] = 0.000000
    arrayOfVariantOfDouble26[7] = 0.000000
    arrayOfVariantOfDouble26[8] = 1.000000
    arrayOfVariantOfDouble26[9] = 0.000000
    arrayOfVariantOfDouble26[10] = - 13.884179
    arrayOfVariantOfDouble26[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble26)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble27[0] = 1.000000
    arrayOfVariantOfDouble27[1] = 0.000000
    arrayOfVariantOfDouble27[2] = 0.000000
    arrayOfVariantOfDouble27[3] = 0.000000
    arrayOfVariantOfDouble27[4] = 1.000000
    arrayOfVariantOfDouble27[5] = 0.000000
    arrayOfVariantOfDouble27[6] = 0.000000
    arrayOfVariantOfDouble27[7] = 0.000000
    arrayOfVariantOfDouble27[8] = 1.000000
    arrayOfVariantOfDouble27[9] = 0.000000
    arrayOfVariantOfDouble27[10] = - 14.805492
    arrayOfVariantOfDouble27[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble27)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble28[0] = 1.000000
    arrayOfVariantOfDouble28[1] = 0.000000
    arrayOfVariantOfDouble28[2] = 0.000000
    arrayOfVariantOfDouble28[3] = 0.000000
    arrayOfVariantOfDouble28[4] = 1.000000
    arrayOfVariantOfDouble28[5] = 0.000000
    arrayOfVariantOfDouble28[6] = 0.000000
    arrayOfVariantOfDouble28[7] = 0.000000
    arrayOfVariantOfDouble28[8] = 1.000000
    arrayOfVariantOfDouble28[9] = 0.000000
    arrayOfVariantOfDouble28[10] = - 52.451370
    arrayOfVariantOfDouble28[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble28)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble29[0] = 1.000000
    arrayOfVariantOfDouble29[1] = 0.000000
    arrayOfVariantOfDouble29[2] = 0.000000
    arrayOfVariantOfDouble29[3] = 0.000000
    arrayOfVariantOfDouble29[4] = 1.000000
    arrayOfVariantOfDouble29[5] = 0.000000
    arrayOfVariantOfDouble29[6] = 0.000000
    arrayOfVariantOfDouble29[7] = 0.000000
    arrayOfVariantOfDouble29[8] = 1.000000
    arrayOfVariantOfDouble29[9] = 0.000000
    arrayOfVariantOfDouble29[10] = - 42.573862
    arrayOfVariantOfDouble29[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble29)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble30[0] = 1.000000
    arrayOfVariantOfDouble30[1] = 0.000000
    arrayOfVariantOfDouble30[2] = 0.000000
    arrayOfVariantOfDouble30[3] = 0.000000
    arrayOfVariantOfDouble30[4] = 1.000000
    arrayOfVariantOfDouble30[5] = 0.000000
    arrayOfVariantOfDouble30[6] = 0.000000
    arrayOfVariantOfDouble30[7] = 0.000000
    arrayOfVariantOfDouble30[8] = 1.000000
    arrayOfVariantOfDouble30[9] = 0.000000
    arrayOfVariantOfDouble30[10] = - 22.818851
    arrayOfVariantOfDouble30[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble30)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble31[0] = 1.000000
    arrayOfVariantOfDouble31[1] = 0.000000
    arrayOfVariantOfDouble31[2] = 0.000000
    arrayOfVariantOfDouble31[3] = 0.000000
    arrayOfVariantOfDouble31[4] = 1.000000
    arrayOfVariantOfDouble31[5] = 0.000000
    arrayOfVariantOfDouble31[6] = 0.000000
    arrayOfVariantOfDouble31[7] = 0.000000
    arrayOfVariantOfDouble31[8] = 1.000000
    arrayOfVariantOfDouble31[9] = 0.000000
    arrayOfVariantOfDouble31[10] = - 18.040807
    arrayOfVariantOfDouble31[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble31)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble32[0] = 1.000000
    arrayOfVariantOfDouble32[1] = 0.000000
    arrayOfVariantOfDouble32[2] = 0.000000
    arrayOfVariantOfDouble32[3] = 0.000000
    arrayOfVariantOfDouble32[4] = 1.000000
    arrayOfVariantOfDouble32[5] = 0.000000
    arrayOfVariantOfDouble32[6] = 0.000000
    arrayOfVariantOfDouble32[7] = 0.000000
    arrayOfVariantOfDouble32[8] = 1.000000
    arrayOfVariantOfDouble32[9] = 0.000000
    arrayOfVariantOfDouble32[10] = - 17.740907
    arrayOfVariantOfDouble32[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble32)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble33[0] = 1.000000
    arrayOfVariantOfDouble33[1] = 0.000000
    arrayOfVariantOfDouble33[2] = 0.000000
    arrayOfVariantOfDouble33[3] = 0.000000
    arrayOfVariantOfDouble33[4] = 1.000000
    arrayOfVariantOfDouble33[5] = 0.000000
    arrayOfVariantOfDouble33[6] = 0.000000
    arrayOfVariantOfDouble33[7] = 0.000000
    arrayOfVariantOfDouble33[8] = 1.000000
    arrayOfVariantOfDouble33[9] = 0.000000
    arrayOfVariantOfDouble33[10] = - 6.170759
    arrayOfVariantOfDouble33[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble33)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble34[0] = 1.000000
    arrayOfVariantOfDouble34[1] = 0.000000
    arrayOfVariantOfDouble34[2] = 0.000000
    arrayOfVariantOfDouble34[3] = 0.000000
    arrayOfVariantOfDouble34[4] = 1.000000
    arrayOfVariantOfDouble34[5] = 0.000000
    arrayOfVariantOfDouble34[6] = 0.000000
    arrayOfVariantOfDouble34[7] = 0.000000
    arrayOfVariantOfDouble34[8] = 1.000000
    arrayOfVariantOfDouble34[9] = 0.000000
    arrayOfVariantOfDouble34[10] = - 4.628060
    arrayOfVariantOfDouble34[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble34)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble35[0] = 1.000000
    arrayOfVariantOfDouble35[1] = 0.000000
    arrayOfVariantOfDouble35[2] = 0.000000
    arrayOfVariantOfDouble35[3] = 0.000000
    arrayOfVariantOfDouble35[4] = 1.000000
    arrayOfVariantOfDouble35[5] = 0.000000
    arrayOfVariantOfDouble35[6] = 0.000000
    arrayOfVariantOfDouble35[7] = 0.000000
    arrayOfVariantOfDouble35[8] = 1.000000
    arrayOfVariantOfDouble35[9] = 0.000000
    arrayOfVariantOfDouble35[10] = - 2.314020
    arrayOfVariantOfDouble35[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble35)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble36[0] = 1.000000
    arrayOfVariantOfDouble36[1] = 0.000000
    arrayOfVariantOfDouble36[2] = 0.000000
    arrayOfVariantOfDouble36[3] = 0.000000
    arrayOfVariantOfDouble36[4] = 1.000000
    arrayOfVariantOfDouble36[5] = 0.000000
    arrayOfVariantOfDouble36[6] = 0.000000
    arrayOfVariantOfDouble36[7] = 0.000000
    arrayOfVariantOfDouble36[8] = 1.000000
    arrayOfVariantOfDouble36[9] = 0.000000
    arrayOfVariantOfDouble36[10] = - 8.034918
    arrayOfVariantOfDouble36[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble36)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble37[0] = 1.000000
    arrayOfVariantOfDouble37[1] = 0.000000
    arrayOfVariantOfDouble37[2] = 0.000000
    arrayOfVariantOfDouble37[3] = 0.000000
    arrayOfVariantOfDouble37[4] = 1.000000
    arrayOfVariantOfDouble37[5] = 0.000000
    arrayOfVariantOfDouble37[6] = 0.000000
    arrayOfVariantOfDouble37[7] = 0.000000
    arrayOfVariantOfDouble37[8] = 1.000000
    arrayOfVariantOfDouble37[9] = 0.000000
    arrayOfVariantOfDouble37[10] = - 3.556805
    arrayOfVariantOfDouble37[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble37)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble38[0] = 1.000000
    arrayOfVariantOfDouble38[1] = 0.000000
    arrayOfVariantOfDouble38[2] = 0.000000
    arrayOfVariantOfDouble38[3] = 0.000000
    arrayOfVariantOfDouble38[4] = 1.000000
    arrayOfVariantOfDouble38[5] = 0.000000
    arrayOfVariantOfDouble38[6] = 0.000000
    arrayOfVariantOfDouble38[7] = 0.000000
    arrayOfVariantOfDouble38[8] = 1.000000
    arrayOfVariantOfDouble38[9] = 0.000000
    arrayOfVariantOfDouble38[10] = - 4.328153
    arrayOfVariantOfDouble38[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble38)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble39[0] = 1.000000
    arrayOfVariantOfDouble39[1] = 0.000000
    arrayOfVariantOfDouble39[2] = 0.000000
    arrayOfVariantOfDouble39[3] = 0.000000
    arrayOfVariantOfDouble39[4] = 1.000000
    arrayOfVariantOfDouble39[5] = 0.000000
    arrayOfVariantOfDouble39[6] = 0.000000
    arrayOfVariantOfDouble39[7] = 0.000000
    arrayOfVariantOfDouble39[8] = 1.000000
    arrayOfVariantOfDouble39[9] = 0.000000
    arrayOfVariantOfDouble39[10] = - 3.706764
    arrayOfVariantOfDouble39[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble39)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble40[0] = 1.000000
    arrayOfVariantOfDouble40[1] = 0.000000
    arrayOfVariantOfDouble40[2] = 0.000000
    arrayOfVariantOfDouble40[3] = 0.000000
    arrayOfVariantOfDouble40[4] = 1.000000
    arrayOfVariantOfDouble40[5] = 0.000000
    arrayOfVariantOfDouble40[6] = 0.000000
    arrayOfVariantOfDouble40[7] = 0.000000
    arrayOfVariantOfDouble40[8] = 1.000000
    arrayOfVariantOfDouble40[9] = 0.000000
    arrayOfVariantOfDouble40[10] = - 3.406842
    arrayOfVariantOfDouble40[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble40)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble41[0] = 1.000000
    arrayOfVariantOfDouble41[1] = 0.000000
    arrayOfVariantOfDouble41[2] = 0.000000
    arrayOfVariantOfDouble41[3] = 0.000000
    arrayOfVariantOfDouble41[4] = 1.000000
    arrayOfVariantOfDouble41[5] = 0.000000
    arrayOfVariantOfDouble41[6] = 0.000000
    arrayOfVariantOfDouble41[7] = 0.000000
    arrayOfVariantOfDouble41[8] = 1.000000
    arrayOfVariantOfDouble41[9] = 0.000000
    arrayOfVariantOfDouble41[10] = - 2.164078
    arrayOfVariantOfDouble41[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble41)
    move2 = product3.Move
    move2 = move2.MovableObject
    arrayOfVariantOfDouble42[0] = 1.000000
    arrayOfVariantOfDouble42[1] = 0.000000
    arrayOfVariantOfDouble42[2] = 0.000000
    arrayOfVariantOfDouble42[3] = 0.000000
    arrayOfVariantOfDouble42[4] = 1.000000
    arrayOfVariantOfDouble42[5] = 0.000000
    arrayOfVariantOfDouble42[6] = 0.000000
    arrayOfVariantOfDouble42[7] = 0.000000
    arrayOfVariantOfDouble42[8] = 1.000000
    arrayOfVariantOfDouble42[9] = 0.000000
    arrayOfVariantOfDouble42[10] = - 0.771354
    arrayOfVariantOfDouble42[11] = 0.000000
    move2.Apply(arrayOfVariantOfDouble42)
    product4 = products1.Item('Part4.1')
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble43[0] = 1.000000
    arrayOfVariantOfDouble43[1] = 0.000000
    arrayOfVariantOfDouble43[2] = 0.000000
    arrayOfVariantOfDouble43[3] = 0.000000
    arrayOfVariantOfDouble43[4] = 1.000000
    arrayOfVariantOfDouble43[5] = 0.000000
    arrayOfVariantOfDouble43[6] = 0.000000
    arrayOfVariantOfDouble43[7] = 0.000000
    arrayOfVariantOfDouble43[8] = 1.000000
    arrayOfVariantOfDouble43[9] = 0.000000
    arrayOfVariantOfDouble43[10] = - 3.169412
    arrayOfVariantOfDouble43[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble43)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble44[0] = 1.000000
    arrayOfVariantOfDouble44[1] = 0.000000
    arrayOfVariantOfDouble44[2] = 0.000000
    arrayOfVariantOfDouble44[3] = 0.000000
    arrayOfVariantOfDouble44[4] = 1.000000
    arrayOfVariantOfDouble44[5] = 0.000000
    arrayOfVariantOfDouble44[6] = 0.000000
    arrayOfVariantOfDouble44[7] = 0.000000
    arrayOfVariantOfDouble44[8] = 1.000000
    arrayOfVariantOfDouble44[9] = 0.000000
    arrayOfVariantOfDouble44[10] = - 1.542688
    arrayOfVariantOfDouble44[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble44)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble45[0] = 1.000000
    arrayOfVariantOfDouble45[1] = 0.000000
    arrayOfVariantOfDouble45[2] = 0.000000
    arrayOfVariantOfDouble45[3] = 0.000000
    arrayOfVariantOfDouble45[4] = 1.000000
    arrayOfVariantOfDouble45[5] = 0.000000
    arrayOfVariantOfDouble45[6] = 0.000000
    arrayOfVariantOfDouble45[7] = 0.000000
    arrayOfVariantOfDouble45[8] = 1.000000
    arrayOfVariantOfDouble45[9] = 0.000000
    arrayOfVariantOfDouble45[10] = - 1.542697
    arrayOfVariantOfDouble45[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble45)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble46[0] = 1.000000
    arrayOfVariantOfDouble46[1] = 0.000000
    arrayOfVariantOfDouble46[2] = 0.000000
    arrayOfVariantOfDouble46[3] = 0.000000
    arrayOfVariantOfDouble46[4] = 1.000000
    arrayOfVariantOfDouble46[5] = 0.000000
    arrayOfVariantOfDouble46[6] = 0.000000
    arrayOfVariantOfDouble46[7] = 0.000000
    arrayOfVariantOfDouble46[8] = 1.000000
    arrayOfVariantOfDouble46[9] = 0.000000
    arrayOfVariantOfDouble46[10] = - 0.771345
    arrayOfVariantOfDouble46[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble46)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble47[0] = 1.000000
    arrayOfVariantOfDouble47[1] = 0.000000
    arrayOfVariantOfDouble47[2] = 0.000000
    arrayOfVariantOfDouble47[3] = 0.000000
    arrayOfVariantOfDouble47[4] = 1.000000
    arrayOfVariantOfDouble47[5] = 0.000000
    arrayOfVariantOfDouble47[6] = 0.000000
    arrayOfVariantOfDouble47[7] = 0.000000
    arrayOfVariantOfDouble47[8] = 1.000000
    arrayOfVariantOfDouble47[9] = 0.000000
    arrayOfVariantOfDouble47[10] = - 4.006666
    arrayOfVariantOfDouble47[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble47)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble48[0] = 1.000000
    arrayOfVariantOfDouble48[1] = 0.000000
    arrayOfVariantOfDouble48[2] = 0.000000
    arrayOfVariantOfDouble48[3] = 0.000000
    arrayOfVariantOfDouble48[4] = 1.000000
    arrayOfVariantOfDouble48[5] = 0.000000
    arrayOfVariantOfDouble48[6] = 0.000000
    arrayOfVariantOfDouble48[7] = 0.000000
    arrayOfVariantOfDouble48[8] = 1.000000
    arrayOfVariantOfDouble48[9] = 0.000000
    arrayOfVariantOfDouble48[10] = - 1.692644
    arrayOfVariantOfDouble48[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble48)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble49[0] = 1.000000
    arrayOfVariantOfDouble49[1] = 0.000000
    arrayOfVariantOfDouble49[2] = 0.000000
    arrayOfVariantOfDouble49[3] = 0.000000
    arrayOfVariantOfDouble49[4] = 1.000000
    arrayOfVariantOfDouble49[5] = 0.000000
    arrayOfVariantOfDouble49[6] = 0.000000
    arrayOfVariantOfDouble49[7] = 0.000000
    arrayOfVariantOfDouble49[8] = 1.000000
    arrayOfVariantOfDouble49[9] = 0.000000
    arrayOfVariantOfDouble49[10] = - 0.921312
    arrayOfVariantOfDouble49[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble49)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble50[0] = 1.000000
    arrayOfVariantOfDouble50[1] = 0.000000
    arrayOfVariantOfDouble50[2] = 0.000000
    arrayOfVariantOfDouble50[3] = 0.000000
    arrayOfVariantOfDouble50[4] = 1.000000
    arrayOfVariantOfDouble50[5] = 0.000000
    arrayOfVariantOfDouble50[6] = 0.000000
    arrayOfVariantOfDouble50[7] = 0.000000
    arrayOfVariantOfDouble50[8] = 1.000000
    arrayOfVariantOfDouble50[9] = 0.000000
    arrayOfVariantOfDouble50[10] = - 2.314024
    arrayOfVariantOfDouble50[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble50)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble51[0] = 1.000000
    arrayOfVariantOfDouble51[1] = 0.000000
    arrayOfVariantOfDouble51[2] = 0.000000
    arrayOfVariantOfDouble51[3] = 0.000000
    arrayOfVariantOfDouble51[4] = 1.000000
    arrayOfVariantOfDouble51[5] = 0.000000
    arrayOfVariantOfDouble51[6] = 0.000000
    arrayOfVariantOfDouble51[7] = 0.000000
    arrayOfVariantOfDouble51[8] = 1.000000
    arrayOfVariantOfDouble51[9] = 0.000000
    arrayOfVariantOfDouble51[10] = - 3.856720
    arrayOfVariantOfDouble51[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble51)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble52[0] = 1.000000
    arrayOfVariantOfDouble52[1] = 0.000000
    arrayOfVariantOfDouble52[2] = 0.000000
    arrayOfVariantOfDouble52[3] = 0.000000
    arrayOfVariantOfDouble52[4] = 1.000000
    arrayOfVariantOfDouble52[5] = 0.000000
    arrayOfVariantOfDouble52[6] = 0.000000
    arrayOfVariantOfDouble52[7] = 0.000000
    arrayOfVariantOfDouble52[8] = 1.000000
    arrayOfVariantOfDouble52[9] = 0.000000
    arrayOfVariantOfDouble52[10] = - 1.692639
    arrayOfVariantOfDouble52[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble52)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble53[0] = 1.000000
    arrayOfVariantOfDouble53[1] = 0.000000
    arrayOfVariantOfDouble53[2] = 0.000000
    arrayOfVariantOfDouble53[3] = 0.000000
    arrayOfVariantOfDouble53[4] = 1.000000
    arrayOfVariantOfDouble53[5] = 0.000000
    arrayOfVariantOfDouble53[6] = 0.000000
    arrayOfVariantOfDouble53[7] = 0.000000
    arrayOfVariantOfDouble53[8] = 1.000000
    arrayOfVariantOfDouble53[9] = 0.000000
    arrayOfVariantOfDouble53[10] = - 2.613949
    arrayOfVariantOfDouble53[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble53)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble54[0] = 1.000000
    arrayOfVariantOfDouble54[1] = 0.000000
    arrayOfVariantOfDouble54[2] = 0.000000
    arrayOfVariantOfDouble54[3] = 0.000000
    arrayOfVariantOfDouble54[4] = 1.000000
    arrayOfVariantOfDouble54[5] = 0.000000
    arrayOfVariantOfDouble54[6] = 0.000000
    arrayOfVariantOfDouble54[7] = 0.000000
    arrayOfVariantOfDouble54[8] = 1.000000
    arrayOfVariantOfDouble54[9] = 0.000000
    arrayOfVariantOfDouble54[10] = - 2.463979
    arrayOfVariantOfDouble54[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble54)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble55[0] = 1.000000
    arrayOfVariantOfDouble55[1] = 0.000000
    arrayOfVariantOfDouble55[2] = 0.000000
    arrayOfVariantOfDouble55[3] = 0.000000
    arrayOfVariantOfDouble55[4] = 1.000000
    arrayOfVariantOfDouble55[5] = 0.000000
    arrayOfVariantOfDouble55[6] = 0.000000
    arrayOfVariantOfDouble55[7] = 0.000000
    arrayOfVariantOfDouble55[8] = 1.000000
    arrayOfVariantOfDouble55[9] = 0.000000
    arrayOfVariantOfDouble55[10] = - 6.170759
    arrayOfVariantOfDouble55[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble55)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble56[0] = 1.000000
    arrayOfVariantOfDouble56[1] = 0.000000
    arrayOfVariantOfDouble56[2] = 0.000000
    arrayOfVariantOfDouble56[3] = 0.000000
    arrayOfVariantOfDouble56[4] = 1.000000
    arrayOfVariantOfDouble56[5] = 0.000000
    arrayOfVariantOfDouble56[6] = 0.000000
    arrayOfVariantOfDouble56[7] = 0.000000
    arrayOfVariantOfDouble56[8] = 1.000000
    arrayOfVariantOfDouble56[9] = 0.000000
    arrayOfVariantOfDouble56[10] = - 3.856713
    arrayOfVariantOfDouble56[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble56)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble57[0] = 1.000000
    arrayOfVariantOfDouble57[1] = 0.000000
    arrayOfVariantOfDouble57[2] = 0.000000
    arrayOfVariantOfDouble57[3] = 0.000000
    arrayOfVariantOfDouble57[4] = 1.000000
    arrayOfVariantOfDouble57[5] = 0.000000
    arrayOfVariantOfDouble57[6] = 0.000000
    arrayOfVariantOfDouble57[7] = 0.000000
    arrayOfVariantOfDouble57[8] = 1.000000
    arrayOfVariantOfDouble57[9] = 0.000000
    arrayOfVariantOfDouble57[10] = - 2.463994
    arrayOfVariantOfDouble57[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble57)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble58[0] = 1.000000
    arrayOfVariantOfDouble58[1] = 0.000000
    arrayOfVariantOfDouble58[2] = 0.000000
    arrayOfVariantOfDouble58[3] = 0.000000
    arrayOfVariantOfDouble58[4] = 1.000000
    arrayOfVariantOfDouble58[5] = 0.000000
    arrayOfVariantOfDouble58[6] = 0.000000
    arrayOfVariantOfDouble58[7] = 0.000000
    arrayOfVariantOfDouble58[8] = 1.000000
    arrayOfVariantOfDouble58[9] = 0.000000
    arrayOfVariantOfDouble58[10] = - 2.463985
    arrayOfVariantOfDouble58[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble58)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble59[0] = 1.000000
    arrayOfVariantOfDouble59[1] = 0.000000
    arrayOfVariantOfDouble59[2] = 0.000000
    arrayOfVariantOfDouble59[3] = 0.000000
    arrayOfVariantOfDouble59[4] = 1.000000
    arrayOfVariantOfDouble59[5] = 0.000000
    arrayOfVariantOfDouble59[6] = 0.000000
    arrayOfVariantOfDouble59[7] = 0.000000
    arrayOfVariantOfDouble59[8] = 1.000000
    arrayOfVariantOfDouble59[9] = 0.000000
    arrayOfVariantOfDouble59[10] = - 4.778016
    arrayOfVariantOfDouble59[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble59)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble60[0] = 1.000000
    arrayOfVariantOfDouble60[1] = 0.000000
    arrayOfVariantOfDouble60[2] = 0.000000
    arrayOfVariantOfDouble60[3] = 0.000000
    arrayOfVariantOfDouble60[4] = 1.000000
    arrayOfVariantOfDouble60[5] = 0.000000
    arrayOfVariantOfDouble60[6] = 0.000000
    arrayOfVariantOfDouble60[7] = 0.000000
    arrayOfVariantOfDouble60[8] = 1.000000
    arrayOfVariantOfDouble60[9] = 0.000000
    arrayOfVariantOfDouble60[10] = - 0.771345
    arrayOfVariantOfDouble60[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble60)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble61[0] = 1.000000
    arrayOfVariantOfDouble61[1] = 0.000000
    arrayOfVariantOfDouble61[2] = 0.000000
    arrayOfVariantOfDouble61[3] = 0.000000
    arrayOfVariantOfDouble61[4] = 1.000000
    arrayOfVariantOfDouble61[5] = 0.000000
    arrayOfVariantOfDouble61[6] = 0.000000
    arrayOfVariantOfDouble61[7] = 0.000000
    arrayOfVariantOfDouble61[8] = 1.000000
    arrayOfVariantOfDouble61[9] = 0.000000
    arrayOfVariantOfDouble61[10] = - 2.463988
    arrayOfVariantOfDouble61[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble61)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble62[0] = 1.000000
    arrayOfVariantOfDouble62[1] = 0.000000
    arrayOfVariantOfDouble62[2] = 0.000000
    arrayOfVariantOfDouble62[3] = 0.000000
    arrayOfVariantOfDouble62[4] = 1.000000
    arrayOfVariantOfDouble62[5] = 0.000000
    arrayOfVariantOfDouble62[6] = 0.000000
    arrayOfVariantOfDouble62[7] = 0.000000
    arrayOfVariantOfDouble62[8] = 1.000000
    arrayOfVariantOfDouble62[9] = 0.000000
    arrayOfVariantOfDouble62[10] = - 0.771340
    arrayOfVariantOfDouble62[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble62)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble63[0] = 1.000000
    arrayOfVariantOfDouble63[1] = 0.000000
    arrayOfVariantOfDouble63[2] = 0.000000
    arrayOfVariantOfDouble63[3] = 0.000000
    arrayOfVariantOfDouble63[4] = 1.000000
    arrayOfVariantOfDouble63[5] = 0.000000
    arrayOfVariantOfDouble63[6] = 0.000000
    arrayOfVariantOfDouble63[7] = 0.000000
    arrayOfVariantOfDouble63[8] = 1.000000
    arrayOfVariantOfDouble63[9] = 0.000000
    arrayOfVariantOfDouble63[10] = - 0.921306
    arrayOfVariantOfDouble63[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble63)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble64[0] = 1.000000
    arrayOfVariantOfDouble64[1] = 0.000000
    arrayOfVariantOfDouble64[2] = 0.000000
    arrayOfVariantOfDouble64[3] = 0.000000
    arrayOfVariantOfDouble64[4] = 1.000000
    arrayOfVariantOfDouble64[5] = 0.000000
    arrayOfVariantOfDouble64[6] = 0.000000
    arrayOfVariantOfDouble64[7] = 0.000000
    arrayOfVariantOfDouble64[8] = 1.000000
    arrayOfVariantOfDouble64[9] = 0.000000
    arrayOfVariantOfDouble64[10] = - 3.235332
    arrayOfVariantOfDouble64[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble64)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble65[0] = 1.000000
    arrayOfVariantOfDouble65[1] = 0.000000
    arrayOfVariantOfDouble65[2] = 0.000000
    arrayOfVariantOfDouble65[3] = 0.000000
    arrayOfVariantOfDouble65[4] = 1.000000
    arrayOfVariantOfDouble65[5] = 0.000000
    arrayOfVariantOfDouble65[6] = 0.000000
    arrayOfVariantOfDouble65[7] = 0.000000
    arrayOfVariantOfDouble65[8] = 1.000000
    arrayOfVariantOfDouble65[9] = 0.000000
    arrayOfVariantOfDouble65[10] = - 0.771336
    arrayOfVariantOfDouble65[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble65)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble66[0] = 1.000000
    arrayOfVariantOfDouble66[1] = 0.000000
    arrayOfVariantOfDouble66[2] = 0.000000
    arrayOfVariantOfDouble66[3] = 0.000000
    arrayOfVariantOfDouble66[4] = 1.000000
    arrayOfVariantOfDouble66[5] = 0.000000
    arrayOfVariantOfDouble66[6] = 0.000000
    arrayOfVariantOfDouble66[7] = 0.000000
    arrayOfVariantOfDouble66[8] = 1.000000
    arrayOfVariantOfDouble66[9] = 0.000000
    arrayOfVariantOfDouble66[10] = - 0.771345
    arrayOfVariantOfDouble66[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble66)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble67[0] = 1.000000
    arrayOfVariantOfDouble67[1] = 0.000000
    arrayOfVariantOfDouble67[2] = 0.000000
    arrayOfVariantOfDouble67[3] = 0.000000
    arrayOfVariantOfDouble67[4] = 1.000000
    arrayOfVariantOfDouble67[5] = 0.000000
    arrayOfVariantOfDouble67[6] = 0.000000
    arrayOfVariantOfDouble67[7] = 0.000000
    arrayOfVariantOfDouble67[8] = 1.000000
    arrayOfVariantOfDouble67[9] = 0.000000
    arrayOfVariantOfDouble67[10] = - 0.149964
    arrayOfVariantOfDouble67[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble67)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble68[0] = 1.000000
    arrayOfVariantOfDouble68[1] = 0.000000
    arrayOfVariantOfDouble68[2] = 0.000000
    arrayOfVariantOfDouble68[3] = 0.000000
    arrayOfVariantOfDouble68[4] = 1.000000
    arrayOfVariantOfDouble68[5] = 0.000000
    arrayOfVariantOfDouble68[6] = 0.000000
    arrayOfVariantOfDouble68[7] = 0.000000
    arrayOfVariantOfDouble68[8] = 1.000000
    arrayOfVariantOfDouble68[9] = 0.000000
    arrayOfVariantOfDouble68[10] = - 0.771342
    arrayOfVariantOfDouble68[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble68)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble69[0] = 1.000000
    arrayOfVariantOfDouble69[1] = 0.000000
    arrayOfVariantOfDouble69[2] = 0.000000
    arrayOfVariantOfDouble69[3] = 0.000000
    arrayOfVariantOfDouble69[4] = 1.000000
    arrayOfVariantOfDouble69[5] = 0.000000
    arrayOfVariantOfDouble69[6] = 0.000000
    arrayOfVariantOfDouble69[7] = 0.000000
    arrayOfVariantOfDouble69[8] = 1.000000
    arrayOfVariantOfDouble69[9] = 0.000000
    arrayOfVariantOfDouble69[10] = - 3.235339
    arrayOfVariantOfDouble69[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble69)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble70[0] = 1.000000
    arrayOfVariantOfDouble70[1] = 0.000000
    arrayOfVariantOfDouble70[2] = 0.000000
    arrayOfVariantOfDouble70[3] = 0.000000
    arrayOfVariantOfDouble70[4] = 1.000000
    arrayOfVariantOfDouble70[5] = 0.000000
    arrayOfVariantOfDouble70[6] = 0.000000
    arrayOfVariantOfDouble70[7] = 0.000000
    arrayOfVariantOfDouble70[8] = 1.000000
    arrayOfVariantOfDouble70[9] = 0.000000
    arrayOfVariantOfDouble70[10] = - 1.692634
    arrayOfVariantOfDouble70[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble70)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble71[0] = 1.000000
    arrayOfVariantOfDouble71[1] = 0.000000
    arrayOfVariantOfDouble71[2] = 0.000000
    arrayOfVariantOfDouble71[3] = 0.000000
    arrayOfVariantOfDouble71[4] = 1.000000
    arrayOfVariantOfDouble71[5] = 0.000000
    arrayOfVariantOfDouble71[6] = 0.000000
    arrayOfVariantOfDouble71[7] = 0.000000
    arrayOfVariantOfDouble71[8] = 1.000000
    arrayOfVariantOfDouble71[9] = 0.000000
    arrayOfVariantOfDouble71[10] = - 7.241999
    arrayOfVariantOfDouble71[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble71)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble72[0] = 1.000000
    arrayOfVariantOfDouble72[1] = 0.000000
    arrayOfVariantOfDouble72[2] = 0.000000
    arrayOfVariantOfDouble72[3] = 0.000000
    arrayOfVariantOfDouble72[4] = 1.000000
    arrayOfVariantOfDouble72[5] = 0.000000
    arrayOfVariantOfDouble72[6] = 0.000000
    arrayOfVariantOfDouble72[7] = 0.000000
    arrayOfVariantOfDouble72[8] = 1.000000
    arrayOfVariantOfDouble72[9] = 0.000000
    arrayOfVariantOfDouble72[10] = - 5.699327
    arrayOfVariantOfDouble72[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble72)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble73[0] = 1.000000
    arrayOfVariantOfDouble73[1] = 0.000000
    arrayOfVariantOfDouble73[2] = 0.000000
    arrayOfVariantOfDouble73[3] = 0.000000
    arrayOfVariantOfDouble73[4] = 1.000000
    arrayOfVariantOfDouble73[5] = 0.000000
    arrayOfVariantOfDouble73[6] = 0.000000
    arrayOfVariantOfDouble73[7] = 0.000000
    arrayOfVariantOfDouble73[8] = 1.000000
    arrayOfVariantOfDouble73[9] = 0.000000
    arrayOfVariantOfDouble73[10] = - 7.391965
    arrayOfVariantOfDouble73[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble73)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble74[0] = 1.000000
    arrayOfVariantOfDouble74[1] = 0.000000
    arrayOfVariantOfDouble74[2] = 0.000000
    arrayOfVariantOfDouble74[3] = 0.000000
    arrayOfVariantOfDouble74[4] = 1.000000
    arrayOfVariantOfDouble74[5] = 0.000000
    arrayOfVariantOfDouble74[6] = 0.000000
    arrayOfVariantOfDouble74[7] = 0.000000
    arrayOfVariantOfDouble74[8] = 1.000000
    arrayOfVariantOfDouble74[9] = 0.000000
    arrayOfVariantOfDouble74[10] = - 5.549368
    arrayOfVariantOfDouble74[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble74)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble75[0] = 1.000000
    arrayOfVariantOfDouble75[1] = 0.000000
    arrayOfVariantOfDouble75[2] = 0.000000
    arrayOfVariantOfDouble75[3] = 0.000000
    arrayOfVariantOfDouble75[4] = 1.000000
    arrayOfVariantOfDouble75[5] = 0.000000
    arrayOfVariantOfDouble75[6] = 0.000000
    arrayOfVariantOfDouble75[7] = 0.000000
    arrayOfVariantOfDouble75[8] = 1.000000
    arrayOfVariantOfDouble75[9] = 0.000000
    arrayOfVariantOfDouble75[10] = - 6.470655
    arrayOfVariantOfDouble75[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble75)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble76[0] = 1.000000
    arrayOfVariantOfDouble76[1] = 0.000000
    arrayOfVariantOfDouble76[2] = 0.000000
    arrayOfVariantOfDouble76[3] = 0.000000
    arrayOfVariantOfDouble76[4] = 1.000000
    arrayOfVariantOfDouble76[5] = 0.000000
    arrayOfVariantOfDouble76[6] = 0.000000
    arrayOfVariantOfDouble76[7] = 0.000000
    arrayOfVariantOfDouble76[8] = 1.000000
    arrayOfVariantOfDouble76[9] = 0.000000
    arrayOfVariantOfDouble76[10] = - 5.699319
    arrayOfVariantOfDouble76[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble76)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble77[0] = 1.000000
    arrayOfVariantOfDouble77[1] = 0.000000
    arrayOfVariantOfDouble77[2] = 0.000000
    arrayOfVariantOfDouble77[3] = 0.000000
    arrayOfVariantOfDouble77[4] = 1.000000
    arrayOfVariantOfDouble77[5] = 0.000000
    arrayOfVariantOfDouble77[6] = 0.000000
    arrayOfVariantOfDouble77[7] = 0.000000
    arrayOfVariantOfDouble77[8] = 1.000000
    arrayOfVariantOfDouble77[9] = 0.000000
    arrayOfVariantOfDouble77[10] = - 7.092058
    arrayOfVariantOfDouble77[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble77)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble78[0] = 1.000000
    arrayOfVariantOfDouble78[1] = 0.000000
    arrayOfVariantOfDouble78[2] = 0.000000
    arrayOfVariantOfDouble78[3] = 0.000000
    arrayOfVariantOfDouble78[4] = 1.000000
    arrayOfVariantOfDouble78[5] = 0.000000
    arrayOfVariantOfDouble78[6] = 0.000000
    arrayOfVariantOfDouble78[7] = 0.000000
    arrayOfVariantOfDouble78[8] = 1.000000
    arrayOfVariantOfDouble78[9] = 0.000000
    arrayOfVariantOfDouble78[10] = - 4.156627
    arrayOfVariantOfDouble78[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble78)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble79[0] = 1.000000
    arrayOfVariantOfDouble79[1] = 0.000000
    arrayOfVariantOfDouble79[2] = 0.000000
    arrayOfVariantOfDouble79[3] = 0.000000
    arrayOfVariantOfDouble79[4] = 1.000000
    arrayOfVariantOfDouble79[5] = 0.000000
    arrayOfVariantOfDouble79[6] = 0.000000
    arrayOfVariantOfDouble79[7] = 0.000000
    arrayOfVariantOfDouble79[8] = 1.000000
    arrayOfVariantOfDouble79[9] = 0.000000
    arrayOfVariantOfDouble79[10] = - 4.006671
    arrayOfVariantOfDouble79[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble79)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble80[0] = 1.000000
    arrayOfVariantOfDouble80[1] = 0.000000
    arrayOfVariantOfDouble80[2] = 0.000000
    arrayOfVariantOfDouble80[3] = 0.000000
    arrayOfVariantOfDouble80[4] = 1.000000
    arrayOfVariantOfDouble80[5] = 0.000000
    arrayOfVariantOfDouble80[6] = 0.000000
    arrayOfVariantOfDouble80[7] = 0.000000
    arrayOfVariantOfDouble80[8] = 1.000000
    arrayOfVariantOfDouble80[9] = 0.000000
    arrayOfVariantOfDouble80[10] = - 1.692646
    arrayOfVariantOfDouble80[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble80)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble81[0] = 1.000000
    arrayOfVariantOfDouble81[1] = 0.000000
    arrayOfVariantOfDouble81[2] = 0.000000
    arrayOfVariantOfDouble81[3] = 0.000000
    arrayOfVariantOfDouble81[4] = 1.000000
    arrayOfVariantOfDouble81[5] = 0.000000
    arrayOfVariantOfDouble81[6] = 0.000000
    arrayOfVariantOfDouble81[7] = 0.000000
    arrayOfVariantOfDouble81[8] = 1.000000
    arrayOfVariantOfDouble81[9] = 0.000000
    arrayOfVariantOfDouble81[10] = - 2.463981
    arrayOfVariantOfDouble81[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble81)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble82[0] = 1.000000
    arrayOfVariantOfDouble82[1] = 0.000000
    arrayOfVariantOfDouble82[2] = 0.000000
    arrayOfVariantOfDouble82[3] = 0.000000
    arrayOfVariantOfDouble82[4] = 1.000000
    arrayOfVariantOfDouble82[5] = 0.000000
    arrayOfVariantOfDouble82[6] = 0.000000
    arrayOfVariantOfDouble82[7] = 0.000000
    arrayOfVariantOfDouble82[8] = 1.000000
    arrayOfVariantOfDouble82[9] = 0.000000
    arrayOfVariantOfDouble82[10] = - 1.542689
    arrayOfVariantOfDouble82[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble82)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble83[0] = 1.000000
    arrayOfVariantOfDouble83[1] = 0.000000
    arrayOfVariantOfDouble83[2] = 0.000000
    arrayOfVariantOfDouble83[3] = 0.000000
    arrayOfVariantOfDouble83[4] = 1.000000
    arrayOfVariantOfDouble83[5] = 0.000000
    arrayOfVariantOfDouble83[6] = 0.000000
    arrayOfVariantOfDouble83[7] = 0.000000
    arrayOfVariantOfDouble83[8] = 1.000000
    arrayOfVariantOfDouble83[9] = 0.000000
    arrayOfVariantOfDouble83[10] = - 0.771350
    arrayOfVariantOfDouble83[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble83)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble84[0] = 1.000000
    arrayOfVariantOfDouble84[1] = 0.000000
    arrayOfVariantOfDouble84[2] = 0.000000
    arrayOfVariantOfDouble84[3] = 0.000000
    arrayOfVariantOfDouble84[4] = 1.000000
    arrayOfVariantOfDouble84[5] = 0.000000
    arrayOfVariantOfDouble84[6] = 0.000000
    arrayOfVariantOfDouble84[7] = 0.000000
    arrayOfVariantOfDouble84[8] = 1.000000
    arrayOfVariantOfDouble84[9] = 0.000000
    arrayOfVariantOfDouble84[10] = - 0.149947
    arrayOfVariantOfDouble84[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble84)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble85[0] = 1.000000
    arrayOfVariantOfDouble85[1] = 0.000000
    arrayOfVariantOfDouble85[2] = 0.000000
    arrayOfVariantOfDouble85[3] = 0.000000
    arrayOfVariantOfDouble85[4] = 1.000000
    arrayOfVariantOfDouble85[5] = 0.000000
    arrayOfVariantOfDouble85[6] = 0.000000
    arrayOfVariantOfDouble85[7] = 0.000000
    arrayOfVariantOfDouble85[8] = 1.000000
    arrayOfVariantOfDouble85[9] = 0.000000
    arrayOfVariantOfDouble85[10] = - 0.771350
    arrayOfVariantOfDouble85[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble85)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble86[0] = 1.000000
    arrayOfVariantOfDouble86[1] = 0.000000
    arrayOfVariantOfDouble86[2] = 0.000000
    arrayOfVariantOfDouble86[3] = 0.000000
    arrayOfVariantOfDouble86[4] = 1.000000
    arrayOfVariantOfDouble86[5] = 0.000000
    arrayOfVariantOfDouble86[6] = 0.000000
    arrayOfVariantOfDouble86[7] = 0.000000
    arrayOfVariantOfDouble86[8] = 1.000000
    arrayOfVariantOfDouble86[9] = 0.000000
    arrayOfVariantOfDouble86[10] = - 2.314042
    arrayOfVariantOfDouble86[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble86)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble87[0] = 1.000000
    arrayOfVariantOfDouble87[1] = 0.000000
    arrayOfVariantOfDouble87[2] = 0.000000
    arrayOfVariantOfDouble87[3] = 0.000000
    arrayOfVariantOfDouble87[4] = 1.000000
    arrayOfVariantOfDouble87[5] = 0.000000
    arrayOfVariantOfDouble87[6] = 0.000000
    arrayOfVariantOfDouble87[7] = 0.000000
    arrayOfVariantOfDouble87[8] = 1.000000
    arrayOfVariantOfDouble87[9] = 0.000000
    arrayOfVariantOfDouble87[10] = - 1.542685
    arrayOfVariantOfDouble87[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble87)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble88[0] = 1.000000
    arrayOfVariantOfDouble88[1] = 0.000000
    arrayOfVariantOfDouble88[2] = 0.000000
    arrayOfVariantOfDouble88[3] = 0.000000
    arrayOfVariantOfDouble88[4] = 1.000000
    arrayOfVariantOfDouble88[5] = 0.000000
    arrayOfVariantOfDouble88[6] = 0.000000
    arrayOfVariantOfDouble88[7] = 0.000000
    arrayOfVariantOfDouble88[8] = 1.000000
    arrayOfVariantOfDouble88[9] = 0.000000
    arrayOfVariantOfDouble88[10] = - 4.778023
    arrayOfVariantOfDouble88[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble88)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble89[0] = 1.000000
    arrayOfVariantOfDouble89[1] = 0.000000
    arrayOfVariantOfDouble89[2] = 0.000000
    arrayOfVariantOfDouble89[3] = 0.000000
    arrayOfVariantOfDouble89[4] = 1.000000
    arrayOfVariantOfDouble89[5] = 0.000000
    arrayOfVariantOfDouble89[6] = 0.000000
    arrayOfVariantOfDouble89[7] = 0.000000
    arrayOfVariantOfDouble89[8] = 1.000000
    arrayOfVariantOfDouble89[9] = 0.000000
    arrayOfVariantOfDouble89[10] = - 1.542666
    arrayOfVariantOfDouble89[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble89)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble90[0] = 1.000000
    arrayOfVariantOfDouble90[1] = 0.000000
    arrayOfVariantOfDouble90[2] = 0.000000
    arrayOfVariantOfDouble90[3] = 0.000000
    arrayOfVariantOfDouble90[4] = 1.000000
    arrayOfVariantOfDouble90[5] = 0.000000
    arrayOfVariantOfDouble90[6] = 0.000000
    arrayOfVariantOfDouble90[7] = 0.000000
    arrayOfVariantOfDouble90[8] = 1.000000
    arrayOfVariantOfDouble90[9] = 0.000000
    arrayOfVariantOfDouble90[10] = - 3.235331
    arrayOfVariantOfDouble90[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble90)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble91[0] = 1.000000
    arrayOfVariantOfDouble91[1] = 0.000000
    arrayOfVariantOfDouble91[2] = 0.000000
    arrayOfVariantOfDouble91[3] = 0.000000
    arrayOfVariantOfDouble91[4] = 1.000000
    arrayOfVariantOfDouble91[5] = 0.000000
    arrayOfVariantOfDouble91[6] = 0.000000
    arrayOfVariantOfDouble91[7] = 0.000000
    arrayOfVariantOfDouble91[8] = 1.000000
    arrayOfVariantOfDouble91[9] = 0.000000
    arrayOfVariantOfDouble91[10] = - 3.235336
    arrayOfVariantOfDouble91[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble91)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble92[0] = 1.000000
    arrayOfVariantOfDouble92[1] = 0.000000
    arrayOfVariantOfDouble92[2] = 0.000000
    arrayOfVariantOfDouble92[3] = 0.000000
    arrayOfVariantOfDouble92[4] = 1.000000
    arrayOfVariantOfDouble92[5] = 0.000000
    arrayOfVariantOfDouble92[6] = 0.000000
    arrayOfVariantOfDouble92[7] = 0.000000
    arrayOfVariantOfDouble92[8] = 1.000000
    arrayOfVariantOfDouble92[9] = 0.000000
    arrayOfVariantOfDouble92[10] = - 0.771349
    arrayOfVariantOfDouble92[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble92)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble93[0] = 1.000000
    arrayOfVariantOfDouble93[1] = 0.000000
    arrayOfVariantOfDouble93[2] = 0.000000
    arrayOfVariantOfDouble93[3] = 0.000000
    arrayOfVariantOfDouble93[4] = 1.000000
    arrayOfVariantOfDouble93[5] = 0.000000
    arrayOfVariantOfDouble93[6] = 0.000000
    arrayOfVariantOfDouble93[7] = 0.000000
    arrayOfVariantOfDouble93[8] = 1.000000
    arrayOfVariantOfDouble93[9] = 0.000000
    arrayOfVariantOfDouble93[10] = - 0.921297
    arrayOfVariantOfDouble93[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble93)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble94[0] = 1.000000
    arrayOfVariantOfDouble94[1] = 0.000000
    arrayOfVariantOfDouble94[2] = 0.000000
    arrayOfVariantOfDouble94[3] = 0.000000
    arrayOfVariantOfDouble94[4] = 1.000000
    arrayOfVariantOfDouble94[5] = 0.000000
    arrayOfVariantOfDouble94[6] = 0.000000
    arrayOfVariantOfDouble94[7] = 0.000000
    arrayOfVariantOfDouble94[8] = 1.000000
    arrayOfVariantOfDouble94[9] = 0.000000
    arrayOfVariantOfDouble94[10] = - 1.542688
    arrayOfVariantOfDouble94[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble94)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble95[0] = 1.000000
    arrayOfVariantOfDouble95[1] = 0.000000
    arrayOfVariantOfDouble95[2] = 0.000000
    arrayOfVariantOfDouble95[3] = 0.000000
    arrayOfVariantOfDouble95[4] = 1.000000
    arrayOfVariantOfDouble95[5] = 0.000000
    arrayOfVariantOfDouble95[6] = 0.000000
    arrayOfVariantOfDouble95[7] = 0.000000
    arrayOfVariantOfDouble95[8] = 1.000000
    arrayOfVariantOfDouble95[9] = 0.000000
    arrayOfVariantOfDouble95[10] = - 0.771334
    arrayOfVariantOfDouble95[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble95)
    move3 = product4.Move
    move3 = move3.MovableObject
    arrayOfVariantOfDouble96[0] = 1.000000
    arrayOfVariantOfDouble96[1] = 0.000000
    arrayOfVariantOfDouble96[2] = 0.000000
    arrayOfVariantOfDouble96[3] = 0.000000
    arrayOfVariantOfDouble96[4] = 1.000000
    arrayOfVariantOfDouble96[5] = 0.000000
    arrayOfVariantOfDouble96[6] = 0.000000
    arrayOfVariantOfDouble96[7] = 0.000000
    arrayOfVariantOfDouble96[8] = 1.000000
    arrayOfVariantOfDouble96[9] = 0.000000
    arrayOfVariantOfDouble96[10] = - 0.771355
    arrayOfVariantOfDouble96[11] = 0.000000
    move3.Apply(arrayOfVariantOfDouble96)
    constraints1 = product1.Connections('CATIAConstraints')
    reference2 = product1.CreateReferenceFromName('Product1/Part1.1/!Selection_RSur:(Face:(Brp:((Brp:(Pad.2;0:(Brp:(Sketch.3;8)));Brp:(Pad.1;2)));None:();Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    reference3 = product1.CreateReferenceFromName('Product1/Part2.1/!Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;8)));None:();Cf11:());Pocket.1_ResultOUT;Z0;G3563)')
    constraint2 = constraints1.AddBiEltCst(catCstTypeOn, reference2, reference3)
    constraint2.Orientation = catCstOrientSame
    specsAndGeomWindow1 = CATIA.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference4 = product1.CreateReferenceFromName('Product1/Part1.1/!Selection_RSur:(Face:(Brp:((Brp:(Pad.2;1);Brp:(Pad.1;0:(Brp:(Sketch.1;29)))));None:();Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    reference5 = product1.CreateReferenceFromName('Product1/Part2.1/!Selection_RSur:(Face:(Brp:(Pad.1;1);None:();Cf11:());Pocket.1_ResultOUT;Z0;G3563)')
    constraint3 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference4, reference5)
    product1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomIn()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    productDocument1.SeeHiddenElements = True
    constraints1 = product1.Connections('CATIAConstraints')
    reference6 = product1.CreateReferenceFromName('Product1/Part3.1/!xy plane')
    reference7 = product1.CreateReferenceFromName('Product1/Part2.1/!xy plane')
    constraint4 = constraints1.AddBiEltCst(catCstTypeOn, reference6, reference7)
    constraint4.Orientation = catCstOrientSame
    productDocument1.SeeHiddenElements = False
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference8 = product1.CreateReferenceFromName('Product1/Part3.1/!Selection_RSur:(Face:(Brp:(Pad.1;2);None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    reference9 = product1.CreateReferenceFromName('Product1/Part1.1/!Selection_RSur:(Face:(Brp:(Pocket.1;0:(Brp:(Sketch.2;5)));AtLeastOneNoSharedIncluded:(Brp:(Pad.1;0:(Brp:(Sketch.1;8)));Brp:(Pad.1;0:(Brp:(Sketch.1;14))));Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    constraint5 = constraints1.AddBiEltCst(catCstTypeOn, reference8, reference9)
    constraint5.Orientation = catCstOrientOpposite
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference10 = product1.CreateReferenceFromName('Product1/Part3.1/!Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;5)));None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    reference11 = product1.CreateReferenceFromName('Product1/Part1.1/!Selection_RSur:(Face:(Brp:(Pocket.1;0:(Brp:(Sketch.2;8)));AtLeastOneNoSharedIncluded:(Brp:(Pad.1;0:(Brp:(Sketch.1;8)));Brp:(Pad.1;0:(Brp:(Sketch.1;14))));Cf11:());Pad.2_ResultOUT;Z0;G3563)')
    constraint6 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference10, reference11)
    product1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    productDocument1.SeeHiddenElements = True
    constraints1 = product1.Connections('CATIAConstraints')
    reference12 = product1.CreateReferenceFromName('Product1/Part4.1/!xy plane')
    reference6 = product1.CreateReferenceFromName('Product1/Part3.1/!xy plane')
    constraint7 = constraints1.AddBiEltCst(catCstTypeOn, reference12, reference6)
    constraint7.Orientation = catCstOrientSame
    productDocument1.SeeHiddenElements = False
    constraints1 = product1.Connections('CATIAConstraints')
    reference8 = product1.CreateReferenceFromName('Product1/Part3.1/!Selection_RSur:(Face:(Brp:(Pad.1;2);None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    reference13 = product1.CreateReferenceFromName('Product1/Part4.1/!Selection_RSur:(Face:(Brp:(Pad.1;2);None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    constraint8 = constraints1.AddBiEltCst(catCstTypeOn, reference8, reference13)
    constraint8.Orientation = catCstOrientSame
    viewpoint3D1 = viewer3D1.Viewpoint3D
    constraints1 = product1.Connections('CATIAConstraints')
    reference14 = product1.CreateReferenceFromName('Product1/Part3.1/!Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;11)));None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    reference15 = product1.CreateReferenceFromName('Product1/Part4.1/!Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;17)));None:();Cf11:());Pad.1_ResultOUT;Z0;G3563)')
    constraint9 = constraints1.AddBiEltCst(catCstTypeSurfContact, reference14, reference15)
    product1.Update()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.ZoomIn()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewer3D1.Reframe()
    viewpoint3D1 = viewer3D1.Viewpoint3D
    viewpoint3D1 = viewer3D1.Viewpoint3D

    #saving...............................
    productDocument1 = CATIA.ActiveDocument
    productDocument1.SaveAs('C:\\%s\\assembly_gib_and_cotter_joint.CATProduct' %(gibfoldername))

def unitkt():
    global kt
    kt = float(box_2.get())

    if (tunit.get() == "N/mm^2"):
        kt = kt
        knuckle()
    elif (tunit.get() == "KN/mm^2"):
        kt = (kt * 1000)
        knuckle()
    elif (tunit.get() == "N/cm^2"):
        kt = (kt / 100)
        knuckle()
    elif (tunit.get() == "KN/cm^2"):
        kt = (kt * 10)
        knuckle()
    elif (tunit.get() == "N/m^2"):
        kt = (kt / 1000000)
        knuckle()
    elif (tunit.get() == "KN/m^2"):
        kt = (kt / 1000)
        knuckle()
    else:
        messagebox.showerror("Unit Error","Please select a unit for TENSILE STRESS")
        

def unitkp():
    global kp
    kp = float(box_1.get())
    
    if (lunit.get() == "N"):
        kp = kp
        unitkt()
    elif (lunit.get() == "KN"):
        kp = (kp * 1000)
        unitkt()
    elif (lunit.get() == "MN"):
        kp = (kp * 1000000)
        unitkt()
    else:
        messagebox.showerror("Unit Error","Please select a unit for LOAD")

def gunitss():
    global ss
    ss = float(gbox_3.get())

    if (gsunit.get() == "N/mm^2"):
        ss = ss
        gib()
    elif (gsunit.get() == "KN/mm^2"):
        ss = (ss * 1000)
        gib()
    elif (gsunit.get() == "N/cm^2"):
        ss = (ss / 100)
        gib()
    elif (gsunit.get() == "KN/cm^2"):
        ss = (ss * 10)
        gib()
    elif (gsunit.get() == "N/m^2"):
        ss = (ss / 1000000)
        gib()
    elif (gsunit.get() == "KN/m^2"):
        ss = (ss / 1000)
        gib()
    else:
        messagebox.showerror("Unit Error","Please select a unit for SHEAR STRESS")

def gunitts():
    global ts
    ts = float(gbox_2.get())

    if (gtunit.get() == "N/mm^2"):
        ts = ts
        gunitss()
    elif (gtunit.get() == "KN/mm^2"):
        ts = (ts * 1000)
        gunitss()
    elif (gtunit.get() == "N/cm^2"):
        ts = (ts / 100)
        gunitss()
    elif (gtunit.get() == "KN/cm^2"):
        ts = (ts * 10)
        gunitss()
    elif (gtunit.get() == "N/m^2"):
        ts = (ts / 1000000)
        gunitss()
    elif (gtunit.get() == "KN/m^2"):
        ts = (ts / 1000)
        gunitss()
    else:
        messagebox.showerror("Unit Error","Please select a unit for TENSILE STRESS")

def gunitgf():
    global gf
    gf = float(gbox_1.get())
    
    if (glunit.get() == "N"):
        gf = gf
        gunitts()
    elif (glunit.get() == "KN"):
        gf = (gf * 1000)
        gunitts()
    elif (glunit.get() == "MN"):
        gf = (gf * 1000000)
        gunitts()
    else:
        messagebox.showerror("Unit Error","Please select a unit for FORCE")

#.........................................................creating gui...........................................................

root=Tk()
root.geometry("1366x768+0+0")
#root.resizable(width=False,height=False)

####background image.......................
main=PhotoImage(file='images\\main1.png')
label_bg=Label(root,image=main)
label_bg.place(x=0,y=0,relwidth=1,relheight=1)


#####time..........................................................................
def time():
    string= strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000,time)
time_label=Label(root,font=('calibri',20,'bold'),bg='#f6f4f1',fg='black')
time_label.place(x=100,y=62)
time()
#######time end................................................................
####heading...
class heading:
    def __init__(self):
        self.txt = "CATIA V5 Automation using PYTHON"
        self.count = 0
        self.text = ''
        self.color = ["black","blue","red"]
        self.heading = Label(root,text=self.txt,font="Vertana 32 bold",bg="#f6f4f1",bd=5,relief=FLAT)
        self.heading.place(x=300,y=55 ,width=850)
        self.slider()
        self.heading_color()
    def slider(self):
        
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)
        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1

        self.heading.after(100,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50,self.heading_color)  

heading()
#heading end......................................................................................
def home_fun():
    global home_label
    if 'gib_label' in globals():
        gib_label.destroy()
        gload_label.destroy()
        gtensile_label.destroy()
        gshear_label.destroy()
        gfolder_label.destroy()
        gbox_1.destroy()
        gbox_2.destroy()
        gbox_3.destroy()
        gbox_4.destroy()
        glunit.destroy()
        gtunit.destroy()
        gsunit.destroy()
        gib_button.destroy()
    if 'knuckle_label' in globals():
        knuckle_label.destroy()
        load_label.destroy()
        folder_label.destroy()
        stress_label.destroy()
        box_1.destroy()
        box_2.destroy()
        box_3.destroy()
        lunit.destroy()
        tunit.destroy()
        knuckle_button.destroy()
    if 'home_label' in globals():
        home_label.destroy()

    
    home_label=Label(root,text="Welcome to our project !!!!!!!!",bg="#eb5d25",fg="black",font="Times 20 bold")
    home_label.place(x=600,y=350)
def knu_fun():
    global knuckle_label,load_label,folder_label,stress_label,box_1,box_2,box_3,lunit,tunit,knuckle_button

    if 'home_label' in globals():
        home_label.destroy()

    if 'gib_label' in globals():
        gib_label.destroy()
        gload_label.destroy()
        gtensile_label.destroy()
        gshear_label.destroy()
        gfolder_label.destroy()
        gbox_1.destroy()
        gbox_2.destroy()
        gbox_3.destroy()
        gbox_4.destroy()
        glunit.destroy()
        gtunit.destroy()
        gsunit.destroy()
        gib_button.destroy()
    if 'knuckle_label' in globals():
        knuckle_label.destroy()
        load_label.destroy()
        folder_label.destroy()
        stress_label.destroy()
        box_1.destroy()
        box_2.destroy()
        box_3.destroy()
        lunit.destroy()
        tunit.destroy()
        knuckle_button.destroy()
        
        

    
    
    knuckle_label=Label(root,text="KNUCKLE JOINT",bd=15,relief="ridge",font="Vertana 32 bold",fg="#6e0404",bg="#bdb655",width=15,height=1)
    knuckle_label.place(x=500,y=150)
    #creating load and stress label
    load_label=Label(root,text="Load                :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    load_label.place(x=400,y=300)
    stress_label=Label(root,text="Tensile stress :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    stress_label.place(x=400,y=400)
    #stress_label=Label(root,text="Materials       :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    #stress_label.place(x=30,y=400)
    folder_label=Label(root,text="Folder Name :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    folder_label.place(x=400,y=500)
    #creating entry boxes
    box_1=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    box_2=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    box_3=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    box_1.place(x=650,y=297)
    box_2.place(x=650,y=397)
    box_3.place(x=650,y=497)
    #creatinting units drop down boxes
    lunit=ttk.Combobox(root,value=["unit","N","KN","MN"],font="Times 25 bold",width=8)
    lunit.current(0)
    lunit.place(x=850,y=300)
    tunit=ttk.Combobox(root,value=["unit","N/mm^2","KN/mm^2","N/cm^2","KN/cm^2","N/m^2","KN/m^2"],font="Times 25 bold",width=8)
    tunit.current(0)
    tunit.place(x=850,y=400)
    #materials_list=ttk.Combobox(root,value=["choose","Aluminium","Brass","Bronze","Brushed metal 1","Brushed metal 2","Chroma","Copper","Eroded metal 1","Eroded metal 2","Gold","Iron","Lead","Magnesium","Nickel","Silver","Steel","Titanium","Tungsten","Uranium","Yellow Brass","Zinc"],font="Times 25 bold",width=9)
    #materials_list.current(0)
    #materials_list.place(x=280,y=400)
    #creating final button
    knuckle_button=Button(root,text=" Draw ",padx=10,pady=10,fg="black",bg="green",font="Times 20 bold",bd=15,command=unitkp)
    knuckle_button.place(x=660,y=600)
def gib_fun():
    global gib_label,gload_label,gtensile_label,gshear_label,gfolder_label,gbox_1,gbox_2,gbox_3,gbox_4,glunit,gtunit,gsunit,gib_button

    if 'home_label' in globals():
        home_label.destroy()

    if 'knuckle_label' in globals():
        knuckle_label.destroy()
        load_label.destroy()
        folder_label.destroy()
        stress_label.destroy()
        box_1.destroy()
        box_2.destroy()
        box_3.destroy()
        lunit.destroy()
        tunit.destroy()
        knuckle_button.destroy()
    if 'gib_label' in globals():
        gib_label.destroy()
        gload_label.destroy()
        gtensile_label.destroy()
        gshear_label.destroy()
        gfolder_label.destroy()
        gbox_1.destroy()
        gbox_2.destroy()
        gbox_3.destroy()
        gbox_4.destroy()
        glunit.destroy()
        gtunit.destroy()
        gsunit.destroy()
        gib_button.destroy()
        
    
    
    gib_label=Label(root,text="GIB and COTTER JOINT",bd=15,relief="ridge",font="Vertana 32 bold",fg="#6e0404",bg="#cfa336",width=20,height=1)
    gib_label.place(x=450,y=150)
    #creating load and stress label
    gload_label=Label(root,text="Force              :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    gload_label.place(x=400,y=250)

    gtensile_label=Label(root,text="Tensile stress :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    gtensile_label.place(x=400,y=330)

    gshear_label=Label(root,text="Shear stress    :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    gshear_label.place(x=400,y=410)

    gfolder_label=Label(root,text="Folder Name :",relief="groove",font="Times 25 bold",fg="#040214",bg="#d1dfed",width=11,height=1,anchor=W)
    gfolder_label.place(x=400,y=490)

    #creating entry boxes
    gbox_1=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    gbox_2=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    gbox_3=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)
    gbox_4=Entry(root,relief="sunken",font="Times 25 bold",width=10,bd=5)

    gbox_1.place(x=650,y=247)
    gbox_2.place(x=650,y=327)
    gbox_3.place(x=650,y=407)
    gbox_4.place(x=650,y=487)

    glunit=ttk.Combobox(root,value=["unit","N","KN","MN"],font="Times 25 bold",width=8)
    glunit.current(0)
    glunit.place(x=850,y=250)

    gtunit=ttk.Combobox(root,value=["unit","N/mm^2","KN/mm^2","N/cm^2","KN/cm^2","N/m^2","KN/m^2"],font="Times 25 bold",width=8)
    gtunit.current(0)
    gtunit.place(x=850,y=330)

    gsunit=ttk.Combobox(root,value=["unit","N/mm^2","KN/mm^2","N/cm^2","KN/cm^2","N/m^2","KN/m^2"],font="Times 25 bold",width=8)
    gsunit.current(0)
    gsunit.place(x=850,y=410)

    gib_button=Button(root,text=" Draw ",padx=10,pady=10,fg="black",bg="green",font="Times 20 bold",bd=15,command=gunitgf)
    gib_button.place(x=660,y=600)

def exit_fun():
    root.destroy()

####main buttons

home_img=PhotoImage(file='images\\hom.png')
knu_img=PhotoImage(file='images\\knu.png')
gib_img=PhotoImage(file='images\\gib.png')
exit_img=PhotoImage(file='images\\exit.png')

home_button=Button(root,image=home_img,bg='#eb6125',bd=15,relief='raised',command=home_fun)
knu_button=Button(root,image=knu_img,bg='#eb6125',bd=15,relief='raised',command=knu_fun)
gibc_button=Button(root,image=gib_img,bg='#eb6125',bd=15,relief='raised',command=gib_fun)
exit_button=Button(root,image=exit_img,bg='#eb6125',bd=15,relief='raised',command=exit_fun)

home_button.place(x=40,y=160)
knu_button.place(x=40,y=300)
gibc_button.place(x=40,y=440)
exit_button.place(x=40,y=580)



home_fun()

mainloop()
#...................................................main button end.................................

        
        

   


#...........................................................................ending GUI.......................................................................#

