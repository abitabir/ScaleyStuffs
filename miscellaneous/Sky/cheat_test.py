import unittest
from cheat import testingPasswords  # only the function tested in this unittest, as opposed to the whole module with
# its unnecessary formattings ~ only for a more user friendly experience (UX)
# uhhh turns out the whole module ends up running but then the unittest does its work so, hmmmmm - if everything else
# but the target function is commented out in the module, only tests pass so idk hmmm

class PasswordDeduceTestCase(unittest.TestCase):

    def test_password_point_one(self):  # every method name beginning with 'test_' will be run automatically when this
        # module 'cheat_test.py' is run due to unittest module functionality
        pw_tested1 = {"little34": 2, "rhyno12": 2}  # unique keyyyys remember
        pw_perhaps1 = ["taller12", "crowded23", "mouse83", "limes52", "thread15", "house49"]
        result1 = testingPasswords(pw_tested1, pw_perhaps1)
        self.assertEqual(result1, "crowded23")  # let me know if they aren't the same, else it is ok ~ all well and good

    def test_password_point_two(self):
        pw_tested2 = {"keyboard951": 6, "12345drone": 6}
        pw_perhaps2 = ["worded73", "56brownie", "johndrew98", "dreaming91", "brandnew12", "crowned56"]
        result2 = testingPasswords(pw_tested2, pw_perhaps2)
        self.assertEqual(result2, "dreaming91")
