"""
1. Define in your own words the following terms: state, state space, goal, action, and successor
function.
• State: data structure representing the present information about the problem.
• State space: all possible permutations of the state.
• Goal: state that satisfies some specified requirement from the problem.
• Action: function that moves between states in the state space.
• Successor function: function that returns all possible successive states and the
corresponding actions to get there.

2. You are provided with a 5-litre jug filled with water and an empty 2-litre jug. How can you get
precisely 1 litre of water into the 2-litre jug? Water may be discarded or poured between jugs,
however no more than the initial 5 litres is available and no other apparatus may be used.
a. Specify a problem representation for the water jug problem. Recall that a problem
representation consists of a set of states, a set of actions, an initial state, a path cost, and
a goal test. As this is a decision problem, the path cost can be ignored. Remember to
specify any preconditions for your actions.
A state is an ordered pair (x,y) where x is the number of litres of water in the large jug,
and y is the number of litres of water in the small jug. The initial state is therefore (5,0),
and the goals are all states of the form (x,1). There are four actions:
• Dump Big (DB): rewrite (x,y) to (0,y) with precondition that x is not 0.
• Dump Small (DS) : rewrite (x,y) to (x,0) with precondition y is not 0.
• Pour into Big (PB) : rewrite (x,y) to (x+p, y-p) where p (the amount poured) is
min(5-x,y) with the precondition that y is not 0, and x is not 5.
• Pour into Small (PS) : rewrite (x,y) to (x-p, y+p) where p (the amount poured) is
min(2-y,x) with the precondition x is not 0, and y is not 2.

b. Draw a search tree (like that on the last slide of the lectures this week) representing the
different states and actions to move between them for the water jug problem. You can
ignore any loops (i.e. ignore any actions that would take you to a node with the same
state as one of its ancestor nodes). Be sure to clearly indicate the initial node and which
nodes pass the goal test.
In the following tree, the label before each node indicates which operator was used to
obtain that node.
(5 0) <--------------- Initial state
 DB:(0 0)
 PS:(3 2)
 DB:(0 2)
 DS:(0 0)
PB:(2 0)
 DB:(0 0)
 DS:(3 0)
 DB:(0 0)
PS:(1 2)
 DB:(0 2)
 DS:(0 0)
PB:(2 0)
 DB:(0 0)
 DS:(1 0)
 DB:(0 0)
 PS:(0 1) <-- Goal state

c. In lay English, briefly describe every solution to the problem that is present in your tree.
The solution is: Pour 2 litres from the big jug into small jug, empty the small jug, pour 2
litres from the big jug into the small jug, empty the small jug, and pour all the water from
the big jug into the small jug.

3. The 2-space vacuum cleaner world is shown in Fig. 1. For this problem, we will be considering
the n-space vacuum cleaner world.
a. Given the aim of the n-space vacuum cleaner world is to eliminate the dirt on the floor,
define a goal for this problem. Be precise.
Clean(A) ∧ Clean(B) ∧ ... ∧ Clean(N)

b. Take your goal from part a and use it to define a problem representation for this problem.
State: ordered list of n boolean literals (1, 2, … n) detailing whether a given space is dirty
(false) or clean (true), and a single integer literal (a) showing the location of the agent.
Initial state: any is acceptable.
Actions: Agent can suck (S), which sets the a-th boolean literal to true; Agent can move
left or right (L, R) which increments/decrements a accordingly. If a is 1 or n, then only R
or L are permissible moves, respectively. If the square is already clean, the S does
nothing.
Goal test: as above, where Clean(i) tests if the i-th literal of state is true.
Path cost: Each action costs 1.

c. Are there any problems with your choice of goal or representation? Why? How might you
change the goal/representation to compensate?
Goal defined in (a) is easy to read, but could be defined more succinctly. If we defined
the state space first, we could have defined the goal as ∀x x.

"""