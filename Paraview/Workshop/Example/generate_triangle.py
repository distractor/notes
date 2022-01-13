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
renderView1.ViewSize = [3126, 1114]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.5, 0.0, 0.5]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.5, -2.7320508075688776, 0.5]
renderView1.CameraFocalPoint = [0.5, 0.0, 0.5]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.7071067811865476
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(3126, 1114)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Programmable Source'
programmableSource1 = ProgrammableSource(registrationName='ProgrammableSource1')
programmableSource1.Script = """points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(1, 0, 0)
points.InsertNextPoint(0, 0, 1)

tri = vtk.vtkPolygon()
tri.GetPointIds().SetNumberOfIds(3)
tri.GetPointIds().SetId(0,0)
tri.GetPointIds().SetId(1,1)
tri.GetPointIds().SetId(2,2)

out = self.GetPolyDataOutput()
out.SetPoints(points)
out.Allocate(1)
out.InsertNextCell(tri.GetCellType(), tri.GetPointIds())"""
programmableSource1.ScriptRequestInformation = ''
programmableSource1.PythonPath = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from programmableSource1
programmableSource1Display = Show(programmableSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
programmableSource1Display.Representation = 'Surface'
programmableSource1Display.ColorArrayName = [None, '']
programmableSource1Display.SelectTCoordArray = 'None'
programmableSource1Display.SelectNormalArray = 'None'
programmableSource1Display.SelectTangentArray = 'None'
programmableSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableSource1Display.SelectOrientationVectors = 'None'
programmableSource1Display.ScaleFactor = -0.2
programmableSource1Display.SelectScaleArray = 'None'
programmableSource1Display.GlyphType = 'Arrow'
programmableSource1Display.GlyphTableIndexArray = 'None'
programmableSource1Display.GaussianRadius = -0.01
programmableSource1Display.SetScaleArray = [None, '']
programmableSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableSource1Display.OpacityArray = [None, '']
programmableSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableSource1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableSource1Display.PolarAxes = 'PolarAxesRepresentation'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(programmableSource1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')