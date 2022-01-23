# Generated from /Users/tieuviettrongnghia/Documents/Document/HỌC TẬP/ĐẠI HỌC BÁCH KHOA/212/PPL/Assignment/Assignment 1/initial copy/src/main/d96/parser/D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u028a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u0152\n\34\3\35\3\35\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\59\u0198\n9\3:\3:\3:\3:\5")
        buf.write(":\u019e\n:\3:\3:\3;\6;\u01a3\n;\r;\16;\u01a4\3;\3;\3;")
        buf.write("\7;\u01aa\n;\f;\16;\u01ad\13;\3;\6;\u01b0\n;\r;\16;\u01b1")
        buf.write("\3;\3;\6;\u01b6\n;\r;\16;\u01b7\3;\5;\u01bb\n;\3;\6;\u01be")
        buf.write("\n;\r;\16;\u01bf\3;\3;\3;\3;\7;\u01c6\n;\f;\16;\u01c9")
        buf.write("\13;\3;\5;\u01cc\n;\5;\u01ce\n;\3;\3;\3<\3<\5<\u01d4\n")
        buf.write("<\3=\3=\7=\u01d8\n=\f=\16=\u01db\13=\3=\3=\3=\3>\3>\7")
        buf.write(">\u01e2\n>\f>\16>\u01e5\13>\3?\3?\3?\7?\u01ea\n?\f?\16")
        buf.write("?\u01ed\13?\3@\3@\7@\u01f1\n@\f@\16@\u01f4\13@\3@\3@\6")
        buf.write("@\u01f8\n@\r@\16@\u01f9\7@\u01fc\n@\f@\16@\u01ff\13@\3")
        buf.write("@\5@\u0202\n@\3A\3A\6A\u0206\nA\rA\16A\u0207\3A\3A\6A")
        buf.write("\u020c\nA\rA\16A\u020d\7A\u0210\nA\fA\16A\u0213\13A\3")
        buf.write("B\3B\3B\6B\u0218\nB\rB\16B\u0219\3B\3B\6B\u021e\nB\rB")
        buf.write("\16B\u021f\7B\u0222\nB\fB\16B\u0225\13B\6B\u0227\nB\r")
        buf.write("B\16B\u0228\3C\3C\3C\6C\u022e\nC\rC\16C\u022f\3C\3C\6")
        buf.write("C\u0234\nC\rC\16C\u0235\7C\u0238\nC\fC\16C\u023b\13C\3")
        buf.write("D\3D\3E\3E\3F\6F\u0242\nF\rF\16F\u0243\3G\3G\5G\u0248")
        buf.write("\nG\3G\6G\u024b\nG\rG\16G\u024c\3H\3H\3I\3I\3I\3J\3J\3")
        buf.write("J\5J\u0257\nJ\3K\3K\5K\u025b\nK\3L\6L\u025e\nL\rL\16L")
        buf.write("\u025f\3L\3L\3M\3M\3M\3M\7M\u0268\nM\fM\16M\u026b\13M")
        buf.write("\3M\3M\3M\3M\3M\3N\3N\3N\3O\3O\7O\u0277\nO\fO\16O\u027a")
        buf.write("\13O\3O\5O\u027d\nO\3O\3O\3P\3P\7P\u0283\nP\fP\16P\u0286")
        buf.write("\13P\3P\3P\3P\3\u0269\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b?\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097@\u0099A\u009bB\u009dC\u009fD")
        buf.write("\3\2\22\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\3\2")
        buf.write("\629\4\2ZZzz\4\2\62;CH\4\2DDdd\3\2\62\63\4\2GGgg\4\2-")
        buf.write("-//\n\2$$))^^ddhhppttvv\3\2^^\7\2\n\f\16\17$$))^^\5\2")
        buf.write("\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\2\u02a9\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u008b\3\2")
        buf.write("\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2")
        buf.write("\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a9")
        buf.write("\3\2\2\2\7\u00ae\3\2\2\2\t\u00b1\3\2\2\2\13\u00b7\3\2")
        buf.write("\2\2\r\u00c0\3\2\2\2\17\u00c3\3\2\2\2\21\u00ca\3\2\2\2")
        buf.write("\23\u00cf\3\2\2\2\25\u00d7\3\2\2\2\27\u00dc\3\2\2\2\31")
        buf.write("\u00e2\3\2\2\2\33\u00e8\3\2\2\2\35\u00eb\3\2\2\2\37\u00ef")
        buf.write("\3\2\2\2!\u00f5\3\2\2\2#\u00fd\3\2\2\2%\u0104\3\2\2\2")
        buf.write("\'\u010b\3\2\2\2)\u0110\3\2\2\2+\u0116\3\2\2\2-\u011a")
        buf.write("\3\2\2\2/\u011e\3\2\2\2\61\u012a\3\2\2\2\63\u0135\3\2")
        buf.write("\2\2\65\u0139\3\2\2\2\67\u0151\3\2\2\29\u0153\3\2\2\2")
        buf.write(";\u0155\3\2\2\2=\u0157\3\2\2\2?\u0159\3\2\2\2A\u015b\3")
        buf.write("\2\2\2C\u015d\3\2\2\2E\u015f\3\2\2\2G\u0162\3\2\2\2I\u0165")
        buf.write("\3\2\2\2K\u0168\3\2\2\2M\u016a\3\2\2\2O\u016d\3\2\2\2")
        buf.write("Q\u016f\3\2\2\2S\u0172\3\2\2\2U\u0174\3\2\2\2W\u0177\3")
        buf.write("\2\2\2Y\u017b\3\2\2\2[\u017e\3\2\2\2]\u0181\3\2\2\2_\u0183")
        buf.write("\3\2\2\2a\u0185\3\2\2\2c\u0187\3\2\2\2e\u0189\3\2\2\2")
        buf.write("g\u018b\3\2\2\2i\u018d\3\2\2\2k\u018f\3\2\2\2m\u0191\3")
        buf.write("\2\2\2o\u0193\3\2\2\2q\u0197\3\2\2\2s\u019d\3\2\2\2u\u01cd")
        buf.write("\3\2\2\2w\u01d3\3\2\2\2y\u01d5\3\2\2\2{\u01df\3\2\2\2")
        buf.write("}\u01e6\3\2\2\2\177\u0201\3\2\2\2\u0081\u0203\3\2\2\2")
        buf.write("\u0083\u0214\3\2\2\2\u0085\u022a\3\2\2\2\u0087\u023c\3")
        buf.write("\2\2\2\u0089\u023e\3\2\2\2\u008b\u0241\3\2\2\2\u008d\u0245")
        buf.write("\3\2\2\2\u008f\u024e\3\2\2\2\u0091\u0250\3\2\2\2\u0093")
        buf.write("\u0256\3\2\2\2\u0095\u025a\3\2\2\2\u0097\u025d\3\2\2\2")
        buf.write("\u0099\u0263\3\2\2\2\u009b\u0271\3\2\2\2\u009d\u0274\3")
        buf.write("\2\2\2\u009f\u0280\3\2\2\2\u00a1\u00a2\7R\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7i\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7o\2\2\u00a8\4")
        buf.write("\3\2\2\2\u00a9\u00aa\7o\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\6\3\2\2\2\u00ae\u00af")
        buf.write("\7\60\2\2\u00af\u00b0\7\60\2\2\u00b0\b\3\2\2\2\u00b1\u00b2")
        buf.write("\7D\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7m\2\2\u00b6\n\3\2\2\2\u00b7\u00b8")
        buf.write("\7E\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7w\2\2\u00be\u00bf\7g\2\2\u00bf\f\3\2\2\2\u00c0\u00c1")
        buf.write("\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\16\3\2\2\2\u00c3\u00c4")
        buf.write("\7G\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9\20")
        buf.write("\3\2\2\2\u00ca\u00cb\7G\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\22\3\2\2\2\u00cf\u00d0")
        buf.write("\7H\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6")
        buf.write("\7j\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\7V\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7g\2\2\u00db\26")
        buf.write("\3\2\2\2\u00dc\u00dd\7H\2\2\u00dd\u00de\7c\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\30")
        buf.write("\3\2\2\2\u00e2\u00e3\7C\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7{\2\2\u00e7\32")
        buf.write("\3\2\2\2\u00e8\u00e9\7K\2\2\u00e9\u00ea\7p\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7K\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7H\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4 \3\2\2\2\u00f5\u00f6\7D\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7p\2\2\u00fc\"")
        buf.write("\3\2\2\2\u00fd\u00fe\7U\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7i\2\2\u0103$\3\2\2\2\u0104\u0105\7T\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7v\2\2\u0107\u0108\7w\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7p\2\2\u010a&\3\2\2\2\u010b\u010c")
        buf.write("\7P\2\2\u010c\u010d\7w\2\2\u010d\u010e\7n\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f(\3\2\2\2\u0110\u0111\7E\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7c\2\2\u0113\u0114\7u\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115*\3\2\2\2\u0116\u0117\7X\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7n\2\2\u0119,\3\2\2\2\u011a\u011b")
        buf.write("\7X\2\2\u011b\u011c\7c\2\2\u011c\u011d\7t\2\2\u011d.\3")
        buf.write("\2\2\2\u011e\u011f\7E\2\2\u011f\u0120\7q\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7u\2\2\u0122\u0123\7v\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124\u0125\7w\2\2\u0125\u0126\7e\2\2\u0126\u0127")
        buf.write("\7v\2\2\u0127\u0128\7q\2\2\u0128\u0129\7t\2\2\u0129\60")
        buf.write("\3\2\2\2\u012a\u012b\7F\2\2\u012b\u012c\7g\2\2\u012c\u012d")
        buf.write("\7u\2\2\u012d\u012e\7v\2\2\u012e\u012f\7t\2\2\u012f\u0130")
        buf.write("\7w\2\2\u0130\u0131\7e\2\2\u0131\u0132\7v\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\u0134\7t\2\2\u0134\62\3\2\2\2\u0135\u0136")
        buf.write("\7P\2\2\u0136\u0137\7g\2\2\u0137\u0138\7y\2\2\u0138\64")
        buf.write("\3\2\2\2\u0139\u013a\7D\2\2\u013a\u013b\7{\2\2\u013b\66")
        buf.write("\3\2\2\2\u013c\u013d\7Y\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7k\2\2\u013f\u0140\7v\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7N\2\2\u0142\u0152\7p\2\2\u0143\u0144\7y\2\2\u0144\u0145")
        buf.write("\7t\2\2\u0145\u0146\7k\2\2\u0146\u0147\7v\2\2\u0147\u0148")
        buf.write("\7g\2\2\u0148\u0149\7n\2\2\u0149\u0152\7p\2\2\u014a\u014b")
        buf.write("\7Y\2\2\u014b\u014c\7T\2\2\u014c\u014d\7K\2\2\u014d\u014e")
        buf.write("\7V\2\2\u014e\u014f\7G\2\2\u014f\u0150\7N\2\2\u0150\u0152")
        buf.write("\7P\2\2\u0151\u013c\3\2\2\2\u0151\u0143\3\2\2\2\u0151")
        buf.write("\u014a\3\2\2\2\u01528\3\2\2\2\u0153\u0154\7-\2\2\u0154")
        buf.write(":\3\2\2\2\u0155\u0156\7/\2\2\u0156<\3\2\2\2\u0157\u0158")
        buf.write("\7,\2\2\u0158>\3\2\2\2\u0159\u015a\7\61\2\2\u015a@\3\2")
        buf.write("\2\2\u015b\u015c\7\'\2\2\u015cB\3\2\2\2\u015d\u015e\7")
        buf.write("#\2\2\u015eD\3\2\2\2\u015f\u0160\7(\2\2\u0160\u0161\7")
        buf.write("(\2\2\u0161F\3\2\2\2\u0162\u0163\7~\2\2\u0163\u0164\7")
        buf.write("~\2\2\u0164H\3\2\2\2\u0165\u0166\7?\2\2\u0166\u0167\7")
        buf.write("?\2\2\u0167J\3\2\2\2\u0168\u0169\7?\2\2\u0169L\3\2\2\2")
        buf.write("\u016a\u016b\7#\2\2\u016b\u016c\7?\2\2\u016cN\3\2\2\2")
        buf.write("\u016d\u016e\7@\2\2\u016eP\3\2\2\2\u016f\u0170\7@\2\2")
        buf.write("\u0170\u0171\7?\2\2\u0171R\3\2\2\2\u0172\u0173\7>\2\2")
        buf.write("\u0173T\3\2\2\2\u0174\u0175\7>\2\2\u0175\u0176\7?\2\2")
        buf.write("\u0176V\3\2\2\2\u0177\u0178\7?\2\2\u0178\u0179\7?\2\2")
        buf.write("\u0179\u017a\7\60\2\2\u017aX\3\2\2\2\u017b\u017c\7-\2")
        buf.write("\2\u017c\u017d\7\60\2\2\u017dZ\3\2\2\2\u017e\u017f\7<")
        buf.write("\2\2\u017f\u0180\7<\2\2\u0180\\\3\2\2\2\u0181\u0182\7")
        buf.write("=\2\2\u0182^\3\2\2\2\u0183\u0184\7.\2\2\u0184`\3\2\2\2")
        buf.write("\u0185\u0186\7\60\2\2\u0186b\3\2\2\2\u0187\u0188\7<\2")
        buf.write("\2\u0188d\3\2\2\2\u0189\u018a\7*\2\2\u018af\3\2\2\2\u018b")
        buf.write("\u018c\7+\2\2\u018ch\3\2\2\2\u018d\u018e\7]\2\2\u018e")
        buf.write("j\3\2\2\2\u018f\u0190\7_\2\2\u0190l\3\2\2\2\u0191\u0192")
        buf.write("\7}\2\2\u0192n\3\2\2\2\u0193\u0194\7\177\2\2\u0194p\3")
        buf.write("\2\2\2\u0195\u0198\5{>\2\u0196\u0198\5}?\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0196\3\2\2\2\u0198r\3\2\2\2\u0199\u019e")
        buf.write("\5\177@\2\u019a\u019e\5\u0081A\2\u019b\u019e\5\u0083B")
        buf.write("\2\u019c\u019e\5\u0085C\2\u019d\u0199\3\2\2\2\u019d\u019a")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\b:\2\2\u01a0t\3\2\2\2\u01a1")
        buf.write("\u01a3\5\177@\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4\3\2\2")
        buf.write("\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01ab\5a\61\2\u01a7\u01aa\5\177@\2\u01a8")
        buf.write("\u01aa\5\u008dG\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2")
        buf.write("\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01ce\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae")
        buf.write("\u01b0\5\177@\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2")
        buf.write("\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b5\5a\61\2\u01b4\u01b6\5\177@\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01bb\5")
        buf.write("\u008dG\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01ce\3\2\2\2\u01bc\u01be\5\177@\2\u01bd\u01bc\3\2\2")
        buf.write("\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\5\u008dG\2\u01c2")
        buf.write("\u01ce\3\2\2\2\u01c3\u01c7\5a\61\2\u01c4\u01c6\5\177@")
        buf.write("\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01ca\u01cc\5\u008dG\2\u01cb\u01ca\3\2")
        buf.write("\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01a2")
        buf.write("\3\2\2\2\u01cd\u01af\3\2\2\2\u01cd\u01bd\3\2\2\2\u01cd")
        buf.write("\u01c3\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\b;\3\2")
        buf.write("\u01d0v\3\2\2\2\u01d1\u01d4\5\25\13\2\u01d2\u01d4\5\27")
        buf.write("\f\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4x\3")
        buf.write("\2\2\2\u01d5\u01d9\7$\2\2\u01d6\u01d8\5\u0095K\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01dd\7$\2\2\u01dd\u01de\b=\4\2\u01dez\3")
        buf.write("\2\2\2\u01df\u01e3\t\2\2\2\u01e0\u01e2\t\3\2\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4|\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u01e7\7&\2\2\u01e7\u01eb\t\2\2\2\u01e8\u01ea\t\3\2\2")
        buf.write("\u01e9\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ec\3\2\2\2\u01ec~\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ee\u01f2\t\4\2\2\u01ef\u01f1\t\5\2\2\u01f0")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01fd\3\2\2\2\u01f4\u01f2\3")
        buf.write("\2\2\2\u01f5\u01f7\7a\2\2\u01f6\u01f8\t\5\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01f5\3\2\2\2")
        buf.write("\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3")
        buf.write("\2\2\2\u01fe\u0202\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0202")
        buf.write("\7\62\2\2\u0201\u01ee\3\2\2\2\u0201\u0200\3\2\2\2\u0202")
        buf.write("\u0080\3\2\2\2\u0203\u0205\7\62\2\2\u0204\u0206\t\6\2")
        buf.write("\2\u0205\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205")
        buf.write("\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0211\3\2\2\2\u0209")
        buf.write("\u020b\7a\2\2\u020a\u020c\t\6\2\2\u020b\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3")
        buf.write("\2\2\2\u020e\u0210\3\2\2\2\u020f\u0209\3\2\2\2\u0210\u0213")
        buf.write("\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u0082\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0215\7\62\2")
        buf.write("\2\u0215\u0226\t\7\2\2\u0216\u0218\t\b\2\2\u0217\u0216")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u0223\3\2\2\2\u021b\u021d\7a\2\2")
        buf.write("\u021c\u021e\t\b\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3")
        buf.write("\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222")
        buf.write("\3\2\2\2\u0221\u021b\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0227\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0226\u0217\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u0084")
        buf.write("\3\2\2\2\u022a\u022b\7\62\2\2\u022b\u022d\t\t\2\2\u022c")
        buf.write("\u022e\t\n\2\2\u022d\u022c\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0239\3")
        buf.write("\2\2\2\u0231\u0233\7a\2\2\u0232\u0234\t\n\2\2\u0233\u0232")
        buf.write("\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0233\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0231\3\2\2\2")
        buf.write("\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3")
        buf.write("\2\2\2\u023a\u0086\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u023d")
        buf.write("\t\5\2\2\u023d\u0088\3\2\2\2\u023e\u023f\t\4\2\2\u023f")
        buf.write("\u008a\3\2\2\2\u0240\u0242\5\u0087D\2\u0241\u0240\3\2")
        buf.write("\2\2\u0242\u0243\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u008c\3\2\2\2\u0245\u0247\t\13\2\2\u0246")
        buf.write("\u0248\5\u008fH\2\u0247\u0246\3\2\2\2\u0247\u0248\3\2")
        buf.write("\2\2\u0248\u024a\3\2\2\2\u0249\u024b\5\u0087D\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024a\3\2\2\2")
        buf.write("\u024c\u024d\3\2\2\2\u024d\u008e\3\2\2\2\u024e\u024f\t")
        buf.write("\f\2\2\u024f\u0090\3\2\2\2\u0250\u0251\7^\2\2\u0251\u0252")
        buf.write("\t\r\2\2\u0252\u0092\3\2\2\2\u0253\u0254\7^\2\2\u0254")
        buf.write("\u0257\n\r\2\2\u0255\u0257\n\16\2\2\u0256\u0253\3\2\2")
        buf.write("\2\u0256\u0255\3\2\2\2\u0257\u0094\3\2\2\2\u0258\u025b")
        buf.write("\n\17\2\2\u0259\u025b\5\u0091I\2\u025a\u0258\3\2\2\2\u025a")
        buf.write("\u0259\3\2\2\2\u025b\u0096\3\2\2\2\u025c\u025e\t\20\2")
        buf.write("\2\u025d\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d")
        buf.write("\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0261\3\2\2\2\u0261")
        buf.write("\u0262\bL\5\2\u0262\u0098\3\2\2\2\u0263\u0264\7%\2\2\u0264")
        buf.write("\u0265\7%\2\2\u0265\u0269\3\2\2\2\u0266\u0268\13\2\2\2")
        buf.write("\u0267\u0266\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u026a\3")
        buf.write("\2\2\2\u0269\u0267\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0269")
        buf.write("\3\2\2\2\u026c\u026d\7%\2\2\u026d\u026e\7%\2\2\u026e\u026f")
        buf.write("\3\2\2\2\u026f\u0270\bM\5\2\u0270\u009a\3\2\2\2\u0271")
        buf.write("\u0272\13\2\2\2\u0272\u0273\bN\6\2\u0273\u009c\3\2\2\2")
        buf.write("\u0274\u0278\7$\2\2\u0275\u0277\5\u0095K\2\u0276\u0275")
        buf.write("\3\2\2\2\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2\u0278")
        buf.write("\u0279\3\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2")
        buf.write("\u027b\u027d\t\21\2\2\u027c\u027b\3\2\2\2\u027d\u027e")
        buf.write("\3\2\2\2\u027e\u027f\bO\7\2\u027f\u009e\3\2\2\2\u0280")
        buf.write("\u0284\7$\2\2\u0281\u0283\5\u0095K\2\u0282\u0281\3\2\2")
        buf.write("\2\u0283\u0286\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285")
        buf.write("\3\2\2\2\u0285\u0287\3\2\2\2\u0286\u0284\3\2\2\2\u0287")
        buf.write("\u0288\5\u0093J\2\u0288\u0289\bP\b\2\u0289\u00a0\3\2\2")
        buf.write("\2,\2\u0151\u0197\u019d\u01a4\u01a9\u01ab\u01b1\u01b7")
        buf.write("\u01ba\u01bf\u01c7\u01cb\u01cd\u01d3\u01d9\u01e3\u01eb")
        buf.write("\u01f2\u01f9\u01fd\u0201\u0207\u020d\u0211\u0219\u021f")
        buf.write("\u0223\u0228\u022f\u0235\u0239\u0243\u0247\u024c\u0256")
        buf.write("\u025a\u025f\u0269\u0278\u027c\u0284\t\3:\2\3;\3\3=\4")
        buf.write("\b\2\2\3N\5\3O\6\3P\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BREAK = 4
    CONTINUE = 5
    IF = 6
    ELSEIF = 7
    ELSE = 8
    FOREACH = 9
    TRUE = 10
    FALSE = 11
    ARRAY = 12
    IN = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    STRING = 17
    RETURN = 18
    NULL = 19
    CLASS = 20
    VAL = 21
    VAR = 22
    CONSTRUCTOR = 23
    DESTRUCTOR = 24
    NEW = 25
    BY = 26
    WRITELN = 27
    PLUS = 28
    MINUS = 29
    STAR = 30
    DIV = 31
    MOD = 32
    NOT = 33
    ANDAND = 34
    OROR = 35
    EQ = 36
    ASSIGN = 37
    NE = 38
    GT = 39
    GE = 40
    LS = 41
    LE = 42
    STR_CMP = 43
    STR_CONCAT = 44
    DCL = 45
    SM = 46
    CM = 47
    DOT = 48
    CL = 49
    LP = 50
    RP = 51
    LSB = 52
    RSB = 53
    LCB = 54
    RCB = 55
    IDENTIFIER = 56
    INT_LIT = 57
    FLOAT_LIT = 58
    BOOL_LIT = 59
    STRING_LIT = 60
    SDIGIT = 61
    WS = 62
    BLOCKCOMMENT = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'..'", "'Break'", "'Continue'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
            "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
            "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'==.'", "'+.'", "'::'", "';'", "','", "'.'", "':'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "WRITELN", "PLUS", "MINUS", "STAR", "DIV", "MOD", 
            "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", 
            "LE", "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", "DOT", "CL", 
            "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", "INT_LIT", 
            "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "SDIGIT", "WS", "BLOCKCOMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "WRITELN", "PLUS", "MINUS", "STAR", "DIV", "MOD", "NOT", 
                  "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", 
                  "LE", "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", "DOT", 
                  "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ID_normal", 
                  "ID_static", "DECIMAL", "OCTAL", "HEX", "BINARY", "DIGIT", 
                  "DIGITNONZERO", "SDIGIT", "EXPONENT", "SIGN", "ESC_SEQ", 
                  "ESC_ILLEGAL", "STR_CHAR", "WS", "BLOCKCOMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[56] = self.INT_LIT_action 
            actions[57] = self.FLOAT_LIT_action 
            actions[59] = self.STRING_LIT_action 
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            y = str(self.text)
            self.text = y[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:]) 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


