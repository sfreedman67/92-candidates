#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flatsurf import *
from sage.all_cmdline import *   # import sage library
from surface_dynamics import CylinderDiagram
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\ This program provides the computational steps to prove Section 8.2


# def to_square(r):
#     B = matrix_length()
#     return B*vector([r.trace()/2, (r-r.norm()/r)/(2*x)])


# def matrix_length():
#     ax = HZ1.trace()/2
#     ay = (HZ1-HZ1.norm()/HZ1)/(2*x)
#     bx = HZ2.trace()/2
#     by = (HZ2-HZ2.norm()/HZ2)/(2*x)
#     return matrix([[ax, bx], [ay, by]]).inverse()


# def initialization_topological_models(model):
#     global slit_squares, lengths, possible_twists, surface_prym, range_gamma
#     # CYLINDERS 1-3-2: SQUARES 1--a1; a1+1--2*a1; 2*a1+1--2*a1+a2
#     cylinders1 = [((0, 2, 3), (4, 0)), ((1, 5), (2, 3, 1)), ((4,), (5,))]
#     cylinders2 = [((0, 5, 3), (2, 0)), ((1, 2), (4, 3, 1)), ((4,), (5,))]
#     cylinders3 = [((0, 1, 2), (4,)), ((3,), (1, 5, 0)), ((4, 5), (2, 3))]
#     cylinders4 = [((0, 3), (4, 0)), ((1, 4), (5, 1)), ((2, 5), (3, 2))]
#     cylinders5 = [((0, 2), (5, 3)), ((1, 3), (4, 2)), ((4, 5), (1, 0))]
#     cylinders6 = [((0, 3), (2,)), ((1,), (5, 3)), ((2, 5, 4), (4, 1, 0))]
#     cylinders7 = [((0,), (2,)), ((1,), (3,)), ((2, 4, 3, 5), (5, 1, 4, 0))]
#     cylinders8 = [((0,), (4,)), ((1,), (3,)), ((2, 3, 4, 5), (1, 5, 2, 0))]

#     def lengths1(gamma): return [a1-a2, a1-a2, gamma, a2-gamma, a2, a2]
#     def lengths2(gamma): return [gamma, gamma, a1-gamma, a1-a2-gamma, a2, a2]
#     def lengths3(gamma): return [gamma, 2*a1-a2-gamma, a2-a1, a1, a1, a2-a1]

#     def lengths4(gamma): return [a1-gamma, a1 -
#                                  gamma, a2-gamma, gamma, gamma, gamma]

#     def lengths5(gamma): return [a1-gamma, a2-a1+gamma,
#                                  gamma, 2*a1-a2-gamma, a1-gamma, a2-a1+gamma]
#     #lengths5 = lambda gamma: [a1-gamma,a2-a1+gamma,gamma,2*a1-a2+gamma,a1-gamma,a2-a1+gamma]
#     def lengths6(gamma): return [gamma, a1, a1, a1-gamma, a2-a1-gamma, gamma]
#     def lengths7(gamma): return [a1, a1, a1, a1, gamma, a2-2*a1-gamma]
#     def lengths8(gamma): return [a1, a1, gamma, a1, a1, a2-2*a1-gamma]

#     def slit1(gamma): return [a1-a2+1..a1-a2+gamma]
#     def slit2(gamma): return [1..gamma]
#     def slit3(gamma): return [1..gamma]
#     def slit4(gamma): return [a1-gamma+1..a1]
#     def slit5(gamma): return [a1-gamma+1..a1]
#     #slit5 = lambda gamma: [1..gamma]
#     def slit6(gamma): return [1..gamma]
#     def slit7(gamma): return [3*a1+1..3*a1+gamma]
#     def slit8(gamma): return [2*a1+1..2*a1+gamma]

#     def twist1(gamma): return [0]
#     def twist2(gamma): return [0]
#     def twist3(gamma): return [0, 1, WC2-1]
#     def twist4(gamma): return [WC2-gamma, gamma]
#     def twist5(gamma): return [1-gamma, WC2-1+gamma]
#     #twist5 = lambda gamma: [gamma,1-gamma]
#     def twist6(gamma): return [1+gamma, 1-gamma, WC2-1-gamma]
#     def twist7(gamma): return [1+gamma, 2+gamma, WC2-2-gamma]
#     def twist8(gamma): return [gamma+2, gamma, WC2-1-gamma, 3-WC2+gamma]

#     range1 = [1..a2-1]
#     range2 = [1..min(a2-1, a1-a2-1)]
#     range3 = [1..min(a1, 2*a1-a2)-1]
#     range4 = [1..min(a1, a2)-1]
#     range5 = [max(a1-a2+1, 1)..min(a1, 2*a1-a2)-1]
#     #range5 = [max(a2-a1,0)+1..min(a2,a1)-1]
#     range6 = [1..min(a2-a1, a1)-1]
#     range7 = [1..a2-2*a1-1]
#     range8 = [1..a2-2*a1-1]

#     surface_prym = CylinderDiagram(eval("cylinders"+str(model)))
#     lengths = eval("lengths"+str(model))
#     slit_squares = eval("slit"+str(model))
#     possible_twists = eval("twist"+str(model))
#     range_gamma = eval("range"+str(model))
#     return "END"


