# Generated from /Users/tieuviettrongnghia/Documents/Document/HỌC TẬP/ĐẠI HỌC BÁCH KHOA/212/PPL/Assignment/Assignment 1/initial copy/src/main/d96/parser/D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0255\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u013e\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\58\u018c\n8\39\39\39\3")
        buf.write("9\39\59\u0193\n9\39\39\3:\3:\3:\6:\u019a\n:\r:\16:\u019b")
        buf.write("\3:\5:\u019f\n:\3:\3:\3:\3:\3:\6:\u01a6\n:\r:\16:\u01a7")
        buf.write("\3:\5:\u01ab\n:\5:\u01ad\n:\3:\3:\3;\3;\7;\u01b3\n;\f")
        buf.write(";\16;\u01b6\13;\3;\3;\3;\3<\3<\7<\u01bd\n<\f<\16<\u01c0")
        buf.write("\13<\3=\3=\3=\7=\u01c5\n=\f=\16=\u01c8\13=\3>\6>\u01cb")
        buf.write("\n>\r>\16>\u01cc\3>\3>\6>\u01d1\n>\r>\16>\u01d2\7>\u01d5")
        buf.write("\n>\f>\16>\u01d8\13>\3?\3?\6?\u01dc\n?\r?\16?\u01dd\3")
        buf.write("?\3?\6?\u01e2\n?\r?\16?\u01e3\7?\u01e6\n?\f?\16?\u01e9")
        buf.write("\13?\3@\3@\3@\6@\u01ee\n@\r@\16@\u01ef\3@\3@\6@\u01f4")
        buf.write("\n@\r@\16@\u01f5\7@\u01f8\n@\f@\16@\u01fb\13@\3A\3A\3")
        buf.write("A\6A\u0200\nA\rA\16A\u0201\3A\3A\6A\u0206\nA\rA\16A\u0207")
        buf.write("\7A\u020a\nA\fA\16A\u020d\13A\3B\3B\5B\u0211\nB\3C\3C")
        buf.write("\3D\3D\3E\3E\5E\u0219\nE\3E\3E\3F\3F\3G\3G\3G\5G\u0222")
        buf.write("\nG\3H\3H\5H\u0226\nH\3I\3I\3I\3J\6J\u022c\nJ\rJ\16J\u022d")
        buf.write("\3J\3J\3K\3K\3K\3K\7K\u0236\nK\fK\16K\u0239\13K\3K\3K")
        buf.write("\3K\3K\3K\3L\3L\3L\3M\3M\7M\u0245\nM\fM\16M\u0248\13M")
        buf.write("\3M\3M\3N\3N\7N\u024e\nN\fN\16N\u0251\13N\3N\3N\3N\3\u0237")
        buf.write("\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093=\u0095")
        buf.write(">\u0097?\u0099@\u009bA\3\2\22\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\3\2\62\63")
        buf.write("\3\2\63;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\3\2^^\6\2")
        buf.write("\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\2")
        buf.write("\u026a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0093\3\2\2\2\2")
        buf.write("\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\3\u009d\3\2\2\2\5\u00a3\3\2\2\2\7\u00ac\3\2\2")
        buf.write("\2\t\u00af\3\2\2\2\13\u00b6\3\2\2\2\r\u00bb\3\2\2\2\17")
        buf.write("\u00c3\3\2\2\2\21\u00c8\3\2\2\2\23\u00ce\3\2\2\2\25\u00d4")
        buf.write("\3\2\2\2\27\u00d7\3\2\2\2\31\u00db\3\2\2\2\33\u00e1\3")
        buf.write("\2\2\2\35\u00e9\3\2\2\2\37\u00f0\3\2\2\2!\u00f7\3\2\2")
        buf.write("\2#\u00fc\3\2\2\2%\u0102\3\2\2\2\'\u0106\3\2\2\2)\u010a")
        buf.write("\3\2\2\2+\u0116\3\2\2\2-\u0121\3\2\2\2/\u0125\3\2\2\2")
        buf.write("\61\u013d\3\2\2\2\63\u013f\3\2\2\2\65\u0144\3\2\2\2\67")
        buf.write("\u0146\3\2\2\29\u0148\3\2\2\2;\u014a\3\2\2\2=\u014c\3")
        buf.write("\2\2\2?\u014e\3\2\2\2A\u0150\3\2\2\2C\u0153\3\2\2\2E\u0156")
        buf.write("\3\2\2\2G\u0159\3\2\2\2I\u015b\3\2\2\2K\u015e\3\2\2\2")
        buf.write("M\u0160\3\2\2\2O\u0163\3\2\2\2Q\u0165\3\2\2\2S\u0168\3")
        buf.write("\2\2\2U\u016c\3\2\2\2W\u016f\3\2\2\2Y\u0172\3\2\2\2[\u0174")
        buf.write("\3\2\2\2]\u0176\3\2\2\2_\u0179\3\2\2\2a\u017b\3\2\2\2")
        buf.write("c\u017d\3\2\2\2e\u017f\3\2\2\2g\u0181\3\2\2\2i\u0183\3")
        buf.write("\2\2\2k\u0185\3\2\2\2m\u0187\3\2\2\2o\u018b\3\2\2\2q\u0192")
        buf.write("\3\2\2\2s\u01ac\3\2\2\2u\u01b0\3\2\2\2w\u01ba\3\2\2\2")
        buf.write("y\u01c1\3\2\2\2{\u01ca\3\2\2\2}\u01d9\3\2\2\2\177\u01ea")
        buf.write("\3\2\2\2\u0081\u01fc\3\2\2\2\u0083\u020e\3\2\2\2\u0085")
        buf.write("\u0212\3\2\2\2\u0087\u0214\3\2\2\2\u0089\u0216\3\2\2\2")
        buf.write("\u008b\u021c\3\2\2\2\u008d\u0221\3\2\2\2\u008f\u0225\3")
        buf.write("\2\2\2\u0091\u0227\3\2\2\2\u0093\u022b\3\2\2\2\u0095\u0231")
        buf.write("\3\2\2\2\u0097\u023f\3\2\2\2\u0099\u0242\3\2\2\2\u009b")
        buf.write("\u024b\3\2\2\2\u009d\u009e\7D\2\2\u009e\u009f\7t\2\2\u009f")
        buf.write("\u00a0\7g\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7m\2\2\u00a2")
        buf.write("\4\3\2\2\2\u00a3\u00a4\7E\2\2\u00a4\u00a5\7q\2\2\u00a5")
        buf.write("\u00a6\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7k\2\2\u00a8")
        buf.write("\u00a9\7p\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\6\3\2\2\2\u00ac\u00ad\7K\2\2\u00ad\u00ae\7h\2\2\u00ae")
        buf.write("\b\3\2\2\2\u00af\u00b0\7G\2\2\u00b0\u00b1\7n\2\2\u00b1")
        buf.write("\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7k\2\2\u00b4")
        buf.write("\u00b5\7h\2\2\u00b5\n\3\2\2\2\u00b6\u00b7\7G\2\2\u00b7")
        buf.write("\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\f\3\2\2\2\u00bb\u00bc\7H\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write("\u00be\7t\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7e\2\2\u00c1\u00c2\7j\2\2\u00c2\16\3\2\2\2\u00c3")
        buf.write("\u00c4\7V\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7w\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\20\3\2\2\2\u00c8\u00c9\7H\2\2\u00c9")
        buf.write("\u00ca\7c\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\22\3\2\2\2\u00ce\u00cf\7C\2\2\u00cf")
        buf.write("\u00d0\7t\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7c\2\2\u00d2")
        buf.write("\u00d3\7{\2\2\u00d3\24\3\2\2\2\u00d4\u00d5\7K\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7K\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\30\3\2\2\2\u00db")
        buf.write("\u00dc\7H\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0\32\3\2\2\2\u00e1")
        buf.write("\u00e2\7D\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7n\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\34\3\2\2\2\u00e9\u00ea\7U\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7k\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7i\2\2\u00ef\36\3\2\2\2\u00f0")
        buf.write("\u00f1\7T\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write("\u00f4\7w\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write(" \3\2\2\2\u00f7\u00f8\7P\2\2\u00f8\u00f9\7w\2\2\u00f9")
        buf.write("\u00fa\7n\2\2\u00fa\u00fb\7n\2\2\u00fb\"\3\2\2\2\u00fc")
        buf.write("\u00fd\7E\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7c\2\2\u00ff")
        buf.write("\u0100\7u\2\2\u0100\u0101\7u\2\2\u0101$\3\2\2\2\u0102")
        buf.write("\u0103\7X\2\2\u0103\u0104\7c\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write("&\3\2\2\2\u0106\u0107\7X\2\2\u0107\u0108\7c\2\2\u0108")
        buf.write("\u0109\7t\2\2\u0109(\3\2\2\2\u010a\u010b\7E\2\2\u010b")
        buf.write("\u010c\7q\2\2\u010c\u010d\7p\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7w\2\2\u0111")
        buf.write("\u0112\7e\2\2\u0112\u0113\7v\2\2\u0113\u0114\7q\2\2\u0114")
        buf.write("\u0115\7t\2\2\u0115*\3\2\2\2\u0116\u0117\7F\2\2\u0117")
        buf.write("\u0118\7g\2\2\u0118\u0119\7u\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\u011b\7t\2\2\u011b\u011c\7w\2\2\u011c\u011d\7e\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7q\2\2\u011f\u0120\7t\2\2\u0120")
        buf.write(",\3\2\2\2\u0121\u0122\7P\2\2\u0122\u0123\7g\2\2\u0123")
        buf.write("\u0124\7y\2\2\u0124.\3\2\2\2\u0125\u0126\7D\2\2\u0126")
        buf.write("\u0127\7{\2\2\u0127\60\3\2\2\2\u0128\u0129\7Y\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7k\2\2\u012b\u012c\7v\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d\u012e\7N\2\2\u012e\u013e\7p\2\2\u012f")
        buf.write("\u0130\7y\2\2\u0130\u0131\7t\2\2\u0131\u0132\7k\2\2\u0132")
        buf.write("\u0133\7v\2\2\u0133\u0134\7g\2\2\u0134\u0135\7n\2\2\u0135")
        buf.write("\u013e\7p\2\2\u0136\u0137\7Y\2\2\u0137\u0138\7T\2\2\u0138")
        buf.write("\u0139\7K\2\2\u0139\u013a\7V\2\2\u013a\u013b\7G\2\2\u013b")
        buf.write("\u013c\7N\2\2\u013c\u013e\7P\2\2\u013d\u0128\3\2\2\2\u013d")
        buf.write("\u012f\3\2\2\2\u013d\u0136\3\2\2\2\u013e\62\3\2\2\2\u013f")
        buf.write("\u0140\7U\2\2\u0140\u0141\7g\2\2\u0141\u0142\7n\2\2\u0142")
        buf.write("\u0143\7h\2\2\u0143\64\3\2\2\2\u0144\u0145\7-\2\2\u0145")
        buf.write("\66\3\2\2\2\u0146\u0147\7/\2\2\u01478\3\2\2\2\u0148\u0149")
        buf.write("\7,\2\2\u0149:\3\2\2\2\u014a\u014b\7\61\2\2\u014b<\3\2")
        buf.write("\2\2\u014c\u014d\7\'\2\2\u014d>\3\2\2\2\u014e\u014f\7")
        buf.write("#\2\2\u014f@\3\2\2\2\u0150\u0151\7(\2\2\u0151\u0152\7")
        buf.write("(\2\2\u0152B\3\2\2\2\u0153\u0154\7~\2\2\u0154\u0155\7")
        buf.write("~\2\2\u0155D\3\2\2\2\u0156\u0157\7?\2\2\u0157\u0158\7")
        buf.write("?\2\2\u0158F\3\2\2\2\u0159\u015a\7?\2\2\u015aH\3\2\2\2")
        buf.write("\u015b\u015c\7#\2\2\u015c\u015d\7?\2\2\u015dJ\3\2\2\2")
        buf.write("\u015e\u015f\7@\2\2\u015fL\3\2\2\2\u0160\u0161\7@\2\2")
        buf.write("\u0161\u0162\7?\2\2\u0162N\3\2\2\2\u0163\u0164\7>\2\2")
        buf.write("\u0164P\3\2\2\2\u0165\u0166\7>\2\2\u0166\u0167\7?\2\2")
        buf.write("\u0167R\3\2\2\2\u0168\u0169\7?\2\2\u0169\u016a\7?\2\2")
        buf.write("\u016a\u016b\7\60\2\2\u016bT\3\2\2\2\u016c\u016d\7-\2")
        buf.write("\2\u016d\u016e\7\60\2\2\u016eV\3\2\2\2\u016f\u0170\7<")
        buf.write("\2\2\u0170\u0171\7<\2\2\u0171X\3\2\2\2\u0172\u0173\7=")
        buf.write("\2\2\u0173Z\3\2\2\2\u0174\u0175\7.\2\2\u0175\\\3\2\2\2")
        buf.write("\u0176\u0177\7\60\2\2\u0177\u0178\7\60\2\2\u0178^\3\2")
        buf.write("\2\2\u0179\u017a\7\60\2\2\u017a`\3\2\2\2\u017b\u017c\7")
        buf.write("<\2\2\u017cb\3\2\2\2\u017d\u017e\7*\2\2\u017ed\3\2\2\2")
        buf.write("\u017f\u0180\7+\2\2\u0180f\3\2\2\2\u0181\u0182\7]\2\2")
        buf.write("\u0182h\3\2\2\2\u0183\u0184\7_\2\2\u0184j\3\2\2\2\u0185")
        buf.write("\u0186\7}\2\2\u0186l\3\2\2\2\u0187\u0188\7\177\2\2\u0188")
        buf.write("n\3\2\2\2\u0189\u018c\5w<\2\u018a\u018c\5y=\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018a\3\2\2\2\u018cp\3\2\2\2\u018d\u0193")
        buf.write("\5{>\2\u018e\u0193\5}?\2\u018f\u0193\5\177@\2\u0190\u0193")
        buf.write("\5\u0081A\2\u0191\u0193\7\62\2\2\u0192\u018d\3\2\2\2\u0192")
        buf.write("\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\b")
        buf.write("9\2\2\u0195r\3\2\2\2\u0196\u0197\5{>\2\u0197\u0199\5_")
        buf.write("\60\2\u0198\u019a\5\u0085C\2\u0199\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c\u019e\3\2\2\2\u019d\u019f\5\u0089E\2\u019e\u019d")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01ad\3\2\2\2\u01a0")
        buf.write("\u01a1\5{>\2\u01a1\u01a2\5\u0089E\2\u01a2\u01ad\3\2\2")
        buf.write("\2\u01a3\u01a5\5_\60\2\u01a4\u01a6\5\u0085C\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab\5\u0089")
        buf.write("E\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad")
        buf.write("\3\2\2\2\u01ac\u0196\3\2\2\2\u01ac\u01a0\3\2\2\2\u01ac")
        buf.write("\u01a3\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\b:\3\2")
        buf.write("\u01aft\3\2\2\2\u01b0\u01b4\7$\2\2\u01b1\u01b3\5\u008f")
        buf.write("H\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b8\7$\2\2\u01b8\u01b9\b;\4\2\u01b9")
        buf.write("v\3\2\2\2\u01ba\u01be\t\2\2\2\u01bb\u01bd\t\3\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bfx\3\2\2\2\u01c0\u01be\3\2\2")
        buf.write("\2\u01c1\u01c2\7&\2\2\u01c2\u01c6\t\2\2\2\u01c3\u01c5")
        buf.write("\t\3\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7z\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c9\u01cb\t\4\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cd\u01d6\3\2\2\2\u01ce\u01d0\7a\2\2\u01cf\u01d1")
        buf.write("\t\4\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2")
        buf.write("\u01d4\u01ce\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3")
        buf.write("\2\2\2\u01d6\u01d7\3\2\2\2\u01d7|\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d9\u01db\7\62\2\2\u01da\u01dc\t\5\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e7\3\2\2\2\u01df\u01e1\7")
        buf.write("a\2\2\u01e0\u01e2\t\5\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01e6\3\2\2\2\u01e5\u01df\3\2\2\2\u01e6\u01e9\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8~\3\2\2")
        buf.write("\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\7\62\2\2\u01eb\u01ed")
        buf.write("\t\6\2\2\u01ec\u01ee\t\7\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f9\3\2\2\2\u01f1\u01f3\7a\2\2\u01f2\u01f4\t")
        buf.write("\7\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7")
        buf.write("\u01f1\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u0080\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fc\u01fd\7\62\2\2\u01fd\u01ff\t\b\2\2\u01fe")
        buf.write("\u0200\t\t\2\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u020b\3")
        buf.write("\2\2\2\u0203\u0205\7a\2\2\u0204\u0206\t\t\2\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0203\3\2\2\2")
        buf.write("\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3")
        buf.write("\2\2\2\u020c\u0082\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0210")
        buf.write("\5_\60\2\u020f\u0211\5{>\2\u0210\u020f\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0084\3\2\2\2\u0212\u0213\t\4\2\2\u0213")
        buf.write("\u0086\3\2\2\2\u0214\u0215\t\n\2\2\u0215\u0088\3\2\2\2")
        buf.write("\u0216\u0218\t\13\2\2\u0217\u0219\5\u008bF\2\u0218\u0217")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a\3\2\2\2\u021a")
        buf.write("\u021b\5{>\2\u021b\u008a\3\2\2\2\u021c\u021d\t\f\2\2\u021d")
        buf.write("\u008c\3\2\2\2\u021e\u021f\7^\2\2\u021f\u0222\n\r\2\2")
        buf.write("\u0220\u0222\n\16\2\2\u0221\u021e\3\2\2\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u008e\3\2\2\2\u0223\u0226\n\17\2\2\u0224")
        buf.write("\u0226\5\u0091I\2\u0225\u0223\3\2\2\2\u0225\u0224\3\2")
        buf.write("\2\2\u0226\u0090\3\2\2\2\u0227\u0228\7^\2\2\u0228\u0229")
        buf.write("\t\20\2\2\u0229\u0092\3\2\2\2\u022a\u022c\t\21\2\2\u022b")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022d\u022e\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\b")
        buf.write("J\5\2\u0230\u0094\3\2\2\2\u0231\u0232\7%\2\2\u0232\u0233")
        buf.write("\7%\2\2\u0233\u0237\3\2\2\2\u0234\u0236\13\2\2\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u023a\u023b\7%\2\2\u023b\u023c\7%\2\2\u023c\u023d")
        buf.write("\3\2\2\2\u023d\u023e\bK\5\2\u023e\u0096\3\2\2\2\u023f")
        buf.write("\u0240\13\2\2\2\u0240\u0241\bL\6\2\u0241\u0098\3\2\2\2")
        buf.write("\u0242\u0246\7$\2\2\u0243\u0245\5\u008fH\2\u0244\u0243")
        buf.write("\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246")
        buf.write("\u0247\3\2\2\2\u0247\u0249\3\2\2\2\u0248\u0246\3\2\2\2")
        buf.write("\u0249\u024a\bM\7\2\u024a\u009a\3\2\2\2\u024b\u024f\7")
        buf.write("$\2\2\u024c\u024e\5\u008fH\2\u024d\u024c\3\2\2\2\u024e")
        buf.write("\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2\u0252\u0253\5")
        buf.write("\u008dG\2\u0253\u0254\bN\b\2\u0254\u009c\3\2\2\2\"\2\u013d")
        buf.write("\u018b\u0192\u019b\u019e\u01a7\u01aa\u01ac\u01b4\u01be")
        buf.write("\u01c6\u01cc\u01d2\u01d6\u01dd\u01e3\u01e7\u01ef\u01f5")
        buf.write("\u01f9\u0201\u0207\u020b\u0210\u0218\u0221\u0225\u022d")
        buf.write("\u0237\u0246\u024f\t\39\2\3:\3\3;\4\b\2\2\3L\5\3M\6\3")
        buf.write("N\7")
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
    DDOT = 46
    DOT = 47
    CL = 48
    LP = 49
    RP = 50
    LSB = 51
    RSB = 52
    LCB = 53
    RCB = 54
    IDENTIFIER = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    WS = 59
    BLOCKCOMMENT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
            "'::'", "';'", "','", "'..'", "'.'", "':'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "WRITELN", "SELF", "PLUS", "MINUS", "STAR", "DIV", 
            "MOD", "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", 
            "GE", "LS", "LE", "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", 
            "DDOT", "DOT", "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", 
            "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "BLOCKCOMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "WRITELN", "SELF", "PLUS", 
                  "MINUS", "STAR", "DIV", "MOD", "NOT", "ANDAND", "OROR", 
                  "EQ", "ASSIGN", "NE", "GT", "GE", "LS", "LE", "STR_CMP", 
                  "STR_CONCAT", "DCL", "SM", "CM", "DDOT", "DOT", "CL", 
                  "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID_normal", "ID_static", 
                  "DECIMAL", "OCTAL", "HEX", "BINARY", "DECIMAL_FLOAT", 
                  "DIGIT", "DIGITNONZERO", "EXPONENT", "SIGN", "ESC_ILLEGAL", 
                  "STR_CHAR", "ESC_ACCEPT", "WS", "BLOCKCOMMENT", "ERROR_CHAR", 
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
            actions[55] = self.INT_LIT_action 
            actions[56] = self.FLOAT_LIT_action 
            actions[57] = self.STRING_LIT_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
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
            	
     


