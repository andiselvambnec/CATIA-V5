# import python modules
import os
from win32com.client import Dispatch
# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')
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

def gib():
    gf=float(input("transmitting force F(N)="))
    ts=float(input("tensile stress(N/mm2)="))
    ss=float(input("shear stress(N/mm2)="))
    gibfoldername = str(input("enter folder name ="))




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

    '''gLG=(gh+(2*(gt1+gt2)))      #over all length of gib

    print(round(gLG))

    gLC=(4*gh)                   #over all length of cotter

    print(round(gLC))
    '''
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
gib()    
