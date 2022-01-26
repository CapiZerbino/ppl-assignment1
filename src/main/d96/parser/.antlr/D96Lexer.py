# Generated from /Users/tieuviettrongnghia/Documents/Document/HỌC TẬP/ĐẠI HỌC BÁCH KHOA/212/PPL/Assignment/Assignment 1/initial copy/src/main/d96/parser/D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0254\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0140\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3")
        buf.write("\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\58\u018e\n8")
        buf.write("\39\39\3:\3:\3:\3:\3:\5:\u0197\n:\3:\3:\3;\3;\3;\5;\u019e")
        buf.write("\n;\3;\5;\u01a1\n;\3;\3;\3;\3;\3;\5;\u01a8\n;\3;\3;\5")
        buf.write(";\u01ac\n;\3;\3;\3<\3<\7<\u01b2\n<\f<\16<\u01b5\13<\3")
        buf.write("<\3<\3<\3=\3=\7=\u01bc\n=\f=\16=\u01bf\13=\3>\3>\3>\7")
        buf.write(">\u01c4\n>\f>\16>\u01c7\13>\3?\6?\u01ca\n?\r?\16?\u01cb")
        buf.write("\3?\3?\6?\u01d0\n?\r?\16?\u01d1\7?\u01d4\n?\f?\16?\u01d7")
        buf.write("\13?\3@\3@\6@\u01db\n@\r@\16@\u01dc\3@\3@\6@\u01e1\n@")
        buf.write("\r@\16@\u01e2\7@\u01e5\n@\f@\16@\u01e8\13@\3A\3A\3A\6")
        buf.write("A\u01ed\nA\rA\16A\u01ee\3A\3A\6A\u01f3\nA\rA\16A\u01f4")
        buf.write("\7A\u01f7\nA\fA\16A\u01fa\13A\3B\3B\3B\6B\u01ff\nB\rB")
        buf.write("\16B\u0200\3B\3B\6B\u0205\nB\rB\16B\u0206\7B\u0209\nB")
        buf.write("\fB\16B\u020c\13B\3C\3C\5C\u0210\nC\3D\3D\3E\3E\3F\3F")
        buf.write("\5F\u0218\nF\3F\3F\3G\3G\3H\3H\3H\5H\u0221\nH\3I\3I\5")
        buf.write("I\u0225\nI\3J\3J\3J\3K\6K\u022b\nK\rK\16K\u022c\3K\3K")
        buf.write("\3L\3L\3L\3L\7L\u0235\nL\fL\16L\u0238\13L\3L\3L\3L\3L")
        buf.write("\3L\3M\3M\3M\3N\3N\7N\u0244\nN\fN\16N\u0247\13N\3N\3N")
        buf.write("\3O\3O\7O\u024d\nO\fO\16O\u0250\13O\3O\3O\3O\3\u0236\2")
        buf.write("P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095>\u0097")
        buf.write("?\u0099@\u009bA\u009dB\3\2\22\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\3\2\62\63")
        buf.write("\3\2\63;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\3\2^^\6\2")
        buf.write("\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\2")
        buf.write("\u0268\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00a5\3\2\2\2\7\u00ae")
        buf.write("\3\2\2\2\t\u00b1\3\2\2\2\13\u00b8\3\2\2\2\r\u00bd\3\2")
        buf.write("\2\2\17\u00c5\3\2\2\2\21\u00ca\3\2\2\2\23\u00d0\3\2\2")
        buf.write("\2\25\u00d6\3\2\2\2\27\u00d9\3\2\2\2\31\u00dd\3\2\2\2")
        buf.write("\33\u00e3\3\2\2\2\35\u00eb\3\2\2\2\37\u00f2\3\2\2\2!\u00f9")
        buf.write("\3\2\2\2#\u00fe\3\2\2\2%\u0104\3\2\2\2\'\u0108\3\2\2\2")
        buf.write(")\u010c\3\2\2\2+\u0118\3\2\2\2-\u0123\3\2\2\2/\u0127\3")
        buf.write("\2\2\2\61\u013f\3\2\2\2\63\u0141\3\2\2\2\65\u0146\3\2")
        buf.write("\2\2\67\u0148\3\2\2\29\u014a\3\2\2\2;\u014c\3\2\2\2=\u014e")
        buf.write("\3\2\2\2?\u0150\3\2\2\2A\u0152\3\2\2\2C\u0155\3\2\2\2")
        buf.write("E\u0158\3\2\2\2G\u015b\3\2\2\2I\u015d\3\2\2\2K\u0160\3")
        buf.write("\2\2\2M\u0162\3\2\2\2O\u0165\3\2\2\2Q\u0167\3\2\2\2S\u016a")
        buf.write("\3\2\2\2U\u016e\3\2\2\2W\u0171\3\2\2\2Y\u0174\3\2\2\2")
        buf.write("[\u0176\3\2\2\2]\u0178\3\2\2\2_\u017a\3\2\2\2a\u017d\3")
        buf.write("\2\2\2c\u017f\3\2\2\2e\u0181\3\2\2\2g\u0183\3\2\2\2i\u0185")
        buf.write("\3\2\2\2k\u0187\3\2\2\2m\u0189\3\2\2\2o\u018d\3\2\2\2")
        buf.write("q\u018f\3\2\2\2s\u0196\3\2\2\2u\u01ab\3\2\2\2w\u01af\3")
        buf.write("\2\2\2y\u01b9\3\2\2\2{\u01c0\3\2\2\2}\u01c9\3\2\2\2\177")
        buf.write("\u01d8\3\2\2\2\u0081\u01e9\3\2\2\2\u0083\u01fb\3\2\2\2")
        buf.write("\u0085\u020d\3\2\2\2\u0087\u0211\3\2\2\2\u0089\u0213\3")
        buf.write("\2\2\2\u008b\u0215\3\2\2\2\u008d\u021b\3\2\2\2\u008f\u0220")
        buf.write("\3\2\2\2\u0091\u0224\3\2\2\2\u0093\u0226\3\2\2\2\u0095")
        buf.write("\u022a\3\2\2\2\u0097\u0230\3\2\2\2\u0099\u023e\3\2\2\2")
        buf.write("\u009b\u0241\3\2\2\2\u009d\u024a\3\2\2\2\u009f\u00a0\7")
        buf.write("D\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7c\2\2\u00a3\u00a4\7m\2\2\u00a4\4\3\2\2\2\u00a5\u00a6")
        buf.write("\7E\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac")
        buf.write("\7w\2\2\u00ac\u00ad\7g\2\2\u00ad\6\3\2\2\2\u00ae\u00af")
        buf.write("\7K\2\2\u00af\u00b0\7h\2\2\u00b0\b\3\2\2\2\u00b1\u00b2")
        buf.write("\7G\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7h\2\2\u00b7\n")
        buf.write("\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\f\3\2\2\2\u00bd\u00be")
        buf.write("\7H\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4")
        buf.write("\7j\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7V\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7g\2\2\u00c9\20")
        buf.write("\3\2\2\2\u00ca\u00cb\7H\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\22")
        buf.write("\3\2\2\2\u00d0\u00d1\7C\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7{\2\2\u00d5\24")
        buf.write("\3\2\2\2\u00d6\u00d7\7K\2\2\u00d7\u00d8\7p\2\2\u00d8\26")
        buf.write("\3\2\2\2\u00d9\u00da\7K\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7H\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\7D\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7p\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7U\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7i\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7p\2\2\u00f8 \3\2\2\2\u00f9\u00fa")
        buf.write("\7P\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7n\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7E\2\2\u00ff\u0100")
        buf.write("\7n\2\2\u0100\u0101\7c\2\2\u0101\u0102\7u\2\2\u0102\u0103")
        buf.write("\7u\2\2\u0103$\3\2\2\2\u0104\u0105\7X\2\2\u0105\u0106")
        buf.write("\7c\2\2\u0106\u0107\7n\2\2\u0107&\3\2\2\2\u0108\u0109")
        buf.write("\7X\2\2\u0109\u010a\7c\2\2\u010a\u010b\7t\2\2\u010b(\3")
        buf.write("\2\2\2\u010c\u010d\7E\2\2\u010d\u010e\7q\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f\u0110\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7w\2\2\u0113\u0114\7e\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\u0116\7q\2\2\u0116\u0117\7t\2\2\u0117*\3")
        buf.write("\2\2\2\u0118\u0119\7F\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7u\2\2\u011b\u011c\7v\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7w\2\2\u011e\u011f\7e\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7t\2\2\u0122,\3\2\2\2\u0123\u0124")
        buf.write("\7P\2\2\u0124\u0125\7g\2\2\u0125\u0126\7y\2\2\u0126.\3")
        buf.write("\2\2\2\u0127\u0128\7D\2\2\u0128\u0129\7{\2\2\u0129\60")
        buf.write("\3\2\2\2\u012a\u012b\7Y\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7k\2\2\u012d\u012e\7v\2\2\u012e\u012f\7g\2\2\u012f\u0130")
        buf.write("\7N\2\2\u0130\u0140\7p\2\2\u0131\u0132\7y\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\u0134\7k\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7n\2\2\u0137\u0140\7p\2\2\u0138\u0139")
        buf.write("\7Y\2\2\u0139\u013a\7T\2\2\u013a\u013b\7K\2\2\u013b\u013c")
        buf.write("\7V\2\2\u013c\u013d\7G\2\2\u013d\u013e\7N\2\2\u013e\u0140")
        buf.write("\7P\2\2\u013f\u012a\3\2\2\2\u013f\u0131\3\2\2\2\u013f")
        buf.write("\u0138\3\2\2\2\u0140\62\3\2\2\2\u0141\u0142\7U\2\2\u0142")
        buf.write("\u0143\7g\2\2\u0143\u0144\7n\2\2\u0144\u0145\7h\2\2\u0145")
        buf.write("\64\3\2\2\2\u0146\u0147\7-\2\2\u0147\66\3\2\2\2\u0148")
        buf.write("\u0149\7/\2\2\u01498\3\2\2\2\u014a\u014b\7,\2\2\u014b")
        buf.write(":\3\2\2\2\u014c\u014d\7\61\2\2\u014d<\3\2\2\2\u014e\u014f")
        buf.write("\7\'\2\2\u014f>\3\2\2\2\u0150\u0151\7#\2\2\u0151@\3\2")
        buf.write("\2\2\u0152\u0153\7(\2\2\u0153\u0154\7(\2\2\u0154B\3\2")
        buf.write("\2\2\u0155\u0156\7~\2\2\u0156\u0157\7~\2\2\u0157D\3\2")
        buf.write("\2\2\u0158\u0159\7?\2\2\u0159\u015a\7?\2\2\u015aF\3\2")
        buf.write("\2\2\u015b\u015c\7?\2\2\u015cH\3\2\2\2\u015d\u015e\7#")
        buf.write("\2\2\u015e\u015f\7?\2\2\u015fJ\3\2\2\2\u0160\u0161\7@")
        buf.write("\2\2\u0161L\3\2\2\2\u0162\u0163\7@\2\2\u0163\u0164\7?")
        buf.write("\2\2\u0164N\3\2\2\2\u0165\u0166\7>\2\2\u0166P\3\2\2\2")
        buf.write("\u0167\u0168\7>\2\2\u0168\u0169\7?\2\2\u0169R\3\2\2\2")
        buf.write("\u016a\u016b\7?\2\2\u016b\u016c\7?\2\2\u016c\u016d\7\60")
        buf.write("\2\2\u016dT\3\2\2\2\u016e\u016f\7-\2\2\u016f\u0170\7\60")
        buf.write("\2\2\u0170V\3\2\2\2\u0171\u0172\7<\2\2\u0172\u0173\7<")
        buf.write("\2\2\u0173X\3\2\2\2\u0174\u0175\7=\2\2\u0175Z\3\2\2\2")
        buf.write("\u0176\u0177\7.\2\2\u0177\\\3\2\2\2\u0178\u0179\7\60\2")
        buf.write("\2\u0179^\3\2\2\2\u017a\u017b\7\60\2\2\u017b\u017c\7\60")
        buf.write("\2\2\u017c`\3\2\2\2\u017d\u017e\7<\2\2\u017eb\3\2\2\2")
        buf.write("\u017f\u0180\7*\2\2\u0180d\3\2\2\2\u0181\u0182\7+\2\2")
        buf.write("\u0182f\3\2\2\2\u0183\u0184\7]\2\2\u0184h\3\2\2\2\u0185")
        buf.write("\u0186\7_\2\2\u0186j\3\2\2\2\u0187\u0188\7}\2\2\u0188")
        buf.write("l\3\2\2\2\u0189\u018a\7\177\2\2\u018an\3\2\2\2\u018b\u018e")
        buf.write("\5y=\2\u018c\u018e\5{>\2\u018d\u018b\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018ep\3\2\2\2\u018f\u0190\5y=\2\u0190r\3\2\2")
        buf.write("\2\u0191\u0197\5}?\2\u0192\u0197\5\177@\2\u0193\u0197")
        buf.write("\5\u0081A\2\u0194\u0197\5\u0083B\2\u0195\u0197\7\62\2")
        buf.write("\2\u0196\u0191\3\2\2\2\u0196\u0192\3\2\2\2\u0196\u0193")
        buf.write("\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0199\b:\2\2\u0199t\3\2\2\2\u019a")
        buf.write("\u019b\5}?\2\u019b\u019d\5\u0085C\2\u019c\u019e\5\u008b")
        buf.write("F\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01ac")
        buf.write("\3\2\2\2\u019f\u01a1\5}?\2\u01a0\u019f\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\5\u0085C\2\u01a3")
        buf.write("\u01a4\5\u008bF\2\u01a4\u01ac\3\2\2\2\u01a5\u01a7\5}?")
        buf.write("\2\u01a6\u01a8\5\u0085C\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\5\u008bF\2\u01aa")
        buf.write("\u01ac\3\2\2\2\u01ab\u019a\3\2\2\2\u01ab\u01a0\3\2\2\2")
        buf.write("\u01ab\u01a5\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\b")
        buf.write(";\3\2\u01aev\3\2\2\2\u01af\u01b3\7$\2\2\u01b0\u01b2\5")
        buf.write("\u0091I\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b6\u01b7\7$\2\2\u01b7\u01b8\b")
        buf.write("<\4\2\u01b8x\3\2\2\2\u01b9\u01bd\t\2\2\2\u01ba\u01bc\t")
        buf.write("\3\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01bez\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01c0\u01c1\7&\2\2\u01c1\u01c5\t\2\2\2\u01c2")
        buf.write("\u01c4\t\3\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6|\3\2\2")
        buf.write("\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\t\4\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01d5\3\2\2\2\u01cd\u01cf\7a\2\2")
        buf.write("\u01ce\u01d0\t\4\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4")
        buf.write("\3\2\2\2\u01d3\u01cd\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6~\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01da\7\62\2\2\u01d9\u01db\t\5\2")
        buf.write("\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e6\3\2\2\2\u01de")
        buf.write("\u01e0\7a\2\2\u01df\u01e1\t\5\2\2\u01e0\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3")
        buf.write("\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01de\3\2\2\2\u01e5\u01e8")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u0080\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01ea\7\62\2")
        buf.write("\2\u01ea\u01ec\t\6\2\2\u01eb\u01ed\t\7\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f8\3\2\2\2\u01f0\u01f2\7a\2\2")
        buf.write("\u01f1\u01f3\t\7\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f4\3")
        buf.write("\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7")
        buf.write("\3\2\2\2\u01f6\u01f0\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u0082\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fc\7\62\2\2\u01fc\u01fe")
        buf.write("\t\b\2\2\u01fd\u01ff\t\t\2\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u020a\3\2\2\2\u0202\u0204\7a\2\2\u0203\u0205\t")
        buf.write("\t\2\2\u0204\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0204")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0209\3\2\2\2\u0208")
        buf.write("\u0202\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u0084\3\2\2\2\u020c\u020a\3")
        buf.write("\2\2\2\u020d\u020f\5]/\2\u020e\u0210\5}?\2\u020f\u020e")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0086\3\2\2\2\u0211")
        buf.write("\u0212\t\4\2\2\u0212\u0088\3\2\2\2\u0213\u0214\t\n\2\2")
        buf.write("\u0214\u008a\3\2\2\2\u0215\u0217\t\13\2\2\u0216\u0218")
        buf.write("\5\u008dG\2\u0217\u0216\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u021a\5}?\2\u021a\u008c\3\2\2\2\u021b")
        buf.write("\u021c\t\f\2\2\u021c\u008e\3\2\2\2\u021d\u021e\7^\2\2")
        buf.write("\u021e\u0221\n\r\2\2\u021f\u0221\n\16\2\2\u0220\u021d")
        buf.write("\3\2\2\2\u0220\u021f\3\2\2\2\u0221\u0090\3\2\2\2\u0222")
        buf.write("\u0225\n\17\2\2\u0223\u0225\5\u0093J\2\u0224\u0222\3\2")
        buf.write("\2\2\u0224\u0223\3\2\2\2\u0225\u0092\3\2\2\2\u0226\u0227")
        buf.write("\7^\2\2\u0227\u0228\t\20\2\2\u0228\u0094\3\2\2\2\u0229")
        buf.write("\u022b\t\21\2\2\u022a\u0229\3\2\2\2\u022b\u022c\3\2\2")
        buf.write("\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u022f\bK\5\2\u022f\u0096\3\2\2\2\u0230")
        buf.write("\u0231\7%\2\2\u0231\u0232\7%\2\2\u0232\u0236\3\2\2\2\u0233")
        buf.write("\u0235\13\2\2\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2\2")
        buf.write("\2\u0236\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0239")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\7%\2\2\u023a")
        buf.write("\u023b\7%\2\2\u023b\u023c\3\2\2\2\u023c\u023d\bL\5\2\u023d")
        buf.write("\u0098\3\2\2\2\u023e\u023f\13\2\2\2\u023f\u0240\bM\6\2")
        buf.write("\u0240\u009a\3\2\2\2\u0241\u0245\7$\2\2\u0242\u0244\5")
        buf.write("\u0091I\2\u0243\u0242\3\2\2\2\u0244\u0247\3\2\2\2\u0245")
        buf.write("\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0248\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0248\u0249\bN\7\2\u0249\u009c\3")
        buf.write("\2\2\2\u024a\u024e\7$\2\2\u024b\u024d\5\u0091I\2\u024c")
        buf.write("\u024b\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024e\u024f\3\2\2\2\u024f\u0251\3\2\2\2\u0250\u024e\3")
        buf.write("\2\2\2\u0251\u0252\5\u008fH\2\u0252\u0253\bO\b\2\u0253")
        buf.write("\u009e\3\2\2\2!\2\u013f\u018d\u0196\u019d\u01a0\u01a7")
        buf.write("\u01ab\u01b3\u01bd\u01c5\u01cb\u01d1\u01d5\u01dc\u01e2")
        buf.write("\u01e6\u01ee\u01f4\u01f8\u0200\u0206\u020a\u020f\u0217")
        buf.write("\u0220\u0224\u022c\u0236\u0245\u024e\t\3:\2\3;\3\3<\4")
        buf.write("\b\2\2\3M\5\3N\6\3O\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOREACH = 6
    TRUE = 7
    FALSE = 8
    ARRAY = 9
    IN = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    STRING = 14
    RETURN = 15
    NULL = 16
    CLASS = 17
    VAL = 18
    VAR = 19
    CONSTRUCTOR = 20
    DESTRUCTOR = 21
    NEW = 22
    BY = 23
    WRITELN = 24
    SELF = 25
    PLUS = 26
    MINUS = 27
    STAR = 28
    DIV = 29
    MOD = 30
    NOT = 31
    ANDAND = 32
    OROR = 33
    EQ = 34
    ASSIGN = 35
    NE = 36
    GT = 37
    GE = 38
    LS = 39
    LE = 40
    STR_CMP = 41
    STR_CONCAT = 42
    DCL = 43
    SM = 44
    CM = 45
    DOT = 46
    DDOT = 47
    CL = 48
    LP = 49
    RP = 50
    LSB = 51
    RSB = 52
    LCB = 53
    RCB = 54
    IDENTIFIER = 55
    IDENTIFIER_NORMAL = 56
    INT_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    WS = 60
    BLOCKCOMMENT = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
            "'::'", "';'", "','", "'.'", "'..'", "':'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "WRITELN", "SELF", "PLUS", "MINUS", "STAR", "DIV", 
            "MOD", "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", 
            "GE", "LS", "LE", "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", 
            "DOT", "DDOT", "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", 
            "IDENTIFIER", "IDENTIFIER_NORMAL", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "WS", "BLOCKCOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "WRITELN", "SELF", "PLUS", 
                  "MINUS", "STAR", "DIV", "MOD", "NOT", "ANDAND", "OROR", 
                  "EQ", "ASSIGN", "NE", "GT", "GE", "LS", "LE", "STR_CMP", 
                  "STR_CONCAT", "DCL", "SM", "CM", "DOT", "DDOT", "CL", 
                  "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "IDENTIFIER_NORMAL", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                  "ID_normal", "ID_static", "DECIMAL", "OCTAL", "HEX", "BINARY", 
                  "DECIMAL_FLOAT", "DIGIT", "DIGITNONZERO", "EXPONENT", 
                  "SIGN", "ESC_ILLEGAL", "STR_CHAR", "ESC_ACCEPT", "WS", 
                  "BLOCKCOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[58] = self.STRING_LIT_action 
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
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
             self.text = self.text[1:-1] 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		possible = ['\n', '\r']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


