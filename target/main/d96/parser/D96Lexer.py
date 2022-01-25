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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0284\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u014d\n\33\3\34\3\34\3\35\3\35\3\36\3\36\3")
        buf.write("\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\59\u0196\n9\3:\3:\3:\3:\5:\u019c")
        buf.write("\n:\3:\3:\3;\6;\u01a1\n;\r;\16;\u01a2\3;\3;\3;\7;\u01a8")
        buf.write("\n;\f;\16;\u01ab\13;\3;\6;\u01ae\n;\r;\16;\u01af\3;\3")
        buf.write(";\6;\u01b4\n;\r;\16;\u01b5\3;\5;\u01b9\n;\3;\6;\u01bc")
        buf.write("\n;\r;\16;\u01bd\3;\3;\3;\3;\7;\u01c4\n;\f;\16;\u01c7")
        buf.write("\13;\3;\5;\u01ca\n;\5;\u01cc\n;\3;\3;\3<\3<\7<\u01d2\n")
        buf.write("<\f<\16<\u01d5\13<\3<\3<\3<\3=\3=\7=\u01dc\n=\f=\16=\u01df")
        buf.write("\13=\3>\3>\3>\7>\u01e4\n>\f>\16>\u01e7\13>\3?\3?\7?\u01eb")
        buf.write("\n?\f?\16?\u01ee\13?\3?\3?\6?\u01f2\n?\r?\16?\u01f3\7")
        buf.write("?\u01f6\n?\f?\16?\u01f9\13?\3?\5?\u01fc\n?\3@\3@\6@\u0200")
        buf.write("\n@\r@\16@\u0201\3@\3@\6@\u0206\n@\r@\16@\u0207\7@\u020a")
        buf.write("\n@\f@\16@\u020d\13@\3A\3A\3A\6A\u0212\nA\rA\16A\u0213")
        buf.write("\3A\3A\6A\u0218\nA\rA\16A\u0219\7A\u021c\nA\fA\16A\u021f")
        buf.write("\13A\6A\u0221\nA\rA\16A\u0222\3B\3B\3B\6B\u0228\nB\rB")
        buf.write("\16B\u0229\3B\3B\6B\u022e\nB\rB\16B\u022f\7B\u0232\nB")
        buf.write("\fB\16B\u0235\13B\3C\3C\3D\3D\3E\6E\u023c\nE\rE\16E\u023d")
        buf.write("\3F\3F\5F\u0242\nF\3F\6F\u0245\nF\rF\16F\u0246\3G\3G\3")
        buf.write("H\3H\3H\3I\3I\3I\5I\u0251\nI\3J\3J\5J\u0255\nJ\3K\6K\u0258")
        buf.write("\nK\rK\16K\u0259\3K\3K\3L\3L\3L\3L\7L\u0262\nL\fL\16L")
        buf.write("\u0265\13L\3L\3L\3L\3L\3L\3M\3M\3M\3N\3N\7N\u0271\nN\f")
        buf.write("N\16N\u0274\13N\3N\5N\u0277\nN\3N\3N\3O\3O\7O\u027d\n")
        buf.write("O\fO\16O\u0280\13O\3O\3O\3O\3\u0263\2P\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089>\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091\2\u0093\2\u0095?\u0097@\u0099A\u009b")
        buf.write("B\u009dC\3\2\22\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2")
        buf.write("\62;\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\3\2\62\63\4\2G")
        buf.write("Ggg\4\2--//\n\2$$))^^ddhhppttvv\3\2^^\7\2\n\f\16\17$$")
        buf.write("))^^\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\2\u02a2\2")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0089\3\2")
        buf.write("\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2")
        buf.write("\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00a7")
        buf.write("\3\2\2\2\7\u00ac\3\2\2\2\t\u00b2\3\2\2\2\13\u00bb\3\2")
        buf.write("\2\2\r\u00be\3\2\2\2\17\u00c5\3\2\2\2\21\u00ca\3\2\2\2")
        buf.write("\23\u00d2\3\2\2\2\25\u00d7\3\2\2\2\27\u00dd\3\2\2\2\31")
        buf.write("\u00e3\3\2\2\2\33\u00e6\3\2\2\2\35\u00ea\3\2\2\2\37\u00f0")
        buf.write("\3\2\2\2!\u00f8\3\2\2\2#\u00ff\3\2\2\2%\u0106\3\2\2\2")
        buf.write("\'\u010b\3\2\2\2)\u0111\3\2\2\2+\u0115\3\2\2\2-\u0119")
        buf.write("\3\2\2\2/\u0125\3\2\2\2\61\u0130\3\2\2\2\63\u0134\3\2")
        buf.write("\2\2\65\u014c\3\2\2\2\67\u014e\3\2\2\29\u0150\3\2\2\2")
        buf.write(";\u0152\3\2\2\2=\u0154\3\2\2\2?\u0156\3\2\2\2A\u0158\3")
        buf.write("\2\2\2C\u015a\3\2\2\2E\u015d\3\2\2\2G\u0160\3\2\2\2I\u0163")
        buf.write("\3\2\2\2K\u0165\3\2\2\2M\u0168\3\2\2\2O\u016a\3\2\2\2")
        buf.write("Q\u016d\3\2\2\2S\u016f\3\2\2\2U\u0172\3\2\2\2W\u0176\3")
        buf.write("\2\2\2Y\u0179\3\2\2\2[\u017c\3\2\2\2]\u017e\3\2\2\2_\u0180")
        buf.write("\3\2\2\2a\u0182\3\2\2\2c\u0185\3\2\2\2e\u0187\3\2\2\2")
        buf.write("g\u0189\3\2\2\2i\u018b\3\2\2\2k\u018d\3\2\2\2m\u018f\3")
        buf.write("\2\2\2o\u0191\3\2\2\2q\u0195\3\2\2\2s\u019b\3\2\2\2u\u01cb")
        buf.write("\3\2\2\2w\u01cf\3\2\2\2y\u01d9\3\2\2\2{\u01e0\3\2\2\2")
        buf.write("}\u01fb\3\2\2\2\177\u01fd\3\2\2\2\u0081\u020e\3\2\2\2")
        buf.write("\u0083\u0224\3\2\2\2\u0085\u0236\3\2\2\2\u0087\u0238\3")
        buf.write("\2\2\2\u0089\u023b\3\2\2\2\u008b\u023f\3\2\2\2\u008d\u0248")
        buf.write("\3\2\2\2\u008f\u024a\3\2\2\2\u0091\u0250\3\2\2\2\u0093")
        buf.write("\u0254\3\2\2\2\u0095\u0257\3\2\2\2\u0097\u025d\3\2\2\2")
        buf.write("\u0099\u026b\3\2\2\2\u009b\u026e\3\2\2\2\u009d\u027a\3")
        buf.write("\2\2\2\u009f\u00a0\7R\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7o\2\2\u00a6\4\3\2\2\2\u00a7\u00a8")
        buf.write("\7o\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7D\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7m\2\2\u00b1\b\3\2\2\2\u00b2\u00b3\7E\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\n\3\2\2\2\u00bb\u00bc\7K\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\f\3\2\2\2\u00be\u00bf\7G\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7h\2\2\u00c4\16\3\2\2\2\u00c5\u00c6")
        buf.write("\7G\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\20\3\2\2\2\u00ca\u00cb\7H\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7c\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7j\2\2\u00d1\22")
        buf.write("\3\2\2\2\u00d2\u00d3\7V\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7w\2\2\u00d5\u00d6\7g\2\2\u00d6\24\3\2\2\2\u00d7\u00d8")
        buf.write("\7H\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7n\2\2\u00da\u00db")
        buf.write("\7u\2\2\u00db\u00dc\7g\2\2\u00dc\26\3\2\2\2\u00dd\u00de")
        buf.write("\7C\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7{\2\2\u00e2\30\3\2\2\2\u00e3\u00e4")
        buf.write("\7K\2\2\u00e4\u00e5\7p\2\2\u00e5\32\3\2\2\2\u00e6\u00e7")
        buf.write("\7K\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\34")
        buf.write("\3\2\2\2\u00ea\u00eb\7H\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7v\2\2\u00ef\36")
        buf.write("\3\2\2\2\u00f0\u00f1\7D\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7p\2\2\u00f7 \3\2\2\2\u00f8\u00f9")
        buf.write("\7U\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\"")
        buf.write("\3\2\2\2\u00ff\u0100\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105$\3\2\2\2\u0106\u0107\7P\2\2\u0107\u0108")
        buf.write("\7w\2\2\u0108\u0109\7n\2\2\u0109\u010a\7n\2\2\u010a&\3")
        buf.write("\2\2\2\u010b\u010c\7E\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7u\2\2\u010f\u0110\7u\2\2\u0110(\3")
        buf.write("\2\2\2\u0111\u0112\7X\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114*\3\2\2\2\u0115\u0116\7X\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7t\2\2\u0118,\3\2\2\2\u0119\u011a")
        buf.write("\7E\2\2\u011a\u011b\7q\2\2\u011b\u011c\7p\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7e\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7q\2\2\u0123\u0124\7t\2\2\u0124.\3\2\2\2\u0125\u0126")
        buf.write("\7F\2\2\u0126\u0127\7g\2\2\u0127\u0128\7u\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7t\2\2\u012a\u012b\7w\2\2\u012b\u012c")
        buf.write("\7e\2\2\u012c\u012d\7v\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\60\3\2\2\2\u0130\u0131\7P\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7y\2\2\u0133\62\3\2\2\2\u0134\u0135")
        buf.write("\7D\2\2\u0135\u0136\7{\2\2\u0136\64\3\2\2\2\u0137\u0138")
        buf.write("\7Y\2\2\u0138\u0139\7t\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\u013c\7g\2\2\u013c\u013d\7N\2\2\u013d\u014d")
        buf.write("\7p\2\2\u013e\u013f\7y\2\2\u013f\u0140\7t\2\2\u0140\u0141")
        buf.write("\7k\2\2\u0141\u0142\7v\2\2\u0142\u0143\7g\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u014d\7p\2\2\u0145\u0146\7Y\2\2\u0146\u0147")
        buf.write("\7T\2\2\u0147\u0148\7K\2\2\u0148\u0149\7V\2\2\u0149\u014a")
        buf.write("\7G\2\2\u014a\u014b\7N\2\2\u014b\u014d\7P\2\2\u014c\u0137")
        buf.write("\3\2\2\2\u014c\u013e\3\2\2\2\u014c\u0145\3\2\2\2\u014d")
        buf.write("\66\3\2\2\2\u014e\u014f\7-\2\2\u014f8\3\2\2\2\u0150\u0151")
        buf.write("\7/\2\2\u0151:\3\2\2\2\u0152\u0153\7,\2\2\u0153<\3\2\2")
        buf.write("\2\u0154\u0155\7\61\2\2\u0155>\3\2\2\2\u0156\u0157\7\'")
        buf.write("\2\2\u0157@\3\2\2\2\u0158\u0159\7#\2\2\u0159B\3\2\2\2")
        buf.write("\u015a\u015b\7(\2\2\u015b\u015c\7(\2\2\u015cD\3\2\2\2")
        buf.write("\u015d\u015e\7~\2\2\u015e\u015f\7~\2\2\u015fF\3\2\2\2")
        buf.write("\u0160\u0161\7?\2\2\u0161\u0162\7?\2\2\u0162H\3\2\2\2")
        buf.write("\u0163\u0164\7?\2\2\u0164J\3\2\2\2\u0165\u0166\7#\2\2")
        buf.write("\u0166\u0167\7?\2\2\u0167L\3\2\2\2\u0168\u0169\7@\2\2")
        buf.write("\u0169N\3\2\2\2\u016a\u016b\7@\2\2\u016b\u016c\7?\2\2")
        buf.write("\u016cP\3\2\2\2\u016d\u016e\7>\2\2\u016eR\3\2\2\2\u016f")
        buf.write("\u0170\7>\2\2\u0170\u0171\7?\2\2\u0171T\3\2\2\2\u0172")
        buf.write("\u0173\7?\2\2\u0173\u0174\7?\2\2\u0174\u0175\7\60\2\2")
        buf.write("\u0175V\3\2\2\2\u0176\u0177\7-\2\2\u0177\u0178\7\60\2")
        buf.write("\2\u0178X\3\2\2\2\u0179\u017a\7<\2\2\u017a\u017b\7<\2")
        buf.write("\2\u017bZ\3\2\2\2\u017c\u017d\7=\2\2\u017d\\\3\2\2\2\u017e")
        buf.write("\u017f\7.\2\2\u017f^\3\2\2\2\u0180\u0181\7\60\2\2\u0181")
        buf.write("`\3\2\2\2\u0182\u0183\7\60\2\2\u0183\u0184\7\60\2\2\u0184")
        buf.write("b\3\2\2\2\u0185\u0186\7<\2\2\u0186d\3\2\2\2\u0187\u0188")
        buf.write("\7*\2\2\u0188f\3\2\2\2\u0189\u018a\7+\2\2\u018ah\3\2\2")
        buf.write("\2\u018b\u018c\7]\2\2\u018cj\3\2\2\2\u018d\u018e\7_\2")
        buf.write("\2\u018el\3\2\2\2\u018f\u0190\7}\2\2\u0190n\3\2\2\2\u0191")
        buf.write("\u0192\7\177\2\2\u0192p\3\2\2\2\u0193\u0196\5y=\2\u0194")
        buf.write("\u0196\5{>\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("r\3\2\2\2\u0197\u019c\5}?\2\u0198\u019c\5\177@\2\u0199")
        buf.write("\u019c\5\u0081A\2\u019a\u019c\5\u0083B\2\u019b\u0197\3")
        buf.write("\2\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b:\2\2\u019e")
        buf.write("t\3\2\2\2\u019f\u01a1\5}?\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a9\5_\60\2\u01a5\u01a8\5")
        buf.write("}?\2\u01a6\u01a8\5\u008bF\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01cc\3\2\2\2\u01ab\u01a9\3")
        buf.write("\2\2\2\u01ac\u01ae\5}?\2\u01ad\u01ac\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b3\5_\60\2\u01b2\u01b4\5}?\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b9\5")
        buf.write("\u008bF\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01cc\3\2\2\2\u01ba\u01bc\5}?\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\5\u008bF\2\u01c0\u01cc")
        buf.write("\3\2\2\2\u01c1\u01c5\5_\60\2\u01c2\u01c4\5}?\2\u01c3\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c8\u01ca\5\u008bF\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01a0\3\2\2\2\u01cb")
        buf.write("\u01ad\3\2\2\2\u01cb\u01bb\3\2\2\2\u01cb\u01c1\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\b;\3\2\u01cev\3\2\2\2")
        buf.write("\u01cf\u01d3\7$\2\2\u01d0\u01d2\5\u0093J\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\7$\2\2\u01d7\u01d8\b<\4\2\u01d8x\3\2\2\2")
        buf.write("\u01d9\u01dd\t\2\2\2\u01da\u01dc\t\3\2\2\u01db\u01da\3")
        buf.write("\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01dez\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1")
        buf.write("\7&\2\2\u01e1\u01e5\t\2\2\2\u01e2\u01e4\t\3\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6|\3\2\2\2\u01e7\u01e5\3\2\2")
        buf.write("\2\u01e8\u01ec\t\4\2\2\u01e9\u01eb\t\5\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01f7\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ef\u01f1\7a\2\2\u01f0\u01f2\t\5\2\2\u01f1\u01f0\3")
        buf.write("\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4")
        buf.write("\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01fc\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fc\7")
        buf.write("\62\2\2\u01fb\u01e8\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc")
        buf.write("~\3\2\2\2\u01fd\u01ff\7\62\2\2\u01fe\u0200\t\6\2\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202\u020b\3\2\2\2\u0203\u0205\7")
        buf.write("a\2\2\u0204\u0206\t\6\2\2\u0205\u0204\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u020a\3\2\2\2\u0209\u0203\3\2\2\2\u020a\u020d\3\2\2\2")
        buf.write("\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0080\3")
        buf.write("\2\2\2\u020d\u020b\3\2\2\2\u020e\u020f\7\62\2\2\u020f")
        buf.write("\u0220\t\7\2\2\u0210\u0212\t\b\2\2\u0211\u0210\3\2\2\2")
        buf.write("\u0212\u0213\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3")
        buf.write("\2\2\2\u0214\u021d\3\2\2\2\u0215\u0217\7a\2\2\u0216\u0218")
        buf.write("\t\b\2\2\u0217\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c\3\2\2\2")
        buf.write("\u021b\u0215\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021d\u021e\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u0220\u0211\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0082\3\2\2\2")
        buf.write("\u0224\u0225\7\62\2\2\u0225\u0227\t\t\2\2\u0226\u0228")
        buf.write("\t\n\2\2\u0227\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u0233\3\2\2\2")
        buf.write("\u022b\u022d\7a\2\2\u022c\u022e\t\n\2\2\u022d\u022c\3")
        buf.write("\2\2\2\u022e\u022f\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022b\3\2\2\2\u0232")
        buf.write("\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2")
        buf.write("\u0234\u0084\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\t")
        buf.write("\5\2\2\u0237\u0086\3\2\2\2\u0238\u0239\t\4\2\2\u0239\u0088")
        buf.write("\3\2\2\2\u023a\u023c\5\u0085C\2\u023b\u023a\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023e\u008a\3\2\2\2\u023f\u0241\t\13\2\2\u0240\u0242")
        buf.write("\5\u008dG\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write("\u0244\3\2\2\2\u0243\u0245\5\u0085C\2\u0244\u0243\3\2")
        buf.write("\2\2\u0245\u0246\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u008c\3\2\2\2\u0248\u0249\t\f\2\2\u0249")
        buf.write("\u008e\3\2\2\2\u024a\u024b\7^\2\2\u024b\u024c\t\r\2\2")
        buf.write("\u024c\u0090\3\2\2\2\u024d\u024e\7^\2\2\u024e\u0251\n")
        buf.write("\r\2\2\u024f\u0251\n\16\2\2\u0250\u024d\3\2\2\2\u0250")
        buf.write("\u024f\3\2\2\2\u0251\u0092\3\2\2\2\u0252\u0255\n\17\2")
        buf.write("\2\u0253\u0255\5\u008fH\2\u0254\u0252\3\2\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255\u0094\3\2\2\2\u0256\u0258\t\20\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0257\3\2\2\2")
        buf.write("\u0259\u025a\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025c\b")
        buf.write("K\5\2\u025c\u0096\3\2\2\2\u025d\u025e\7%\2\2\u025e\u025f")
        buf.write("\7%\2\2\u025f\u0263\3\2\2\2\u0260\u0262\13\2\2\2\u0261")
        buf.write("\u0260\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0264\3\2\2\2")
        buf.write("\u0263\u0261\3\2\2\2\u0264\u0266\3\2\2\2\u0265\u0263\3")
        buf.write("\2\2\2\u0266\u0267\7%\2\2\u0267\u0268\7%\2\2\u0268\u0269")
        buf.write("\3\2\2\2\u0269\u026a\bL\5\2\u026a\u0098\3\2\2\2\u026b")
        buf.write("\u026c\13\2\2\2\u026c\u026d\bM\6\2\u026d\u009a\3\2\2\2")
        buf.write("\u026e\u0272\7$\2\2\u026f\u0271\5\u0093J\2\u0270\u026f")
        buf.write("\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2\u0272")
        buf.write("\u0273\3\2\2\2\u0273\u0276\3\2\2\2\u0274\u0272\3\2\2\2")
        buf.write("\u0275\u0277\t\21\2\2\u0276\u0275\3\2\2\2\u0277\u0278")
        buf.write("\3\2\2\2\u0278\u0279\bN\7\2\u0279\u009c\3\2\2\2\u027a")
        buf.write("\u027e\7$\2\2\u027b\u027d\5\u0093J\2\u027c\u027b\3\2\2")
        buf.write("\2\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027f")
        buf.write("\3\2\2\2\u027f\u0281\3\2\2\2\u0280\u027e\3\2\2\2\u0281")
        buf.write("\u0282\5\u0091I\2\u0282\u0283\bO\b\2\u0283\u009e\3\2\2")
        buf.write("\2+\2\u014c\u0195\u019b\u01a2\u01a7\u01a9\u01af\u01b5")
        buf.write("\u01b8\u01bd\u01c5\u01c9\u01cb\u01d3\u01dd\u01e5\u01ec")
        buf.write("\u01f3\u01f7\u01fb\u0201\u0207\u020b\u0213\u0219\u021d")
        buf.write("\u0222\u0229\u022f\u0233\u023d\u0241\u0246\u0250\u0254")
        buf.write("\u0259\u0263\u0272\u0276\u027e\t\3:\2\3;\3\3<\4\b\2\2")
        buf.write("\3M\5\3N\6\3O\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSEIF = 6
    ELSE = 7
    FOREACH = 8
    TRUE = 9
    FALSE = 10
    ARRAY = 11
    IN = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    STRING = 16
    RETURN = 17
    NULL = 18
    CLASS = 19
    VAL = 20
    VAR = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    NEW = 24
    BY = 25
    WRITELN = 26
    PLUS = 27
    MINUS = 28
    STAR = 29
    DIV = 30
    MOD = 31
    NOT = 32
    ANDAND = 33
    OROR = 34
    EQ = 35
    ASSIGN = 36
    NE = 37
    GT = 38
    GE = 39
    LS = 40
    LE = 41
    STR_CMP = 42
    STR_CONCAT = 43
    DCL = 44
    SM = 45
    CM = 46
    DOT = 47
    DDOT = 48
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
    STRING_LIT = 59
    SDIGIT = 60
    WS = 61
    BLOCKCOMMENT = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
            "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'==.'", "'+.'", "'::'", "';'", "','", "'.'", "'..'", "':'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "WRITELN", "PLUS", "MINUS", "STAR", "DIV", "MOD", 
            "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", 
            "LE", "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", "DOT", "DDOT", 
            "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "SDIGIT", "WS", "BLOCKCOMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "WRITELN", 
                  "PLUS", "MINUS", "STAR", "DIV", "MOD", "NOT", "ANDAND", 
                  "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", "LE", 
                  "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", "DOT", "DDOT", 
                  "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID_normal", "ID_static", 
                  "DECIMAL", "OCTAL", "HEX", "BINARY", "DIGIT", "DIGITNONZERO", 
                  "SDIGIT", "EXPONENT", "SIGN", "ESC_SEQ", "ESC_ILLEGAL", 
                  "STR_CHAR", "WS", "BLOCKCOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            	
     


