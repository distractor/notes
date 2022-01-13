import os
points = vtk.vtkPoints()
path="/Users/pppebay/Documents/Git/NGA-Courses/ParaView"
name=os.path.normcase(os.path.join(path,"data.txt"))
f=open(name)
next(f)
for line in f:
  x,y,z = [float(n) for n in line.split(' ')[:3]]
  points.InsertNextPoint(x,y,z)
f.close()
self.GetOutput().SetPoints(points)

