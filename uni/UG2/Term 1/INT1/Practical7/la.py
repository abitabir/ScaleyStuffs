"""
Intelligent Systems 1
Week 8 Lab Sheet
Dr James Stovold
This week we are focussing on SAT solving. Once again, this is split into two sections, the first
contains pen and paper logic exercises, the second looks at applying this logic in Python.
Pen & Paper Exercises
1. Consider the following logical sentence, L:
(� ⟺ �) ∧ (¬� ∨ ¬�)
Convert L to CNF. Show your working.
2. Solve L using the DPLL algorithm. Show your working.
Computer-Based Exercises
For the computer-based exercises this week, we will be using a simple SAT solver. This is provided
on the VLE, along with an example input file and readme showing how to run the solver.
3. Using the SAT solver provided to you, check your answers from above.
4. Consider the following problem:
Following your excellent work retrieving her cat treats in week 4, Pixel (autocratic ruler of
Pixeldale) has decided to employ you to help redesign her map of Pixeldale. The problem
she has is that her current map has lots of regions with similar colours, so now she would
like to re-colour the map in order to prevent any two neighbouring regions from having
the same colour.
Recall that the current map of Pixeldale looks like this:
Using the SAT solver, implement the above graph-colouring problem and find a solution
which colours all the castles (and therefore the regions surrounding the castles) without
any two neighbouring castles having the same colour. What is the fewest number of
colours you need to successfully colour this map?
"""

# DPLL algorithm ~ old school method, essentially search tree approach to SAT solving, depth first search

# typing into cmd on Windows:
# C:\projects\ScaleyStuffs\uni\INT1\Practical8>python SimpleSAT\simple-sat-master\src\sat.py -v --input example.in
# returns:
# Trying a = 0
# Trying b = 0
# Trying c = 0
# Current watchlist:
# a:
# ~a:
# b:
# ~b: ~b c, a ~b
# c: a b c
# ~c:
# Current assignment: ~a ~b ~c
# Clause a b c contradicted.
# Trying c = 1
# Found satisfying assignment #1:
# ~a ~b c

