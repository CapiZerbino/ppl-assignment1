# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u021a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\6")
        buf.write("\2v\n\2\r\2\16\2w\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\5\4\u0085\n\4\3\5\3\5\7\5\u0089\n\5\f\5\16\5")
        buf.write("\u008c\13\5\3\6\3\6\3\6\5\6\u0091\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u009d\n\b\f\b\16\b\u00a0")
        buf.write("\13\b\3\t\3\t\5\t\u00a4\n\t\3\n\3\n\3\n\5\n\u00a9\n\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b1\n\n\3\13\3\13\3\13")
        buf.write("\7\13\u00b6\n\13\f\13\16\13\u00b9\13\13\3\f\3\f\3\f\7")
        buf.write("\f\u00be\n\f\f\f\16\f\u00c1\13\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\16\7\16\u00cb\n\16\f\16\16\16\u00ce\13\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00d5\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00dc\n\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u00e4\n\21\f\21\16\21\u00e7\13\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\7\22\u00ef\n\22\f\22\16\22\u00f2\13")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00fa\n\23\f\23")
        buf.write("\16\23\u00fd\13\23\3\24\3\24\3\24\5\24\u0102\n\24\3\25")
        buf.write("\3\25\3\25\5\25\u0107\n\25\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u010e\n\26\f\26\16\26\u0111\13\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u0119\n\27\f\27\16\27\u011c\13\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0123\n\30\3\31\3\31\3\31")
        buf.write("\5\31\u0128\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u012f\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0137\n\33\3\33")
        buf.write("\3\33\3\33\3\33\7\33\u013d\n\33\f\33\16\33\u0140\13\33")
        buf.write("\3\34\3\34\3\34\5\34\u0145\n\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\7\35\u014c\n\35\f\35\16\35\u014f\13\35\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \5 \u015e\n")
        buf.write(" \3!\3!\3!\5!\u0163\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u016c")
        buf.write("\n\"\3#\3#\3#\7#\u0171\n#\f#\16#\u0174\13#\3$\3$\3$\7")
        buf.write("$\u0179\n$\f$\16$\u017c\13$\3%\3%\3%\7%\u0181\n%\f%\16")
        buf.write("%\u0184\13%\3&\3&\3&\7&\u0189\n&\f&\16&\u018c\13&\3\'")
        buf.write("\3\'\3\'\7\'\u0191\n\'\f\'\16\'\u0194\13\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3)\3)\5)\u019f\n)\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u01ad\n+\3,\3,\7,\u01b1\n,\f,\16,\u01b4")
        buf.write("\13,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01c1\n-\3.\3")
        buf.write(".\3.\3.\3.\5.\u01c8\n.\3.\3.\3/\3/\3/\3\60\3\60\3\60\7")
        buf.write("\60\u01d2\n\60\f\60\16\60\u01d5\13\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\5\62\u01de\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01e5\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\7\64\u01f2\n\64\f\64\16\64\u01f5")
        buf.write("\13\64\3\64\3\64\5\64\u01f9\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u0204\n\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\58\u0211\n8\38\3")
        buf.write("8\39\39\39\3:\3:\3:\2\b \"$*,\64;\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnpr\2\f\3\2\24\25\4\2\26\2699\3\2\r\20\3")
        buf.write("\2+,\4\2$$&*\3\2\"#\3\2\34\35\3\2\36 \3\2\65\66\3\2\t")
        buf.write("\n\2\u0222\2u\3\2\2\2\4{\3\2\2\2\6\u0081\3\2\2\2\b\u008a")
        buf.write("\3\2\2\2\n\u0090\3\2\2\2\f\u0092\3\2\2\2\16\u0099\3\2")
        buf.write("\2\2\20\u00a3\3\2\2\2\22\u00b0\3\2\2\2\24\u00b2\3\2\2")
        buf.write("\2\26\u00ba\3\2\2\2\30\u00c5\3\2\2\2\32\u00c7\3\2\2\2")
        buf.write("\34\u00d4\3\2\2\2\36\u00db\3\2\2\2 \u00dd\3\2\2\2\"\u00e8")
        buf.write("\3\2\2\2$\u00f3\3\2\2\2&\u0101\3\2\2\2(\u0106\3\2\2\2")
        buf.write("*\u0108\3\2\2\2,\u0112\3\2\2\2.\u0122\3\2\2\2\60\u0127")
        buf.write("\3\2\2\2\62\u012e\3\2\2\2\64\u0136\3\2\2\2\66\u0141\3")
        buf.write("\2\2\28\u0148\3\2\2\2:\u0150\3\2\2\2<\u0154\3\2\2\2>\u015d")
        buf.write("\3\2\2\2@\u015f\3\2\2\2B\u016b\3\2\2\2D\u016d\3\2\2\2")
        buf.write("F\u0175\3\2\2\2H\u017d\3\2\2\2J\u0185\3\2\2\2L\u018d\3")
        buf.write("\2\2\2N\u0195\3\2\2\2P\u019e\3\2\2\2R\u01a0\3\2\2\2T\u01ac")
        buf.write("\3\2\2\2V\u01ae\3\2\2\2X\u01c0\3\2\2\2Z\u01c2\3\2\2\2")
        buf.write("\\\u01cb\3\2\2\2^\u01ce\3\2\2\2`\u01d6\3\2\2\2b\u01dd")
        buf.write("\3\2\2\2d\u01e4\3\2\2\2f\u01e6\3\2\2\2h\u01fa\3\2\2\2")
        buf.write("j\u0208\3\2\2\2l\u020b\3\2\2\2n\u020e\3\2\2\2p\u0214\3")
        buf.write("\2\2\2r\u0217\3\2\2\2tv\5\4\3\2ut\3\2\2\2vw\3\2\2\2wu")
        buf.write("\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\2\2\3z\3\3\2\2\2{|\7")
        buf.write("\23\2\2|}\5\6\4\2}~\7\67\2\2~\177\5\b\5\2\177\u0080\7")
        buf.write("8\2\2\u0080\5\3\2\2\2\u0081\u0084\79\2\2\u0082\u0083\7")
        buf.write("\62\2\2\u0083\u0085\79\2\2\u0084\u0082\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\7\3\2\2\2\u0086\u0089\5\f\7\2\u0087\u0089")
        buf.write("\5\22\n\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\t\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u0091\5\30")
        buf.write("\r\2\u008e\u0091\5N(\2\u008f\u0091\79\2\2\u0090\u008d")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\13\3\2\2\2\u0092\u0093\t\2\2\2\u0093\u0094\5\16\b\2\u0094")
        buf.write("\u0095\7\62\2\2\u0095\u0096\5\n\6\2\u0096\u0097\5\20\t")
        buf.write("\2\u0097\u0098\7.\2\2\u0098\r\3\2\2\2\u0099\u009e\79\2")
        buf.write("\2\u009a\u009b\7/\2\2\u009b\u009d\79\2\2\u009c\u009a\3")
        buf.write("\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\17\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2")
        buf.write("\7%\2\2\u00a2\u00a4\5\32\16\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\21\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6")
        buf.write("\u00a8\7\63\2\2\u00a7\u00a9\5\24\13\2\u00a8\u00a7\3\2")
        buf.write("\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab")
        buf.write("\7\64\2\2\u00ab\u00b1\5V,\2\u00ac\u00ad\7\27\2\2\u00ad")
        buf.write("\u00ae\7\63\2\2\u00ae\u00af\7\64\2\2\u00af\u00b1\5V,\2")
        buf.write("\u00b0\u00a5\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b1\23\3\2")
        buf.write("\2\2\u00b2\u00b7\5\26\f\2\u00b3\u00b4\7.\2\2\u00b4\u00b6")
        buf.write("\5\26\f\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\25\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bf\79\2\2\u00bb\u00bc\7/\2\2\u00bc")
        buf.write("\u00be\79\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c1\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3")
        buf.write("\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\7\62\2\2\u00c3")
        buf.write("\u00c4\5\n\6\2\u00c4\27\3\2\2\2\u00c5\u00c6\t\4\2\2\u00c6")
        buf.write("\31\3\2\2\2\u00c7\u00cc\5\34\17\2\u00c8\u00c9\7/\2\2\u00c9")
        buf.write("\u00cb\5\34\17\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2")
        buf.write("\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\33\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\5\36\20\2\u00d0")
        buf.write("\u00d1\t\5\2\2\u00d1\u00d2\5\36\20\2\u00d2\u00d5\3\2\2")
        buf.write("\2\u00d3\u00d5\5\36\20\2\u00d4\u00cf\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\35\3\2\2\2\u00d6\u00d7\5 \21\2\u00d7\u00d8")
        buf.write("\t\6\2\2\u00d8\u00d9\5 \21\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00dc\5 \21\2\u00db\u00d6\3\2\2\2\u00db\u00da\3\2\2\2")
        buf.write("\u00dc\37\3\2\2\2\u00dd\u00de\b\21\1\2\u00de\u00df\5\"")
        buf.write("\22\2\u00df\u00e5\3\2\2\2\u00e0\u00e1\f\4\2\2\u00e1\u00e2")
        buf.write("\t\7\2\2\u00e2\u00e4\5\"\22\2\u00e3\u00e0\3\2\2\2\u00e4")
        buf.write("\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6!\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\b\22\1")
        buf.write("\2\u00e9\u00ea\5$\23\2\u00ea\u00f0\3\2\2\2\u00eb\u00ec")
        buf.write("\f\4\2\2\u00ec\u00ed\t\b\2\2\u00ed\u00ef\5$\23\2\u00ee")
        buf.write("\u00eb\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1#\3\2\2\2\u00f2\u00f0\3\2\2")
        buf.write("\2\u00f3\u00f4\b\23\1\2\u00f4\u00f5\5&\24\2\u00f5\u00fb")
        buf.write("\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7\u00f8\t\t\2\2\u00f8")
        buf.write("\u00fa\5&\24\2\u00f9\u00f6\3\2\2\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc%\3\2\2")
        buf.write("\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7!\2\2\u00ff\u0102")
        buf.write("\5&\24\2\u0100\u0102\5(\25\2\u0101\u00fe\3\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\'\3\2\2\2\u0103\u0104\7\35\2\2\u0104")
        buf.write("\u0107\5(\25\2\u0105\u0107\5*\26\2\u0106\u0103\3\2\2\2")
        buf.write("\u0106\u0105\3\2\2\2\u0107)\3\2\2\2\u0108\u0109\b\26\1")
        buf.write("\2\u0109\u010a\5,\27\2\u010a\u010f\3\2\2\2\u010b\u010c")
        buf.write("\f\4\2\2\u010c\u010e\t\n\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110+\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\b\27\1")
        buf.write("\2\u0113\u0114\5.\30\2\u0114\u011a\3\2\2\2\u0115\u0116")
        buf.write("\f\4\2\2\u0116\u0117\7\60\2\2\u0117\u0119\5.\30\2\u0118")
        buf.write("\u0115\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b-\3\2\2\2\u011c\u011a\3\2\2")
        buf.write("\2\u011d\u011e\5\60\31\2\u011e\u011f\7-\2\2\u011f\u0120")
        buf.write("\5\60\31\2\u0120\u0123\3\2\2\2\u0121\u0123\5\60\31\2\u0122")
        buf.write("\u011d\3\2\2\2\u0122\u0121\3\2\2\2\u0123/\3\2\2\2\u0124")
        buf.write("\u0125\7\30\2\2\u0125\u0128\5\60\31\2\u0126\u0128\5\62")
        buf.write("\32\2\u0127\u0124\3\2\2\2\u0127\u0126\3\2\2\2\u0128\61")
        buf.write("\3\2\2\2\u0129\u012f\5\64\33\2\u012a\u012b\7\63\2\2\u012b")
        buf.write("\u012c\5\34\17\2\u012c\u012d\7\64\2\2\u012d\u012f\3\2")
        buf.write("\2\2\u012e\u0129\3\2\2\2\u012e\u012a\3\2\2\2\u012f\63")
        buf.write("\3\2\2\2\u0130\u0131\b\33\1\2\u0131\u0137\79\2\2\u0132")
        buf.write("\u0137\5> \2\u0133\u0137\5\66\34\2\u0134\u0137\7\33\2")
        buf.write("\2\u0135\u0137\7\22\2\2\u0136\u0130\3\2\2\2\u0136\u0132")
        buf.write("\3\2\2\2\u0136\u0133\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137\u013e\3\2\2\2\u0138\u0139\f\6\2\2")
        buf.write("\u0139\u013d\5:\36\2\u013a\u013b\f\5\2\2\u013b\u013d\5")
        buf.write("<\37\2\u013c\u0138\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\65\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\79\2\2\u0142")
        buf.write("\u0144\7\63\2\2\u0143\u0145\58\35\2\u0144\u0143\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147")
        buf.write("\7\64\2\2\u0147\67\3\2\2\2\u0148\u014d\5\34\17\2\u0149")
        buf.write("\u014a\7/\2\2\u014a\u014c\5\34\17\2\u014b\u0149\3\2\2")
        buf.write("\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e9\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151")
        buf.write("\7\63\2\2\u0151\u0152\5\32\16\2\u0152\u0153\7\64\2\2\u0153")
        buf.write(";\3\2\2\2\u0154\u0155\7\65\2\2\u0155\u0156\5\34\17\2\u0156")
        buf.write("\u0157\7\66\2\2\u0157=\3\2\2\2\u0158\u015e\7;\2\2\u0159")
        buf.write("\u015e\7<\2\2\u015a\u015e\5r:\2\u015b\u015e\7=\2\2\u015c")
        buf.write("\u015e\5@!\2\u015d\u0158\3\2\2\2\u015d\u0159\3\2\2\2\u015d")
        buf.write("\u015a\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015e?\3\2\2\2\u015f\u0160\7\13\2\2\u0160\u0162\7\63")
        buf.write("\2\2\u0161\u0163\5B\"\2\u0162\u0161\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7\64\2\2\u0165")
        buf.write("A\3\2\2\2\u0166\u016c\5D#\2\u0167\u016c\5F$\2\u0168\u016c")
        buf.write("\5H%\2\u0169\u016c\5J&\2\u016a\u016c\5L\'\2\u016b\u0166")
        buf.write("\3\2\2\2\u016b\u0167\3\2\2\2\u016b\u0168\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cC\3\2\2\2\u016d")
        buf.write("\u0172\7;\2\2\u016e\u016f\7/\2\2\u016f\u0171\7;\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173E\3\2\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0175\u017a\7<\2\2\u0176\u0177\7/\2\2\u0177\u0179\7")
        buf.write("<\2\2\u0178\u0176\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017bG\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017d\u0182\5r:\2\u017e\u017f\7/\2\2\u017f\u0181")
        buf.write("\5r:\2\u0180\u017e\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183I\3\2\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0185\u018a\7=\2\2\u0186\u0187\7/\2\2\u0187\u0189")
        buf.write("\7=\2\2\u0188\u0186\3\2\2\2\u0189\u018c\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018bK\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018d\u0192\5@!\2\u018e\u018f\7/\2\2\u018f")
        buf.write("\u0191\5@!\2\u0190\u018e\3\2\2\2\u0191\u0194\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193M\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0195\u0196\7\13\2\2\u0196\u0197\7\65\2")
        buf.write("\2\u0197\u0198\5P)\2\u0198\u0199\7/\2\2\u0199\u019a\7")
        buf.write(";\2\2\u019a\u019b\7\66\2\2\u019bO\3\2\2\2\u019c\u019f")
        buf.write("\5\30\r\2\u019d\u019f\7\13\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019fQ\3\2\2\2\u01a0\u01a1\5\34\17\2\u01a1")
        buf.write("\u01a2\5T+\2\u01a2S\3\2\2\2\u01a3\u01a4\7\65\2\2\u01a4")
        buf.write("\u01a5\5\34\17\2\u01a5\u01a6\7\66\2\2\u01a6\u01ad\3\2")
        buf.write("\2\2\u01a7\u01a8\7\65\2\2\u01a8\u01a9\5\34\17\2\u01a9")
        buf.write("\u01aa\7\66\2\2\u01aa\u01ab\5T+\2\u01ab\u01ad\3\2\2\2")
        buf.write("\u01ac\u01a3\3\2\2\2\u01ac\u01a7\3\2\2\2\u01adU\3\2\2")
        buf.write("\2\u01ae\u01b2\7\67\2\2\u01af\u01b1\5X-\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b6\78\2\2\u01b6W\3\2\2\2\u01b7\u01c1\5Z.\2\u01b8")
        buf.write("\u01c1\5`\61\2\u01b9\u01c1\5f\64\2\u01ba\u01c1\5h\65\2")
        buf.write("\u01bb\u01c1\5j\66\2\u01bc\u01c1\5l\67\2\u01bd\u01c1\5")
        buf.write("n8\2\u01be\u01c1\5p9\2\u01bf\u01c1\5V,\2\u01c0\u01b7\3")
        buf.write("\2\2\2\u01c0\u01b8\3\2\2\2\u01c0\u01b9\3\2\2\2\u01c0\u01ba")
        buf.write("\3\2\2\2\u01c0\u01bb\3\2\2\2\u01c0\u01bc\3\2\2\2\u01c0")
        buf.write("\u01bd\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c1Y\3\2\2\2\u01c2\u01c3\t\2\2\2\u01c3\u01c4\5^\60")
        buf.write("\2\u01c4\u01c5\7\62\2\2\u01c5\u01c7\5\n\6\2\u01c6\u01c8")
        buf.write("\5\\/\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01ca\7.\2\2\u01ca[\3\2\2\2\u01cb")
        buf.write("\u01cc\7%\2\2\u01cc\u01cd\5\32\16\2\u01cd]\3\2\2\2\u01ce")
        buf.write("\u01d3\7:\2\2\u01cf\u01d0\7/\2\2\u01d0\u01d2\7:\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2")
        buf.write("\u01d3\u01d4\3\2\2\2\u01d4_\3\2\2\2\u01d5\u01d3\3\2\2")
        buf.write("\2\u01d6\u01d7\5b\62\2\u01d7\u01d8\7%\2\2\u01d8\u01d9")
        buf.write("\5d\63\2\u01d9\u01da\7.\2\2\u01daa\3\2\2\2\u01db\u01de")
        buf.write("\79\2\2\u01dc\u01de\5R*\2\u01dd\u01db\3\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01dec\3\2\2\2\u01df\u01e0\5b\62\2\u01e0\u01e1")
        buf.write("\7%\2\2\u01e1\u01e2\5d\63\2\u01e2\u01e5\3\2\2\2\u01e3")
        buf.write("\u01e5\5\34\17\2\u01e4\u01df\3\2\2\2\u01e4\u01e3\3\2\2")
        buf.write("\2\u01e5e\3\2\2\2\u01e6\u01e7\7\5\2\2\u01e7\u01e8\7\63")
        buf.write("\2\2\u01e8\u01e9\5\34\17\2\u01e9\u01ea\7\64\2\2\u01ea")
        buf.write("\u01f3\5V,\2\u01eb\u01ec\7\6\2\2\u01ec\u01ed\7\63\2\2")
        buf.write("\u01ed\u01ee\5\34\17\2\u01ee\u01ef\7\64\2\2\u01ef\u01f0")
        buf.write("\5V,\2\u01f0\u01f2\3\2\2\2\u01f1\u01eb\3\2\2\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f8\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\7\7\2\2")
        buf.write("\u01f7\u01f9\5V,\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2")
        buf.write("\2\2\u01f9g\3\2\2\2\u01fa\u01fb\7\b\2\2\u01fb\u01fc\7")
        buf.write("\63\2\2\u01fc\u01fd\79\2\2\u01fd\u01fe\7\f\2\2\u01fe\u01ff")
        buf.write("\7;\2\2\u01ff\u0200\7\61\2\2\u0200\u0203\7;\2\2\u0201")
        buf.write("\u0202\7\31\2\2\u0202\u0204\7;\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\7")
        buf.write("\64\2\2\u0206\u0207\5V,\2\u0207i\3\2\2\2\u0208\u0209\7")
        buf.write("\3\2\2\u0209\u020a\7.\2\2\u020ak\3\2\2\2\u020b\u020c\7")
        buf.write("\4\2\2\u020c\u020d\7.\2\2\u020dm\3\2\2\2\u020e\u0210\7")
        buf.write("\21\2\2\u020f\u0211\5\34\17\2\u0210\u020f\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\7.\2\2")
        buf.write("\u0213o\3\2\2\2\u0214\u0215\5\34\17\2\u0215\u0216\7.\2")
        buf.write("\2\u0216q\3\2\2\2\u0217\u0218\t\13\2\2\u0218s\3\2\2\2")
        buf.write("\63w\u0084\u0088\u008a\u0090\u009e\u00a3\u00a8\u00b0\u00b7")
        buf.write("\u00bf\u00cc\u00d4\u00db\u00e5\u00f0\u00fb\u0101\u0106")
        buf.write("\u010f\u011a\u0122\u0127\u012e\u0136\u013c\u013e\u0144")
        buf.write("\u014d\u015d\u0162\u016b\u0172\u017a\u0182\u018a\u0192")
        buf.write("\u019e\u01ac\u01b2\u01c0\u01c7\u01d3\u01dd\u01e4\u01f3")
        buf.write("\u01f8\u0203\u0210")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "<INVALID>", 
                     "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", 
                     "'<'", "'<='", "'==.'", "'+.'", "'::'", "';'", "','", 
                     "'.'", "'..'", "':'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "WRITELN", "SELF", "PLUS", "MINUS", "STAR", 
                      "DIV", "MOD", "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", 
                      "NE", "GT", "GE", "LS", "LE", "STR_CMP", "STR_CONCAT", 
                      "DCL", "SM", "CM", "DOT", "DDOT", "CL", "LP", "RP", 
                      "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", "IDENTIFIER_NORMAL", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "BLOCKCOMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_classname = 2
    RULE_classbody = 3
    RULE_type_decl = 4
    RULE_attribute_decl = 5
    RULE_attributename_list = 6
    RULE_attribute_init = 7
    RULE_method_decl = 8
    RULE_parameter_list = 9
    RULE_parameter = 10
    RULE_primitive_types = 11
    RULE_expression_list = 12
    RULE_expression = 13
    RULE_expr_1 = 14
    RULE_expr_2 = 15
    RULE_expr_3 = 16
    RULE_expr_4 = 17
    RULE_expr_5 = 18
    RULE_expr_6 = 19
    RULE_expr_7 = 20
    RULE_expr_8 = 21
    RULE_expr_9 = 22
    RULE_expr_10 = 23
    RULE_expr_11 = 24
    RULE_operands = 25
    RULE_call_expr = 26
    RULE_expr_list = 27
    RULE_postfix = 28
    RULE_postfix_array = 29
    RULE_literals = 30
    RULE_array_lit = 31
    RULE_array_list = 32
    RULE_arrayitemint_list = 33
    RULE_arrayitemfloat_list = 34
    RULE_arrayitembool_list = 35
    RULE_arrayitemstring_list = 36
    RULE_arrayitemarray_list = 37
    RULE_array_decl = 38
    RULE_element_type = 39
    RULE_index_expression = 40
    RULE_index_op = 41
    RULE_block_stmt = 42
    RULE_stmt_list = 43
    RULE_vardecl_stmt = 44
    RULE_var_init = 45
    RULE_varname_list = 46
    RULE_assign_stmt = 47
    RULE_assign_lhs = 48
    RULE_assign_tail = 49
    RULE_if_stmt = 50
    RULE_forin_stmt = 51
    RULE_break_stmt = 52
    RULE_continue_stmt = 53
    RULE_return_stmt = 54
    RULE_methodinvocation_stmt = 55
    RULE_bool_lit = 56

    ruleNames =  [ "program", "class_decl", "classname", "classbody", "type_decl", 
                   "attribute_decl", "attributename_list", "attribute_init", 
                   "method_decl", "parameter_list", "parameter", "primitive_types", 
                   "expression_list", "expression", "expr_1", "expr_2", 
                   "expr_3", "expr_4", "expr_5", "expr_6", "expr_7", "expr_8", 
                   "expr_9", "expr_10", "expr_11", "operands", "call_expr", 
                   "expr_list", "postfix", "postfix_array", "literals", 
                   "array_lit", "array_list", "arrayitemint_list", "arrayitemfloat_list", 
                   "arrayitembool_list", "arrayitemstring_list", "arrayitemarray_list", 
                   "array_decl", "element_type", "index_expression", "index_op", 
                   "block_stmt", "stmt_list", "vardecl_stmt", "var_init", 
                   "varname_list", "assign_stmt", "assign_lhs", "assign_tail", 
                   "if_stmt", "forin_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "methodinvocation_stmt", "bool_lit" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    TRUE=7
    FALSE=8
    ARRAY=9
    IN=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    VAL=18
    VAR=19
    CONSTRUCTOR=20
    DESTRUCTOR=21
    NEW=22
    BY=23
    WRITELN=24
    SELF=25
    PLUS=26
    MINUS=27
    STAR=28
    DIV=29
    MOD=30
    NOT=31
    ANDAND=32
    OROR=33
    EQ=34
    ASSIGN=35
    NE=36
    GT=37
    GE=38
    LS=39
    LE=40
    STR_CMP=41
    STR_CONCAT=42
    DCL=43
    SM=44
    CM=45
    DOT=46
    DDOT=47
    CL=48
    LP=49
    RP=50
    LSB=51
    RSB=52
    LCB=53
    RCB=54
    IDENTIFIER=55
    IDENTIFIER_NORMAL=56
    INT_LIT=57
    FLOAT_LIT=58
    STRING_LIT=59
    WS=60
    BLOCKCOMMENT=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.class_decl()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 119
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def classname(self):
            return self.getTypedRuleContext(D96Parser.ClassnameContext,0)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def classbody(self):
            return self.getTypedRuleContext(D96Parser.ClassbodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(D96Parser.CLASS)
            self.state = 122
            self.classname()
            self.state = 123
            self.match(D96Parser.LCB)
            self.state = 124
            self.classbody()
            self.state = 125
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassname" ):
                return visitor.visitClassname(self)
            else:
                return visitor.visitChildren(self)




    def classname(self):

        localctx = D96Parser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(D96Parser.IDENTIFIER)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 128
                self.match(D96Parser.CL)
                self.state = 129
                self.match(D96Parser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_declContext,i)


        def method_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassbody" ):
                return visitor.visitClassbody(self)
            else:
                return visitor.visitChildren(self)




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 132
                    self.attribute_decl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDENTIFIER]:
                    self.state = 133
                    self.method_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(D96Parser.Array_declContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = D96Parser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_decl)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.array_decl()
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(D96Parser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributename_list(self):
            return self.getTypedRuleContext(D96Parser.Attributename_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def type_decl(self):
            return self.getTypedRuleContext(D96Parser.Type_declContext,0)


        def attribute_init(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.attributename_list()
            self.state = 146
            self.match(D96Parser.CL)
            self.state = 147
            self.type_decl()
            self.state = 148
            self.attribute_init()
            self.state = 149
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attributename_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attributename_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributename_list" ):
                return visitor.visitAttributename_list(self)
            else:
                return visitor.visitChildren(self)




    def attributename_list(self):

        localctx = D96Parser.Attributename_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributename_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D96Parser.IDENTIFIER)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 152
                self.match(D96Parser.CM)
                self.state = 153
                self.match(D96Parser.IDENTIFIER)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_init" ):
                return visitor.visitAttribute_init(self)
            else:
                return visitor.visitChildren(self)




    def attribute_init(self):

        localctx = D96Parser.Attribute_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 159
                self.match(D96Parser.ASSIGN)
                self.state = 160
                self.expression_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                _la = self._input.LA(1)
                if not(_la==D96Parser.CONSTRUCTOR or _la==D96Parser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.match(D96Parser.LP)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 165
                    self.parameter_list()


                self.state = 168
                self.match(D96Parser.RP)
                self.state = 169
                self.block_stmt()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(D96Parser.DESTRUCTOR)
                self.state = 171
                self.match(D96Parser.LP)
                self.state = 172
                self.match(D96Parser.RP)
                self.state = 173
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParameterContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SM)
            else:
                return self.getToken(D96Parser.SM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.parameter()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 177
                self.match(D96Parser.SM)
                self.state = 178
                self.parameter()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def type_decl(self):
            return self.getTypedRuleContext(D96Parser.Type_declContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D96Parser.IDENTIFIER)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 185
                self.match(D96Parser.CM)
                self.state = 186
                self.match(D96Parser.IDENTIFIER)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(D96Parser.CL)
            self.state = 193
            self.type_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_types" ):
                return visitor.visitPrimitive_types(self)
            else:
                return visitor.visitChildren(self)




    def primitive_types(self):

        localctx = D96Parser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = D96Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expression()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 198
                self.match(D96Parser.CM)
                self.state = 199
                self.expression()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_1Context,i)


        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def STR_CMP(self):
            return self.getToken(D96Parser.STR_CMP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.expr_1()
                self.state = 206
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 207
                self.expr_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.expr_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NE(self):
            return self.getToken(D96Parser.NE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_1" ):
                return visitor.visitExpr_1(self)
            else:
                return visitor.visitChildren(self)




    def expr_1(self):

        localctx = D96Parser.Expr_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_1)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.expr_2(0)
                self.state = 213
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GE) | (1 << D96Parser.LS) | (1 << D96Parser.LE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.expr_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.expr_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_3(self):
            return self.getTypedRuleContext(D96Parser.Expr_3Context,0)


        def expr_2(self):
            return self.getTypedRuleContext(D96Parser.Expr_2Context,0)


        def ANDAND(self):
            return self.getToken(D96Parser.ANDAND, 0)

        def OROR(self):
            return self.getToken(D96Parser.OROR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_2" ):
                return visitor.visitExpr_2(self)
            else:
                return visitor.visitChildren(self)



    def expr_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.expr_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_2)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDAND or _la==D96Parser.OROR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 224
                    self.expr_3(0) 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_4(self):
            return self.getTypedRuleContext(D96Parser.Expr_4Context,0)


        def expr_3(self):
            return self.getTypedRuleContext(D96Parser.Expr_3Context,0)


        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_3" ):
                return visitor.visitExpr_3(self)
            else:
                return visitor.visitChildren(self)



    def expr_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.expr_4(0) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_5(self):
            return self.getTypedRuleContext(D96Parser.Expr_5Context,0)


        def expr_4(self):
            return self.getTypedRuleContext(D96Parser.Expr_4Context,0)


        def STAR(self):
            return self.getToken(D96Parser.STAR, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_4" ):
                return visitor.visitExpr_4(self)
            else:
                return visitor.visitChildren(self)



    def expr_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.STAR) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    self.expr_5() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr_5(self):
            return self.getTypedRuleContext(D96Parser.Expr_5Context,0)


        def expr_6(self):
            return self.getTypedRuleContext(D96Parser.Expr_6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_5" ):
                return visitor.visitExpr_5(self)
            else:
                return visitor.visitChildren(self)




    def expr_5(self):

        localctx = D96Parser.Expr_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr_5)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(D96Parser.NOT)
                self.state = 253
                self.expr_5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.LP, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.expr_6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def expr_6(self):
            return self.getTypedRuleContext(D96Parser.Expr_6Context,0)


        def expr_7(self):
            return self.getTypedRuleContext(D96Parser.Expr_7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_6" ):
                return visitor.visitExpr_6(self)
            else:
                return visitor.visitChildren(self)




    def expr_6(self):

        localctx = D96Parser.Expr_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_6)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(D96Parser.MINUS)
                self.state = 258
                self.expr_6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.expr_7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_8(self):
            return self.getTypedRuleContext(D96Parser.Expr_8Context,0)


        def expr_7(self):
            return self.getTypedRuleContext(D96Parser.Expr_7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_7" ):
                return visitor.visitExpr_7(self)
            else:
                return visitor.visitChildren(self)



    def expr_7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expr_8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_7)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LSB or _la==D96Parser.RSB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_9(self):
            return self.getTypedRuleContext(D96Parser.Expr_9Context,0)


        def expr_8(self):
            return self.getTypedRuleContext(D96Parser.Expr_8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_8" ):
                return visitor.visitExpr_8(self)
            else:
                return visitor.visitChildren(self)



    def expr_8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr_8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr_9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_8)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    self.match(D96Parser.DOT)
                    self.state = 277
                    self.expr_9() 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_10(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_10Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_10Context,i)


        def DCL(self):
            return self.getToken(D96Parser.DCL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_9" ):
                return visitor.visitExpr_9(self)
            else:
                return visitor.visitChildren(self)




    def expr_9(self):

        localctx = D96Parser.Expr_9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_9)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.expr_10()
                self.state = 284
                self.match(D96Parser.DCL)
                self.state = 285
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.expr_10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr_10(self):
            return self.getTypedRuleContext(D96Parser.Expr_10Context,0)


        def expr_11(self):
            return self.getTypedRuleContext(D96Parser.Expr_11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_10" ):
                return visitor.visitExpr_10(self)
            else:
                return visitor.visitChildren(self)




    def expr_10(self):

        localctx = D96Parser.Expr_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_10)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(D96Parser.NEW)
                self.state = 291
                self.expr_10()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.expr_11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_11" ):
                return visitor.visitExpr_11(self)
            else:
                return visitor.visitChildren(self)




    def expr_11(self):

        localctx = D96Parser.Expr_11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_11)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.operands(0)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(D96Parser.LP)
                self.state = 297
                self.expression()
                self.state = 298
                self.match(D96Parser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(D96Parser.Call_exprContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def postfix(self):
            return self.getTypedRuleContext(D96Parser.PostfixContext,0)


        def postfix_array(self):
            return self.getTypedRuleContext(D96Parser.Postfix_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)



    def operands(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.OperandsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_operands, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 303
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 304
                self.literals()
                pass

            elif la_ == 3:
                self.state = 305
                self.call_expr()
                pass

            elif la_ == 4:
                self.state = 306
                self.match(D96Parser.SELF)
                pass

            elif la_ == 5:
                self.state = 307
                self.match(D96Parser.NULL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 314
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 310
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 311
                        self.postfix()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 312
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 313
                        self.postfix_array()
                        pass

             
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = D96Parser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.IDENTIFIER)
            self.state = 320
            self.match(D96Parser.LP)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 321
                self.expr_list()


            self.state = 324
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expression()
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 327
                self.match(D96Parser.CM)
                self.state = 328
                self.expression()
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_postfix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)




    def postfix(self):

        localctx = D96Parser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_postfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(D96Parser.LP)
            self.state = 335
            self.expression_list()
            self.state = 336
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_postfix_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_array" ):
                return visitor.visitPostfix_array(self)
            else:
                return visitor.visitChildren(self)




    def postfix_array(self):

        localctx = D96Parser.Postfix_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_postfix_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(D96Parser.LSB)
            self.state = 339
            self.expression()
            self.state = 340
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(D96Parser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(D96Parser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(D96Parser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literals)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
                self.bool_lit()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 345
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 346
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(D96Parser.ARRAY)
            self.state = 350
            self.match(D96Parser.LP)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 351
                self.array_list()


            self.state = 354
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayitemint_list(self):
            return self.getTypedRuleContext(D96Parser.Arrayitemint_listContext,0)


        def arrayitemfloat_list(self):
            return self.getTypedRuleContext(D96Parser.Arrayitemfloat_listContext,0)


        def arrayitembool_list(self):
            return self.getTypedRuleContext(D96Parser.Arrayitembool_listContext,0)


        def arrayitemstring_list(self):
            return self.getTypedRuleContext(D96Parser.Arrayitemstring_listContext,0)


        def arrayitemarray_list(self):
            return self.getTypedRuleContext(D96Parser.Arrayitemarray_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_list)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.arrayitemint_list()
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.arrayitemfloat_list()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.arrayitembool_list()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.arrayitemstring_list()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 360
                self.arrayitemarray_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrayitemint_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INT_LIT)
            else:
                return self.getToken(D96Parser.INT_LIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitemint_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayitemint_list" ):
                return visitor.visitArrayitemint_list(self)
            else:
                return visitor.visitChildren(self)




    def arrayitemint_list(self):

        localctx = D96Parser.Arrayitemint_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayitemint_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(D96Parser.INT_LIT)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 364
                self.match(D96Parser.CM)
                self.state = 365
                self.match(D96Parser.INT_LIT)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrayitemfloat_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.FLOAT_LIT)
            else:
                return self.getToken(D96Parser.FLOAT_LIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitemfloat_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayitemfloat_list" ):
                return visitor.visitArrayitemfloat_list(self)
            else:
                return visitor.visitChildren(self)




    def arrayitemfloat_list(self):

        localctx = D96Parser.Arrayitemfloat_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arrayitemfloat_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(D96Parser.FLOAT_LIT)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 372
                self.match(D96Parser.CM)
                self.state = 373
                self.match(D96Parser.FLOAT_LIT)
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrayitembool_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Bool_litContext)
            else:
                return self.getTypedRuleContext(D96Parser.Bool_litContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitembool_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayitembool_list" ):
                return visitor.visitArrayitembool_list(self)
            else:
                return visitor.visitChildren(self)




    def arrayitembool_list(self):

        localctx = D96Parser.Arrayitembool_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrayitembool_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.bool_lit()
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 380
                self.match(D96Parser.CM)
                self.state = 381
                self.bool_lit()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrayitemstring_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STRING_LIT)
            else:
                return self.getToken(D96Parser.STRING_LIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitemstring_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayitemstring_list" ):
                return visitor.visitArrayitemstring_list(self)
            else:
                return visitor.visitChildren(self)




    def arrayitemstring_list(self):

        localctx = D96Parser.Arrayitemstring_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayitemstring_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.STRING_LIT)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 388
                self.match(D96Parser.CM)
                self.state = 389
                self.match(D96Parser.STRING_LIT)
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrayitemarray_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_litContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_litContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitemarray_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayitemarray_list" ):
                return visitor.visitArrayitemarray_list(self)
            else:
                return visitor.visitChildren(self)




    def arrayitemarray_list(self):

        localctx = D96Parser.Arrayitemarray_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arrayitemarray_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.array_lit()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 396
                self.match(D96Parser.CM)
                self.state = 397
                self.array_lit()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def element_type(self):
            return self.getTypedRuleContext(D96Parser.Element_typeContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = D96Parser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(D96Parser.ARRAY)
            self.state = 404
            self.match(D96Parser.LSB)
            self.state = 405
            self.element_type()
            self.state = 406
            self.match(D96Parser.CM)
            self.state = 407
            self.match(D96Parser.INT_LIT)
            self.state = 408
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = D96Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_element_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 410
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 411
                self.match(D96Parser.ARRAY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = D96Parser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expression()
            self.state = 415
            self.index_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = D96Parser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_index_op)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(D96Parser.LSB)
                self.state = 418
                self.expression()
                self.state = 419
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(D96Parser.LSB)
                self.state = 422
                self.expression()
                self.state = 423
                self.match(D96Parser.RSB)
                self.state = 424
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_listContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.LCB)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.LCB) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 429
                self.stmt_list()
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl_stmt(self):
            return self.getTypedRuleContext(D96Parser.Vardecl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def forin_stmt(self):
            return self.getTypedRuleContext(D96Parser.Forin_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def methodinvocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Methodinvocation_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_list)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.vardecl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 440
                self.forin_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 442
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 443
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 444
                self.methodinvocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 445
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varname_list(self):
            return self.getTypedRuleContext(D96Parser.Varname_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def type_decl(self):
            return self.getTypedRuleContext(D96Parser.Type_declContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def var_init(self):
            return self.getTypedRuleContext(D96Parser.Var_initContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_vardecl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_stmt" ):
                return visitor.visitVardecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_stmt(self):

        localctx = D96Parser.Vardecl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_vardecl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 449
            self.varname_list()
            self.state = 450
            self.match(D96Parser.CL)
            self.state = 451
            self.type_decl()
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 452
                self.var_init()


            self.state = 455
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = D96Parser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(D96Parser.ASSIGN)
            self.state = 458
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER_NORMAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER_NORMAL)
            else:
                return self.getToken(D96Parser.IDENTIFIER_NORMAL, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_varname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarname_list" ):
                return visitor.visitVarname_list(self)
            else:
                return visitor.visitChildren(self)




    def varname_list(self):

        localctx = D96Parser.Varname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_varname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(D96Parser.IDENTIFIER_NORMAL)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 461
                self.match(D96Parser.CM)
                self.state = 462
                self.match(D96Parser.IDENTIFIER_NORMAL)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def assign_tail(self):
            return self.getTypedRuleContext(D96Parser.Assign_tailContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.assign_lhs()
            self.state = 469
            self.match(D96Parser.ASSIGN)
            self.state = 470
            self.assign_tail()
            self.state = 471
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assign_lhs)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.index_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def assign_tail(self):
            return self.getTypedRuleContext(D96Parser.Assign_tailContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_tail" ):
                return visitor.visitAssign_tail(self)
            else:
                return visitor.visitChildren(self)




    def assign_tail(self):

        localctx = D96Parser.Assign_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assign_tail)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.assign_lhs()
                self.state = 478
                self.match(D96Parser.ASSIGN)
                self.state = 479
                self.assign_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(D96Parser.IF)
            self.state = 485
            self.match(D96Parser.LP)
            self.state = 486
            self.expression()
            self.state = 487
            self.match(D96Parser.RP)
            self.state = 488
            self.block_stmt()
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 489
                self.match(D96Parser.ELSEIF)
                self.state = 490
                self.match(D96Parser.LP)
                self.state = 491
                self.expression()
                self.state = 492
                self.match(D96Parser.RP)
                self.state = 493
                self.block_stmt()
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 500
                self.match(D96Parser.ELSE)
                self.state = 501
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INT_LIT)
            else:
                return self.getToken(D96Parser.INT_LIT, i)

        def DDOT(self):
            return self.getToken(D96Parser.DDOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forin_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin_stmt" ):
                return visitor.visitForin_stmt(self)
            else:
                return visitor.visitChildren(self)




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(D96Parser.FOREACH)
            self.state = 505
            self.match(D96Parser.LP)
            self.state = 506
            self.match(D96Parser.IDENTIFIER)
            self.state = 507
            self.match(D96Parser.IN)
            self.state = 508
            self.match(D96Parser.INT_LIT)
            self.state = 509
            self.match(D96Parser.DDOT)
            self.state = 510
            self.match(D96Parser.INT_LIT)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 511
                self.match(D96Parser.BY)
                self.state = 512
                self.match(D96Parser.INT_LIT)


            self.state = 515
            self.match(D96Parser.RP)
            self.state = 516
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(D96Parser.BREAK)
            self.state = 519
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(D96Parser.CONTINUE)
            self.state = 522
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(D96Parser.RETURN)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 525
                self.expression()


            self.state = 528
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methodinvocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodinvocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocation_stmt" ):
                return visitor.visitMethodinvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocation_stmt(self):

        localctx = D96Parser.Methodinvocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_methodinvocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.expression()
            self.state = 531
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = D96Parser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_2_sempred
        self._predicates[16] = self.expr_3_sempred
        self._predicates[17] = self.expr_4_sempred
        self._predicates[20] = self.expr_7_sempred
        self._predicates[21] = self.expr_8_sempred
        self._predicates[25] = self.operands_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_2_sempred(self, localctx:Expr_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_3_sempred(self, localctx:Expr_3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_4_sempred(self, localctx:Expr_4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_7_sempred(self, localctx:Expr_7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_8_sempred(self, localctx:Expr_8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def operands_sempred(self, localctx:OperandsContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




