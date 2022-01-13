# Get handle on input data
inData = self.GetInputDataObject(0,0).GetPointData()

# Get handle on output data
outData = self.GetOutputDataObject(0).GetPointData()

# Data attributes must be explicitly passed to output
outData.PassData(inData)

# Retrieve number of values
values = inData.GetScalars()
n = values.GetNumberOfTuples()

# Prepare storage for integral values
integral = vtk.vtkDoubleArray()
integral.SetName("RTData_integral")
integral.SetNumberOfTuples(n)

# Now iterate and update integral on the fly
s = 0.0
for i in range(n):
  s += values.GetValue(i)
  integral.SetValue(i,s)

# Append results to the output
outData.AddArray(integral)

