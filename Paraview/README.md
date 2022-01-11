# Paraview
## Importing from CSV-like files
1. Upload CSV/TXT.
    
    Check if data has headers and set the right delimiter.
2. Use `TableToPoint` filter.

    And set the point coordinates.
3. Scalar fields work by default but vector fields need more attention:

    Add filter `Calculator` and type:
    ```
    v1*iHat+v2*jHat+v3*kHat
    ```
    This will add velocity to the values.

## Link camera
To link camera for interactive side-by-side view:
- right-click -> Link camera

## Important facts
- There is a possibility that it can be run on server. Installing `paraview-client` on desktop and `paraview` on server should do the trick. Makes sense for large data only.

