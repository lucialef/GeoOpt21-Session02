from flask import Flask
import ghhops_server as hs

import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createCylinder",
    name = "Create a Cylinder",
    inputs=[

        hs.HopsNumber("X Base Coordinate", "X", "X-coordinate at the base of the cylinder", hs.HopsParamAccess.ITEM, default= 5),
        hs.HopsNumber("Y Base Coordinate", "Y", "Y-coordinate at the base of the cylinder", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsNumber("Z Base Coordinate", "Z", "Z-coordinate at the base of the cylinder", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsNumber("Radius", "R", "Radius of the cylinder", hs.HopsParamAccess.ITEM, default= 2),
        hs.HopsNumber("Height", "H", "Height of the cylinder", hs.HopsParamAccess.ITEM, default= 8),

    ],
    outputs=[
       
       hs.HopsBrep("Geometry","G","Resulting Geometry", hs.HopsParamAccess.LIST)
    ]
)
def createCylinder(rX, rY, rZ, radi, height):

    point = rg.Point3d(rX,rY,rZ)
    circle = rg.Circle(point,radi)
        

    geo = rg.Cylinder(circle, height)
    return geo.ToBrep(True, True)

if __name__== "__main__":
    app.run(debug=True)
