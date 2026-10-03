import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def Test_upper(self):
        name="Jannat"
        upper=to_upper(name)
        self.assertEqual(upper, "Jannat")
        
if __name__=='__main__':
    unittest.main()