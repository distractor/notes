# state file generated using paraview version 5.10.0

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1150, 1610]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [36.06866887382632, 79.3815883028298, 4.1538187128784525]
renderView1.CameraViewUp = [-0.8835028571527825, 0.413003320134514, -0.22102253043691772]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 22.972463585917456
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1150, 1610]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [36.06866887382632, 79.3815883028298, 4.1538187128784525]
renderView2.CameraViewUp = [-0.8835028571527825, 0.413003320134514, -0.22102253043691772]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 22.972463585917456
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)
layout1.SetSize(2301, 1610)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Wavelet'
wavelet1 = Wavelet(registrationName='Wavelet1')

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=wavelet1)
pointDatatoCellData1.PointDataArraytoprocess = ['RTData']

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=pointDatatoCellData1)
clip1.ClipType = 'Sphere'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['CELLS', 'RTData']
clip1.Value = 159.75022888183594

# init the 'Sphere' selected for 'ClipType'
clip1.ClipType.Radius = 10.0

# create a new 'Cell Centers'
cellCenters1 = CellCenters(registrationName='CellCenters1', Input=clip1)
cellCenters1.VertexCells = 1

# create a new 'Delaunay 3D'
delaunay3D1 = Delaunay3D(registrationName='Delaunay3D1', Input=cellCenters1)

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=delaunay3D1)
contour1.ContourBy = ['POINTS', 'RTData']
contour1.Isosurfaces = [195.72352600097656, 127.20733642578125, 142.43315633138022, 157.65897623697916, 172.88479614257812, 188.1106160481771, 203.33643595377606, 218.562255859375, 233.78807576497397, 249.01389567057294, 264.2397155761719]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display = Show(wavelet1, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')
rTDataLUT.RGBPoints = [37.35310363769531, 0.231373, 0.298039, 0.752941, 157.0909652709961, 0.865003, 0.865003, 0.865003, 276.8288269042969, 0.705882, 0.0156863, 0.14902]
rTDataLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RTData'
rTDataPWF = GetOpacityTransferFunction('RTData')
rTDataPWF.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]
rTDataPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
wavelet1Display.Representation = 'Surface'
wavelet1Display.ColorArrayName = ['POINTS', 'RTData']
wavelet1Display.LookupTable = rTDataLUT
wavelet1Display.SelectTCoordArray = 'None'
wavelet1Display.SelectNormalArray = 'None'
wavelet1Display.SelectTangentArray = 'None'
wavelet1Display.OSPRayScaleArray = 'RTData'
wavelet1Display.OSPRayScaleFunction = 'PiecewiseFunction'
wavelet1Display.SelectOrientationVectors = 'None'
wavelet1Display.ScaleFactor = 2.0
wavelet1Display.SelectScaleArray = 'RTData'
wavelet1Display.GlyphType = 'Arrow'
wavelet1Display.GlyphTableIndexArray = 'RTData'
wavelet1Display.GaussianRadius = 0.1
wavelet1Display.SetScaleArray = ['POINTS', 'RTData']
wavelet1Display.ScaleTransferFunction = 'PiecewiseFunction'
wavelet1Display.OpacityArray = ['POINTS', 'RTData']
wavelet1Display.OpacityTransferFunction = 'PiecewiseFunction'
wavelet1Display.DataAxesGrid = 'GridAxesRepresentation'
wavelet1Display.PolarAxes = 'PolarAxesRepresentation'
wavelet1Display.ScalarOpacityUnitDistance = 1.7320508075688774
wavelet1Display.ScalarOpacityFunction = rTDataPWF
wavelet1Display.OpacityArrayName = ['POINTS', 'RTData']
wavelet1Display.IsosurfaceValues = [157.0909652709961]
wavelet1Display.SliceFunction = 'Plane'
wavelet1Display.Slice = 10

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
wavelet1Display.ScaleTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
wavelet1Display.OpacityTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for rTDataLUT in view renderView1
rTDataLUTColorBar = GetScalarBar(rTDataLUT, renderView1)
rTDataLUTColorBar.Title = 'RTData'
rTDataLUTColorBar.ComponentTitle = ''

