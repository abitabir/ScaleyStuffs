"""
Intelligent Systems 1
Week 7 Practical Lab Sheet
Dr James Stovold
This week we are focussing on propositional logic. This is split into two sections, the first contains
pen and paper logic exercises, the second looks at applying this logic in Python.
N.B. Just because these are called “pen & paper” exercises doesn’t mean you can’t use a computer,
in fact I recommend using a spreadsheet when producing a truth table (such as Q3a) to make your
life substantially easier.
Pen & Paper Exercises
1. Show that the following sentence of propositional logic is a tautology:
!(� ⇒ �) ∧ (� ⇒ �)* ⇒ !(� ⇒ �) ∨ (� ⇒ �)*
2. Prove that the following argument is not valid:
Every foo is a bar.
Baz is not a foo.
------------------
Baz is not a bar.
3. Consider the following knowledge base KB, based on the Wumpus world representation
from the lectures:
Along with the addition of a new sentence:
�! ∶ ¬B",$
Given the KB, R1—R6, and the following queries a, test if �� ⊨ � using the specified
methods:
a. Process of enumeration (i.e. produce the truth table) for � = �!,#
b. Inference for � = �#,!
Hint: you will need to add more than just R6 to your knowledge base!
Computer-Based Exercises
For the computer-based exercises this week, we will be using a propositional logic module from
Stanford (available on the VLE as logic.py). Don’t worry too much about how logic.py works right
now, instead peruse the example.py file to see how we can use it to develop simple propositional
logic sentences and a knowledge base.
4. Implement your logical sentences from Q3 above into a knowledge base in Python.
a. Verify your answers to 3a and 3b using Python.
"""
from logic import *

#pit = Atom("Pit")
#breeze = Atom("Breeze")
# going down wrong rabbit holes, hum

def ask_print(kb, f):  # to have records, hum
    print("Asking: ", f)
    print("Reply: ", kb.ask(f))
    return

def tell_print(kb, f):
    print("Informing: ", f)
    print("Reply: ", kb.tell(f))
    return

kb = createResolutionKB()

P11 = Atom("P11")
B11 = Atom("B11")
P12 = Atom("P12")
B12 = Atom("B12")
P21 = Atom("P21")
B21 = Atom("B21")
P22 = Atom("P22")
P31 = Atom("P31")
P13 = Atom("P13")

R1 = Not(P11)
#R2 = And(Implies(B11, Or(P12, P21)), Implies(Or(P12, P21), B11))  # a simpler equiv function exists
#R3 = And(Implies(B21, Or(P11, P21, P31)), Implies(Or(P11, P21, P31), B21))
R2 = Equiv(B11, Or(P12, P21))
R3 = Equiv(B21, Or(P11, Or(P22, P31)))
R4 = Not(B11)
R5 = B21

R6 = Not(B12)
#R7 = Equiv(B12, Or(P11, P22, P31))  # Or takes only 2 params - doesm't matter which two evaluated first as communicative
# P13 NOT P31!!! silly little typoes XO
R7 = Equiv(B12, Or(Or(P11, P22), P13))

tell_print(kb, R1)
tell_print(kb, R2)
tell_print(kb, R3)
tell_print(kb, R4)
tell_print(kb, R5)
tell_print(kb, R6)
tell_print(kb, R7)

ask_print(kb, P31)
ask_print(kb, P13)
