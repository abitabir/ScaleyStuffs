# notes

# in order to use sentences of the form Bv(x, y) we need a more powerful logic, as opposed to bloating our knowledge base with facts
# first order logic comes in
# Sibling(James, x) ⟹ Sibling(x,James), where James is a constant, x is a variable
# ∀x∃y Loves(x, y) <- means all loves some/for all x, there exists y who x loves aka everyone loves someone
# ∃y∀x Loves(x, y) <- means all loves some/for{/there exists} some y, there exists y who is loved by everyone
# ∃y∀x Loves(y, x) <- means some loves all/for{/there exists} some y, there exists y who loves everyone
# ∀y∃x Loves(x, y) <- means all loved by some/for all y, there exists some x who loves them  # I thinks XOS

# Tell_KB(Brother(Richard, John))  # kinda a setter
# Ask_KB(Brother(Richard, x))  # a getter returning x/John
# Tell(KB, ∀x King(x) => Person(x))  # fopl inquiring KB =)
# but not all queries make sense, it just gives T or F e.g Ask(KB, ∃x Person(x))
# would be more useful if gave us an instance of x - what x satisfies this particular sentence query
# e.g if it returned {x/John} - meaning this is true if we replace x by John
# but how do we find our substitution ~ informally, a substitution is some function which maps variables to terms
# consider formula e = Likes(x, y), where neither variable bound by quantifier
# and substitution θ = {x/Abir, y/Driving}  # other notations: Subst(e, θ); eθ etc
# ∀v a | Subst({v/g}, a)  # meaning for all v, some sentence alpha | applying a substitution, where v is replaced by some g, and we're gonna apply that substitution to some alpha again
# key point is that the substitution is simultaneous, as opposed to sequential (so don't need a thord variable to swap two variables as you tend to need to when programming)
# {very a level mathsy substitution, hummies}
# if e is an expression, and θ is a substitution, then θ(e) is an instance of e {ohhhhh yeahhhhhh},
#getting rid of all of its free variables and replacing them with bound variables, making e ground (an expression is ground if it contains no free varibales)
# expression θ(e) is a ground instance of e if it is both an instance of e and its ground
# for expression e, ev(gr) is the set of all ground instances of e ~ all the subsitutions substitutions we van use
# for expressions set E, Ev(gr) is the set of ground instances of all expressions in E

# can eliminate existential quantifiers: ∃x Crown(x) ∧ OnHead(x,John)  turns to  Crown(C1) ∧ OnHead(C1,John)
# this is done by producing a new constant K and replacing the {free} variable by that new constant
# existential quantifier eliminated cuz we are only talking about an instance of x now I think
# we call it C1 cuz we don't care what x is, all we know is that it exists
# by making it into a constant we can set up a new set of sentences based off that existential quantifier
# and replace sentences containing existential quantifiers by sentences which have new all bound variables

# universal instantiation, on other hand, more complicated
# ∀x King(x) ∧ Greedy(x) ⟹ Evil(x)
# becomes
# King(John) ∧ Greedy(John) ⟹ Evil(John)
# King(Richard) ∧ Greedy(Richard) ⟹ Evil(Richard)
# key thing we do not replace for all x like we do for there exists

# propositionalisation  # can reduce first ordr logic down into propositional logic ~ lifting lemma

# Unification {making two sentences identical}
# Examples
# Unify(Knows(John, x), Knows(John, Jane)) = {x/Jane}
# Unify(Knows(John, x), Knows(y, Bill)) = {x/Bill, y/John}
# Unify(Knows(John, x), Knows(y, Mother(y)) = {y/John, x/Mother(John)}
# Unify(Knows(John, x), Knows(x, Elizabeth)) = Fail
# Unify(Knows(John, x), Knows(z17, Elizabeth)) = {x/Elizabeth,z17/John}
# This last step is referred to as standardising apart the variable x
# to rectify this, introducing a new variable z17 ~ now substitution can work, hum


"""
Intelligent Systems 1
Week 9 Lab Sheet
Dr James Stovold
This week we are looking at first-order logic. Once again, this is split into two sections, the first
contains pen and paper logic exercises, the second looks at applying this logic in Python.
Pen & Paper Exercises
1. For each of the following formulae, state whether they are unifiable. If they are, provide a
unifying substitution. (Variables are represented by lower-case letters, constants by
upper-case).
a. p(x) p(A)
b. s(x) t(A)
c. s(x) s(y)
d. s(x) s(A, B)
e. p(f(x, A), g(B, B)) p(y, g(z, w))
f. q(x, g(y, x)) q(A, g(B, C))
2. Consider the following scenario:
If something both croaks and eats flies, it must be a frog. If something both chirps and
sings, it must be a canary. All frogs are green, and all canaries are yellow.
a. Represent the above scenario in first-order logic.
b. Consider the following statement, S:
Fritz croaks and eats flies, therefore Fritz is green.
Use the following methods to prove S:
i. Forward chaining
ii. Backward chaining
Computer-Based Exercises
For the computer-based exercises this week, we will be using the logic library from week 7 {aka Practical 6}. This
is provided on the VLE, along with an example input file updated for FO logic.
3. Implement the scenario from Q2 into Python using the logic library.
a. Test whether the statement S is true.
b. Ask whether all frogs eat flies.
c. Ask whether any frogs eat flies.
d. Which of these queries (b, c) work? Why?
Challenge: Consider the following scenario:
There is a monkey at the door to a room. In the middle of the room a banana is hanging from the
ceiling. The monkey is hungry and wants to get the banana, but it cannot reach high enough from
the door. At the window of the room there is a box that the monkey may use. The monkey can
perform the following actions: walk on the floor, climb onto the box, push the box around (if the
monkey is already at the box) and grasp the banana if standing on the box directly under the
banana.
Write a Python program which can determine whether the monkey can get the banana.
"""

