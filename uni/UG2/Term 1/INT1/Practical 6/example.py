from logic import *

Summer = Atom('Summer')
California = Atom('California')
Rain = Atom('Rain')
Wet = Atom('Wet')
print(Implies(And(Summer, California), Not(Rain)))  # summer /\ cali => not raining



def ask_p(kb, f):
  print("Ask: ", f)
  print(kb.ask(f))

def tell_p(kb, f):
  print("Tell: ", f)
  print(kb.tell(f))

kb = createResolutionKB()
tell_p(kb, Implies(Rain,Wet))
ask_p(kb, Wet)
ask_p(kb, Rain)
tell_p(kb, Rain)
ask_p(kb, Wet)
kb.dump()