# def initialization(D, i=1, model=1):
#     initialization_coordinates(D, i)
#     if model == 1 and not a2 < a1:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 2 and not a2 < a1:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 3 and not (a1 < a2 and a2 < 2*a1):
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 5 and not a2 < 2*a1:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 6 and not a1 < a2:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 7 and not 2*a1 < a2:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     if model == 8 and not 2*a1 < a2:
#         print("MODEL NOT COMPATIBLE WITH a1,a2")
#         return False
#     initialization_topological_models(model)
#     return True

# # initialization(3,1,6)


# def surface_check(parameters=[1, 1, 0]):
#     [gamma, t1, t2] = parameters
#     origami_prym = surface_prym.cylcoord_to_origami(
#         lengths(gamma), [1, 1, 1], [t1, t1, t2])
#     print(origami_prym.cylinder_diagram())
#     print(origami_prym.mirror().cylinder_diagram())
#     return origami_prym.orientation_data()
# # ******************************************************************************************************************************
# # ******************************************************************************************************************************
# # ******************************************************************************************************************************
# # GIVEN PARAMETERS, CHECK THAT THE INTERSECTION MATRIX IS THE GOOD ONE


# def is_good_parameters(gamma, t1, t2):
#     origami_prym = surface_prym.cylcoord_to_origami(
#         lengths(gamma), [1, 1, 1], [t1, t1, t2])
#     V = origami_prym.u()
#     cyl_vert = V.cycles()
#     if not len(cyl_vert) == 3:
#         return [False, 0]
#     cyl = [b2, b1, b1]
#     cyl.sort()
#     cyl2 = [c.order() for c in cyl_vert]
#     cyl2.sort()
#     if not cyl == cyl2:
#         return [False, 0]

#     if cyl_vert[0].order() == b2:
#         Z1 = cyl_vert[1]
#         Z2 = cyl_vert[0]
#     if cyl_vert[1].order() == b2:
#         Z1 = cyl_vert[0]
#         Z2 = cyl_vert[1]
#     if cyl_vert[2].order() == b2:
#         Z1 = cyl_vert[0]
#         Z2 = cyl_vert[2]
#     Z1 = list(eval(Z1.cycle_string()))
#     Z2 = list(eval(Z2.cycle_string()))
#     # check the REDUCED INTERSECTION MATRIX
#     [M11, M12, M21, M22] = [0, 0, 0, 0]

#     for i in [1..a1]:
#         if i in Z2:
#             M12 = M12 + 1
#         else:
#             M11 = M11 + 1  # COMPUTE THE SUM M11 + M13!!

#     for i in [2*a1+1..2*a1+a2]:
#         if i in Z1:
#             M21 = M21 + 1
#         if i in Z2:
#             M22 = M22 + 1

#     # for i in Z2:
#     #   if i>2*a1: M22 = M22 + 1
#     #   if i<a1+1: M21 = M21 + 1

#     # for i in Z1:
#     #   if i>2*a1: M12 = M12 + 1
#     #   if i<a1+1 or (i>a1 and i<2*a1+1): M11 = M11 + 1 # COMPUTE THE SUM M11 + M13!!

#     if matrix([[M11, 2*M12], [M21, M22]]) == Mred:
#         if len((origami_prym.mirror()).cylinder_diagram().cylinders()) == 3:
#             return [True, Z2]
#     return [False, 0]


# def find_arithmetic_surfaces():
#     surfaces = []
#     # print(range_gamma)
#     for gamma in range_gamma:
#         # print(gamma)
#         for t1 in range(a1):
#             #[check,Z] = is_good_parameters(gamma,t1,0)
#             #if check: surfaces.append([gamma,t1,0,Z])
#             for t2 in range(a2):  # [a2-gamma,gamma]:#
#                 [check, Z] = is_good_parameters(gamma, t1, t2)
#                 if check:
#                     surfaces.append([gamma, t1, t2, Z])
#     return surfaces


# # ******************************************************************************************************************************
# # ******************************************************************************************************************************
# # ******************************************************************************************************************************
# # GIVEN A LIST L OF SQUARES AND CYLINDER Z2, RETURN THE SQUARES THAT ARE IN Z2 (B) AND IN Z1,Z3 (i.e. NOT IN Z2) (A)
# def count_squares(L, Z):
#     [A, B] = [0, 0]
#     for i in L:
#         if i in Z:
#             B = B+1
#         else:
#             A = A+1
#     return [A, B]

# # COMPUTES THE LENGTHS OF TWISTS AND SLIT IN TERMS OF SQUARES


# def combinatoric_to_length(parameters):
#     [gamma, t1, t2, Z] = parameters
#     # saddle_0 = count_squares([1..gamma],Z); print saddle_0; print "saddle_0" + str(HZ1*saddle_0[0]+HZ2*saddle_0[1])
#     # saddle_1 = count_squares([a1+1..2*a1],Z); print saddle_1; print "saddle_1" + str( HZ1*saddle_1[0]+HZ2*saddle_1[1])
#     # saddle_4 = count_squares([3*a1+gamma+1..2*a1+a2],Z); print saddle_4; print "saddle_4" + str( HZ1*saddle_4[0]+HZ2*saddle_4[1])
#     # saddle_2 = count_squares([1..a1],Z); print saddle_2; print "saddle_2" + str( HZ1*saddle_2[0]+HZ2*saddle_2[1])
#     # saddle_3 = count_squares([gamma+1..a1],Z); print saddle_3; print "saddle_3" + str( HZ1*saddle_3[0]+HZ2*saddle_3[1])
#     # saddle_5 = count_squares([2*a1+a2-gamma+1..2*a1+a2],Z); print "saddle_5" + str( saddle_5)

