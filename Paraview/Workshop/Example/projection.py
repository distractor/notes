# Retrieve input data object
inObject = self.GetInputDataObject(0,0)

# Instantiate container for new points
n = inObject.GetNumberOfPoints()
projection = vtk.vtkPoints()
projection.SetNumberOfPoints(n)

# Iterate over input points
for i in range(0, n):
  # Retrieve point coordinates
  coord = inObject.GetPoint(i)
  x,y,z = coord[:3]

  # Modify coordinates as needed by geometric transform
  x *= 1.5
  y = 1
  z = z * 0.8

  # Set new point coordinates
  projection.SetPoint(i,x,y,z)

# Assign new points to output
self.GetOutputDataObject(0).SetPoints(projection)
