import unittest

from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_case_201(self):
        self.assertTrue(TestParser.test(
"""Class Diagram:Shape {
    haha(){
        Return $dfshjgsdj;
    }
}
Class Program{
    main(){
        Foreach(x In 3 .. 4 By 2){
            
        }
    }
}"""
    ,"successful",201))
    def test_case_202(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
}"""
    ,"Error on line 2 col 1: <EOF>",202))
