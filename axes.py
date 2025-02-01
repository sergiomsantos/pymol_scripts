from pymol.cgo import *
from pymol import cmd
from math import *


def axes(state="on", objname="axes", length=5.0, color="red",
         radius=0.1, coneradius=0.4, coneheigth=0.8, origin="[0, 0, 0]"):
    """

    DESCRIPTION

        Generates and visualizes 3D coordinate axes.

        This function creates a set of three axes (X, Y, Z) in the 3D space,
        each consisting of a cylinder (representing the shaft) and a cone
        (representing the arrowhead). The axes are positioned relative to the
        specified `origin` and can be customized with various parameters like
        length, color, and size. If the `state` is set to anything other than
        'on' or '1', the axes will not be displayed.

    USAGE

        axes on, [objname="axes" [, length=5.0 [, color="red" [, radius=0.1
            [, coneradius=0.4 [, coneheigth=0.8 [, origin="[0, 0, 0]"]]]]]]]

    ARGUMENTS

        state = The state of the axes. Can be 'on' or 'off'
                (default is "on").
        objname = The name of the object representing the axes
                (default is "axes").
        length = (optional) The length of the axes
                (default is 5.0).
        color = (optional) The color of the axes
                (default is "red").
        radius = (optional) The radius of the cylindrical part of the axes
                (default is 0.1).
        coneradius = (optional) The radius of the cone at the end of the axes
                (default is 0.4).
        coneheigth = (optional) The height of the cone at the end of the axes
                (default is 0.8).
        origin = (optional) The coordinates of the origin of the axes as a
                string in the format "[x, y, z]"
                (default is "[0, 0, 0]").


        (c) Sergio M. Santos, University of Aveiro, 1st Feb. 2017

    """

    cmd.delete(objname)

    if state.upper() not in ("ON", "1"):
        return

    currentview = cmd.get_view(output=1, quiet=1)

    length = float(length)
    radius = float(radius)
    coneheigth = float(coneheigth)
    coneradius = float(coneradius)
    color_tuple = cmd.get_color_tuple(color)
    origin = list(map(float, origin.strip("[]()").split(",")))

    labels_objname = objname + "_labels"
    vector_objname = objname + "_vectors"
    cmd.pseudoatom(labels_objname, pos=origin, label="o")

    obj = []
    for i, label in enumerate("xyz"):
        cone_base = origin[:]
        cone_base[i] += length

        cone_tip = origin[:]
        cone_tip[i] += length + coneheigth

        cmd.pseudoatom(labels_objname, pos=cone_base, label=label)
        obj.extend([SAUSAGE, *origin, *cone_base,
                    radius, *color_tuple, *color_tuple])
        obj.extend([CONE, *cone_base, *cone_tip,
                    coneradius, 0.0, *color_tuple, *color_tuple, 1.0, 1.0])

    cmd.color(color, labels_objname)
    cmd.show("spheres", labels_objname)
    cmd.set("sphere_scale", radius, labels_objname)

    cmd.load_cgo(obj, vector_objname, 1)
    cmd.group(objname, labels_objname + " " + vector_objname, action="add")

    cmd.set_view(currentview)

    return

cmd.extend("axes", axes)
