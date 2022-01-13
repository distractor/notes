points = vtk.vtkPoints()
points.InsertNextPoint(.5,.5,1.)
points.InsertNextPoint(0.,0.,0.)
points.InsertNextPoint(1.,0.,0.)
points.InsertNextPoint(2.,.5,0.)
points.InsertNextPoint(1.,1.,0.)
points.InsertNextPoint(0.,1.,0.)

output=self.GetOutputDataObject(0)
output.SetPoints(points)

polys=vtk.vtkCellArray()
n=points.GetNumberOfPoints()-1
print("n:", n)
for i in range(n):
    tri=vtk.vtkTriangle()
    tri.GetPointIds().SetId(0,0)
    tri.GetPointIds().SetId(1,i+1)
    j = i+2 if i < n-1 else 1
    print(i,j)
    tri.GetPointIds().SetId(2,j)
    polys.InsertNextCell(tri)

output.SetPolys(polys)