#     slit = count_squares(slit_squares(gamma), Z)
#     twist_1 = [0, 0]
#     twist_2 = [0, 0]
#     if t1 > 0:
#         twist_1 = count_squares([1..t1], Z)
#     if t2 > 0:
#         twist_2 = count_squares([2*a1+1..2*a1+t2], Z)
#     [wA, wB] = [HZ1, HZ2]
#     return [wA*s[0]+wB*s[1] for s in [slit, twist_1, twist_2]]
# # Donne les vraies valeurs de slit, twist_1 et twist_2 à partir du modèle arithmétique


# def combinatoric_to_surface(parameters):
#     [gamma, t1, t2, Z] = parameters
#     sur = combinatoric_to_length(parameters)
#     # CHECK THAT THE VERTICAL DIRECTION IS ALSO GOOD
#     if sur[-1] in possible_twists(sur[0]):
#         return [sur, [gamma, t1, t2]]
#     return []

# # sur is [slit,twist_1,twist_2]


# def surface_to_prototype(sur):
#     if sur == []:
#         return []
#     # sur_without_t1 = [sur[0],sur[2] + (WC1-sur[1])*HC2/HC1]  #eliminate_twists_t1
#     sur_without_t2 = [sur[0], sur[1] +
#                       (WC2-sur[2])*HC1/HC2]  # eliminate_twists_t2
#     [slit, twist_t1] = [e*HC2/WC2 for e in sur_without_t2]  # HENCE twist_t1 is in Q
#     # return [slit,twist_t1]
#     p = twist_t1.numerator()
#     q = twist_t1.denominator()
#     # PROTOTYPE w,h,t,lambda
#     # [w,h,t,s] = [2*q*WC1*HC2/WC2,2*q*HC1,2*p,q*slit] # w MAY BE IN Q AND NOT IN N
#     [w, h, t, s] = [q*WC1*HC2/WC2, q*HC1, p, q*slit]  # w MAY BE IN Q AND NOT IN N
#     a = w.numerator()
#     b = w.denominator()
#     [w, h, t, s] = [a, b*h, b*t, b*s]
#     t = Integer(mod(t, gcd(Integer(w), Integer(h))))
#     d = gcd([w, h, t])
#     Lambda = HC2*q*b/d
#     e = sqrt(Lambda.minpoly().discriminant()-8*(w/d)*(h/d))
#     return [w/d, h/d, t/d, s/d/Lambda, Lambda, Lambda.minpoly().discriminant(), e]


# def final(listofsur):
#     listofproto = []
#     listofprotoandparameters = []
#     for parameters in listofsur:
#         p = combinatoric_to_surface(parameters)
#         if not p == []:
#             [sur, [gamma, t1, t2]] = p
#             proto = surface_to_prototype(sur)
#             if not proto in listofproto and not proto == []:
#                 listofproto.append(proto)
#                 listofprotoandparameters.append([proto, [gamma, t1, t2]])
#     return listofprotoandparameters


# def final_metric(listofsur):
#     listofparameters = []
#     for parameters in listofsur:
#         p = combinatoric_to_surface(parameters)
#         if not p == []:
#             #[sur,[gamma,t1,t2]] = p
#             if not p in listofparameters:
#                 listofparameters.append(p)
#     return listofparameters


# def final2(listofsur):
#     c = 0
#     for parameters in listofsur:
#         p = combinatoric_to_surface(parameters)
#         if not p == []:
#             c = c+1
#             print([p[0][0], p[0][1], p[0][2], p[1]])
#             #print [to_square(sur[0][0]),to_square(sur[0][1]),sur[1]]
#             #print [surface_to_prototype(sur[0]),sur[1]]
#     return "END", c


# def to_discriminant(listofproto):
#     for p in listofproto:
#         P = p[0][-2].minpoly()
#         print([p, P.discriminant()])
#     return "END"


# def solve_problem(D, i, model):
#     if not initialization(D, i, model):
#         return "END"
#     listofsur = find_arithmetic_surfaces()
#     listofproto = final(listofsur)
#     print("Candidates for topological surfaces: " + str(len(listofsur)))
#     print(" ")
#     print("The discriminant is " + str(D) + " and the case is i="+str(i))
#     print(" ")
#     print("The model is "+str(model)+" and there are " +
#           str(len(listofproto)) + " solutions given by:")
#     return to_discriminant(listofproto)


# def solve_problem_2(D, i, model):
#     if not initialization(D, i, model):
#         return "END"
#     listofsur = find_arithmetic_surfaces()
#     listofproto = final_metric(listofsur)
#     print("Candidates for topological surfaces: " + str(len(listofsur)))
#     print(" ")
#     print("The discriminant is " + str(D) + " and the case is i="+str(i))
#     print(" ")
#     print("The model is "+str(model)+" and there are " +
#           str(len(listofproto)) + " solutions given by:")
#     return listofproto


# def solve_problem_3(D, i, model):
#     if not initialization(D, i, model):
#         return "END"
#     listofsur = find_arithmetic_surfaces()
#     listofproto = final2(listofsur)
#     print("Candidates for topological surfaces: " + str(len(listofsur)))
#     print(" ")
#     print("The discriminant is " + str(D) + " and the case is i="+str(i))
#     print(" ")
#     print("The model is "+str(model)+" and there are " +
#           str(listofproto[1]) + " solutions given above")
#     return listofproto[0]


