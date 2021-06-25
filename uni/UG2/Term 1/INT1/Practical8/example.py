from logic import *


##### helper functions #####

counter = 1
def ask_p(kb, f):
  global counter
  print("\r\n", counter, "\tAsk: \t", f, "?")
  print(">>", "\t" + str(kb.ask(f)))
  counter = counter + 1

def tell_p(kb, f):
  global counter
  print("\r\n",counter, "\tTell: \t", f)
  print(">>", "\t" + str(kb.tell(f)))
  counter = counter + 1

##### /helper functions #####

kb = createResolutionKB()


# define some functions...
def Raining(x):
  return(Atom('Raining', x))

def Wet(x):
  return(Atom('Wet', x))

california = Constant('california')

kb = createResolutionKB()

# anywhere it is raining, it is wet
tell_p(kb, Forall('$x', Implies(Raining('$x'), Wet('$x'))))

# it is raining in california
tell_p(kb, Raining(california))

# is it wet in california?
ask_p(kb, Wet(california))

# is somewhere wet?
ask_p(kb, Exists('$y', Wet('$y')))

#kb.dump()


