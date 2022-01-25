import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):

    def test_case_201(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
} 
Class Program{
    main(){
        Var r, s: Int;
        r = 2.0;
        Var a, b: Array[Int, 5];
        s = r * r * Self.myPI;
        a[0] = s;
    }
}"""
    ,"successful",201))
    def test_case_202(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
}"""
    ,"Error on line 2 col 1: <EOF>",202))
    def test_case_203(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
    getArea(){
        Return a;
    }
}
Class Program{
    main(){
        ## Comment something here ##
        Var a : Int;
        a = 5;
        Var b : String;
    }
}"""
    ,"successful",203))
    def test_case_204(self):
        self.assertTrue(TestParser.test(
"""Class Program{
    main(){
        ## Comment something here ##
        Var a : Int;
        a = 5;
        ## Comment something here ##
        Var b : String;
        Val $c, d, $acc: String = "Here is another string","asd";
        Foreach(a In 1 .. 2){
            Var a: Int;
            If(a ==1){
                a = 2 * call(aladin);
                Break;
                Invocation::$id();
            }
        }
        Return;
    }
}"""
    ,"successful",204))
    def test_case_205(self):
        self.assertTrue(TestParser.test(
"""Class Program {
    main(){
        Var $num1, $num2, $num3, $num4 :  Boolean = True, True, False;

    }
}"""
    ,"successful",205))
    def test_case_206(self):
        self.assertTrue(TestParser.test(
"""Class Shape {
    GetFunc(a,b : Int ; c : Float) {
        Val num1: Int = 1;
        Val num1, num2: Int = 1,2;
    }
}
Class Program{
    main(){
        something = (True == (!False));
    }
}"""
    ,"successful",206))
    def test_case_207(self):
        self.assertTrue(TestParser.test(
"""Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, $width: Int;
    Var a : Array[Int,3] = Array( 1,2,3 );

    $getNumOfShape() {
        Return $numOfShape;
    }
}
Class Program{
    main(){
        Var a : Int = 12;
        If(a > 0){
            a = 0x0A + 0x12_ABCD; 
            Foreach(i In 1 .. 100 By 2){
                a =  a[1+2+3];
                a = a::getShape();
                Continue;
            }
            
        }
        Else{
            a = a * 3 / 3 /3 /4 /4 + 5 -9; 
            Break;
        }
    }
}"""
    ,"successfu",207))