# # GALOIS CONJUGATE
# def galois(r):
#     if r in QQ:
#         return r
#     return r.norm()/r


def initialization_coordinates(D, i=1):
    global K, x, WC1, HC1, WZ1, HZ1, WC2, HC2, WZ2, HZ2
    K = QuadraticField(D)
    x = K.gen()

    WHD2_1 = [1, 1, 48*x + 72, -1/12*x + 1/8, 1/2*x,
              2*x, 36*x + 48, 1/4*x - 1/3]
    WHD3_1 = [1, 1, 24*x + 48, -1/24*x + 1/12, 1/2*x - 1/2,
              2*x - 2, 12*x + 12, 1/4*x - 5/12]
    WHD3_2 = [1, 1, 96*x + 168, -1/24*x + 1/12, 1/2*x + 1/2,
              2*x + 2, 36*x + 60, 1/4*x - 5/12]
    WHD3_3 = [1, 1, 20*x + 36, -1/12*x + 1/6, x, 2/3*x, 8*x + 12, 1/2*x - 5/6]
    WHD33_1 = [1, 1, 2*x + 12, -1/6*x + 1, 1/2*x + 3/2,
               1/6*x + 1/2, 9*x + 51, 1/12*x - 5/12]
    WHD33_2 = [1, 1, 1/2*x + 9/2, -1/6*x + 1, 1/2*x - 3/2,
               1/6*x - 1/2, 3*x + 15, 1/12*x - 5/12]
    WHD33_3 = [1, 1, 1/2*x + 3/2, 1/12*x - 1/4, 1/2*x - 3/2,
               1/6*x - 1/2, 6, -1/12*x + 7/12]

    [WC1, HC1, WZ1, HZ1, WC2, HC2, WZ2, HZ2] = eval("WHD"+str(D)+"_"+str(i))

# # Model 1 -- No TCurves

# In[3]:


# def check_model1(D, i):
#     # Construction of the translation surfaces for the model 1.
#     #[D,i] in [[2,1],[3,1]]
#     initialization_coordinates(D, i)
#     # Below is the list of possible [slit,twist1, twist2] for the candidates of model 1 (obtained with the function (solve_problem_2))
#     candidates2_1 = [[1/4*x - 1/3, 1/12*x + 3/8, 0], [1/12*x, 13/24, 0], [-7/12*x + 1, -1/4*x + 11/24, 0], [11/12*x - 1, 1/4*x + 11/24, 0],
#                      [-3/4*x + 4/3, -1/3*x + 5/8, 0], [-1 /
#                                                        4*x + 2/3, -1/6*x + 3/8, 0],
#                      [3/4*x - 2/3, 1/6*x + 5/8, 0], [5/4*x - 4/3, 1/3 *
#                                                      x + 3/8, 0], [-5/12*x + 1, -1/4*x + 13/24, 0],
#                      [13/12*x - 1, 1/4*x + 13/24, 0], [5/12*x, 11/24, 0], [1/4*x + 1/3, -1/12*x + 5/8, 0]]
#     # There are 12 candidates in candidates21, meaning D=2 and i=1
#     candidates3_1 = [[1/4*x - 5/12, 1/24*x + 5/12, 0], [-1/12*x + 1/4, -1/24*x + 7/12, 0], [5/12*x - 7/12, 1/24*x + 5/6, 0],
#                      [11/12*x - 17/12, 1/8*x + 2/3, 0], [-5/12*x + 11/12, -
#                                                          1/8*x + 1/3, 0], [1/12*x + 1/12, -1/24*x + 1/6, 0],
#                      [7/12*x - 3/4, 1/24*x + 5/12, 0], [1/4*x - 1/12, -1/24*x + 7/12, 0]]
#     # There are 8 candidates in candidates31
#     # No other candidates for model 1.
#     for slit, t1, t2 in eval('candidates'+str(D)+'_'+str(i)):
#         p0 = polygons(vertices=[(0, 0), (WC1-WC2, 0), (WC1-WC2+slit, 0),
#                                 (WC1, 0), (WC1+t1, HC1), (WC1-WC2+t1, HC1), (t1, HC1)], ring=K)
#         p1 = polygons(vertices=[(0, 0), (WC2, 0),
#                                 (WC2+t2, HC2), (t2, HC2)], ring=K)
#         p2 = polygons(vertices=[(0, 0), (WC1-WC2, 0), (WC1, 0), (WC1+t1, HC1),
#                                 (WC1-slit+t1, HC1), (WC1-WC2+t1, HC1), (t1, HC1)], ring=K)
#         surface = Surface_dict(base_ring=K)
#         surface.add_polygon(p0, label=0)
#         surface.add_polygon(p1, label=1)
#         surface.add_polygon(p2, label=2)
#         surface.change_base_label(0)
#         surface.change_edge_gluing(0, 0, 0, 5)
#         surface.change_edge_gluing(0, 1, 2, 3)
#         surface.change_edge_gluing(0, 2, 2, 4)
#         surface.change_edge_gluing(0, 3, 0, 6)
#         surface.change_edge_gluing(0, 4, 1, 0)
#         surface.change_edge_gluing(1, 1, 1, 3)
#         surface.change_edge_gluing(1, 2, 2, 1)
#         surface.change_edge_gluing(2, 2, 2, 6)
#         surface.change_edge_gluing(2, 5, 2, 0)
#         # s1 is the surface correspoding to model 1, D, i, and the parameters candidatesD_i[j]
#         s1 = TranslationSurface(surface)
#         O = GL2ROrbitClosure(s1)
#         print(O.is_teichmueller_curve(3, 50))


