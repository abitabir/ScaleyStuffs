"""
5 (30 marks) User-Defined Data Structure
The code for this question must be written in the provided file question_5.py.
Optimal Polygon triangulation problem.
We consider convex polygons P defined by a sequence of vertices hv0, v1, . . . , vni where the
straight line segments between consecutive vertices, called sides, form the boundary of P.
Convexity means that any segment between two vertices will not go outside P. If a segment goes
between two non-adjacent vertices of P it is called a chord. A chord splits the polygon into two
smaller polygons. Note that a chord always divides a convex polygon into two convex polygons.
(a) (b) (c)
Figure 2: a) a convex polygon P, b) and c) two possible triangulations of P.
A triangulation of a polygon can be thought of as a set of chords that divide the polygon into
triangles such that no two chords intersect (except possibly at a vertex). The problem is to find a
triangulation that minimises the sum of the weights of the triangles. Two examples of a polygon
triangulation are given in Figure 2. To determine which of the two triangulation is optimal, we
need to define a cost function. The cost function used for this question is the sum of the side
lengths in a triangle using the 1-norm distance d1 given in Equation 1.
d1(v1, v2) = jx1 􀀀 x2j + jy1 􀀀 y2j (1)
To facilitate your implementation, we have provided a partially implemented class Polygon that
you will need to complete in the file question_5.py.
• The attribute _vertices stores the list of vertices representing the polygon
• The "constructor" __init__(vertices) creates an instance of Polygon given a
list of vertices (a list of Point objects). For simplicity and in order to minimise the amount
of code you need to read, we assume that the list given in the parameter represents a
convex polygon.
Page 5 of 7 Continued.
In the same file we have also provided the class Point representing a point in a 2D space. The
class Point is complete and must not be changed. The class has:
• two attributes x and y which are float representing the coordinates of the point in a 2D
space.
• a static method distance(p1, p2) that returns the 1-norm distance d1(p1, p2)
between the two Point objects p1 and p2.
(i) [15 marks] Implement a public method split(p1, p2) in the class Polygon. The
method splits the polygon into two sub-polygons along the chord [p1, p2] where p1 and p2 are
two Point objects.
• The method returns a set of Polygon objects containing the two polygons resulting
from the split.
• The method must raise a TypeError if any parameter is None.
• The method must raise a ValueError if at least one of the parameters is not a
polygon’s vertex.
• The method must raise a ValueError if p1 and p2 are the same vertex or two
adjacent vertices in the polygon.
(ii) [15 marks] Finding the cost of an optimal triangulation of a polygon P = hv0, v1, ..., vni has a
nice recursive substructure. The idea is to divide the polygon into three parts (see Figure 3(a)): a
single triangle (in white), the sub-polygon to the left (dark grey), and the sub-polygon to the right
(light grey). We try all possible divisions like this until we find the one that minimises the weight
of the triangle plus the cost of the triangulation of the two sub-polygons.
The cost can be determine by the recursive function cost[1, n]. The base case of the recursion
is a line segment hvi, vi+1i (that is, a polygon with zero area), which has a cost cost[i, i] = 0.
Figure 3(a) shows the first step of the recursion, where vertex v4 is picked for dividing the
polygon P. The cost function cost is defined by Equation 2.
cost[i, j] =

0 if i = j
minik<j(cost[i, k] + cost[k + 1, j] + weight(vi􀀀1, vk, vj)) if i < j (2)
Where weight(vi, vk, vj) = d1(vi, vk) + d1(vk, vj) + d1(vj, vi) is the weight of a triangle
hvi, vk, vji, and d1(vi, vk) is the 1-norm distance between vertices vi and vk.
Page 6 of 7
Module Code
COM00015C
(a) (b) (c)
Figure 3: a) a convex polygon P, b) one possible triangulation of P, and c) an alternative
triangulation of P.
For example, to triangulate the four-sided polygon hv4, v5, v6, v7i, shown in light grey in
Figure 3(a), there are two alternatives:
• k = 5 ) cost[5, 7] = cost[5, 5] + cost[6, 7] + weight(v4, v5, v7) (Figure 3(b))
• k = 6 ) cost[5, 7] = cost[5, 6] + cost[7, 7] + weight(v4, v6, v7) (Figure 3(c))
If the distance from v4 to v6 is greater than the distance from v5 to v7, k = 5 is chosen,
otherwise k = 6 is chosen.
Implement the public method cost() in the class Polygon. The method must return the cost
(as a float) of an optimal triangulation of the polygon. The implementation must use recursion,
failing to do so will result in a mark of 0 for this question.
End of examination paper
Page 7
"""