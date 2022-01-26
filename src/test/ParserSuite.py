import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):

    def test_case_201(self):
        self.assertTrue(TestParser.test(
"""Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfShape() {
            Return $numOfShape;
}
}
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}"""
    ,"successful",201))
    def test_case_202(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
}"""
    ,"successful",202))
    def test_case_203(self):
        self.assertTrue(TestParser.test(
"""Class Rectangle: Shape {}"""
    ,"successful",203))
    def test_case_204(self):
        self.assertTrue(TestParser.test(
"""class Rectangle {}"""
    ,"Error on line 1 col 0: class",204))
    def test_case_205(self):
        self.assertTrue(TestParser.test(
"""Class _Shape {}"""
    ,"successful",205))
    def test_case_206(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_1{
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0;
}"""
    ,"successful",206))
    def test_case_207(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_2{
    Val My1stCons, My2ndCons: Int;
    Val $staticname, nonstatic: String;
    Var $x, $y : Int = 0, 0;
}"""
    ,"successful",207))
    def test_case_208(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_2{
    My1stCons, My2ndCons: Int;
}"""
    ,"Error on line 2 col 13: ,",208))
    def test_case_209(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_2{
    Val Var, My2ndCons: Int;
}"""
    ,"Error on line 2 col 8: Var",209))
    def test_case_210(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_2{
    Val My2ndCons, : Int;
}"""
    ,"Error on line 2 col 19: :",210))
    def test_case_211(self):
        self.assertTrue(TestParser.test(
"""Class Test_Attribute_2{
    Val My2ndCons, My1ndCons;
}"""
    ,"Error on line 2 col 28: ;",211))
    def test_case_212(self):
        self.assertTrue(TestParser.test(
"""Class Test_Method{
    method1 (para1: Int; para2: String; para3: Float; para4: Array[Int, 5]; para5: Newclass){}
}"""
    ,"successful",212))
    def test_case_213(self):
        self.assertTrue(TestParser.test(
"""Class Test_Method{
    Constructor (para1: Int; para2: String; para3: Float; para4: Array[Int, 5]){}
}"""
    ,"successful",213))
    def test_case_214(self):
        self.assertTrue(TestParser.test(
"""Class Test_Method{
    Destructor (){}
}"""
    ,"successful",214))
    def test_case_215(self):
        self.assertTrue(TestParser.test(
"""Class Test_Method{
    Destructor (para1: Int){}
}"""
    ,"Error on line 2 col 16: para1",215))
    def test_case_216(self):
        self.assertTrue(TestParser.test(
"""Class Dog {
    Val breed: String;
    Var age: Int;
    Val color: String;
    barking() {

    }
    hungry(){

    }
    sleeping() {

    }
}
Class Program {
    main(){
        
    }
}"""
    ,"successful",216))
    def test_case_217(self):
        self.assertTrue(TestParser.test(
"""Class Test_Expression{
    Val x : Int = 1 + 2 * 3 / 4 % 5 - 6;
}
Class Program{
    main(){

    }
}"""
    ,"successful",217))
    def test_case_218(self):
        self.assertTrue(TestParser.test(
"""Class Test_Expression{
    Var isCorrect: Boolean = True;
    Var isWrong: Boolean = False;
    Val x : Boolean = !isCorrect && isWrong;
}
Class Program{
    main(){
        
    }
}"""
    ,"successful",218))
    def test_case_219(self):
        self.assertTrue(TestParser.test(
"""Class Test_Expression{
    Var String1: String = "hello";
    Val String2: String = "World";
    Val $StringFinal : String = String1 +. String2;
    Val $AnotherString : String = "String1" +. "String2";
}
Class Program{
    main(){
        
    }
}"""
    ,"successful",219))
    def test_case_220(self):
        self.assertTrue(TestParser.test(
"""Class Test_Expression{
    Val isSame: Boolean = "This is my string" ==. "This is also another string";
}
Class Program{
    main(){
        
    }
}"""
    ,"successful",220))
    def test_case_221(self):
        self.assertTrue(TestParser.test(
"""Class Shape{
    Val width: Float;
    Val height: Float;
    Constructor(height: Float; width: Float){
        width = width;
        height = height;
    }
    getArea(){
        Return width * height;
    }
}
Class Test_Expression{
    Val getArea: Float = Shape.getArea();
}
Class Program{
    main(){

    }
}"""
    ,"successful",221))
    def test_case_222(self):
        self.assertTrue(TestParser.test(
"""Class MenuItem: GuiComponents{
    Var LABEL: String;
    Var anchor: Anchor;
    Var bounds: Rectangle;
    Var font: Font;
    Constructor(label: String; hoverColor: Color){
        LABEL = label;
        hoverColor = hoverColor;
    }
    setProperties(anchor: Anchor; x: int; width: int; height: int){
        anchor = anchor;
        bounds = New Rectangle(x,y,width, height);
    }
    update(gametime: GameTime){
        
        if(bounds.intersects(Mouse.getPosition())){
            fontColor = hoverColor;
            onHover();
            if(Mouse.buttonDownOnce(MouseKeys.BUTTON_1)){
                onClick();
            }
        } Else {
             fontColor = Color.WHITE;
        }
    }
    draw(g2d: Graphic2D){
         g2d.setFont(font);
        g2d.setColor(fontColor);
        g2d.drawString(LABEL, bounds.x + 5, bounds.y + 15);
    }
}"""
    ,"successful",222))
    def test_case_223(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
} 
Class Program{
    main(){
        a=3;
    }
}"""
    ,"successful",223))
    def test_case_224(self):
        self.assertTrue(TestParser.test(
"""Class Diagram{
}"""
    ,"successful",224))
    def test_case_225(self):
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
    ,"successful",225))
    def test_case_226(self):
        self.assertTrue(TestParser.test(
"""Class Program{
    main(){
        ## Comment something here ##
        Var a : Int;
        a = 5;
        ## Comment something here ##
        Var b : String;
        Val $c, d, $acc: String = "Here is another string","asd";
        Foreach(a In 1..2){
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
    ,"successful",226))
    def test_case_227(self):
        self.assertTrue(TestParser.test(
"""Class Program {
    main(){
        Var $num1, $num2, $num3, $num4 :  Boolean = True, True, False;
        Myfunc(){
            a = 1;
        }
    }
}"""
    ,"successful",227))
    def test_case_228(self):
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
    ,"successful",228))
    def test_case_229(self):
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
        }
    }
}"""
    ,"successful",229))
    def test_case_230(self):
        self.assertTrue(TestParser.test(
"""Class main{}"""
    ,"successful",230))