# # In[4]:


# check_model1(2, 1)
# check_model1(3, 1)


# # # Model 2 -- No TCurves

# # In[5]:


# # Construction of the unique candidate in model 2. (In fact Erwan already tested it and it shouldn't be Veech)
# D = 2
# i = 1
# initialization_coordinates(D, i)
# [slit, t1, t2] = [-1/12*x + 1/3, 1/6*x + 5/8, 0]
# p0 = polygons(vertices=[(0, 0), (slit, 0), (WC1, 0), (WC1+t1, HC1),
#                         (WC1-WC2+t1, HC1), (slit+t1, HC1), (t1, HC1)], ring=K)
# p1 = polygons(vertices=[(0, 0), (WC2, 0), (WC2+t2, HC2), (t2, HC2)], ring=K)
# p2 = polygons(vertices=[(0, 0), (WC2, 0), (WC1-slit, 0), (WC1, 0),
#                         (WC1+t1, HC1), (WC1-slit+t1, HC1), (t1, HC1)], ring=K)
# surface = Surface_dict(base_ring=K)
# surface.add_polygon(p0, label=0)
# surface.add_polygon(p1, label=1)
# surface.add_polygon(p2, label=2)
# surface.change_base_label(0)
# surface.change_edge_gluing(0, 0, 0, 5)
# surface.change_edge_gluing(0, 1, 2, 5)
# surface.change_edge_gluing(0, 2, 0, 6)
# surface.change_edge_gluing(0, 3, 1, 0)
# surface.change_edge_gluing(0, 4, 2, 1)
# surface.change_edge_gluing(1, 1, 1, 3)
# surface.change_edge_gluing(2, 2, 2, 4)
# surface.change_edge_gluing(2, 3, 2, 6)
# surface.change_edge_gluing(1, 2, 2, 0)
# s2 = TranslationSurface(surface)
# O = GL2ROrbitClosure(s2)
# O.is_teichmueller_curve(3, 50)


# # # Model 4 -- No TCurves

# # In[6]:


# # Construction of the translation surfaces for the model 4.
# # I changed the polygons so that the slit correspond to side 3 (and 4,5)
# def build_s4(slit, t1, t2):
#     c1 = c3 = polygons((WC1 - slit, 0), (slit, 0), (t1, HC1),  # Modified
#                        (-slit, 0), (slit - WC1, 0), (-t1, -HC1))  # Modified
#     c2 = polygons((WC2-slit, 0), (slit, 0), (t2, HC2),
#                   (- slit, 0), (-(WC2-slit), 0), (-t2, -HC2))
#     surface = Surface_dict(base_ring=K)
#     surface.add_polygon(c1, label=1)
#     surface.add_polygon(c2, label=2)
#     surface.add_polygon(c3, label=3)
#     surface.change_base_label(2)
#     surface.change_edge_gluing(1, 0, 1, 4)
#     surface.change_edge_gluing(1, 1, 2, 3)
#     surface.change_edge_gluing(1, 2, 1, 5)
#     surface.change_edge_gluing(2, 0, 2, 4)
#     surface.change_edge_gluing(2, 1, 3, 3)
#     surface.change_edge_gluing(2, 2, 2, 5)
#     surface.change_edge_gluing(3, 0, 3, 4)
#     surface.change_edge_gluing(3, 1, 1, 3)
#     surface.change_edge_gluing(3, 2, 3, 5)
#     s4 = TranslationSurface(surface)
# #     s4.plot().show()
#     return s4


# def check_model4(D, i):
#     # [D,i] in [[2,1],[3,1],[3,2],[3,3]]:

#     initialization_coordinates(D, i)

#     # Below is the list of all the prototypes we have to test according to the table p.26
#     candidates2_1 = [[1/4*x + 1/3, -1/12*x + 5/24, 1/4*x - 1/3],
#                      [1/4*x + 1/3, -1/12*x + 3/8, 1/4*x - 1/3],
#                      [1/4*x + 1/3, -1/12*x + 13/24, 1/4*x - 1/3],
#                      [1/4*x + 1/3, 1/12*x + 11/24, 1/4*x + 1/3],
#                      [1/4*x + 1/3, 1/12*x + 5/8, 1/4*x + 1/3],
#                      [1/4*x + 1/3, 1/12*x + 19/24, 1/4*x + 1/3]]
#     candidates3_1 = [[1/4*x - 1/12, -1/24*x + 1/6, 1/4*x - 5/12],
#                      [1/4*x - 1/12, -1/24*x + 1/3, 1/4*x - 5/12],
#                      [1/4*x - 1/12, -1/24*x + 1/2, 1/4*x - 5/12],
#                      [1/4*x - 1/12, 1/24*x + 1/2, 1/4*x - 1/12],
#                      [1/4*x - 1/12, 1/24*x + 2/3, 1/4*x - 1/12],
#                      [1/4*x - 1/12, 1/24*x + 5/6, 1/4*x - 1/12]]
#     candidates3_2 = [[1/12*x + 1/4, 1/24*x + 1/3, 1/12*x + 1/4],
#                      [1/12*x + 1/4, -1/24*x + 2/3, 5/12*x + 1/4],
#                      [1/4*x + 5/12, -1/24*x + 1/6, 1/4*x + 1/12],
#                      [1/4*x + 5/12, 1/24*x + 5/6, 1/4*x + 5/12]]
#     candidates3_3 = [[1/3*x - 1/6, -1/12*x + 1/3, 1/3*x - 1/6],
#                      [1/3*x - 1/6, 1/12*x + 2/3, 2/3*x + 1/6],
#                      [1/3*x + 1/6, 1/12*x + 1/3, 1/3*x + 1/6],
#                      [1/3*x + 1/6, -1/12*x + 2/3, 2/3*x - 1/6],
#                      [1/6*x + 1/2, 1/4*x - 1/6, 1/6*x + 1/2],
#                      [1/6*x + 1/2, -1/4*x + 7/6, 5/6*x - 1/2]]

