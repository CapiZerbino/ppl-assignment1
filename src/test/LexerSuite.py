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
        self.assertTrue(TestLexer.test("""abc12d a1bCd""","abc12d,a1bCd,<EOF>",108))
    def test_case_109(self):
        self.assertTrue(TestLexer.test("""ab?cd""","ab,Error Token ?",109))
    def test_case_110(self):
        self.assertTrue(TestLexer.test("""a12b_Dd""","a12b_Dd,<EOF>",110))
    def test_case_111(self):
        self.assertTrue(TestLexer.test("""12abc""","12,abc,<EOF>",111))
    def test_case_112(self):
        self.assertTrue(TestLexer.test("""12_Abc""","12,_Abc,<EOF>",112))
    def test_case_113(self):
        self.assertTrue(TestLexer.test("""abc 1A2""","abc,1,A2,<EOF>",113))
    def test_case_114(self):
        self.assertTrue(TestLexer.test("""Class Triangle::Shape {}""","Class,Triangle,::,Shape,{,},<EOF>",114))
    def test_case_115(self):
        self.assertTrue(TestLexer.test("""Val My1stCons, My2ndCons: Int = 1 + 5, 2;""","Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,<EOF>",115))
    def test_case_116(self):
        self.assertTrue(TestLexer.test("""Class Program {main() {Out.printInt(Shape::$numOfShape);}}""","Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>",116))
    def test_case_117(self):
        self.assertTrue(TestLexer.test("""Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New By WriteLn writeln WRITELN Self""","Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,By,WriteLn,writeln,WRITELN,Self,<EOF>",117))
    def test_case_118(self):
        self.assertTrue(TestLexer.test("""+ - * / % ! && == = != < <= > >= ==. +. . .. ::""","+,-,*,/,%,!,&&,==,=,!=,<,<=,>,>=,==.,+.,.,..,::,<EOF>",118))
    def test_case_119(self):
        self.assertTrue(TestLexer.test("""()[].,;:{}""","(,),[,],.,,,;,:,{,},<EOF>",119))
    def test_case_120(self):
        self.assertTrue(TestLexer.test("""1_4561_13""","1456113,<EOF>",120))
    def test_case_121(self):
        self.assertTrue(TestLexer.test("""1234""","1234,<EOF>",121))
    def test_case_122(self):
        self.assertTrue(TestLexer.test("""0123""","0123,<EOF>",122))
    def test_case_123(self):
        self.assertTrue(TestLexer.test("""0x1_A""","0x1A,<EOF>",123))
    def test_case_124(self):
        self.assertTrue(TestLexer.test("""0b11111111""","0b11111111,<EOF>",124))
    def test_case_125(self):
        self.assertTrue(TestLexer.test("""0""","0,<EOF>",125))
    def test_case_126(self):
        self.assertTrue(TestLexer.test("""0X1_ATB""","0X1A,TB,<EOF>",126))
    def test_case_127(self):
        self.assertTrue(TestLexer.test("""0b1_0201""","0b10,201,<EOF>",127))
    def test_case_128(self):
        self.assertTrue(TestLexer.test("""0b123""","0b1,23,<EOF>",128))
    def test_case_129(self):
        self.assertTrue(TestLexer.test("""1234-0982""","1234,-,0982,<EOF>",129))
    def test_case_130(self):
        self.assertTrue(TestLexer.test("""1234 abcd 0982""","1234,abcd,0982,<EOF>",130))
    def test_case_131(self):
        self.assertTrue(TestLexer.test("""984753aBc_4s""","984753,aBc_4s,<EOF>",131))
    def test_case_132(self):
        self.assertTrue(TestLexer.test("""-----9877""","-,-,-,-,-,9877,<EOF>",132))
    def test_case_133(self):
        self.assertTrue(TestLexer.test("""5*1+3/2%f""","5,*,1,+,3,/,2,%,f,<EOF>",133))
    def test_case_134(self):
        self.assertTrue(TestLexer.test("""r = 111 + 55_658 * 0b111_11_111 / 0x1A67F5EE % 02425;""","r,=,111,+,55658,*,0b11111111,/,0x1A67F5EE,%,02425,;,<EOF>",134))
    def test_case_135(self):
        self.assertTrue(TestLexer.test("""'123'""","Error Token '",135))
    def test_case_136(self):
        self.assertTrue(TestLexer.test("""1.234 1.23_4""","1.234,1.234,<EOF>",136))
    def test_case_137(self):
        self.assertTrue(TestLexer.test("""1.2e3 1.2E3""","1.2e3,1.2E3,<EOF>",137))
    def test_case_138(self):
        self.assertTrue(TestLexer.test("""7E-10 7e-10 7E+10 7e+10""","7E-10,7e-10,7E+10,7e+10,<EOF>",138))
    def test_case_139(self):
        self.assertTrue(TestLexer.test("""1_234.567 1_23_4.56_7""","1234.567,1234.567,<EOF>",139))
    def test_case_140(self):
        self.assertTrue(TestLexer.test("""1_23.12_3""","123.123,<EOF>",140))
    def test_case_141(self):
        self.assertTrue(TestLexer.test("""123.""","123.,<EOF>",141))
    def test_case_142(self):
        self.assertTrue(TestLexer.test(""".123e10 .12_3e1_0""",".123e10,.123e10,<EOF>",142))
    def test_case_143(self):
        self.assertTrue(TestLexer.test(""".123e-10""",".123e-10,<EOF>",143))
    def test_case_144(self):
        self.assertTrue(TestLexer.test(""".e-123""",".e-123,<EOF>",144))
    def test_case_145(self):
        self.assertTrue(TestLexer.test("""123E-9""","123E-9,<EOF>",145))
    def test_case_146(self):
        self.assertTrue(TestLexer.test("""123e9""","123e9,<EOF>",146))
    def test_case_147(self):
        self.assertTrue(TestLexer.test("""123.123e-123""","123.123e-123,<EOF>",147))
    def test_case_148(self):
        self.assertTrue(TestLexer.test("""123.123E123""","123.123E123,<EOF>",148))
    def test_case_149(self):
        self.assertTrue(TestLexer.test("""1,234""","1,,,234,<EOF>",149))
    def test_case_150(self):
        self.assertTrue(TestLexer.test(""".1e34""",".1e34,<EOF>",150))
    def test_case_151(self):
        self.assertTrue(TestLexer.test("""1token""","1,token,<EOF>",151))
    def test_case_152(self):
        self.assertTrue(TestLexer.test("""asdfh#$afnd""","asdfh,Error Token #",152))
    def test_case_153(self):
        self.assertTrue(TestLexer.test("""token1 token2""","token1,token2,<EOF>",153))
    def test_case_154(self):
        self.assertTrue(TestLexer.test("""1.0""","1.0,<EOF>",154))
    def test_case_155(self):
        self.assertTrue(TestLexer.test("""1e-12""","1e-12,<EOF>",155))
    def test_case_156(self):
        self.assertTrue(TestLexer.test("""1.0e-12""","1.0e-12,<EOF>",156))
    def test_case_157(self):
        self.assertTrue(TestLexer.test("""0.001""","0.001,<EOF>",157))
    def test_case_158(self):
        self.assertTrue(TestLexer.test("""Boolean True""","Boolean,True,<EOF>",158))
    def test_case_159(self):
        self.assertTrue(TestLexer.test("""Boolean False""","Boolean,False,<EOF>",159))
    def test_case_160(self):
        self.assertTrue(TestLexer.test("""TRUE""","TRUE,<EOF>",160))
    def test_case_161(self):
        self.assertTrue(TestLexer.test("""FaLse""","FaLse,<EOF>",161))
    def test_case_162(self):
        self.assertTrue(TestLexer.test("""$var""","$var,<EOF>",162))
    def test_case_163(self):
        self.assertTrue(TestLexer.test("""$$var""","Error Token $",163))
    def test_case_164(self):
        self.assertTrue(TestLexer.test("""$avs$ags""","$avs,$ags,<EOF>",164))
    def test_case_165(self):
        self.assertTrue(TestLexer.test("""$""","Error Token $",165))
    def test_case_166(self):
        self.assertTrue(TestLexer.test("""$avs\n avg""","$avs,avg,<EOF>",166))
    def test_case_167(self):
        self.assertTrue(TestLexer.test("""$avs $ags""","$avs,$ags,<EOF>",167))
    def test_case_168(self):
        self.assertTrue(TestLexer.test("""abc?svn""","abc,Error Token ?",168))
    def test_case_169(self):
        self.assertTrue(TestLexer.test("""abc A12""","abc,A12,<EOF>",169))
    def test_case_170(self):
        self.assertTrue(TestLexer.test("""Array(1,2,3)""","Array,(,1,,,2,,,3,),<EOF>",170))
    def test_case_171(self):
        self.assertTrue(TestLexer.test("""Array(1.0,2.001,0.03)""","Array,(,1.0,,,2.001,,,0.03,),<EOF>",171))
    def test_case_172(self):
        self.assertTrue(TestLexer.test("""Array(0x1A,0b01)""","Array,(,0x1A,,,0b01,),<EOF>",172))
    def test_case_173(self):
        self.assertTrue(TestLexer.test("""\"This is a string containing tab \t\"""","\"This is a string containing tab \t\",<EOF>",173))
    def test_case_174(self):
        self.assertTrue(TestLexer.test("""Var r, s: Int;""","Var,r,,,s,:,Int,;,<EOF>",174))
    def test_case_175(self):
        self.assertTrue(TestLexer.test("""Class Diagram{}""","Class,Diagram,{,},<EOF>",175))
    def test_case_176(self):
        self.assertTrue(TestLexer.test("""main(){}""","main,(,),{,},<EOF>",176))