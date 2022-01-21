import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):

    def test_case_201(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
} 
Class Program{
    main(){
        var r, s: Int;
        r = 2.0;
        var a, b: Array[Int, 5];
        a[0] = s;
    }
}"""
    ,"successful",201))
    def test_case_202(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
}"""
    ,"Error on line 2 col 1: <EOF>",202))