# set color bar visibility
rTDataLUTColorBar.Visibility = 1

# show color legend
wavelet1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display_1 = Show(wavelet1, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
wavelet1Display_1.Representation = 'Outline'
wavelet1Display_1.ColorArrayName = ['POINTS', '']
wavelet1Display_1.SelectTCoordArray = 'None'
wavelet1Display_1.SelectNormalArray = 'None'
wavelet1Display_1.SelectTangentArray = 'None'
wavelet1Display_1.OSPRayScaleArray = 'RTData'
wavelet1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
wavelet1Display_1.SelectOrientationVectors = 'None'
wavelet1Display_1.ScaleFactor = 2.0
wavelet1Display_1.SelectScaleArray = 'RTData'
wavelet1Display_1.GlyphType = 'Arrow'
wavelet1Display_1.GlyphTableIndexArray = 'RTData'
wavelet1Display_1.GaussianRadius = 0.1
wavelet1Display_1.SetScaleArray = ['POINTS', 'RTData']
wavelet1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
wavelet1Display_1.OpacityArray = ['POINTS', 'RTData']
wavelet1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
wavelet1Display_1.DataAxesGrid = 'GridAxesRepresentation'
wavelet1Display_1.PolarAxes = 'PolarAxesRepresentation'
wavelet1Display_1.ScalarOpacityUnitDistance = 1.7320508075688774
wavelet1Display_1.OpacityArrayName = ['POINTS', 'RTData']
wavelet1Display_1.IsosurfaceValues = [157.0909652709961]
wavelet1Display_1.SliceFunction = 'Plane'
wavelet1Display_1.Slice = 10

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
wavelet1Display_1.ScaleTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
wavelet1Display_1.OpacityTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# show data from pointDatatoCellData1
pointDatatoCellData1Display = Show(pointDatatoCellData1, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
pointDatatoCellData1Display.Representation = 'Surface With Edges'
pointDatatoCellData1Display.ColorArrayName = ['CELLS', 'RTData']
pointDatatoCellData1Display.LookupTable = rTDataLUT
pointDatatoCellData1Display.SelectTCoordArray = 'None'
pointDatatoCellData1Display.SelectNormalArray = 'None'
pointDatatoCellData1Display.SelectTangentArray = 'None'
pointDatatoCellData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.SelectOrientationVectors = 'None'
pointDatatoCellData1Display.ScaleFactor = 2.0
pointDatatoCellData1Display.SelectScaleArray = 'RTData'
pointDatatoCellData1Display.GlyphType = 'Arrow'
pointDatatoCellData1Display.GlyphTableIndexArray = 'RTData'
pointDatatoCellData1Display.GaussianRadius = 0.1
pointDatatoCellData1Display.SetScaleArray = [None, '']
pointDatatoCellData1Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.OpacityArray = [None, '']
pointDatatoCellData1Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData1Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData1Display.ScalarOpacityUnitDistance = 1.7320508075688774
pointDatatoCellData1Display.ScalarOpacityFunction = rTDataPWF
pointDatatoCellData1Display.OpacityArrayName = ['CELLS', 'RTData']
pointDatatoCellData1Display.IsosurfaceValues = [159.75022888183594]
pointDatatoCellData1Display.SliceFunction = 'Plane'
pointDatatoCellData1Display.Slice = 10

# show data from clip1
clip1Display = Show(clip1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['CELLS', 'RTData']
clip1Display.LookupTable = rTDataLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 2.0
clip1Display.SelectScaleArray = 'RTData'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'RTData'
clip1Display.GaussianRadius = 0.1
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = rTDataPWF
clip1Display.ScalarOpacityUnitDistance = 1.7019511490060497
clip1Display.OpacityArrayName = ['CELLS', 'RTData']

# show data from cellCenters1
cellCenters1Display = Show(cellCenters1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
cellCenters1Display.Representation = 'Points'
cellCenters1Display.ColorArrayName = ['POINTS', 'RTData']
cellCenters1Display.LookupTable = rTDataLUT
cellCenters1Display.SelectTCoordArray = 'None'
cellCenters1Display.SelectNormalArray = 'None'
cellCenters1Display.SelectTangentArray = 'None'
cellCenters1Display.OSPRayScaleArray = 'RTData'
cellCenters1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellCenters1Display.SelectOrientationVectors = 'None'
cellCenters1Display.ScaleFactor = 1.8947368621826173
cellCenters1Display.SelectScaleArray = 'RTData'
cellCenters1Display.GlyphType = 'Arrow'
cellCenters1Display.GlyphTableIndexArray = 'RTData'
cellCenters1Display.GaussianRadius = 0.09473684310913086
cellCenters1Display.SetScaleArray = ['POINTS', 'RTData']
cellCenters1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellCenters1Display.OpacityArray = ['POINTS', 'RTData']
cellCenters1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellCenters1Display.DataAxesGrid = 'GridAxesRepresentation'
cellCenters1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellCenters1Display.ScaleTransferFunction.Points = [127.20733642578125, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellCenters1Display.OpacityTransferFunction.Points = [127.20733642578125, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# show data from delaunay3D1
delaunay3D1Display = Show(delaunay3D1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
delaunay3D1Display.Representation = 'Surface With Edges'
delaunay3D1Display.ColorArrayName = ['POINTS', 'RTData']
delaunay3D1Display.LookupTable = rTDataLUT
delaunay3D1Display.SelectTCoordArray = 'None'
delaunay3D1Display.SelectNormalArray = 'None'
delaunay3D1Display.SelectTangentArray = 'None'
delaunay3D1Display.OSPRayScaleArray = 'RTData'
delaunay3D1Display.OSPRayScaleFunction = 'PiecewiseFunction'
delaunay3D1Display.SelectOrientationVectors = 'None'
delaunay3D1Display.ScaleFactor = 1.8947368621826173
delaunay3D1Display.SelectScaleArray = 'RTData'
delaunay3D1Display.GlyphType = 'Arrow'
delaunay3D1Display.GlyphTableIndexArray = 'RTData'
delaunay3D1Display.GaussianRadius = 0.09473684310913086
delaunay3D1Display.SetScaleArray = ['POINTS', 'RTData']
delaunay3D1Display.ScaleTransferFunction = 'PiecewiseFunction'
delaunay3D1Display.OpacityArray = ['POINTS', 'RTData']
delaunay3D1Display.OpacityTransferFunction = 'PiecewiseFunction'
delaunay3D1Display.DataAxesGrid = 'GridAxesRepresentation'
delaunay3D1Display.PolarAxes = 'PolarAxesRepresentation'
delaunay3D1Display.ScalarOpacityFunction = rTDataPWF
delaunay3D1Display.ScalarOpacityUnitDistance = 0.889994241067837
delaunay3D1Display.OpacityArrayName = ['POINTS', 'RTData']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
delaunay3D1Display.ScaleTransferFunction.Points = [127.20733642578125, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
delaunay3D1Display.OpacityTransferFunction.Points = [127.20733642578125, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'RTData']
contour1Display.LookupTable = rTDataLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'RTData'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 1.8947368621826173
contour1Display.SelectScaleArray = 'RTData'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'RTData'
contour1Display.GaussianRadius = 0.09473684310913086
contour1Display.SetScaleArray = ['POINTS', 'RTData']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'RTData']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [142.4331512451172, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [142.4331512451172, 0.0, 0.5, 0.0, 264.2397155761719, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for rTDataLUT in view renderView2
rTDataLUTColorBar_1 = GetScalarBar(rTDataLUT, renderView2)
rTDataLUTColorBar_1.Title = 'RTData'
rTDataLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
rTDataLUTColorBar_1.Visibility = 1

# hide data in view
Hide(wavelet1, renderView2)

# show color legend
pointDatatoCellData1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(pointDatatoCellData1, renderView2)

# show color legend
clip1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(clip1, renderView2)

# show color legend
cellCenters1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(cellCenters1, renderView2)

# show color legend
delaunay3D1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(delaunay3D1, renderView2)

# show color legend
contour1Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')