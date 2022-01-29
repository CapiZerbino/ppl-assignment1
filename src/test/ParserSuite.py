import unittest

from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_class_declaration(self):
        input = """
        Class Shape {

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_class_with_keyword_as_name(self):
        input = """
        Class Array {
            
        }
        """
        expect = "Error on line 2 col 14: Array"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_static_attribute_declaration(self):
        input = """
        Class Program {
            Val $a, $c: Int = 1,2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_attribute_declaration(self):
        input = """
        Class Program {
            Val a, c: Int = 1,2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_normal_method_declaration(self):
        input = """
        Class Program {
            main() {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_method_declaration_with_parameter(self):
        input = """
        Class Program {
            main(a, b, c :Int) {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_method_declaration_with_parameter_list(self):
        input = """
        Class Program {
            main(a, b, c: Int; d, e, f: Int; g, h: Float) {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_constructor_method(self):
        input = """
        Class Program {
            Constructor(a, b, c: Int; d, e, f: Int; g, h: Float) {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_destructor_method(self):
        input = """
        Class Program {
            Destructor() {

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_destructor_method_with_parameter(self):
        input = """
        Class Program {
            Destructor(ant, bee, cat: Int) {

            }
        }
        """
        expect = "Error on line 3 col 23: ant"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_method_declaration_with_static_parameter(self):
        input = """
        Class Program {
            main(ant, bee, cat: Int; $dog: Float) {

            }
        }
        """
        expect = "Error on line 3 col 37: $dog"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_mixed_attribute_declaration(self):
        input = """
        Class Program {
            Val a, $b, $c, d : Int = 1, 2, 3, 4;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_attribute_declaration_without_semi_ending(self):
        input = """
        Class Program {
            Val a, $b, $c, d : Int = 1, 2, 3, 4
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_attribute_declaration_with_more_expression(self):
        input = """
        Class Dog {
            Val a, $b, $c, d : Int = 1, 2, 3, 4, 5;

            Constructor(height : Float; age : Int;  is_tall : Boolean) {
                
            }

            Destructor() {

            }

            main(action: String) {
                
            }
        }
        """
        expect = "Error on line 3 col 47: ,"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_attribute_declaration_with_less_expression(self):
        input = """
        Class Dog {
            Val a, $b, $c, d : Int = 1, 2, 3;

            Constructor(height : Float; age : Int;  is_tall : Boolean) {
                
            }

            Destructor() {

            }

            main(action: String) {
                
            }
        }
        """
        expect = "Error on line 3 col 44: ;"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_data_type(self):
        input = """
        Class Dog {
            Val a : Int = 1;
            Val b : Float = 1.4;
            Val c : String = "abc";
            Val d : Boolean = True;
            Val e : Array[Int, 5] = Array(1, 5, 7, 12, 8);
            Val f : Animal = New Animal();
            Val g : Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(1,2,3,4,5));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_normal_integer_literal(self):
        input = """
        Class IntLit {
            Val a : Int = 1_234_567;
            Val b : Int = 1_2_3_4_5_6_7;
            Val c : Int = 0b110;
            Val d : Int = 0123456;
            Val e : Int = 0x123456789ABCDEF;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_wrong_integer_literal(self):
        input = """
        Class IntLit {
            Val a : Int = 1__2345;
        }
        """
        expect = "Error on line 3 col 27: __2345"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_wrong_integer_literal1(self):
        input = """
        Class IntLit {
            Val a : Int = 12345__;
        }
        """
        expect = "Error on line 3 col 31: __"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_wrong_integer_literal2(self):
        input = """
        Class IntLit {
            Val a : Int = 0b102;
        }
        """
        expect = "Error on line 3 col 30: 2"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_wrong_array(self):
        input = """
        Class ArrayLit {
            Val a : Array[Int,2] = Array();
            Val b : Array[Int,2] = Array(1,);
        }
        """
        expect = "Error on line 4 col 43: )"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_wrong_instance_method_call(self):
        input = """
        Class Program {
            main() {
                Shape.$numOfShape;
            }
        }
        """
        expect = "Error on line 4 col 22: $numOfShape"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_self_keyword(self):
        input = """
        Class ABC {
            Var w, h : Int;

            Constructor(w: Int; h: Int) {
                Self.w = w;
                Self.h = h;
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_wrong_array_declaration(self):
        input = """
        Class ArrayLit {
            Val a : Array[Int,0] = Array();
        }
        """
        expect = "Error on line 3 col 30: 0"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_calling_function_of_class(self):
        input = """
        Class Program {
            main(){
                Return New X().Y();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_chaining_method(self):
        input = """
        Class Program {
            main(){
                Return Animal.Dog.bark();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_chaining_method_method(self):
        input = """
        Class Program {
            main(){
                Return Animal.getDog().bark();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_weird_case_in_foreach(self):
        input = """
        Class Shape{
            foo(){
                Foreach(a In 1..10){ ## It understands as 1.,.,10 ##

                }
            }
        }
        """
        expect = "Error on line 4 col 31: ."
        self.assertTrue(TestParser.test(input,expect,228)) #Case này ko check đâu, vì cơ bản 1..10 vẫn hợp lệ
    def test_chain_object_creation(self):
        input = """
        Class Program {
            main(){
                Return New A(New B(New C()), 1+2, C::$x);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_normal_foreach(self):
        input = """
        Class Program {
            main(){
                Foreach (x In 5 .. 2) {
                    Out.printInt(arr[x]);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_negative_size_array(self):
        input = """
        Class ArrayLit {
            main(){
                Var a : Array[Int, -1];
            }
        }
        """
        expect = "Error on line 4 col 35: -"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_class_inheritance(self):
        input = """
        Class Dog : Animal {

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_array_declaration(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 5] = Array(1,2,3,4,5);
            Var a1: Array[Int, 5];
            Var b: Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(6,7,8,9,10));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_array_with_expression(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 3] = Array(1 + 2, 345, 6 * 8);
            ## Var b: Array = 123; ##
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_method_call(self):
        input = """
        Class Program {
            getName(person : Person){
                Return "John";
            }
            main(){
                If(a >= b){
                    Var a: Int = 0;
                    a = a + 3;
                }
                Elseif (b >= c){
                    John = Stupid;
                }
                Else {
                    getName(John);
                }
            }
        }
        """
        expect = "Error on line 15 col 27: ("
        self.assertTrue(TestParser.test(input,expect,235))
    def test_zero_sized_array(self):
        input = """
        Class Program {
            Val a : Array[Int, 0];
        }
        """
        expect = "Error on line 3 col 31: 0"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_zero_sized_array1(self):
        input = """
        Class Program {
            Val a : Array[Int, 0x0];
        }
        """
        expect = "Error on line 3 col 31: 0x0"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_zero_sized_array2(self):
        input = """
        Class Program {
            Val a : Array[Int, 0b0];
        }
        """
        expect = "Error on line 3 col 31: 0b0"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_method_invocation(self):
        input = """
        Class Program {
            main(){
                a = Dog.bark() + Cat::$Meow() + Dog.name + Cat::$age + Animal.Dog[1] + Animal.type().name;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_statement_in_class_body(self):
        input = """
        Class Program {
            Var a,b: Int;

            If (a > 0) {
            ## Do something ##
            }
        }
        """
        expect = "Error on line 5 col 12: If"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_multi_dimension_array_declaration(self):
        input = """
        Class Program {
            Var a: Array[Array[Array[Array[Int,2],2],2],2] = Array(Array(Array(Array(), Array()), Array(Array(), Array())),Array(Array(Array(), Array()), Array(Array(), Array())));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_static_method_declaration(self):
        input = """
        Class Program {
            main(){

            }

            $getName(){

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_wrong_method_invocation(self):
        input = """
        Class Program {
            main(){
                a[5] = Dog::name();
            }
        }
        """
        expect = "Error on line 4 col 28: name"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_wrong_method_invocation_again(self):
        input = """
        Class Program {
            main(){
                a[5] = Dog.$name();
            }
        }
        """
        expect = "Error on line 4 col 26: ."
        self.assertTrue(TestParser.test(input,expect,244)) #Lỗi ở $name vì token . vẫn nhận mà nhỉ
    def test_wrong_attribute_access(self):
        input = """
        Class Program {
            main(){
                a[5] = Dog::name;
            }
        }
        """
        expect = "Error on line 4 col 28: name"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_wrong_attribute_access_again(self):
        input = """
        Class Program {
            main(){
                a[5] = Dog.$name;
            }
        }
        """
        expect = "Error on line 4 col 26: ."
        self.assertTrue(TestParser.test(input,expect,246))#Lỗi ở $name vì token . vẫn nhận
    def test_object_creation(self):
        input = """
        Class Program {
            Val student : Student = New Student(name, age, course);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_wrong_object_creation(self):
        input = """
        Class Program {
            Val student : $Student = New Student(name, age, course);
        }
        """
        expect = "Error on line 3 col 26: $Student"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_wrong_object_creation_again(self):
        input = """
        Class Program {
            Val student : Student = New $Student(name, age, course);
        }
        """
        expect = "Error on line 3 col 40: $Student"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_wrong_object_creation_once_again(self):
        input = """
        Class Program {
            Val student : Student = New Student($name, age, course);
        }
        """
        expect = "Error on line 3 col 48: $name"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_variable_and_constant_declaration(self):
        input = """
        Class Program {
            main() {
                Val student : Int = 1 + 5 * 9 / 10 % 3;
                Var teacher : Boolean = a >= b || c < d ;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_wrong_static_variable_declaration(self):
        input = """
        Class Program {
            main() {
                Val $student : Int = 1 + 5 * 9 / 10 % 3;
                Var teacher : Boolean = a >= b || c < d ;
            }
        }        
        """
        expect = "Error on line 4 col 20: $student"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_if_statement(self):
        input = """
        Class Program {
            main() {
                If(a > b){

                }
                Elseif(a > c){

                }
                Else{

                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_wrong_else_statement(self):
        input = """
        Class Program {
            main() {
                If(a > b){

                }
                Else(){

                }
            }
        }
        """
        expect = "Error on line 7 col 20: ("
        self.assertTrue(TestParser.test(input,expect,254))
    def test_for_statement(self):
        input = """
        Class Program {
            main(){
                Foreach(index In 10 .. 100 By 1000){
                    Out.printInt(arr[x]);
                    If(index % 19 == 4){
                        Break;
                    }
                    Elseif(index % 20 == 1){
                        Continue;
                    }
                    Elseif(index % 9 == 2){
                        Return index;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_block_statement(self):
        input = """
        Class Program {
            main(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_mixed_program(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return Shape::$numOfShape;
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_258(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In 1+1 .. 100+100 By a.foo()){}
                    }
                }
            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 258))

    def test_259(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Class Shape{}
                        }
                    }
                }
            """
        output = """Error on line 5 col 28: Class"""
        self.assertTrue(TestParser.test(input, output, 259))

    def test_260(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Var $a:Int;
                        }
                }
                """
        output = """Error on line 5 col 32: $a"""
        self.assertTrue(TestParser.test(input, output, 260))

    def test_261(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 261))

    def test_262(self):
        input = """
                Class Shape{
                    foo(){
                        a[b[c[d[e[f::$g]]]]][h::$i][j.k()][Lzzzzz::$m()]=0;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 262))

    def test_263(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b==True){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 263))

    def test_264(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 264))

    def test_265(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                            Elseif( a == b ==. c){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 265))

    def test_266(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                            Elseif( a == b ==. c){}
                            Else(1=2){}
                        }
                    }
                } 
                """
        output = """Error on line 7 col 32: ("""
        self.assertTrue(TestParser.test(input, output, 266))

    def test_267(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){

                                    }
                                }
                            }
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 267))
    def test_268(self):
        input = """
                Class Shape{
                    foo(){
                        a = b == c == d;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 268))
    def test_269(self):
        input = """
                Class Shape{
                    foo(){
                        a = b <= c >= d;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 269))
    def test_270(self):
        input = """
                Class Shape{
                    foo(){
                        a = b == c < d;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 270))
    def test_271(self):
        input = """
                Class Shape{
                    Foreach(i In 1 . . 100 by 2 ){}
                }   
                """
        output = """Error on line 3 col 20: Foreach"""
        self.assertTrue(TestParser.test(input, output, 271))
    def test_272(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[1,1_12],1],1];
                }   
                """
        output = """Error on line 3 col 45: 1"""
        self.assertTrue(TestParser.test(input, output, 272))
    def test_273(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,1_12],1],1];
                }   
                """
        output = """Error on line 3 col 45: d"""
        self.assertTrue(TestParser.test(input, output, 273))
    def test_274(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,_1_12],1],1];
                }   
                """
        output = """Error on line 3 col 45: d"""
        self.assertTrue(TestParser.test(input, output, 274))
    def test_275(self):
        input = """
                Class Shape{
                    Var a: Array[b,Array[c,Array[d,1]]];
                }   
                """
        output = """Error on line 3 col 33: b"""
        self.assertTrue(TestParser.test(input, output, 275))
    def test_276(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                Foreach (i In a[1] .. foo() By _123()) {}
            } 
        }
        """
        expect = "Error on line 4 col 41: ("
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = !!!!!!!!!!!!True;
                b = ------------5;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = !!!!!!!!!!!!True;
                b = ------------5;
                c=d.d.d.d.d.d.d.d;
                e=f[1][1][1][1];
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = (b==c) == True;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = b == c  == True;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = (b < c)  == True;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test_282(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[1,1_12],1],1];
                }   
                """
        output = """Error on line 3 col 45: 1"""
        self.assertTrue(TestParser.test(input, output, 282))

    def test_283(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = ("a"+."b")+."b";
                c = ("a"==."a")==True;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        """More complex program"""
        input = """
        Class Shape:a:b{}
        """
        expect = "Error on line 2 col 21: :"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a::$b=2;
                a::$e();
                a::$c::$d=2;
            } 
        }
        """
        expect = "Error on line 6 col 21: ::"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a::$b=2;
                a::$e();
                a::$c()::$d=2;
            } 
        }
        """
        expect = "Error on line 6 col 23: ::"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
            a += 1;
            } 
        }
        """
        expect = "Error on line 4 col 15: ="
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a = -1 + 1;
                b = 1 + -1 - -1 + -1 - --1;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
            b = 1 + -1 - -1 + -1 - + -1;
            } 
        }
        """
        expect = "Error on line 4 col 35: +"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
            Var a :Int = $1-----5;
            } 
        }
        """
        expect = "Error on line 4 col 25: $1"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
                Class Shape{
                    foo(){
                        a = New X().Y();
                        Var a: Array[Int, 0];
                    }
                }
            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 291))

    def test_292(self):
        input = """
                Class Shape{
                    foo(){
                        b::$f=1;
                    }
                    a = 1;
                }
            """
        output = """Error on line 6 col 22: ="""
        self.assertTrue(TestParser.test(input, output, 292))
    def test_293(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 01];
                        Var a: Array[Int, 0x1];
                        Var a: Array[Int, 0X1];
                        Var a: Array[Int, 0b1];
                        Var a: Array[Int, 0B1];
                        Var a: Array[Int, 1];
                        Var a: Array[Int, 00];
                    }
                }
            """
        output = """Error on line 10 col 42: 00"""
        self.assertTrue(TestParser.test(input, output, 293))
    def test_294(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 1_23.456e+7];
                    }
                }

            """
        output = """Error on line 4 col 42: 123.456e+7"""
        self.assertTrue(TestParser.test(input, output, 294))

    def test_295(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, b::$c.foo()];
                    }
                }

            """
        output = """Error on line 4 col 42: b"""
        self.assertTrue(TestParser.test(input, output, 295))
    def test_296(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a[b[1]][c][foo()] = 1;
            }
            Var e,f : Int = 1 + 1, 1 - 2;
        }
        """
        expect = "Error on line 4 col 30: ("
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        """More complex program"""
        input = """
        Class Shape2 {
            $getNumOfShape() {
                If (a == (1+1) ){
                    Var b,c:Boolean = True, False;
                }
                Foreach (i In 1 .. 100 By 2) {
                    Var a:Boolean = True;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                foo2(1+1,"a"+."b","a"==."b");
            }
        }
        """
        expect = "Error on line 4 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        """More complex program"""
        input = """
        Class Shape {
            Constructor(width, height : Int; name:String){
                Self.Area=Self.width*Self.height;
                Self.name="shape"+.name;
            } 
            Destructor(){} 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                    Out.printInt(i);
                }
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
