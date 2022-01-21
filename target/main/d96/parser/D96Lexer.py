# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u027e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0159\n\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\6<\u01a2\n<\r<\16<\u01a3\3=\3=\5=\u01a8\n=\3=\6=")
        buf.write("\u01ab\n=\r=\16=\u01ac\3>\3>\3?\6?\u01b2\n?\r?\16?\u01b3")
        buf.write("\3?\3?\3@\3@\3@\3@\7@\u01bc\n@\f@\16@\u01bf\13@\3@\3@")
        buf.write("\3@\3@\3@\3A\3A\5A\u01c8\nA\3B\3B\7B\u01cc\nB\fB\16B\u01cf")
        buf.write("\13B\3C\3C\3C\7C\u01d4\nC\fC\16C\u01d7\13C\3D\3D\3D\3")
        buf.write("D\5D\u01dd\nD\3D\3D\3E\3E\7E\u01e3\nE\fE\16E\u01e6\13")
        buf.write("E\3E\3E\6E\u01ea\nE\rE\16E\u01eb\7E\u01ee\nE\fE\16E\u01f1")
        buf.write("\13E\3E\5E\u01f4\nE\3F\3F\6F\u01f8\nF\rF\16F\u01f9\3F")
        buf.write("\3F\6F\u01fe\nF\rF\16F\u01ff\7F\u0202\nF\fF\16F\u0205")
        buf.write("\13F\3G\3G\6G\u0209\nG\rG\16G\u020a\3H\3H\3H\6H\u0210")
        buf.write("\nH\rH\16H\u0211\3H\3H\6H\u0216\nH\rH\16H\u0217\7H\u021a")
        buf.write("\nH\fH\16H\u021d\13H\3I\3I\3I\3J\6J\u0223\nJ\rJ\16J\u0224")
        buf.write("\3J\3J\6J\u0229\nJ\rJ\16J\u022a\7J\u022d\nJ\fJ\16J\u0230")
        buf.write("\13J\3K\6K\u0233\nK\rK\16K\u0234\3K\3K\3K\7K\u023a\nK")
        buf.write("\fK\16K\u023d\13K\3K\6K\u0240\nK\rK\16K\u0241\3K\3K\6")
        buf.write("K\u0246\nK\rK\16K\u0247\3K\5K\u024b\nK\3K\6K\u024e\nK")
        buf.write("\rK\16K\u024f\3K\3K\3K\3K\7K\u0256\nK\fK\16K\u0259\13")
        buf.write("K\3K\5K\u025c\nK\5K\u025e\nK\3K\3K\3L\3L\5L\u0264\nL\3")
        buf.write("M\3M\7M\u0268\nM\fM\16M\u026b\13M\3M\3M\3M\3N\3N\3N\3")
        buf.write("O\3O\5O\u0275\nO\3P\3P\3P\3Q\3Q\3Q\5Q\u027d\nQ\3\u01bd")
        buf.write("\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2")
        buf.write("q9s\2u\2w:y\2{\2};\177<\u0081=\u0083>\u0085?\u0087@\u0089")
        buf.write("A\u008bB\u008dC\u008fD\u0091E\u0093F\u0095G\u0097H\u0099")
        buf.write("I\u009bJ\u009dK\u009f\2\u00a1\2\3\2\21\3\2\62;\3\2\63")
        buf.write(";\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\629\4\2DDdd\3\2\62\63\4\2ZZzz\4\2\62;CH\7")
        buf.write("\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u02a1\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2q\3\2\2\2\2w")
        buf.write("\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u00a3")
        buf.write("\3\2\2\2\5\u00ab\3\2\2\2\7\u00b0\3\2\2\2\t\u00b5\3\2\2")
        buf.write("\2\13\u00b8\3\2\2\2\r\u00be\3\2\2\2\17\u00c7\3\2\2\2\21")
        buf.write("\u00ca\3\2\2\2\23\u00d1\3\2\2\2\25\u00d6\3\2\2\2\27\u00de")
        buf.write("\3\2\2\2\31\u00e3\3\2\2\2\33\u00e9\3\2\2\2\35\u00ef\3")
        buf.write("\2\2\2\37\u00f2\3\2\2\2!\u00f6\3\2\2\2#\u00fc\3\2\2\2")
        buf.write("%\u0104\3\2\2\2\'\u010b\3\2\2\2)\u0112\3\2\2\2+\u0117")
        buf.write("\3\2\2\2-\u011d\3\2\2\2/\u0121\3\2\2\2\61\u0125\3\2\2")
        buf.write("\2\63\u0131\3\2\2\2\65\u013c\3\2\2\2\67\u0140\3\2\2\2")
        buf.write("9\u0158\3\2\2\2;\u015a\3\2\2\2=\u015c\3\2\2\2?\u015e\3")
        buf.write("\2\2\2A\u0160\3\2\2\2C\u0162\3\2\2\2E\u0164\3\2\2\2G\u0166")
        buf.write("\3\2\2\2I\u0169\3\2\2\2K\u016c\3\2\2\2M\u016f\3\2\2\2")
        buf.write("O\u0171\3\2\2\2Q\u0174\3\2\2\2S\u0176\3\2\2\2U\u0179\3")
        buf.write("\2\2\2W\u017b\3\2\2\2Y\u017e\3\2\2\2[\u0182\3\2\2\2]\u0185")
        buf.write("\3\2\2\2_\u0188\3\2\2\2a\u018a\3\2\2\2c\u018c\3\2\2\2")
        buf.write("e\u018e\3\2\2\2g\u0190\3\2\2\2i\u0192\3\2\2\2k\u0194\3")
        buf.write("\2\2\2m\u0196\3\2\2\2o\u0198\3\2\2\2q\u019a\3\2\2\2s\u019c")
        buf.write("\3\2\2\2u\u019e\3\2\2\2w\u01a1\3\2\2\2y\u01a5\3\2\2\2")
        buf.write("{\u01ae\3\2\2\2}\u01b1\3\2\2\2\177\u01b7\3\2\2\2\u0081")
        buf.write("\u01c7\3\2\2\2\u0083\u01c9\3\2\2\2\u0085\u01d0\3\2\2\2")
        buf.write("\u0087\u01dc\3\2\2\2\u0089\u01f3\3\2\2\2\u008b\u01f5\3")
        buf.write("\2\2\2\u008d\u0206\3\2\2\2\u008f\u020c\3\2\2\2\u0091\u021e")
        buf.write("\3\2\2\2\u0093\u0222\3\2\2\2\u0095\u025d\3\2\2\2\u0097")
        buf.write("\u0263\3\2\2\2\u0099\u0265\3\2\2\2\u009b\u026f\3\2\2\2")
        buf.write("\u009d\u0274\3\2\2\2\u009f\u0276\3\2\2\2\u00a1\u027c\3")
        buf.write("\2\2\2\u00a3\u00a4\7R\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7i\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac")
        buf.write("\7o\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\6\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7z\2\2\u00b2\u00b3\7r\2\2\u00b3\u00b4\7t\2\2\u00b4\b")
        buf.write("\3\2\2\2\u00b5\u00b6\7\60\2\2\u00b6\u00b7\7\60\2\2\u00b7")
        buf.write("\n\3\2\2\2\u00b8\u00b9\7D\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7m\2\2\u00bd")
        buf.write("\f\3\2\2\2\u00be\u00bf\7E\2\2\u00bf\u00c0\7q\2\2\u00c0")
        buf.write("\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\16\3\2\2\2\u00c7\u00c8\7K\2\2\u00c8\u00c9\7h\2\2\u00c9")
        buf.write("\20\3\2\2\2\u00ca\u00cb\7G\2\2\u00cb\u00cc\7n\2\2\u00cc")
        buf.write("\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7k\2\2\u00cf")
        buf.write("\u00d0\7h\2\2\u00d0\22\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\24\3\2\2\2\u00d6\u00d7\7H\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7e\2\2\u00dc\u00dd\7j\2\2\u00dd\26\3\2\2\2\u00de")
        buf.write("\u00df\7V\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7w\2\2\u00e1")
        buf.write("\u00e2\7g\2\2\u00e2\30\3\2\2\2\u00e3\u00e4\7H\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8\32\3\2\2\2\u00e9\u00ea\7C\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7c\2\2\u00ed")
        buf.write("\u00ee\7{\2\2\u00ee\34\3\2\2\2\u00ef\u00f0\7K\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7K\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5 \3\2\2\2\u00f6")
        buf.write("\u00f7\7H\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write("\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fb\"\3\2\2\2\u00fc")
        buf.write("\u00fd\7D\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7q\2\2\u00ff")
        buf.write("\u0100\7n\2\2\u0100\u0101\7g\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103$\3\2\2\2\u0104\u0105\7U\2\2\u0105")
        buf.write("\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107\u0108\7k\2\2\u0108")
        buf.write("\u0109\7p\2\2\u0109\u010a\7i\2\2\u010a&\3\2\2\2\u010b")
        buf.write("\u010c\7T\2\2\u010c\u010d\7g\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7w\2\2\u010f\u0110\7t\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("(\3\2\2\2\u0112\u0113\7P\2\2\u0113\u0114\7w\2\2\u0114")
        buf.write("\u0115\7n\2\2\u0115\u0116\7n\2\2\u0116*\3\2\2\2\u0117")
        buf.write("\u0118\7E\2\2\u0118\u0119\7n\2\2\u0119\u011a\7c\2\2\u011a")
        buf.write("\u011b\7u\2\2\u011b\u011c\7u\2\2\u011c,\3\2\2\2\u011d")
        buf.write("\u011e\7X\2\2\u011e\u011f\7c\2\2\u011f\u0120\7n\2\2\u0120")
        buf.write(".\3\2\2\2\u0121\u0122\7X\2\2\u0122\u0123\7c\2\2\u0123")
        buf.write("\u0124\7t\2\2\u0124\60\3\2\2\2\u0125\u0126\7E\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7p\2\2\u0128\u0129\7u\2\2\u0129")
        buf.write("\u012a\7v\2\2\u012a\u012b\7t\2\2\u012b\u012c\7w\2\2\u012c")
        buf.write("\u012d\7e\2\2\u012d\u012e\7v\2\2\u012e\u012f\7q\2\2\u012f")
        buf.write("\u0130\7t\2\2\u0130\62\3\2\2\2\u0131\u0132\7F\2\2\u0132")
        buf.write("\u0133\7g\2\2\u0133\u0134\7u\2\2\u0134\u0135\7v\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136\u0137\7w\2\2\u0137\u0138\7e\2\2\u0138")
        buf.write("\u0139\7v\2\2\u0139\u013a\7q\2\2\u013a\u013b\7t\2\2\u013b")
        buf.write("\64\3\2\2\2\u013c\u013d\7P\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7y\2\2\u013f\66\3\2\2\2\u0140\u0141\7D\2\2\u0141")
        buf.write("\u0142\7{\2\2\u01428\3\2\2\2\u0143\u0144\7Y\2\2\u0144")
        buf.write("\u0145\7t\2\2\u0145\u0146\7k\2\2\u0146\u0147\7v\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148\u0149\7N\2\2\u0149\u0159\7p\2\2\u014a")
        buf.write("\u014b\7y\2\2\u014b\u014c\7t\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014e\u014f\7g\2\2\u014f\u0150\7n\2\2\u0150")
        buf.write("\u0159\7p\2\2\u0151\u0152\7Y\2\2\u0152\u0153\7T\2\2\u0153")
        buf.write("\u0154\7K\2\2\u0154\u0155\7V\2\2\u0155\u0156\7G\2\2\u0156")
        buf.write("\u0157\7N\2\2\u0157\u0159\7P\2\2\u0158\u0143\3\2\2\2\u0158")
        buf.write("\u014a\3\2\2\2\u0158\u0151\3\2\2\2\u0159:\3\2\2\2\u015a")
        buf.write("\u015b\7-\2\2\u015b<\3\2\2\2\u015c\u015d\7/\2\2\u015d")
        buf.write(">\3\2\2\2\u015e\u015f\7,\2\2\u015f@\3\2\2\2\u0160\u0161")
        buf.write("\7\61\2\2\u0161B\3\2\2\2\u0162\u0163\7\'\2\2\u0163D\3")
        buf.write("\2\2\2\u0164\u0165\7#\2\2\u0165F\3\2\2\2\u0166\u0167\7")
        buf.write("(\2\2\u0167\u0168\7(\2\2\u0168H\3\2\2\2\u0169\u016a\7")
        buf.write("~\2\2\u016a\u016b\7~\2\2\u016bJ\3\2\2\2\u016c\u016d\7")
        buf.write("?\2\2\u016d\u016e\7?\2\2\u016eL\3\2\2\2\u016f\u0170\7")
        buf.write("?\2\2\u0170N\3\2\2\2\u0171\u0172\7#\2\2\u0172\u0173\7")
        buf.write("?\2\2\u0173P\3\2\2\2\u0174\u0175\7@\2\2\u0175R\3\2\2\2")
        buf.write("\u0176\u0177\7@\2\2\u0177\u0178\7?\2\2\u0178T\3\2\2\2")
        buf.write("\u0179\u017a\7>\2\2\u017aV\3\2\2\2\u017b\u017c\7>\2\2")
        buf.write("\u017c\u017d\7?\2\2\u017dX\3\2\2\2\u017e\u017f\7?\2\2")
        buf.write("\u017f\u0180\7?\2\2\u0180\u0181\7\60\2\2\u0181Z\3\2\2")
        buf.write("\2\u0182\u0183\7-\2\2\u0183\u0184\7\60\2\2\u0184\\\3\2")
        buf.write("\2\2\u0185\u0186\7<\2\2\u0186\u0187\7<\2\2\u0187^\3\2")
        buf.write("\2\2\u0188\u0189\7*\2\2\u0189`\3\2\2\2\u018a\u018b\7+")
        buf.write("\2\2\u018bb\3\2\2\2\u018c\u018d\7]\2\2\u018dd\3\2\2\2")
        buf.write("\u018e\u018f\7_\2\2\u018ff\3\2\2\2\u0190\u0191\7}\2\2")
        buf.write("\u0191h\3\2\2\2\u0192\u0193\7\177\2\2\u0193j\3\2\2\2\u0194")
        buf.write("\u0195\7=\2\2\u0195l\3\2\2\2\u0196\u0197\7.\2\2\u0197")
        buf.write("n\3\2\2\2\u0198\u0199\7\60\2\2\u0199p\3\2\2\2\u019a\u019b")
        buf.write("\7<\2\2\u019br\3\2\2\2\u019c\u019d\t\2\2\2\u019dt\3\2")
        buf.write("\2\2\u019e\u019f\t\3\2\2\u019fv\3\2\2\2\u01a0\u01a2\5")
        buf.write("s:\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4x\3\2\2\2\u01a5\u01a7")
        buf.write("\t\4\2\2\u01a6\u01a8\5{>\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab\5s:\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01adz\3\2\2\2\u01ae\u01af\t\5\2\2\u01af")
        buf.write("|\3\2\2\2\u01b0\u01b2\t\6\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b6\b?\2\2\u01b6~\3\2\2\2")
        buf.write("\u01b7\u01b8\7%\2\2\u01b8\u01b9\7%\2\2\u01b9\u01bd\3\2")
        buf.write("\2\2\u01ba\u01bc\13\2\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\7%\2\2")
        buf.write("\u01c1\u01c2\7%\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\b")
        buf.write("@\2\2\u01c4\u0080\3\2\2\2\u01c5\u01c8\5\u0083B\2\u01c6")
        buf.write("\u01c8\5\u0085C\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3\2")
        buf.write("\2\2\u01c8\u0082\3\2\2\2\u01c9\u01cd\t\7\2\2\u01ca\u01cc")
        buf.write("\t\b\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u0084\3\2\2\2")
        buf.write("\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7&\2\2\u01d1\u01d5\t")
        buf.write("\7\2\2\u01d2\u01d4\t\b\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u0086\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01dd\5\u0089")
        buf.write("E\2\u01d9\u01dd\5\u008bF\2\u01da\u01dd\5\u008dG\2\u01db")
        buf.write("\u01dd\5\u008fH\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9\3\2")
        buf.write("\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01df\bD\3\2\u01df\u0088\3\2\2\2\u01e0")
        buf.write("\u01e4\t\3\2\2\u01e1\u01e3\t\2\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01ef\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e9")
        buf.write("\7a\2\2\u01e8\u01ea\t\2\2\2\u01e9\u01e8\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01ee\3\2\2\2\u01ed\u01e7\3\2\2\2\u01ee\u01f1\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f4")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4\7\62\2\2\u01f3")
        buf.write("\u01e0\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4\u008a\3\2\2\2")
        buf.write("\u01f5\u01f7\7\62\2\2\u01f6\u01f8\t\t\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u0203\3\2\2\2\u01fb\u01fd\7a\2\2")
        buf.write("\u01fc\u01fe\t\t\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3")
        buf.write("\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202")
        buf.write("\3\2\2\2\u0201\u01fb\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u008c\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0206\u0208\5\u0091I\2\u0207\u0209")
        buf.write("\5\u0093J\2\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u008e\3\2\2\2")
        buf.write("\u020c\u020d\7\62\2\2\u020d\u020f\t\n\2\2\u020e\u0210")
        buf.write("\t\13\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u021b\3\2\2\2")
        buf.write("\u0213\u0215\7a\2\2\u0214\u0216\t\13\2\2\u0215\u0214\3")
        buf.write("\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0213\3\2\2\2\u021a")
        buf.write("\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u0090\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u021f\7")
        buf.write("\62\2\2\u021f\u0220\t\f\2\2\u0220\u0092\3\2\2\2\u0221")
        buf.write("\u0223\t\r\2\2\u0222\u0221\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u022e\3")
        buf.write("\2\2\2\u0226\u0228\7a\2\2\u0227\u0229\t\r\2\2\u0228\u0227")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u0226\3\2\2\2")
        buf.write("\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3")
        buf.write("\2\2\2\u022f\u0094\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0233")
        buf.write("\5\u0089E\2\u0232\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write("\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0236\3\2\2\2")
        buf.write("\u0236\u023b\5o8\2\u0237\u023a\5\u0089E\2\u0238\u023a")
        buf.write("\5y=\2\u0239\u0237\3\2\2\2\u0239\u0238\3\2\2\2\u023a\u023d")
        buf.write("\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u025e\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u0240\5\u0089")
        buf.write("E\2\u023f\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u023f")
        buf.write("\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u0245\5o8\2\u0244\u0246\5\u0089E\2\u0245\u0244\3\2\2")
        buf.write("\2\u0246\u0247\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248")
        buf.write("\3\2\2\2\u0248\u024a\3\2\2\2\u0249\u024b\5y=\2\u024a\u0249")
        buf.write("\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u025e\3\2\2\2\u024c")
        buf.write("\u024e\5\u0089E\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2")
        buf.write("\2\2\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u0252\5y=\2\u0252\u025e\3\2\2\2\u0253\u0257")
        buf.write("\5o8\2\u0254\u0256\5\u0089E\2\u0255\u0254\3\2\2\2\u0256")
        buf.write("\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2")
        buf.write("\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025c\5")
        buf.write("y=\2\u025b\u025a\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025e")
        buf.write("\3\2\2\2\u025d\u0232\3\2\2\2\u025d\u023f\3\2\2\2\u025d")
        buf.write("\u024d\3\2\2\2\u025d\u0253\3\2\2\2\u025e\u025f\3\2\2\2")
        buf.write("\u025f\u0260\bK\4\2\u0260\u0096\3\2\2\2\u0261\u0264\5")
        buf.write("\27\f\2\u0262\u0264\5\31\r\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0262\3\2\2\2\u0264\u0098\3\2\2\2\u0265\u0269\7$\2\2")
        buf.write("\u0266\u0268\5\u009dO\2\u0267\u0266\3\2\2\2\u0268\u026b")
        buf.write("\3\2\2\2\u0269\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a")
        buf.write("\u026c\3\2\2\2\u026b\u0269\3\2\2\2\u026c\u026d\7$\2\2")
        buf.write("\u026d\u026e\bM\5\2\u026e\u009a\3\2\2\2\u026f\u0270\13")
        buf.write("\2\2\2\u0270\u0271\bN\6\2\u0271\u009c\3\2\2\2\u0272\u0275")
        buf.write("\n\16\2\2\u0273\u0275\5\u009fP\2\u0274\u0272\3\2\2\2\u0274")
        buf.write("\u0273\3\2\2\2\u0275\u009e\3\2\2\2\u0276\u0277\7^\2\2")
        buf.write("\u0277\u0278\t\17\2\2\u0278\u00a0\3\2\2\2\u0279\u027a")
        buf.write("\7^\2\2\u027a\u027d\n\17\2\2\u027b\u027d\n\20\2\2\u027c")
        buf.write("\u0279\3\2\2\2\u027c\u027b\3\2\2\2\u027d\u00a2\3\2\2\2")
        buf.write(")\2\u0158\u01a3\u01a7\u01ac\u01b3\u01bd\u01c7\u01cd\u01d5")
        buf.write("\u01dc\u01e4\u01eb\u01ef\u01f3\u01f9\u01ff\u0203\u020a")
        buf.write("\u0211\u0217\u021b\u0224\u022a\u022e\u0234\u0239\u023b")
        buf.write("\u0241\u0247\u024a\u024f\u0257\u025b\u025d\u0263\u0269")
        buf.write("\u0274\u027c\7\b\2\2\3D\2\3K\3\3M\4\3N\5")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELSEIF = 8
    ELSE = 9
    FOREACH = 10
    TRUE = 11
    FALSE = 12
    ARRAY = 13
    IN = 14
    INT = 15
    FLOAT = 16
    BOOLEAN = 17
    STRING = 18
    RETURN = 19
    NULL = 20
    CLASS = 21
    VAL = 22
    VAR = 23
    CONSTRUCTOR = 24
    DESTRUCTOR = 25
    NEW = 26
    BY = 27
    WRITELN = 28
    PLUS = 29
    MINUS = 30
    STAR = 31
    DIV = 32
    MOD = 33
    NOT = 34
    ANDAND = 35
    OROR = 36
    EQ = 37
    ASSIGN = 38
    NE = 39
    GT = 40
    GE = 41
    LS = 42
    LE = 43
    EQD = 44
    PDOT = 45
    DCL = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    SM = 53
    CM = 54
    CL = 55
    SDIGIT = 56
    WS = 57
    BLOCKCOMMENT = 58
    IDENTIFIER = 59
    ID_normal = 60
    ID_static = 61
    INT_LIT = 62
    DecimalConstant = 63
    OctalConstant = 64
    HexadecimalConstant = 65
    BinaryConstant = 66
    HexadecimalPrefix = 67
    HexadecimalDigit = 68
    FLOAT_LIT = 69
    BOOL_LIT = 70
    STRING_LIT = 71
    ERROR_CHAR = 72
    STR_CHAR = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'expr'", "'..'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", 
            "'>='", "'<'", "'<='", "'==.'", "'+.'", "'::'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "WRITELN", "PLUS", "MINUS", "STAR", "DIV", "MOD", 
            "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", 
            "LE", "EQD", "PDOT", "DCL", "LP", "RP", "LSB", "RSB", "LCB", 
            "RCB", "SM", "CM", "CL", "SDIGIT", "WS", "BLOCKCOMMENT", "IDENTIFIER", 
            "ID_normal", "ID_static", "INT_LIT", "DecimalConstant", "OctalConstant", 
            "HexadecimalConstant", "BinaryConstant", "HexadecimalPrefix", 
            "HexadecimalDigit", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ERROR_CHAR", 
            "STR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "BREAK", "CONTINUE", "IF", 
                  "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "WRITELN", "PLUS", "MINUS", "STAR", "DIV", "MOD", 
                  "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", 
                  "LS", "LE", "EQD", "PDOT", "DCL", "LP", "RP", "LSB", "RSB", 
                  "LCB", "RCB", "SM", "CM", "DOT", "CL", "DIGIT", "DIGITNONZERO", 
                  "SDIGIT", "EXPONENT", "SIGN", "WS", "BLOCKCOMMENT", "IDENTIFIER", 
                  "ID_normal", "ID_static", "INT_LIT", "DecimalConstant", 
                  "OctalConstant", "HexadecimalConstant", "BinaryConstant", 
                  "HexadecimalPrefix", "HexadecimalDigit", "FLOAT_LIT", 
                  "BOOL_LIT", "STRING_LIT", "ERROR_CHAR", "STR_CHAR", "ESC_SEQ", 
                  "ESC_ILLEGAL" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.INT_LIT_action 
            actions[73] = self.FLOAT_LIT_action 
            actions[75] = self.STRING_LIT_action 
            actions[76] = self.ERROR_CHAR_action 
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
     