# 1.
# Unify(p(x), p(A)) = {x/A}
# Unify(s(x), t(A)) = Ununifiable {can't replace functions smh}
# Unify(s(x), s(y) = {x/y} or {y/x}
# Unify(s(x), s(A, B) = Ununifiable {cant replace one var with two! {x/{A, B)}}
# Unify(p(f(x, A), g(B, B)), p(y, g(z, w))) = {y/f(x, A), z/B, w/B}
# Unify(q(x, g(y, x)), q(A, g(B, C))) = Fail

# 2.
# a)
# ∀x Croaks(x) /\ EatsFlies(x) => IsFrog(x)
# ∀y Chirps(y) /\ Sings(y) => IsCanary(y)
# ∀x IsFrog(x) => IsGreen(x)
# ∀y IsCanary => IsYellow(y)
# b)
# i.
# S can be represented as Croaks(Fritz) /\ EatsFlies(Fritz) => IsGreen(Fritz)
# Forward Chaining (starting bottom up):
#
#           IsGreen(Fritz)
#                 |         ∀x IsFrog(x) => IsGreen(x)
#           IsFrog(Fritz)
#                 /\        ∀x Croaks(x) /\ EatsFlies(x) => IsFrog(x)
#                /--\
#               /    \
#    Croaks(Fritz)  EatsFlies(Fritz)
# ii.
# Backward Chaining (starting top down):
#
# {x/Fritz} IsGreen(Fritz)
#                 |         ∀x IsFrog(x) => IsGreen(x)
#           IsFrog(Fritz)
#                 /\        ∀x Croaks(x) /\ EatsFlies(x) => IsFrog(x)
#                /--\
#               /    \
#    Croaks(Fritz)  EatsFlies(Fritz)
#          {}               {}
# 3.
# a
from logic import *

# helper functions

counter = 1

def ask_print(kb, f):
    global counter
    print("\n", counter, "\tAsking: \t", f, "?")
    print(">>", "\t" + str(kb.ask(f)))
    counter += 1

def tell_print(kb, f):
    global counter
    print("\n", counter, "\tTelling: \t", f, "!")
    print(">>", "\t" + str(kb.tell(f)))
    counter += 1

kb = createResolutionKB()

def Croaks(x):
    return Atom("Croaks", x)

def EatsFlies(x):
    return Atom("EatsFlies", x)

def IsFrog(x):
    return Atom("IsFrog", x)

def Chirps(x):
    return Atom("Chirps", x)

def Sings(x):
    return Atom("Sings", x)

def IsCanary(x):
    return Atom("IsCanary", x)

def IsGreen(x):
    return Atom("IsGreen", x)

def IsYellow(x):
    return Atom("IsYellow", x)

# defining the rules of the world we want to model R1..R4, hum
frogging = Forall("$x", Implies(And(Croaks("$x"), EatsFlies("$x")), IsFrog("$x")))  # didn't allow me to be patriotically "£x" T.T
canarying = Forall("$x", Implies(And(Chirps("$x"), Sings("$x")), IsCanary("$x")))
frogcoloured = Forall("$x", Implies(IsFrog("$x"), IsGreen("$x")))
canarycoloured = Forall("$x", Implies(IsCanary("$x"), IsYellow("$x")))

tell_print(kb, frogging)
tell_print(kb, canarying)
tell_print(kb, frogcoloured)
tell_print(kb, canarycoloured)

# defining what we know about our dear fritz
fritz = Constant("fritz")  # didn't let me do "FRITZ" even tho constants should be capital in FOPL T.T ~ different conventions, ig
f1 = Croaks(fritz)
f2 = EatsFlies(fritz)
#S = Implies(And(Croaks(fritz), EatsFlies(fritz)), IsGreen(fritz))  # did this wrong
#ask_print(kb, S)

tell_print(kb, f1)
tell_print(kb, f2)

ask_print(kb, IsGreen(fritz))

# b.
b = Forall("$x", Implies(IsFrog("$x"), EatsFlies("$x")))
# c.
c = Exists("$x", And(IsFrog("$x"), EatsFlies("$x")))

ask_print(kb, b)  # should return true, but returns I don't know, hum
ask_print(kb, c)