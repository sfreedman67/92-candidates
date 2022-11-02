#!/usr/bin/env python
# coding: utf-8

from flatsurf import *
from sage.all import *

"""
Construction of the 7 models
(there are no candidates in model 3, so we don't consider it).
"""

def model1(slit, t1, t2, reduced_matrix):
    r'''
    Construct the surface with 
        - separatrix diagram 1
        - `reduced_matrix` -- the corresponding reduced matrix
        - `slit`  -- the slit
        - `t1` -- the twist of the first cylinder
        - `t2` -- the twist of the second cylinder
    Note that the data of the reduced matrix allows to define the trace field 
    and the size of the cylinders WC1, HC1, WZ1, HZ1, WC2, HC2, WZ2, HZ2
    '''
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = polygons(vertices=[(0, 0), (WC1-WC2, 0), (WC1-WC2+slit, 0),
                            (WC1, 0), (WC1+t1, HC1), (WC1-WC2+t1, HC1),
                            (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (WC2, 0), (WC2+t2, HC2),
                            (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    p2 = polygons(vertices=[(0, 0), (WC1-WC2, 0), (WC1, 0), (WC1+t1, HC1),
                            (WC1-slit+t1, HC1), (WC1-WC2+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 0, 5)
    surface.change_edge_gluing(0, 1, 2, 3)
    surface.change_edge_gluing(0, 2, 2, 4)
    surface.change_edge_gluing(0, 3, 0, 6)
    surface.change_edge_gluing(0, 4, 1, 0)
    surface.change_edge_gluing(1, 1, 1, 3)
    surface.change_edge_gluing(1, 2, 2, 1)
    surface.change_edge_gluing(2, 2, 2, 6)
    surface.change_edge_gluing(2, 5, 2, 0)
    return TranslationSurface(surface)


def model2(slit, t1, t2, reduced_matrix):
    r'''
    Same as model1 but for separatrix diagram equal to 2.
    '''
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = polygons(vertices=[(0, 0), (slit, 0), (WC1, 0), (WC1+t1, HC1),
                            (WC1-WC2+t1, HC1), (slit+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (WC2, 0), (WC2+t2, HC2),
                            (t2, HC2)], ring=FIELDS[reduced_matrix])
    p2 = polygons(vertices=[(0, 0), (WC2, 0), (WC1-slit, 0), (WC1, 0),
                            (WC1+t1, HC1), (WC1-slit+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 0, 5)
    surface.change_edge_gluing(0, 1, 2, 5)
    surface.change_edge_gluing(0, 2, 0, 6)
    surface.change_edge_gluing(0, 3, 1, 0)
    surface.change_edge_gluing(0, 4, 2, 1)
    surface.change_edge_gluing(1, 1, 1, 3)
    surface.change_edge_gluing(2, 2, 2, 4)
    surface.change_edge_gluing(2, 3, 2, 6)
    surface.change_edge_gluing(1, 2, 2, 0)
    return TranslationSurface(surface)


def model4(slit, t1, t2, reduced_matrix):
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = p2 = polygons(vertices=[(0, 0), (WC1-slit, 0),
                                 (WC1, 0), (WC1+t1, HC1),
                                 (t1 + WC1-slit, HC1), (t1, HC1)],
                       ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (slit, 0), (WC2, 0), (WC2+t2, HC2),
                            (t2+slit, HC2), (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(2)
    surface.change_edge_gluing(0, 0, 0, 4)
    surface.change_edge_gluing(0, 1, 1, 4)
    surface.change_edge_gluing(0, 2, 0, 5)
    surface.change_edge_gluing(1, 0, 2, 3)
    surface.change_edge_gluing(1, 1, 1, 3)
    surface.change_edge_gluing(1, 2, 1, 5)
    surface.change_edge_gluing(2, 0, 2, 4)
    surface.change_edge_gluing(2, 1, 0, 3)
    surface.change_edge_gluing(2, 2, 2, 5)
    return TranslationSurface(surface)


def model5(slit, t1, t2, reduced_matrix):
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = polygons(vertices=[(0, 0), (WC1-slit, 0), (WC1, 0), (WC1+t1, HC1),
                            (2*WC1-WC2-slit+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (WC2-WC1+slit, 0), (WC2, 0), (WC2+t2, HC2),
                            (WC2-WC1+slit+t2, HC2), (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    p2 = polygons(vertices=[(0, 0), (2*WC1-WC2-slit, 0), (WC1, 0),
                            (WC1+t1, HC1), (WC1-slit+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 1, 3)
    surface.change_edge_gluing(0, 1, 2, 3)
    surface.change_edge_gluing(0, 2, 0, 5)
    surface.change_edge_gluing(0, 3, 1, 0)
    surface.change_edge_gluing(0, 4, 2, 0)
    surface.change_edge_gluing(1, 1, 2, 4)
    surface.change_edge_gluing(1, 2, 1, 5)
    surface.change_edge_gluing(1, 4, 2, 1)
    surface.change_edge_gluing(2, 2, 2, 5)
    return TranslationSurface(surface)


def model6(slit, t1, t2, reduced_matrix):
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = polygons(vertices=[(0, 0), (slit, 0), (WC1, 0),
                            (WC1+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+slit, 0), (WC2, 0),
                            (WC2+t2, HC2), (WC1+slit+t2, HC2),
                            (slit+t2, HC2), (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    p2 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1),
                            (WC1-slit+t1, HC1), (t1, HC1)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 1, 6)
    surface.change_edge_gluing(0, 1, 2, 3)
    surface.change_edge_gluing(0, 2, 0, 4)
    surface.change_edge_gluing(0, 3, 1, 0)
    surface.change_edge_gluing(1, 1, 2, 2)
    surface.change_edge_gluing(1, 2, 1, 4)
    surface.change_edge_gluing(1, 3, 1, 7)
    surface.change_edge_gluing(1, 5, 2, 0)
    surface.change_edge_gluing(2, 1, 2, 4)
    return TranslationSurface(surface)


def model7(slit, t1, t2, reduced_matrix):
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1),
                            (t1, HC1)], ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+slit, 0),
                            (2*WC1+slit, 0), (WC2, 0), (WC2+t2, HC2),
                            (2*WC1+slit+t2, HC2), (WC1+slit+t2, HC2),
                            (WC1+t2, HC2), (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    p2 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1),
                            (t1, HC1)], ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 1, 8)
    surface.change_edge_gluing(0, 1, 0, 3)
    surface.change_edge_gluing(0, 2, 1, 0)
    surface.change_edge_gluing(1, 1, 1, 7)
    surface.change_edge_gluing(1, 2, 2, 2)
    surface.change_edge_gluing(1, 3, 1, 5)
    surface.change_edge_gluing(1, 4, 1, 9)
    surface.change_edge_gluing(1, 6, 2, 0)
    surface.change_edge_gluing(2, 1, 2, 3)
    return TranslationSurface(surface)


def model8(slit, t1, t2, reduced_matrix):
    [WC1, HC1, WC2, HC2] = [
        FIELDS[reduced_matrix](x) for x in SIZE_CYLINDERS[reduced_matrix][0]]
    p0 = p2 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1), (t1, HC1)],
                       ring=FIELDS[reduced_matrix])
    p1 = polygons(vertices=[(0, 0), (slit, 0), (WC1+slit, 0),
                            (2*WC1+slit, 0), (WC2, 0), (WC2+t2, HC2),
                            (WC2-WC1+t2, HC2), (WC1+slit+t2, HC2),
                            (WC1+t2, HC2), (t2, HC2)],
                  ring=FIELDS[reduced_matrix])
    surface = Surface_dict(base_ring=FIELDS[reduced_matrix])
    surface.add_polygon(p0, label=0)
    surface.add_polygon(p1, label=1)
    surface.add_polygon(p2, label=2)
    surface.change_base_label(0)
    surface.change_edge_gluing(0, 0, 1, 8)
    surface.change_edge_gluing(0, 1, 0, 3)
    surface.change_edge_gluing(0, 2, 1, 2)
    surface.change_edge_gluing(1, 0, 1, 7)
    surface.change_edge_gluing(1, 1, 2, 2)
    surface.change_edge_gluing(1, 3, 1, 6)
    surface.change_edge_gluing(1, 4, 1, 9)
    surface.change_edge_gluing(1, 5, 2, 0)
    surface.change_edge_gluing(2, 1, 2, 3)
    return TranslationSurface(surface)


"""
`CANDIDATES_k_l` is the list of `[slit,t1,t2]` parameters
for all candidate surfaces with
    - model `k` in `[[1,8]]` and
    - reduced matrix `l` in `[[1,7]]`
The following list comes from the file `Section_8.2.sage`,
attached to Lanneau-Möller [LM18].

More precisely: the function `solve_problem(D,i,model)` in their code
gives the below list of parameters*, where
     - `model` corresponds to separatrix diagram`k` in `[[1,8]]`
     - `(D,i)` correspond to the reduced matrix, where
        - `D` in `{2, 3, 33}` has square root generating the trace field,
        - `i` denotes the possible reduced matrices having that trace field

The relationship between our notation `l in [[1,7]]` for reduced matrices
and theirs is:
    - 1=(2,1),
    - 2=(3,1), 3=(3,2), 4=(3,3),
    - 5=(33,1), 6=(33,2), 7=(33,3).
 (In fact, there are no candidates for the reduced matrices number 6 and 7)

*in fact, to get the parameters you have to replace
the last line of the function `solve_problem` by `return listofproto`
instead of `return to_discriminant(listofproto)`.
"""

R = QQ['x']

CANDIDATES_1_1 = matrix(R, [[1/4*x - 1/3, 1/12*x + 3/8, 0],
                            [1/12*x, 13/24, 0],
                            [-7/12*x + 1, -1/4*x + 11/24, 0],
                            [11/12*x - 1, 1/4*x + 11/24, 0],
                            [-3/4*x + 4/3, -1/3*x + 5/8, 0],
                            [-1/4*x + 2/3, -1/6*x + 3/8, 0],
                            [3/4*x - 2/3, 1/6*x + 5/8, 0],
                            [5/4*x - 4/3, 1/3*x + 3/8, 0],
                            [-5/12*x + 1, -1/4*x + 13/24, 0],
                            [13/12*x - 1, 1/4*x + 13/24, 0],
                            [5/12*x, 11/24, 0],
                            [1/4*x + 1/3, -1/12*x + 5/8, 0]])

CANDIDATES_1_2 = matrix(R, [[1/4*x - 5/12, 1/24*x + 5/12, 0],
                            [-1/12*x + 1/4, -1/24*x + 7/12, 0],
                            [5/12*x - 7/12, 1/24*x + 5/6, 0],
                            [11/12*x - 17/12, 1/8*x + 2/3, 0],
                            [-5/12*x + 11/12, -1/8*x + 1/3, 0],
                            [1/12*x + 1/12, -1/24*x + 1/6, 0],
                            [7/12*x - 3/4, 1/24*x + 5/12, 0],
                            [1/4*x - 1/12, -1/24*x + 7/12, 0]])

CANDIDATES_2_1 = matrix(R, [[-1/12*x + 1/3, 1/6*x + 5/8, 0]])

CANDIDATES_4_1 = matrix(R, [[1/4*x + 1/3, -1/12*x + 5/24, 1/4*x - 1/3],
                            [1/4*x + 1/3, -1/12*x + 3/8, 1/4*x - 1/3],
                            [1/4*x + 1/3, -1/12*x + 13/24, 1/4*x - 1/3],
                            [1/4*x + 1/3, 1/12*x + 11/24, 1/4*x + 1/3],
                            [1/4*x + 1/3, 1/12*x + 5/8, 1/4*x + 1/3],
                            [1/4*x + 1/3, 1/12*x + 19/24, 1/4*x + 1/3]])

CANDIDATES_4_2 = matrix(R, [[1/4*x - 1/12, -1/24*x + 1/6, 1/4*x - 5/12],
                            [1/4*x - 1/12, -1/24*x + 1/3, 1/4*x - 5/12],
                            [1/4*x - 1/12, -1/24*x + 1/2, 1/4*x - 5/12],
                            [1/4*x - 1/12, 1/24*x + 1/2, 1/4*x - 1/12],
                            [1/4*x - 1/12, 1/24*x + 2/3, 1/4*x - 1/12],
                            [1/4*x - 1/12, 1/24*x + 5/6, 1/4*x - 1/12]])

CANDIDATES_4_3 = matrix(R, [[1/12*x + 1/4, 1/24*x + 1/3, 1/12*x + 1/4],
                            [1/12*x + 1/4, -1/24*x + 2/3, 5/12*x + 1/4],
                            [1/4*x + 5/12, -1/24*x + 1/6, 1/4*x + 1/12],
                            [1/4*x + 5/12, 1/24*x + 5/6, 1/4*x + 5/12]])

CANDIDATES_4_4 = matrix(R, [[1/3*x - 1/6, -1/12*x + 1/3, 1/3*x - 1/6],
                            [1/3*x - 1/6, 1/12*x + 2/3, 2/3*x + 1/6],
                            [1/3*x + 1/6, 1/12*x + 1/3, 1/3*x + 1/6],
                            [1/3*x + 1/6, -1/12*x + 2/3, 2/3*x - 1/6],
                            [1/6*x + 1/2, 1/4*x - 1/6, 1/6*x + 1/2],
                            [1/6*x + 1/2, -1/4*x + 7/6, 5/6*x - 1/2]])

CANDIDATES_5_1 = matrix(R, [[-7/12*x + 4/3, 1/3*x - 7/24, -1/12*x + 1/3],
                            [-7/12*x + 4/3, 1/6*x + 7/24, 7/12*x - 1/3],
                            [1/12*x + 2/3, 1/3*x - 7/24, -1/12*x + 1/3],
                            [1/12*x + 2/3, 1/6*x + 7/24, 7/12*x - 1/3]])

CANDIDATES_5_3 = matrix(R, [[-7/12*x + 5/4, 11/24*x - 2/3, -1/12*x + 3/4],
                            [-7/12*x + 5/4, 1/24*x + 1/6, 7/12*x - 1/4],
                            [-1/12*x + 5/12, 3/8*x - 1/12, 1/12*x + 7/12],
                            [-1/12*x + 5/12, 1/8*x + 7/12, 5/12*x - 1/12],
                            [-5/12*x + 13/12, 3/8*x - 1/12, 1/12*x + 7/12],
                            [-5/12*x + 13/12, 1/8*x + 7/12, 5/12*x - 1/12],
                            [1/12*x + 1/4, 11/24*x - 2/3, -1/12*x + 3/4],
                            [1/12*x + 1/4, 1/24*x + 1/6, 7/12*x - 1/4]])

CANDIDATES_6_3 = matrix(R, [[1/12*x - 1/12, 5/24*x + 1/3, 1/12*x + 11/12],
                            [-1/12*x + 5/12, 3/8*x + 1/12, -1/12*x + 17/12],
                            [5/12*x - 5/12, 1/24*x + 1/6, 5/12*x + 7/12]])

CANDIDATES_6_4 = matrix(R, [[1/3*x - 1/2, 1/4*x - 1/3, 1/3*x + 1/2],
                            [1/6*x - 1/6, 5/12*x + 1/6, 1/6*x + 5/6],
                            [1/3*x - 1/6, 5/12*x - 2/3, 1/3*x + 5/6],
                            [1/6*x + 1/6, 7/12*x - 1/2, 1/6*x + 7/6],
                            [1/2*x - 1/6, 5/12*x - 1/2, 1/2*x + 5/6],
                            [1/2*x - 1/6, 5/12*x - 1/3, 1/2*x + 5/6],
                            [1/2*x - 1/6, 5/12*x, 1/2*x + 5/6],
                            [1/2*x - 1/6, 5/12*x + 1/6, 1/2*x + 5/6]])

CANDIDATES_6_5 = matrix(R, [[1/12*x - 5/12, -1/12*x + 7/12, 5/12*x + 11/12],
                            [1/12*x - 5/12, -1/12*x + 5/4, 5/12*x + 11/12],
                            [-1/4*x + 19/12, -1/3*x + 13/6, 1/4*x - 7/12],
                            [-1/12*x + 3/4, 1/6, 1/12*x + 1/4],
                            [1/12*x - 1/12, -1/6*x + 1, 5/12*x + 7/12],
                            [1/4*x - 11/12, 1/6*x, 1/4*x + 17/12],
                            [1/4*x - 7/12, 1/12*x + 5/12, 1/4*x + 13/12]])

CANDIDATES_7_5 = matrix(R, [[1/4*x - 11/12, -1/12*x + 7/12, 1/4*x + 5/12],
                            [1/4*x - 11/12, 1/12*x + 5/12, 1/4*x + 13/12],
                            [1/12*x + 1/4, 1/4*x - 13/12, 1/12*x + 5/4],
                            [1/4*x - 7/12, -1/6*x + 1, 1/4*x + 1/12],
                            [1/4*x - 7/12, -1/12*x + 11/12, 1/4*x + 5/12],
                            [1/4*x - 7/12, 1/6*x, 1/4*x + 17/12],
                            [5/12*x - 17/12, -1/6*x + 1, 5/12*x + 7/12],
                            [5/12*x - 17/12, 1/6*x, 1/12*x + 11/12],
                            [5/12*x - 13/12, -1/12*x + 7/12, 5/12*x + 11/12],
                            [5/12*x - 13/12, 1/12*x - 1/4, 1/12*x + 7/12],
                            [5/12*x - 13/12, -1/12*x + 5/4, 5/12*x + 11/12],
                            [5/12*x - 13/12, 1/12*x + 5/12, 1/12*x + 7/12],
                            [1/4*x + 1/12, -1/3*x + 13/6, 1/4*x - 7/12],
                            [1/4*x + 1/12, 1/12*x + 1/12, 1/4*x + 13/12],
                            [1/4*x + 1/12, 1/3*x - 7/6, 1/4*x + 25/12],
                            [5/12*x - 3/4, 1/6, 1/12*x + 1/4],
                            [5/12*x - 3/4, -1/4*x + 25/12, 5/12*x + 1/4],
                            [5/12*x - 3/4, 5/6, 5/12*x + 5/4]])

CANDIDATES_8_5 = matrix(R, [[1/12*x - 5/12, 1/6*x - 2/3, 1/12*x + 19/12],
                            [1/12*x - 5/12, 1/6*x, 1/12*x + 19/12],
                            [5/12*x - 25/12, -1/6*x + 1, 5/12*x - 1/12],
                            [5/12*x - 25/12, -1/6*x + 5/3, 5/12*x - 1/12],
                            [-5/12*x + 11/4, 1/3*x - 7/6, -5/12*x + 11/4],
                            [-1/4*x + 23/12, 1/6*x, -1/4*x + 23/12],
                            [1/12*x + 1/4, 1/3*x - 7/6, 1/12*x + 9/4],
                            [1/4*x - 7/12, 1/12*x + 1/12, 1/4*x + 13 / 12],
                            [1/4*x - 7/12, 1/6*x, 1/4*x + 17/12],
                            [1/4*x + 1/12, -1/6*x + 1, 1/4*x + 1/12],
                            [1/4*x + 1/12, -1/12*x + 11/12, 1/4*x + 5/12],
                            [5/12*x - 3/4, -1/3*x + 13/6, 5/12*x - 3 / 4],
                            [3/4*x - 29/12, -1/6*x + 1, 3/4*x - 5/12],
                            [11/12*x - 13/4, -1/3*x + 13/6, 11/12*x - 5/4],
                            [1/12*x + 19/12, 1/6*x - 2/3, 1/12*x + 19/12],
                            [7/12*x - 5/4, 1/3*x - 7/6, 1/12*x + 1/4],
                            [1/12*x + 19/12, 1/6*x, 1/12*x + 19/12],
                            [3/4*x - 25/12, 1/6*x - 1/3, 1/4*x - 7/12],
                            [5/12*x - 1/12, -1/6*x + 1, 5/12*x - 1/12],
                            [5/12*x - 1/12, -1/6*x + 5/3, 5/12*x - 1/12]])

CANDIDATES = {(1, 1): CANDIDATES_1_1,
              (1, 2): CANDIDATES_1_2,
              (2, 1): CANDIDATES_2_1,
              (4, 1): CANDIDATES_4_1,
              (4, 2): CANDIDATES_4_2,
              (4, 3): CANDIDATES_4_3,
              (4, 4): CANDIDATES_4_4,
              (5, 1): CANDIDATES_5_1,
              (5, 3): CANDIDATES_5_3,
              (6, 3): CANDIDATES_6_3,
              (6, 4): CANDIDATES_6_4,
              (6, 5): CANDIDATES_6_5,
              (7, 5): CANDIDATES_7_5,
              (8, 5): CANDIDATES_8_5}

MODELS = {1: model1, 2: model2, 4: model4,
          5: model5, 6: model6, 7: model7, 8: model8}

"""
The dictionnary `SIZE_CYLINDERS` gives the parameters
WC1, HC1, WC2, HC2
(see section 6.3-6.5 of Lanneau-Möller [LM18])
associated to each reduced matrix l \in [[1,7]]
"""

SIZE_CYLINDERS = {1: matrix(R, [[1, 1, 1/2*x, 2*x,]]),
                  2: matrix(R, [[1, 1, 1/2*x - 1/2, 2*x - 2]]),
                  3: matrix(R, [[1, 1, 1/2*x + 1/2, 2*x + 2]]),
                  4: matrix(R, [[1, 1, x, 2/3*x]]),
                  5: matrix(R, [[1, 1, 1/2*x + 3/2, 1/6*x + 1/2]]),
#                  6: matrix(R, [[1, 1, 1/2*x - 3/2,1/6*x - 1/2]]),
#                  7: matrix(R, [[1, 1, 1/2*x - 3/2,1/6*x - 1/2]])}

FIELDS = {1: QuadraticField(2, name='x'),  # D=2, i=1
          2: QuadraticField(3, name='x'),  # D=3, i=1
          3: QuadraticField(3, name='x'),  # D=3, i=2
          4: QuadraticField(3, name='x'),  # D=3, i=3
          5: QuadraticField(33, name='x'),  # D=33, i=1
#          6: QuadraticField(33, name='x'),  # D=33, i=2
#          7: QuadraticField(33, name='x')}  # D=33, i=3

NUMBER_CANDIDATES = {(1, 1): 12,(1, 2): 8,(2, 1): 1,(4, 1): 3,(4, 2): 3,(4, 3): 3,(4, 4): 6,
                     (5, 1): 4,(5, 3): 8,(6, 3): 3,(6, 4): 8,(6, 5): 7,(7, 5): 18,(8, 5): 20}


def surface_candidate(sd,reduced_matrix,i):
    r'''
    Constructs the candidate surface number `i` associated to
        - the model `sd` in [[1,8]]
        - the reduced matrix number `reduced_matrix` in [[1,7]]
    In particular, i should be smaller than  NUMBER_CANDIDATES[(sd,reduced_matrix)]
    '''
    assert i < NUMBER_CANDIDATES[(sd,reduced_matrix)], ("i should be smaller than ", NUMBER_CANDIDATES[(sd,reduced_matrix)])
    slit, t1, t2 = [FIELDS[reduced_matrix](x) for x in CANDIDATES[(sd, reduced_matrix)][i]] 
    s = MODELS[sd](slit, t1, t2,reduced_matrix)
    return s


def test_candidate(sd, reduced_matrix):
    r'''
    Constructs all candidates surfaces with 
        - model number `sd`
        - reduced matrix number `reduced_matrix`
    And check that for each surface its orbit closure is not the one of a Teichmüller curve.
    '''
    for parameters in CANDIDATES[(sd, reduced_matrix)]:
        # Initialize the parameters to lie in the correct quadratic field
        slit, t1, t2 = [FIELDS[reduced_matrix](x) for x in parameters]
        s = MODELS[sd](slit, t1, t2, reduced_matrix)
        O = GL2ROrbitClosure(s)
        if not O.is_teichmueller_curve(3, 50):
            continue
        else:
            assert False

    return "No Teichmueller curves found for model", sd,
    "and reduced matrix", reduced_matrix


def test_candidates():
    r'''
    Conduce the check of the previous function for all admissible pairs (sd,reduced_matrix).
    '''
    for (sd, reduced_matrix) in CANDIDATES:
        print(test_candidate(sd, reduced_matrix))



def find_decomposition_for_candidate(sd, reduced_matrix,i): 
    r'''
    gives an explicit direction such that the moduli of the cylinders is irrationnal.
    The original code is part of the Flatsurf project and can be found here: 
    https://flatsurf.github.io/sage-flatsurf/examples/apisa_wright.html
    The entry i is the number of the candidate in CANDIDATES[(sd,reduced_matrix)],
    it should be smaller than  NUMBER_CANDIDATES[(sd,reduced_matrix)]
    '''
    assert i < NUMBER_CANDIDATES[(sd,reduced_matrix)], ("i should be smaller than ", NUMBER_CANDIDATES[(sd,reduced_matrix)])
    
    slit, t1, t2 = [FIELDS[reduced_matrix](x) for x in CANDIDATES[(sd, reduced_matrix)][i]] 
    s = MODELS[sd](slit, t1, t2,reduced_matrix)
    O = GL2ROrbitClosure(s)
        
    old_dim = O.dimension() #It should be 2
    for i, dec in enumerate(O.decompositions(16, bfs=True)):
        O.update_tangent_space_from_flow_decomposition(dec)
        new_dim = O.dimension()
        if old_dim != new_dim:
            holonomies = [cyl.circumferenceHolonomy() for cyl in dec.cylinders()]
            areas = [cyl.area() for cyl in dec.cylinders()]
            moduli = [(v.x()*v.x() + v.y()*v.y()) / area for v, area in zip(holonomies, areas)]
            u = dec.vertical().vertical()
            print("saddle connection number", i)
            print("holonomy           :", u)
            print("length             :", RDF(u.x()*u.x() + u.y()*u.y()).sqrt())
            print("num cylinders      :", len(dec.cylinders()))
#            print("num minimal comps. :", len(dec.minimalComponents()))
#            print("current dimension  :", new_dim)
            print("cyls. holonomies   :", holonomies)
            print("cyls. moduli       :", moduli)
            for i in range(1,len(moduli)):
                if not moduli[0]==moduli[1]:
                    print("The ratio of the first module over the module number", i+1,
                          "is irrationnal and equal to", moduli[0]/moduli[1], 'in the', FIELDS[reduced_matrix])
                    break
            break
