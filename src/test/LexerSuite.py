import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):

    def test_case_101(self):
        self.assertTrue(TestLexer.test("""##header1##""","<EOF>",101))
    def test_case_102(self):
        self.assertTrue(TestLexer.test("""##header2#header3##""","<EOF>",102))
    def test_case_103(self):
        self.assertTrue(TestLexer.test("""##header2## var x \n ##header3##""","var,x,<EOF>",103))
    def test_case_104(self):
        self.assertTrue(TestLexer.test("""##header2#abc#header3##""","<EOF>",104))
    def test_case_105(self):
        self.assertTrue(TestLexer.test("""##header1\n header2\n header3\t ##""","<EOF>",105))
    def test_case_106(self):
        self.assertTrue(TestLexer.test("""##header1#""","Error Token #",106))
    def test_case_107(self):
        self.assertTrue(TestLexer.test("""##header2<EOF>##""","<EOF>",107))
    def test_case_108(self):
        self.assertTrue(TestLexer.test("""1_4561_13""","1456113,<EOF>",108))
    def test_case_109(self):
        self.assertTrue(TestLexer.test("""1234""","1234,<EOF>",109))
    def test_case_110(self):
        self.assertTrue(TestLexer.test("""0123""","0123,<EOF>",110))
    def test_case_111(self):
        self.assertTrue(TestLexer.test("""0x1_A""","0x1A,<EOF>",111))
    def test_case_112(self):
        self.assertTrue(TestLexer.test("""0b11111111""","0b11111111,<EOF>",112))
    def test_case_113(self):
        self.assertTrue(TestLexer.test("""0""","0,<EOF>",113))
    def test_case_114(self):
        self.assertTrue(TestLexer.test("""0X1_ATB""","0X1A,TB,<EOF>",114))
    def test_case_115(self):
        self.assertTrue(TestLexer.test("""0b1_0201""","0b10,201,<EOF>",115))
    def test_case_116(self):
        self.assertTrue(TestLexer.test("""0b123""","0b1,23,<EOF>",116))
    def test_case_117(self):
        self.assertTrue(TestLexer.test("""'123'""","Error Token '",117))
    def test_case_118(self):
        self.assertTrue(TestLexer.test("""1.234""","1.234,<EOF>",118))
    def test_case_119(self):
        self.assertTrue(TestLexer.test("""1.2e3""","1.2e3,<EOF>",119))
    def test_case_120(self):
        self.assertTrue(TestLexer.test("""7E-10""","7E-10,<EOF>",120))
    def test_case_121(self):
        self.assertTrue(TestLexer.test("""1_234.567""","1234.567,<EOF>",121))
    def test_case_122(self):
        self.assertTrue(TestLexer.test("""1,234""","1,,,234,<EOF>",122))
    def test_case_123(self):
        self.assertTrue(TestLexer.test(""".1e34""",".1e34,<EOF>",123))
    def test_case_124(self):
        self.assertTrue(TestLexer.test("""1token""","1,token,<EOF>",124))
    def test_case_125(self):
        self.assertTrue(TestLexer.test("""asdfh#$afnd""","asdfh,Error Token #",125))
    def test_case_126(self):
        self.assertTrue(TestLexer.test("""token1 token2""","token1,token2,<EOF>",126))
    def test_case_127(self):
        self.assertTrue(TestLexer.test("""1.0""","1.0,<EOF>",127))
    def test_case_128(self):
        self.assertTrue(TestLexer.test("""1e-12""","1e-12,<EOF>",128))
    def test_case_129(self):
        self.assertTrue(TestLexer.test("""1.0e-12""","1.0e-12,<EOF>",129))
    def test_case_130(self):
        self.assertTrue(TestLexer.test("""0.001""","0.001,<EOF>",130))
    def test_case_131(self):
        self.assertTrue(TestLexer.test(""".01""",".01,<EOF>",131))
    def test_case_132(self):
        self.assertTrue(TestLexer.test("""1.0e""","1.0,e,<EOF>",132))
    def test_case_133(self):
        self.assertTrue(TestLexer.test("""0e123""","0e123,<EOF>",133))
    def test_case_134(self):
        self.assertTrue(TestLexer.test(""".e123""",".,e123,<EOF>",134))
    def test_case_135(self):
        self.assertTrue(TestLexer.test("""e123""","e123,<EOF>",135))
    def test_case_136(self):
        self.assertTrue(TestLexer.test("""Boolean True""","Boolean,True,<EOF>",136))
    def test_case_137(self):
        self.assertTrue(TestLexer.test("""Boolean False""","Boolean,False,<EOF>",137))
    def test_case_138(self):
        self.assertTrue(TestLexer.test("""TRUE""","TRUE,<EOF>",138))
    def test_case_139(self):
        self.assertTrue(TestLexer.test("""FaLse""","FaLse,<EOF>",139))
    def test_case_140(self):
        self.assertTrue(TestLexer.test("""$var""","$var,<EOF>",140))
    def test_case_141(self):
        self.assertTrue(TestLexer.test("""$$var""","Error Token $",141))
    def test_case_142(self):
        self.assertTrue(TestLexer.test("""$avs$ags""","$avs,$ags,<EOF>",142))
    def test_case_143(self):
        self.assertTrue(TestLexer.test("""$""","Error Token $",143))
    def test_case_144(self):
        self.assertTrue(TestLexer.test("""$avs\n avg""","$avs,avg,<EOF>",144))
    def test_case_145(self):
        self.assertTrue(TestLexer.test("""$avs $ags""","$avs,$ags,<EOF>",145))
    def test_case_146(self):
        self.assertTrue(TestLexer.test("""abc?svn""","abc,Error Token ?",146))
    def test_case_147(self):
        self.assertTrue(TestLexer.test("""abc A12""","abc,A12,<EOF>",147))
    def test_case_148(self):
        self.assertTrue(TestLexer.test("""Array(1,2,3)""","Array,(,1,,,2,,,3,),<EOF>",148))
    def test_case_149(self):
        self.assertTrue(TestLexer.test("""Array(1.0,2.001,0.03)""","Array,(,1.0,,,2.001,,,0.03,),<EOF>",149))
    def test_case_150(self):
        self.assertTrue(TestLexer.test("""Array(0x1A,0b01)""","Array,(,0x1A,,,0b01,),<EOF>",150))
    def test_case_151(self):
        self.assertTrue(TestLexer.test("""\"This isn\'\"t my thing\t\"""","This isn\'\"t my thing\t,<EOF>",151))
    def test_case_152(self):
        self.assertTrue(TestLexer.test("""Var r, s: Int;""","Var,r,,,s,:,Int,;,<EOF>",152))
    def test_case_153(self):
        self.assertTrue(TestLexer.test("""Class Diagram{}""","Class,Diagram,{,},<EOF>",153))
    def test_case_154(self):
        self.assertTrue(TestLexer.test("""main(){}""","main,(,),{,},<EOF>",154))