#     candidates = eval('candidates'+str(D)+'_'+str(i))
#     for slit, t1, t2 in candidates:
#         s4 = build_s4(slit, t1, t2)
#         O = GL2ROrbitClosure(s4)
#         print(O.is_teichmueller_curve(5, 50))


# # In[7]:


# check_model4(2, 1)
# check_model4(3, 1)
# check_model4(3, 2)
# check_model4(3, 3)


# # In[8]:


# # Construction of the translation surfaces for the model 4 via the prototypes - This is the correct version

# def prototype(w, h, t, e, slit):
#     assert 0 < slit < 1

#     K = slit.parent()

#     D = e**2 + 8*w*h
#     l = (e+K(sqrt(D)))/2

#     p0 = polygons((l - slit * l, 0), (slit * l, 0), (0, l),
#                   (-slit * l, 0), (slit * l - l, 0), (0, -l))
#     p1 = p2 = polygons((slit * l, 0), (w - slit * l, 0),
#                        (t, h), ((slit * l) - w, 0), (-slit * l, 0), (-t, -h))
#     surface = Surface_dict(base_ring=K)
#     surface.add_polygon(p0, label=0)
#     surface.add_polygon(p1, label=1)
#     surface.add_polygon(p2, label=2)
#     surface.change_base_label(0)
#     surface.change_edge_gluing(0, 0, 0, 4)
#     surface.change_edge_gluing(0, 1, 2, 4)
#     surface.change_edge_gluing(0, 2, 0, 5)
#     surface.change_edge_gluing(0, 3, 1, 0)
#     surface.change_edge_gluing(1, 1, 1, 3)
#     surface.change_edge_gluing(1, 2, 1, 5)
#     surface.change_edge_gluing(1, 4, 2, 0)
#     surface.change_edge_gluing(2, 1, 2, 3)
#     surface.change_edge_gluing(2, 2, 2, 5)
#     s = TranslationSurface(surface)
#     return s


# # Below is the list of all the prototypes we have to test according to the table p.26
# candidates2_1 = [[12, 3, 1, 0, 1/2+x/3],
#                  [4, 1, 0, 0, 1/2+x/3], [12, 3, 2, 0, 1/2+x/3]]
# candidates3_1 = [[12, 3, 1, -12, 2/3+x/6],
#                  [4, 1, 0, -4, 2/3+x/6], [12, 3, 2, -12, 2/3+x/6]]
# candidates3_2 = [[4, 1, 0, 4, x/6], [12, 3, 1, 12, x/6], [12, 3, 2, 12, x/6]]
# candidates3_3 = [[6, 9, 1, 0, 1/3-x/18], [6, 9, 2, 0, 1/3-x/18], [6, 9, 1, 0, 1/3+x/18], [6, 9, 2, 0, 1/3+x/18],
#                  [12, 18, 1, 0, 1/6+x/6], [12, 18, 1, 0, 1/6+x/6]]

# # [D,i] in [[2,1],[3,1],[3,2],[3,3]]:


# def test_model4_prototypes(D, i):
#     initialization_coordinates(D, i)
#     for w, h, t, e, slit in eval('candidates'+str(D)+'_'+str(i)):
#         #         print(w,h,t,e,slit)
#         s4 = prototype(w, h, t, e, slit)
#         O = GL2ROrbitClosure(s4)
#         print(O.is_teichmueller_curve(20))


# # test_model4_prototypes(2, 1)
# test_model4_prototypes(3, 1)
# test_model4_prototypes(3, 2)
# test_model4_prototypes(3, 3)


# # # Model 5 -- No TCurves

# # In[ ]:


# def check_model5(D, i):
#     # Construction of the translation surfaces for the model 5.
#     # D, i in [[2,1],[3,2]]

#     # 4 candidates for D=2 and i=1 in model 5
#     candidates2_1 = [[-7/12*x + 4/3, 1/3*x - 7/24, -1/12*x + 1/3],
#                      [-7/12*x + 4/3, 1/6*x + 7/24, 7/12*x - 1/3],
#                      [1/12*x + 2/3, 1/3*x - 7/24, -1/12*x + 1/3],
#                      [1/12*x + 2/3, 1/6*x + 7/24, 7/12*x - 1/3]]

#     # 8 candidates for D=3 and i=2 in model 5
#     candidates3_2 = [[-7/12*x + 5/4, 11/24*x - 2/3, -1/12*x + 3/4],
#                      [-7/12*x + 5/4, 1/24*x + 1/6, 7/12*x - 1/4],
#                      [-1/12*x + 5/12, 3/8*x - 1/12, 1/12*x + 7/12],
#                      [-1/12*x + 5/12, 1/8*x + 7/12, 5/12*x - 1/12],
#                      [-5/12*x + 13/12, 3/8*x - 1/12, 1/12*x + 7/12],
#                      [-5/12*x + 13/12, 1/8*x + 7/12, 5/12*x - 1/12],
#                      [1/12*x + 1/4, 11/24*x - 2/3, -1/12*x + 3/4],
#                      [1/12*x + 1/4, 1/24*x + 1/6, 7/12*x - 1/4]]

