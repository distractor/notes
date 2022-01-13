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

## Tensor Glyph

For tensor visualisation.

## VTK user guide

Check it, should be useful, specially for the C++ development.

## Plugins

You can create your own readers, writers, etc... Meaning we could create a reader to a Medusa H5 file.
Similar could be achieved with a `programmable source`.

## Important facts
- There is a possibility that it can be run on server. Installing `paraview-client` on desktop and `paraview` on server should do the trick. Makes sense for large data only.

# Contact

philippe.pebay@ng-analytics.com
