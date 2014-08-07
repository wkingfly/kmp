import unittest
import sys
sys.path.append('..')
from kmp import kmp

class Test_strFind(unittest.TestCase):

    def setUp(self):
        matrix = 'acdabcabcdabcabcx' 
        child = 'abcabcx'
        self.sF = kmp.strFind(child, matrix)
    def tearDown(self):
        del self.sF
    
    def test_part_match(self):
        self.sF.part_match()
        l = [0,0,0,1,2,3,0]
        self.assertEqual(self.sF.part_list, l)

    def test_find(self):
        self.assertTrue(self.sF.find())


if __name__ == '__main__':
    unittest.main()