#     for slit, t1, t2 in eval('candidates'+str(D)+'_'+str(i)):
#         initialization_coordinates(D, i)
#         p0 = polygons(vertices=[(0, 0), (WC1-slit, 0), (WC1, 0),
#                                 (WC1+t1, HC1), (2*WC1-WC2-slit+t1, HC1), (t1, HC1)], ring=K)
#         p1 = polygons(vertices=[(0, 0), (WC2-WC1+slit, 0), (WC2, 0),
#                                 (WC2+t2, HC2), (WC2-WC1+slit+t2, HC2), (t2, HC2)], ring=K)
#         p2 = polygons(vertices=[(0, 0), (2*WC1-WC2-slit, 0), (WC1, 0),
#                                 (WC1+t1, HC1), (WC1-slit+t1, HC1), (t1, HC1)], ring=K)
#         surface = Surface_dict(base_ring=K)
#         surface.add_polygon(p0, label=0)
#         surface.add_polygon(p1, label=1)
#         surface.add_polygon(p2, label=2)
#         surface.change_base_label(0)
#         surface.change_edge_gluing(0, 0, 1, 3)
#         surface.change_edge_gluing(0, 1, 2, 3)
#         surface.change_edge_gluing(0, 2, 0, 5)
#         surface.change_edge_gluing(0, 3, 1, 0)
#         surface.change_edge_gluing(0, 4, 2, 0)
#         surface.change_edge_gluing(1, 1, 2, 4)
#         surface.change_edge_gluing(1, 2, 1, 5)
#         surface.change_edge_gluing(1, 4, 2, 1)
#         surface.change_edge_gluing(2, 2, 2, 5)
#         s5 = TranslationSurface(surface)
#         O = GL2ROrbitClosure(s5)
#         print(O.is_teichmueller_curve(3, 50))


# # In[ ]:


# # check_model5(2, 1)
# check_model5(3, 2)


# # # Model 6 -- No TCurves

# # In[ ]:


# def check_model6(D, i):
#     # Construction of the translation surfaces for the model 6.
#     #[D,i] in [[3,2],[3,3],[33,1]]
#     initialization_coordinates(D, i)
#     candidates3_2 = [[1/12*x - 1/12, 5/24*x + 1/3, 1/12*x + 11/12], [-1/12*x + 5/12, 3/8*x + 1/12, -1/12*x + 17/12],
#                      [5/12*x - 5/12, 1/24*x + 1/6, 5/12*x + 7/12]]
#     # 3 candidates
#     candidates3_3 = [[1/3*x - 1/2, 1/4*x - 1/3, 1/3*x + 1/2], [1/6*x - 1/6, 5/12*x + 1/6, 1/6*x + 5/6],
#                      [1/3*x - 1/6, 5/12*x - 2/3, 1/3*x + 5/6], [1 /
#                                                                 6*x + 1/6, 7/12*x - 1/2, 1/6*x + 7/6],
#                      [1/2*x - 1/6, 5/12*x - 1/2, 1/2*x + 5/6], [1 /
#                                                                 2*x - 1/6, 5/12*x - 1/3, 1/2*x + 5/6],
#                      [1/2*x - 1/6, 5/12*x, 1/2*x + 5/6], [1/2*x - 1/6, 5/12*x + 1/6, 1/2*x + 5/6]]
#     # 8 candidates
#     candidates33_1 = [[1/12*x - 5/12, -1/12*x + 7/12, 5/12*x + 11/12], [1/12*x - 5/12, -1/12*x + 5/4, 5/12*x + 11/12],
#                       [-1/4*x + 19/12, -1/3*x + 13/6, 1/4*x - 7/12], [-1/12*x + 3/4,
#                                                                       1/6, 1/12*x + 1/4], [1/12*x - 1/12, -1/6*x + 1, 5/12*x + 7/12],
#                       [1/4*x - 11/12, 1/6*x, 1/4*x + 17/12], [1/4*x - 7/12, 1/12*x + 5/12, 1/4*x + 13/12]]
#     # 7 candidates

#     for slit, t1, t2 in eval('candidates'+str(D)+'_'+str(i)):
#         p0 = polygons(vertices=[(0, 0), (slit, 0),
#                                 (WC1, 0), (WC1+t1, HC1), (t1, HC1)], ring=K)
#         p1 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+slit, 0), (WC2, 0),
#                                 (WC2+t2, HC2), (WC1+slit+t2, HC2), (slit+t2, HC2), (t2, HC2)], ring=K)
#         p2 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1),
#                                 (WC1-slit+t1, HC1), (t1, HC1)], ring=K)
#         surface = Surface_dict(base_ring=K)
#         surface.add_polygon(p0, label=0)
#         surface.add_polygon(p1, label=1)
#         surface.add_polygon(p2, label=2)
#         surface.change_base_label(0)
#         surface.change_edge_gluing(0, 0, 1, 6)
#         surface.change_edge_gluing(0, 1, 2, 3)
#         surface.change_edge_gluing(0, 2, 0, 4)
#         surface.change_edge_gluing(0, 3, 1, 0)
#         surface.change_edge_gluing(1, 1, 2, 2)
#         surface.change_edge_gluing(1, 2, 1, 4)
#         surface.change_edge_gluing(1, 3, 1, 7)
#         surface.change_edge_gluing(1, 5, 2, 0)
#         surface.change_edge_gluing(2, 1, 2, 4)
#         s6 = TranslationSurface(surface)
#         O = GL2ROrbitClosure(s6)
#         print(O.is_teichmueller_curve(3, 50))