# C:\projects\ScaleyStuffs\uni\INT1\Practical7>python SimpleSAT\simple-sat-master\src\sat.py -v --input question4.in
# Trying RA = 0 Trying BA = 0 Trying GA = 0 Trying YA = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA,
# ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA YA: RA BA GA YA ~YA: RB: RB BB GB YB ~RB: ~RB
# ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: ~GB: ~GB ~YB, ~GB ~GA YB: ~YB: ~YB ~YA RC: RC
# BC GC YC ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: ~GC: ~GC ~YC, ~GC ~GA YC:
# ~YC: ~YC ~YA RD: RD BD GD YD ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD,
# ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD: ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG,
# ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC,
# ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF
# ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG:
# ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH,
# ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA ~YA Clause RA BA GA YA contradicted. Trying YA = 1 Trying RB = 0 Trying BB
# = 0 Trying GB = 0 Trying YB = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC,
# ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: ~GB: ~GB ~YB, ~GB ~GA YB: RB BB GB YB ~YB: ~YB ~YA RC: RC BC GC YC
# ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: ~GC: ~GC ~YC, ~GC ~GA YC: ~YC: ~YC
# ~YA RD: RD BD GD YD ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: ~GD:
# ~GD ~YD, ~GD ~GA YD: ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE
# ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC, ~YE ~YD RF: RF BF GF YF ~RF:
# ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: ~YF:
# ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG:
# ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH,
# ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI,
# ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ
# GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH,
# ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA
# ~GA YA ~RB ~BB ~GB ~YB Clause RB BB GB YB contradicted. Trying YB = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA,
# ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA YA: RA BA GA YA ~YA: RB: ~RB: ~RB
# ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: ~GB: ~GB ~YB, ~GB ~GA YB: RB BB GB YB ~YB:
# ~YB ~YA RC: RC BC GC YC ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: ~GC: ~GC
# ~YC, ~GC ~GA YC: ~YC: ~YC ~YA RD: RD BD GD YD ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD,
# ~BD ~YD, ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD: ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE,
# ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC,
# ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF
# ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG:
# ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH,
# ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB ~GB YB Clause ~YB ~YA contradicted. Trying GB = 1 Trying YB = 0
# Trying RC = 0 Trying BC = 0 Trying GC = 0 Trying YC = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA,
# ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB
# ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA,
# ~GB ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: ~GC: ~GC ~YC,
# ~GC ~GA YC: RC BC GC YC ~YC: ~YC ~YA RD: RD BD GD YD ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD
# ~GD, ~BD ~YD, ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD: ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE,
# ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC,
# ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF
# ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG:
# ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH,
# ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC ~GC ~YC Clause RC BC GC YC contradicted. Trying
# YC = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB
# ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC,
# ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: ~GC: ~GC ~YC, ~GC ~GA YC: RC BC GC YC ~YC: ~YC ~YA RD: RD BD GD YD
# ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD:
# ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC,
# ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC, ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF,
# ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB,
# ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG
# ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE,
# ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI,
# ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ:
# ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ:
# ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB
# ~YB ~RC ~BC ~GC YC Clause ~YC ~YA contradicted. Trying GC = 1 Trying YC = 0 Trying RD = 0 Trying BD = 0 Trying GD =
# 0 Trying YD = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB:
# ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC,
# ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC RD: ~RD: ~RD ~BD,
# ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD: RD BD GD YD
# ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC,
# ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE: ~YE ~YC, ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF,
# ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB,
# ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG
# ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE,
# ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI,
# ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ:
# ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ:
# ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB
# ~YB ~RC ~BC GC ~YC ~RD ~BD ~GD ~YD Clause RD BD GD YD contradicted. Trying YD = 1 Current watchlist: RA: ~RA: ~RA
# ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA YA:
# RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB
# ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC:
# RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD,
# ~BD ~YD, ~BD ~BA GD: ~GD: ~GD ~YD, ~GD ~GA YD: RD BD GD YD ~YD: ~YD ~YA RE: RE BE GE YE ~RE: ~RE ~BE, ~RE ~GE,
# ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: ~YE:
# ~YE ~YC, ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF:
# ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG,
# ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH,
# ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD ~GD YD Clause ~YD ~YA
# contradicted. Trying GD = 1 Trying YD = 0 Trying RE = 0 Trying BE = 0 Trying GE = 0 Trying YE = 0 Current
# watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA
# ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB,
# ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC:
# ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD,
# ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD RE: ~RE: ~RE
# ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC,
# ~GE ~GD YE: RE BE GE YE ~YE: ~YE ~YC, ~YE ~YD RF: RF BF GF YF ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF,
# ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: ~YF: ~YF ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG
# ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH
# BH GH YH ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE,
# ~GH ~GG YH: ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI,
# ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ,
# ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH,
# ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD
# GD ~YD ~RE ~BE ~GE ~YE Clause RE BE GE YE contradicted. Trying YE = 1 Trying RF = 0 Trying BF = 0 Trying GF = 0
# Trying YF = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB RC: ~RC: ~RC ~BC,
# ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC,
# ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD
# ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE,
# ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF, ~RF ~GF,
# ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF ~YF: ~YF
# ~YB, ~YF ~YD RG: RG BG GG YG ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: ~GG:
# ~GG ~YG, ~GG ~GE YG: ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH,
# ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI,
# ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ
# GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH,
# ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA
# ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF ~YF Clause RF BF GF YF contradicted.
# Trying YF = 1 Trying RG = 0 Trying BG = 0 Trying GG = 0 Trying YG = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA,
# ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA
# GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB:
# ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC:
# RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC, ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD:
# ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE,
# ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC,
# ~GE ~GD YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF:
# ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG,
# ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: RG BG GG YG ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH,
# ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF
# YF ~RG ~BG ~GG ~YG Clause RG BG GG YG contradicted. Trying YG = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA,
# ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA
# GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB:
# ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC:
# RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC, ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD:
# ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE,
# ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC,
# ~GE ~GD YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF:
# ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG,
# ~BG ~YG, ~BG ~BE GG: ~GG: ~GG ~YG, ~GG ~GE YG: RG BG GG YG ~YG: ~YG ~YE RH: RH BH GH YH ~RH: ~RH ~BH, ~RH ~GH,
# ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH, ~GH ~GE, ~GH ~GG YH: ~YH: ~YH ~YE,
# ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI
# ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ:
# ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH,
# ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF
# YF ~RG ~BG ~GG YG Clause ~YG ~YE contradicted. Trying GG = 1 Trying YG = 0 Trying RH = 0 Trying BH = 0 Trying GH =
# 0 Trying YH = 0 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC
# ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC,
# ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD
# ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE
# ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF,
# ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF
# ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: RG BG GG YG ~GG: YG: ~YG:
# ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH,
# ~GH ~GE, ~GH ~GG YH: RH BH GH YH ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI:
# ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ,
# ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG,
# ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC
# ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH ~BH ~GH ~YH Clause RH BH GH YH contradicted.
# Trying YH = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC
# ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC,
# ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD
# ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE
# ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF,
# ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF
# ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: RG BG GG YG ~GG: YG: ~YG:
# ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH ~YH,
# ~GH ~GE, ~GH ~GG YH: RH BH GH YH ~YH: ~YH ~YE, ~YH ~YG RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI:
# ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ,
# ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG,
# ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC
# ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH ~BH ~GH YH Clause ~YH ~YE contradicted. Trying
# GH = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC
# ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC,
# ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD
# ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE
# ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE, ~GH ~GE YE: RE BE GE YE ~YE: RF: ~RF:
# ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF
# GF YF ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE GG: RG BG GG YG ~GG: YG:
# ~YG: ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: ~BH: ~BH ~GH, ~BH ~YH, ~BH ~BE, ~BH ~BG GH: ~GH: ~GH
# ~GG YH: RH BH GH YH ~YH: ~YH ~YE, ~YH ~YG, ~GH ~YH RI: RI BI GI YI ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI:
# ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ,
# ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG,
# ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC
# ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH ~BH GH Clause ~GH ~GG contradicted. Trying BH =
# 1 Trying GH = 0 Trying YH = 0 Trying RI = 0 Trying BI = 0 Trying GI = 0 Trying YI = 0 Current watchlist: RA: ~RA:
# ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA,
# ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB
# BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC,
# ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC, ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD,
# ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD,
# ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD,
# ~BH ~BE GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE, ~GH ~GE YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF, ~RF ~GF,
# ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD YF: RF BF GF YF ~YF: RG:
# ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE, ~BH ~BG GG: RG BG GG YG ~GG: YG: ~YG:
# ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: RH BH GH YH ~BH: GH: ~GH: ~GH ~GG, ~BH ~GH YH: ~YH: ~YH
# ~YE, ~YH ~YG, ~GH ~YH, ~BH ~YH RI: ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI:
# ~GI: ~GI ~YI, ~GI ~GF YI: RI BI GI YI ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG,
# ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH,
# ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC ~YC ~RD ~BD
# GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH BH ~GH ~YH ~RI ~BI ~GI ~YI Clause RI BI GI YI contradicted.
# Trying YI = 1 Current watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA,
# ~BA ~YA GA: ~GA: ~GA ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB,
# ~RB ~RF BB: ~BB: ~BB ~GB, ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC
# ~BC, ~RC ~GC, ~RC ~YC, ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC,
# ~YE ~YC RD: ~RD: ~RD ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD
# ~GD: YD: ~YD: ~YD ~YA, ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE
# ~GE, ~BE ~YE, ~BE ~BC, ~BE ~BD, ~BH ~BE GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE, ~GH ~GE YE: RE BE GE YE ~YE:
# RF: ~RF: ~RF ~BF, ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB,
# ~GF ~GD YF: RF BF GF YF ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE,
# ~BH ~BG GG: RG BG GG YG ~GG: YG: ~YG: ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: RH BH GH YH ~BH: GH:
# ~GH: ~GH ~GG, ~BH ~GH YH: ~YH: ~YH ~YE, ~YH ~YG, ~GH ~YH, ~BH ~YH RI: ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI:
# ~BI: ~BI ~GI, ~BI ~YI, ~BI ~BF GI: ~GI: ~GI ~YI, ~GI ~GF YI: RI BI GI YI ~YI: ~YI ~YF RJ: RJ BJ GJ YJ ~RJ: ~RJ ~BJ,
# ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG, ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ,
# ~GJ ~GG, ~GJ ~GH, ~GJ ~GI YJ: ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC
# ~BC GC ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH BH ~GH ~YH ~RI ~BI ~GI YI Clause ~YI ~YF
# contradicted. Trying GI = 1 Trying YI = 0 Trying RJ = 0 Trying BJ = 0 Trying GJ = 0 Trying YJ = 0 Current
# watchlist: RA: ~RA: ~RA ~BA, ~RA ~GA, ~RA ~YA, ~RA ~RB, ~RA ~RC, ~RA ~RD BA: ~BA: ~BA ~GA, ~BA ~YA GA: ~GA: ~GA
# ~YA, ~GB ~GA, ~GC ~GA, ~GD ~GA YA: RA BA GA YA ~YA: RB: ~RB: ~RB ~BB, ~RB ~GB, ~RB ~YB, ~RB ~RF BB: ~BB: ~BB ~GB,
# ~BB ~YB, ~BB ~BA GB: RB BB GB YB ~GB: YB: ~YB: ~YB ~YA, ~GB ~YB, ~YF ~YB RC: ~RC: ~RC ~BC, ~RC ~GC, ~RC ~YC,
# ~RC ~RE BC: ~BC: ~BC ~GC, ~BC ~YC, ~BC ~BA GC: RC BC GC YC ~GC: YC: ~YC: ~YC ~YA, ~GC ~YC, ~YE ~YC RD: ~RD: ~RD
# ~BD, ~RD ~GD, ~RD ~YD, ~RD ~RE, ~RD ~RF BD: ~BD: ~BD ~GD, ~BD ~YD, ~BD ~BA GD: RD BD GD YD ~GD: YD: ~YD: ~YD ~YA,
# ~GD ~YD, ~YE ~YD, ~YF ~YD RE: ~RE: ~RE ~BE, ~RE ~GE, ~RE ~YE, ~RE ~RG, ~RE ~RH BE: ~BE: ~BE ~GE, ~BE ~YE, ~BE ~BC,
# ~BE ~BD, ~BH ~BE GE: ~GE: ~GE ~YE, ~GE ~GC, ~GE ~GD, ~GG ~GE, ~GH ~GE YE: RE BE GE YE ~YE: RF: ~RF: ~RF ~BF,
# ~RF ~GF, ~RF ~YF BF: ~BF: ~BF ~GF, ~BF ~YF, ~BF ~BB, ~BF ~BD GF: ~GF: ~GF ~YF, ~GF ~GB, ~GF ~GD, ~GI ~GF YF: RF BF
# GF YF ~YF: RG: ~RG: ~RG ~BG, ~RG ~GG, ~RG ~YG, ~RG ~RH BG: ~BG: ~BG ~GG, ~BG ~YG, ~BG ~BE, ~BH ~BG GG: RG BG GG YG
# ~GG: YG: ~YG: ~YG ~YE, ~GG ~YG RH: ~RH: ~RH ~BH, ~RH ~GH, ~RH ~YH BH: RH BH GH YH ~BH: GH: ~GH: ~GH ~GG,
# ~BH ~GH YH: ~YH: ~YH ~YE, ~YH ~YG, ~GH ~YH, ~BH ~YH RI: ~RI: ~RI ~BI, ~RI ~GI, ~RI ~YI, ~RI ~RF BI: ~BI: ~BI ~GI,
# ~BI ~YI, ~BI ~BF GI: RI BI GI YI ~GI: YI: ~YI: ~YI ~YF, ~GI ~YI RJ: ~RJ: ~RJ ~BJ, ~RJ ~GJ, ~RJ ~YJ, ~RJ ~RG,
# ~RJ ~RH, ~RJ ~RI BJ: ~BJ: ~BJ ~GJ, ~BJ ~YJ, ~BJ ~BG, ~BJ ~BH, ~BJ ~BI GJ: ~GJ: ~GJ ~YJ, ~GJ ~GG, ~GJ ~GH,
# ~GJ ~GI YJ: RJ BJ GJ YJ ~YJ: ~YJ ~YG, ~YJ ~YH, ~YJ ~YI Current assignment: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC ~BC GC
# ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH BH ~GH ~YH ~RI ~BI GI ~YI ~RJ ~BJ ~GJ ~YJ
# Clause RJ BJ GJ YJ contradicted. Trying YJ = 1 Found satisfying assignment #1: ~RA ~BA ~GA YA ~RB ~BB GB ~YB ~RC
# ~BC GC ~YC ~RD ~BD GD ~YD ~RE ~BE ~GE YE ~RF ~BF ~GF YF ~RG ~BG GG ~YG ~RH BH ~GH ~YH ~RI ~BI GI ~YI ~RJ ~BJ ~GJ YJ

# yay it got it so much computation OmO