# # In[ ]:


# check_model6(3, 2)
# check_model6(3, 3)
# check_model6(33, 1)


# # # Model 7 -- No TCurves

# # In[ ]:


# # Construction of the translation surfaces for the model 7.
# D = 33
# i = 1
# initialization_coordinates(D, i)
# candidates = [[1/4*x - 11/12, -1/12*x + 7/12, 1/4*x + 5/12],
#               [1/4*x - 11/12, 1/12*x + 5/12, 1/4*x + 13/12],
#               [1/12*x + 1/4, 1/4*x - 13/12, 1/12*x + 5/4],
#               [1/4*x - 7/12, -1/6*x + 1, 1/4*x + 1/12],
#               [1/4*x - 7/12, -1/12*x + 11/12, 1/4*x + 5/12],
#               [1/4*x - 7/12, 1/6*x, 1/4*x + 17/12],
#               [5/12*x - 17/12, -1/6*x + 1, 5/12*x + 7/12],
#               [5/12*x - 17/12, 1/6*x, 1/12*x + 11/12],
#               [5/12*x - 13/12, -1/12*x + 7/12, 5/12*x + 11/12],
#               [5/12*x - 13/12, 1/12*x - 1/4, 1/12*x + 7/12],
#               [5/12*x - 13/12, -1/12*x + 5/4, 5/12*x + 11/12],
#               [5/12*x - 13/12, 1/12*x + 5/12, 1/12*x + 7/12],
#               [1/4*x + 1/12, -1/3*x + 13/6, 1/4*x - 7/12],
#               [1/4*x + 1/12, 1/12*x + 1/12, 1/4*x + 13/12],
#               [1/4*x + 1/12, 1/3*x - 7/6, 1/4*x + 25/12],
#               [5/12*x - 3/4, 1/6, 1/12*x + 1/4],
#               [5/12*x - 3/4, -1/4*x + 25/12, 5/12*x + 1/4],
#               [5/12*x - 3/4, 5/6, 5/12*x + 5/4]]
# # The only candidates are for D=33 and i=1, there are 18 candidates

# for slit, t1, t2 in candidates:
#     p0 = polygons(vertices=[(0, 0), (WC1, 0),
#                             (WC1+t1, HC1), (t1, HC1)], ring=K)
#     p1 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+slit, 0), (2*WC1+slit, 0), (WC2, 0),
#                             (WC2+t2, HC2), (2*WC1+slit+t2, HC2), (WC1+slit+t2, HC2), (WC1+t2, HC2), (t2, HC2)], ring=K)
#     p2 = polygons(vertices=[(0, 0), (WC1, 0),
#                             (WC1+t1, HC1), (t1, HC1)], ring=K)
#     surface = Surface_dict(base_ring=K)
#     surface.add_polygon(p0, label=0)
#     surface.add_polygon(p1, label=1)
#     surface.add_polygon(p2, label=2)
#     surface.change_base_label(0)
#     surface.change_edge_gluing(0, 0, 1, 8)
#     surface.change_edge_gluing(0, 1, 0, 3)
#     surface.change_edge_gluing(0, 2, 1, 0)
#     surface.change_edge_gluing(1, 1, 1, 7)
#     surface.change_edge_gluing(1, 2, 2, 2)
#     surface.change_edge_gluing(1, 3, 1, 5)
#     surface.change_edge_gluing(1, 4, 1, 9)
#     surface.change_edge_gluing(1, 6, 2, 0)
#     surface.change_edge_gluing(2, 1, 2, 3)
#     s7 = TranslationSurface(surface)
#     O = GL2ROrbitClosure(s7)
#     print(O.is_teichmueller_curve(3, 50))


# # # Model 8 -- No TCurves

# # In[ ]:

# This is a test of github

# Construction of the translation surfaces for the model 8.
def check_model8():
    def model8(slit, t1, t2):
        p0 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1), (t1, HC1)],
                      ring=K)
        p1 = polygons(vertices=[(0, 0), (slit, 0), (WC1+slit, 0),
                                (2*WC1+slit, 0), (WC2, 0), (WC2+t2, HC2),
                                (WC2-WC1+t2, HC2), (WC1+slit+t2, HC2),
                                (WC1+t2, HC2), (t2, HC2)],
                      ring=K)
        p2 = polygons(vertices=[(0, 0), (WC1, 0), (WC1+t1, HC1), (t1, HC1)],
                      ring=K)
        surface = Surface_dict(base_ring=K)
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

    initialization_coordinates(33, 1)
    # The only candidates are for D=33 and i=1, there are 20 candidates
    candidates = [[1/12*x - 5/12, 1/6*x - 2/3, 1/12*x + 19/12],
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
                  [5/12*x - 1/12, -1/6*x + 5/3, 5/12*x - 1/12]]
    for [slit, t1, t2] in candidates:
        s8 = model8(slit, t1, t2)
        O = GL2ROrbitClosure(s8)
        print(O.is_teichmueller_curve(3, 50))
