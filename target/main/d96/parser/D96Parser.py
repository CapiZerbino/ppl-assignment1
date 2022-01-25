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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0221\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\5\6\u0090\n\6\3\7\3\7\7\7\u0094\n\7\f\7\16\7\u0097")
        buf.write("\13\7\3\b\3\b\3\b\3\b\3\b\5\b\u009e\n\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\7\t\u00a6\n\t\f\t\16\t\u00a9\13\t\3\n\3\n\5")
        buf.write("\n\u00ad\n\n\3\13\3\13\3\13\5\13\u00b2\n\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00ba\n\13\3\f\3\f\3\f\7\f\u00bf")
        buf.write("\n\f\f\f\16\f\u00c2\13\f\3\r\3\r\3\r\7\r\u00c7\n\r\f\r")
        buf.write("\16\r\u00ca\13\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\7\17\u00d4\n\17\f\17\16\17\u00d7\13\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\7\20\u00df\n\20\f\20\16\20\u00e2\13\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00ea\n\21\f\21\16")
        buf.write("\21\u00ed\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00f5")
        buf.write("\n\22\f\22\16\22\u00f8\13\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u0100\n\23\f\23\16\23\u0103\13\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u010b\n\24\f\24\16\24\u010e")
        buf.write("\13\24\3\25\3\25\3\25\5\25\u0113\n\25\3\26\3\26\3\26\5")
        buf.write("\26\u0118\n\26\3\27\3\27\3\27\3\27\3\27\7\27\u011f\n\27")
        buf.write("\f\27\16\27\u0122\13\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u012a\n\30\f\30\16\30\u012d\13\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\7\31\u0135\n\31\f\31\16\31\u0138\13\31")
        buf.write("\3\32\3\32\3\32\5\32\u013d\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0144\n\33\3\34\3\34\3\34\5\34\u0149\n\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\7\35\u0150\n\35\f\35\16\35\u0153")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\5\36\u015a\n\36\3\37\3")
        buf.write("\37\3\37\5\37\u015f\n\37\3\37\3\37\3 \3 \3 \3 \3 \5 \u0168")
        buf.write("\n \3!\3!\3!\7!\u016d\n!\f!\16!\u0170\13!\3\"\3\"\3\"")
        buf.write("\7\"\u0175\n\"\f\"\16\"\u0178\13\"\3#\3#\3#\7#\u017d\n")
        buf.write("#\f#\16#\u0180\13#\3$\3$\3$\7$\u0185\n$\f$\16$\u0188\13")
        buf.write("$\3%\3%\3%\7%\u018d\n%\f%\16%\u0190\13%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\5\'\u019b\n\'\3(\3(\3(\3(\5(\u01a1\n(")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01b2")
        buf.write("\n*\3+\3+\7+\u01b6\n+\f+\16+\u01b9\13+\3+\3+\3,\3,\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\5,\u01c6\n,\3-\3-\3-\3-\3-\5-\u01cd")
        buf.write("\n-\3-\5-\u01d0\n-\3-\3-\3.\3.\3.\3/\3/\3/\7/\u01da\n")
        buf.write("/\f/\16/\u01dd\13/\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\5\61\u01e6\n\61\3\62\3\62\3\62\3\62\3\62\5\62\u01ed\n")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\7\63\u01fa\n\63\f\63\16\63\u01fd\13\63\3\63\3\63")
        buf.write("\5\63\u0201\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u020c\n\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\5\67\u0219\n\67\3\67\3\67\3")
        buf.write("8\38\39\39\39\2\n\36 \"$&,.\60:\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnp\2\f\3\2\26\27\4\2\30\30::\3\2\17\22\3\2")
        buf.write(",-\4\2%%\'+\3\2#$\3\2\35\36\3\2\37!\3\2\66\67\3\2\13\f")
        buf.write("\2\u0228\2u\3\2\2\2\4{\3\2\2\2\6\u0081\3\2\2\2\b\u0086")
        buf.write("\3\2\2\2\n\u008c\3\2\2\2\f\u0095\3\2\2\2\16\u0098\3\2")
        buf.write("\2\2\20\u00a2\3\2\2\2\22\u00ac\3\2\2\2\24\u00b9\3\2\2")
        buf.write("\2\26\u00bb\3\2\2\2\30\u00c3\3\2\2\2\32\u00ce\3\2\2\2")
        buf.write("\34\u00d0\3\2\2\2\36\u00d8\3\2\2\2 \u00e3\3\2\2\2\"\u00ee")
        buf.write("\3\2\2\2$\u00f9\3\2\2\2&\u0104\3\2\2\2(\u0112\3\2\2\2")
        buf.write("*\u0117\3\2\2\2,\u0119\3\2\2\2.\u0123\3\2\2\2\60\u012e")
        buf.write("\3\2\2\2\62\u013c\3\2\2\2\64\u0143\3\2\2\2\66\u0145\3")
        buf.write("\2\2\28\u014c\3\2\2\2:\u0159\3\2\2\2<\u015b\3\2\2\2>\u0167")
        buf.write("\3\2\2\2@\u0169\3\2\2\2B\u0171\3\2\2\2D\u0179\3\2\2\2")
        buf.write("F\u0181\3\2\2\2H\u0189\3\2\2\2J\u0191\3\2\2\2L\u019a\3")
        buf.write("\2\2\2N\u019c\3\2\2\2P\u01a5\3\2\2\2R\u01b1\3\2\2\2T\u01b3")
        buf.write("\3\2\2\2V\u01c5\3\2\2\2X\u01c7\3\2\2\2Z\u01d3\3\2\2\2")
        buf.write("\\\u01d6\3\2\2\2^\u01de\3\2\2\2`\u01e5\3\2\2\2b\u01ec")
        buf.write("\3\2\2\2d\u01ee\3\2\2\2f\u0202\3\2\2\2h\u0210\3\2\2\2")
        buf.write("j\u0213\3\2\2\2l\u0216\3\2\2\2n\u021c\3\2\2\2p\u021e\3")
        buf.write("\2\2\2rt\5\b\5\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2")
        buf.write("\2vx\3\2\2\2wu\3\2\2\2xy\5\4\3\2yz\7\2\2\3z\3\3\2\2\2")
        buf.write("{|\7\25\2\2|}\7\3\2\2}~\78\2\2~\177\5\6\4\2\177\u0080")
        buf.write("\79\2\2\u0080\5\3\2\2\2\u0081\u0082\7\4\2\2\u0082\u0083")
        buf.write("\7\64\2\2\u0083\u0084\7\65\2\2\u0084\u0085\5T+\2\u0085")
        buf.write("\7\3\2\2\2\u0086\u0087\7\25\2\2\u0087\u0088\5\n\6\2\u0088")
        buf.write("\u0089\78\2\2\u0089\u008a\5\f\7\2\u008a\u008b\79\2\2\u008b")
        buf.write("\t\3\2\2\2\u008c\u008f\7:\2\2\u008d\u008e\7\63\2\2\u008e")
        buf.write("\u0090\7:\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\13\3\2\2\2\u0091\u0094\5\16\b\2\u0092\u0094\5\24")
        buf.write("\13\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\r\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\t\2\2\2\u0099")
        buf.write("\u009a\5\20\t\2\u009a\u009d\7\63\2\2\u009b\u009e\5\32")
        buf.write("\16\2\u009c\u009e\5J&\2\u009d\u009b\3\2\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\5\22\n\2\u00a0")
        buf.write("\u00a1\7/\2\2\u00a1\17\3\2\2\2\u00a2\u00a7\7:\2\2\u00a3")
        buf.write("\u00a4\7\60\2\2\u00a4\u00a6\7:\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3")
        buf.write("\2\2\2\u00a8\21\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab")
        buf.write("\7&\2\2\u00ab\u00ad\5\34\17\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\23\3\2\2\2\u00ae\u00af\t\3\2\2\u00af")
        buf.write("\u00b1\7\64\2\2\u00b0\u00b2\5\26\f\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\7\65\2\2\u00b4\u00ba\5T+\2\u00b5\u00b6\7\31\2\2\u00b6")
        buf.write("\u00b7\7\64\2\2\u00b7\u00b8\7\65\2\2\u00b8\u00ba\5T+\2")
        buf.write("\u00b9\u00ae\3\2\2\2\u00b9\u00b5\3\2\2\2\u00ba\25\3\2")
        buf.write("\2\2\u00bb\u00c0\5\30\r\2\u00bc\u00bd\7/\2\2\u00bd\u00bf")
        buf.write("\5\30\r\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\27\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c8\7:\2\2\u00c4\u00c5\7\60\2\2")
        buf.write("\u00c5\u00c7\7:\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00ca\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb")
        buf.write("\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cc\7\63\2\2\u00cc")
        buf.write("\u00cd\5\32\16\2\u00cd\31\3\2\2\2\u00ce\u00cf\t\4\2\2")
        buf.write("\u00cf\33\3\2\2\2\u00d0\u00d5\5\36\20\2\u00d1\u00d2\7")
        buf.write("\60\2\2\u00d2\u00d4\5\36\20\2\u00d3\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\35\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\b\20")
        buf.write("\1\2\u00d9\u00da\5 \21\2\u00da\u00e0\3\2\2\2\u00db\u00dc")
        buf.write("\f\4\2\2\u00dc\u00dd\t\5\2\2\u00dd\u00df\5\36\20\5\u00de")
        buf.write("\u00db\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\37\3\2\2\2\u00e2\u00e0\3\2")
        buf.write("\2\2\u00e3\u00e4\b\21\1\2\u00e4\u00e5\5\"\22\2\u00e5\u00eb")
        buf.write("\3\2\2\2\u00e6\u00e7\f\4\2\2\u00e7\u00e8\t\6\2\2\u00e8")
        buf.write("\u00ea\5 \21\5\u00e9\u00e6\3\2\2\2\u00ea\u00ed\3\2\2\2")
        buf.write("\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec!\3\2\2")
        buf.write("\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\b\22\1\2\u00ef\u00f0")
        buf.write("\5$\23\2\u00f0\u00f6\3\2\2\2\u00f1\u00f2\f\4\2\2\u00f2")
        buf.write("\u00f3\t\7\2\2\u00f3\u00f5\5$\23\2\u00f4\u00f1\3\2\2\2")
        buf.write("\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7#\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa")
        buf.write("\b\23\1\2\u00fa\u00fb\5&\24\2\u00fb\u0101\3\2\2\2\u00fc")
        buf.write("\u00fd\f\4\2\2\u00fd\u00fe\t\b\2\2\u00fe\u0100\5&\24\2")
        buf.write("\u00ff\u00fc\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0101\u0102\3\2\2\2\u0102%\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0104\u0105\b\24\1\2\u0105\u0106\5(\25\2\u0106")
        buf.write("\u010c\3\2\2\2\u0107\u0108\f\4\2\2\u0108\u0109\t\t\2\2")
        buf.write("\u0109\u010b\5(\25\2\u010a\u0107\3\2\2\2\u010b\u010e\3")
        buf.write("\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\'")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7\"\2\2\u0110")
        buf.write("\u0113\5(\25\2\u0111\u0113\5*\26\2\u0112\u010f\3\2\2\2")
        buf.write("\u0112\u0111\3\2\2\2\u0113)\3\2\2\2\u0114\u0115\7\36\2")
        buf.write("\2\u0115\u0118\5*\26\2\u0116\u0118\5,\27\2\u0117\u0114")
        buf.write("\3\2\2\2\u0117\u0116\3\2\2\2\u0118+\3\2\2\2\u0119\u011a")
        buf.write("\b\27\1\2\u011a\u011b\5.\30\2\u011b\u0120\3\2\2\2\u011c")
        buf.write("\u011d\f\4\2\2\u011d\u011f\t\n\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3")
        buf.write("\2\2\2\u0121-\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124")
        buf.write("\b\30\1\2\u0124\u0125\5\60\31\2\u0125\u012b\3\2\2\2\u0126")
        buf.write("\u0127\f\4\2\2\u0127\u0128\7\61\2\2\u0128\u012a\5\60\31")
        buf.write("\2\u0129\u0126\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c/\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u012f\b\31\1\2\u012f\u0130\5\62\32\2\u0130")
        buf.write("\u0136\3\2\2\2\u0131\u0132\f\4\2\2\u0132\u0133\7.\2\2")
        buf.write("\u0133\u0135\5\60\31\5\u0134\u0131\3\2\2\2\u0135\u0138")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\61\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\7\32\2\2\u013a")
        buf.write("\u013d\5\62\32\2\u013b\u013d\5\64\33\2\u013c\u0139\3\2")
        buf.write("\2\2\u013c\u013b\3\2\2\2\u013d\63\3\2\2\2\u013e\u0144")
        buf.write("\7:\2\2\u013f\u0144\5:\36\2\u0140\u0144\5\66\34\2\u0141")
        buf.write("\u0144\5N(\2\u0142\u0144\5R*\2\u0143\u013e\3\2\2\2\u0143")
        buf.write("\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0142\3\2\2\2\u0144\65\3\2\2\2\u0145\u0146\7:\2")
        buf.write("\2\u0146\u0148\7\64\2\2\u0147\u0149\58\35\2\u0148\u0147")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\7\65\2\2\u014b\67\3\2\2\2\u014c\u0151\5\36\20\2")
        buf.write("\u014d\u014e\7\60\2\2\u014e\u0150\5\36\20\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u01529\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u015a\7;\2\2\u0155\u015a\7<\2\2\u0156\u015a\5p9\2\u0157")
        buf.write("\u015a\7=\2\2\u0158\u015a\5<\37\2\u0159\u0154\3\2\2\2")
        buf.write("\u0159\u0155\3\2\2\2\u0159\u0156\3\2\2\2\u0159\u0157\3")
        buf.write("\2\2\2\u0159\u0158\3\2\2\2\u015a;\3\2\2\2\u015b\u015c")
        buf.write("\7\r\2\2\u015c\u015e\7\64\2\2\u015d\u015f\5> \2\u015e")
        buf.write("\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0161\7\65\2\2\u0161=\3\2\2\2\u0162\u0168\5@!\2")
        buf.write("\u0163\u0168\5B\"\2\u0164\u0168\5D#\2\u0165\u0168\5F$")
        buf.write("\2\u0166\u0168\5H%\2\u0167\u0162\3\2\2\2\u0167\u0163\3")
        buf.write("\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168?\3\2\2\2\u0169\u016e\7;\2\2\u016a\u016b")
        buf.write("\7\60\2\2\u016b\u016d\7;\2\2\u016c\u016a\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016fA\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0176\7<\2\2")
        buf.write("\u0172\u0173\7\60\2\2\u0173\u0175\7<\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177C\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017e")
        buf.write("\5p9\2\u017a\u017b\7\60\2\2\u017b\u017d\5p9\2\u017c\u017a")
        buf.write("\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017fE\3\2\2\2\u0180\u017e\3\2\2\2\u0181")
        buf.write("\u0186\7=\2\2\u0182\u0183\7\60\2\2\u0183\u0185\7=\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187G\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0189\u018e\5<\37\2\u018a\u018b\7\60\2\2\u018b")
        buf.write("\u018d\5<\37\2\u018c\u018a\3\2\2\2\u018d\u0190\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018fI\3\2\2")
        buf.write("\2\u0190\u018e\3\2\2\2\u0191\u0192\7\r\2\2\u0192\u0193")
        buf.write("\7\66\2\2\u0193\u0194\5L\'\2\u0194\u0195\7\60\2\2\u0195")
        buf.write("\u0196\7;\2\2\u0196\u0197\7\67\2\2\u0197K\3\2\2\2\u0198")
        buf.write("\u019b\5\32\16\2\u0199\u019b\7\r\2\2\u019a\u0198\3\2\2")
        buf.write("\2\u019a\u0199\3\2\2\2\u019bM\3\2\2\2\u019c\u019d\7\32")
        buf.write("\2\2\u019d\u019e\7:\2\2\u019e\u01a0\7\64\2\2\u019f\u01a1")
        buf.write("\5\34\17\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\7\65\2\2\u01a3\u01a4\7/\2\2")
        buf.write("\u01a4O\3\2\2\2\u01a5\u01a6\5\36\20\2\u01a6\u01a7\5R*")
        buf.write("\2\u01a7Q\3\2\2\2\u01a8\u01a9\7\66\2\2\u01a9\u01aa\5\36")
        buf.write("\20\2\u01aa\u01ab\7\67\2\2\u01ab\u01b2\3\2\2\2\u01ac\u01ad")
        buf.write("\7\66\2\2\u01ad\u01ae\5\36\20\2\u01ae\u01af\7\67\2\2\u01af")
        buf.write("\u01b0\5R*\2\u01b0\u01b2\3\2\2\2\u01b1\u01a8\3\2\2\2\u01b1")
        buf.write("\u01ac\3\2\2\2\u01b2S\3\2\2\2\u01b3\u01b7\78\2\2\u01b4")
        buf.write("\u01b6\5V,\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01ba\u01bb\79\2\2\u01bbU\3\2\2\2")
        buf.write("\u01bc\u01c6\5X-\2\u01bd\u01c6\5^\60\2\u01be\u01c6\5d")
        buf.write("\63\2\u01bf\u01c6\5f\64\2\u01c0\u01c6\5h\65\2\u01c1\u01c6")
        buf.write("\5j\66\2\u01c2\u01c6\5l\67\2\u01c3\u01c6\5n8\2\u01c4\u01c6")
        buf.write("\5T+\2\u01c5\u01bc\3\2\2\2\u01c5\u01bd\3\2\2\2\u01c5\u01be")
        buf.write("\3\2\2\2\u01c5\u01bf\3\2\2\2\u01c5\u01c0\3\2\2\2\u01c5")
        buf.write("\u01c1\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c4\3\2\2\2\u01c6W\3\2\2\2\u01c7\u01c8\t\2\2")
        buf.write("\2\u01c8\u01c9\5\\/\2\u01c9\u01cc\7\63\2\2\u01ca\u01cd")
        buf.write("\5\32\16\2\u01cb\u01cd\5J&\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01d0\5Z.\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\7/\2\2\u01d2Y\3\2\2\2\u01d3\u01d4\7&\2\2")
        buf.write("\u01d4\u01d5\5\34\17\2\u01d5[\3\2\2\2\u01d6\u01db\7:\2")
        buf.write("\2\u01d7\u01d8\7\60\2\2\u01d8\u01da\7:\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc]\3\2\2\2\u01dd\u01db\3\2\2\2\u01de")
        buf.write("\u01df\5`\61\2\u01df\u01e0\7&\2\2\u01e0\u01e1\5b\62\2")
        buf.write("\u01e1\u01e2\7/\2\2\u01e2_\3\2\2\2\u01e3\u01e6\7:\2\2")
        buf.write("\u01e4\u01e6\5P)\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3\2")
        buf.write("\2\2\u01e6a\3\2\2\2\u01e7\u01e8\5`\61\2\u01e8\u01e9\7")
        buf.write("&\2\2\u01e9\u01ea\5b\62\2\u01ea\u01ed\3\2\2\2\u01eb\u01ed")
        buf.write("\5\36\20\2\u01ec\u01e7\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("c\3\2\2\2\u01ee\u01ef\7\7\2\2\u01ef\u01f0\7\64\2\2\u01f0")
        buf.write("\u01f1\5\36\20\2\u01f1\u01f2\7\65\2\2\u01f2\u01fb\5T+")
        buf.write("\2\u01f3\u01f4\7\b\2\2\u01f4\u01f5\7\64\2\2\u01f5\u01f6")
        buf.write("\5\36\20\2\u01f6\u01f7\7\65\2\2\u01f7\u01f8\5T+\2\u01f8")
        buf.write("\u01fa\3\2\2\2\u01f9\u01f3\3\2\2\2\u01fa\u01fd\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u0200\3")
        buf.write("\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\7\t\2\2\u01ff\u0201")
        buf.write("\5T+\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201e")
        buf.write("\3\2\2\2\u0202\u0203\7\n\2\2\u0203\u0204\7\64\2\2\u0204")
        buf.write("\u0205\7:\2\2\u0205\u0206\7\16\2\2\u0206\u0207\7;\2\2")
        buf.write("\u0207\u0208\7\62\2\2\u0208\u020b\7;\2\2\u0209\u020a\7")
        buf.write("\33\2\2\u020a\u020c\7;\2\2\u020b\u0209\3\2\2\2\u020b\u020c")
        buf.write("\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e\7\65\2\2\u020e")
        buf.write("\u020f\5T+\2\u020fg\3\2\2\2\u0210\u0211\7\5\2\2\u0211")
        buf.write("\u0212\7/\2\2\u0212i\3\2\2\2\u0213\u0214\7\6\2\2\u0214")
        buf.write("\u0215\7/\2\2\u0215k\3\2\2\2\u0216\u0218\7\23\2\2\u0217")
        buf.write("\u0219\5\36\20\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2\2")
        buf.write("\2\u0219\u021a\3\2\2\2\u021a\u021b\7/\2\2\u021bm\3\2\2")
        buf.write("\2\u021c\u021d\7\26\2\2\u021do\3\2\2\2\u021e\u021f\t\13")
        buf.write("\2\2\u021fq\3\2\2\2\62u\u008f\u0093\u0095\u009d\u00a7")
        buf.write("\u00ac\u00b1\u00b9\u00c0\u00c8\u00d5\u00e0\u00eb\u00f6")
        buf.write("\u0101\u010c\u0112\u0117\u0120\u012b\u0136\u013c\u0143")
        buf.write("\u0148\u0151\u0159\u015e\u0167\u016e\u0176\u017e\u0186")
        buf.write("\u018e\u019a\u01a0\u01b1\u01b7\u01c5\u01cc\u01cf\u01db")
        buf.write("\u01e5\u01ec\u01fb\u0200\u020b\u0218")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'main'", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'==.'", "'+.'", "'::'", "';'", 
                     "','", "'.'", "'..'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "WRITELN", "PLUS", "MINUS", 
                      "STAR", "DIV", "MOD", "NOT", "ANDAND", "OROR", "EQ", 
                      "ASSIGN", "NE", "GT", "GE", "LS", "LE", "STR_CMP", 
                      "STR_CONCAT", "DCL", "SM", "CM", "DOT", "DDOT", "CL", 
                      "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "SDIGIT", "WS", 
                      "BLOCKCOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_init = 1
    RULE_body = 2
    RULE_class_decl = 3
    RULE_classname = 4
    RULE_classbody = 5
    RULE_attribute_decl = 6
    RULE_attributename_list = 7
    RULE_attribute_init = 8
    RULE_method_decl = 9
    RULE_parameter_list = 10
    RULE_parameter = 11
    RULE_primitive_types = 12
    RULE_expression_list = 13
    RULE_expression = 14
    RULE_expr_1 = 15
    RULE_expr_2 = 16
    RULE_expr_3 = 17
    RULE_expr_4 = 18
    RULE_expr_5 = 19
    RULE_expr_6 = 20
    RULE_expr_7 = 21
    RULE_expr_8 = 22
    RULE_expr_9 = 23
    RULE_expr_10 = 24
    RULE_operands = 25
    RULE_call_expr = 26
    RULE_expr_list = 27
    RULE_literals = 28
    RULE_array_lit = 29
    RULE_array_list = 30
    RULE_arrayitemint_list = 31
    RULE_arrayitemfloat_list = 32
    RULE_arrayitembool_list = 33
    RULE_arrayitemstring_list = 34
    RULE_arrayitemarray_list = 35
    RULE_array_decl = 36
    RULE_element_type = 37
    RULE_object_create = 38
    RULE_index_expression = 39
    RULE_index_op = 40
    RULE_block_stmt = 41
    RULE_stmt_list = 42
    RULE_vardecl_stmt = 43
    RULE_var_init = 44
    RULE_varname_list = 45
    RULE_assign_stmt = 46
    RULE_assign_lhs = 47
    RULE_assign_tail = 48
    RULE_if_stmt = 49
    RULE_forin_stmt = 50
    RULE_break_stmt = 51
    RULE_continue_stmt = 52
    RULE_return_stmt = 53
    RULE_methodinvocation_stmt = 54
    RULE_bool_lit = 55

    ruleNames =  [ "program", "class_init", "body", "class_decl", "classname", 
                   "classbody", "attribute_decl", "attributename_list", 
                   "attribute_init", "method_decl", "parameter_list", "parameter", 
                   "primitive_types", "expression_list", "expression", "expr_1", 
                   "expr_2", "expr_3", "expr_4", "expr_5", "expr_6", "expr_7", 
                   "expr_8", "expr_9", "expr_10", "operands", "call_expr", 
                   "expr_list", "literals", "array_lit", "array_list", "arrayitemint_list", 
                   "arrayitemfloat_list", "arrayitembool_list", "arrayitemstring_list", 
                   "arrayitemarray_list", "array_decl", "element_type", 
                   "object_create", "index_expression", "index_op", "block_stmt", 
                   "stmt_list", "vardecl_stmt", "var_init", "varname_list", 
                   "assign_stmt", "assign_lhs", "assign_tail", "if_stmt", 
                   "forin_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "methodinvocation_stmt", "bool_lit" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSEIF=6
    ELSE=7
    FOREACH=8
    TRUE=9
    FALSE=10
    ARRAY=11
    IN=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    STRING=16
    RETURN=17
    NULL=18
    CLASS=19
    VAL=20
    VAR=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    WRITELN=26
    PLUS=27
    MINUS=28
    STAR=29
    DIV=30
    MOD=31
    NOT=32
    ANDAND=33
    OROR=34
    EQ=35
    ASSIGN=36
    NE=37
    GT=38
    GE=39
    LS=40
    LE=41
    STR_CMP=42
    STR_CONCAT=43
    DCL=44
    SM=45
    CM=46
    DOT=47
    DDOT=48
    CL=49
    LP=50
    RP=51
    LSB=52
    RSB=53
    LCB=54
    RCB=55
    IDENTIFIER=56
    INT_LIT=57
    FLOAT_LIT=58
    STRING_LIT=59
    SDIGIT=60
    WS=61
    BLOCKCOMMENT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

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

        def class_init(self):
            return self.getTypedRuleContext(D96Parser.Class_initContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 112
                    self.class_decl() 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 118
            self.class_init()
            self.state = 119
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_init" ):
                return visitor.visitClass_init(self)
            else:
                return visitor.visitChildren(self)




    def class_init(self):

        localctx = D96Parser.Class_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(D96Parser.CLASS)
            self.state = 122
            self.match(D96Parser.T__0)
            self.state = 123
            self.match(D96Parser.LCB)
            self.state = 124
            self.body()
            self.state = 125
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return D96Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(D96Parser.T__1)
            self.state = 128
            self.match(D96Parser.LP)
            self.state = 129
            self.match(D96Parser.RP)
            self.state = 130
            self.block_stmt()
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
        self.enterRule(localctx, 6, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(D96Parser.CLASS)
            self.state = 133
            self.classname()
            self.state = 134
            self.match(D96Parser.LCB)
            self.state = 135
            self.classbody()
            self.state = 136
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
        self.enterRule(localctx, 8, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(D96Parser.IDENTIFIER)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 139
                self.match(D96Parser.CL)
                self.state = 140
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
        self.enterRule(localctx, 10, self.RULE_classbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 143
                    self.attribute_decl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDENTIFIER]:
                    self.state = 144
                    self.method_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def attribute_init(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(D96Parser.Array_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.attributename_list()
            self.state = 152
            self.match(D96Parser.CL)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 153
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 154
                self.array_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self.attribute_init()
            self.state = 158
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
        self.enterRule(localctx, 14, self.RULE_attributename_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(D96Parser.IDENTIFIER)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 161
                self.match(D96Parser.CM)
                self.state = 162
                self.match(D96Parser.IDENTIFIER)
                self.state = 167
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
        self.enterRule(localctx, 16, self.RULE_attribute_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 168
                self.match(D96Parser.ASSIGN)
                self.state = 169
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
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==D96Parser.CONSTRUCTOR or _la==D96Parser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.match(D96Parser.LP)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 174
                    self.parameter_list()


                self.state = 177
                self.match(D96Parser.RP)
                self.state = 178
                self.block_stmt()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(D96Parser.DESTRUCTOR)
                self.state = 180
                self.match(D96Parser.LP)
                self.state = 181
                self.match(D96Parser.RP)
                self.state = 182
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
        self.enterRule(localctx, 20, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.parameter()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 186
                self.match(D96Parser.SM)
                self.state = 187
                self.parameter()
                self.state = 192
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

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


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
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(D96Parser.IDENTIFIER)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 194
                self.match(D96Parser.CM)
                self.state = 195
                self.match(D96Parser.IDENTIFIER)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(D96Parser.CL)
            self.state = 202
            self.primitive_types()
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
        self.enterRule(localctx, 24, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
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
        self.enterRule(localctx, 26, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expression(0)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 207
                self.match(D96Parser.CM)
                self.state = 208
                self.expression(0)
                self.state = 213
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

        def expr_1(self):
            return self.getTypedRuleContext(D96Parser.Expr_1Context,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.expr_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 219
                    self.expression(3) 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_2(self):
            return self.getTypedRuleContext(D96Parser.Expr_2Context,0)


        def expr_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_1Context,i)


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



    def expr_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.expr_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_1)
                    self.state = 228
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 229
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GE) | (1 << D96Parser.LS) | (1 << D96Parser.LE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 230
                    self.expr_1(3) 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expr_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_2)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDAND or _la==D96Parser.OROR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.expr_3(0) 
                self.state = 246
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.expr_4(0) 
                self.state = 257
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expr_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.STAR) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.expr_5() 
                self.state = 268
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
        self.enterRule(localctx, 38, self.RULE_expr_5)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(D96Parser.NOT)
                self.state = 270
                self.expr_5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NEW, D96Parser.MINUS, D96Parser.LSB, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 40, self.RULE_expr_6)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(D96Parser.MINUS)
                self.state = 275
                self.expr_6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NEW, D96Parser.LSB, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr_7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.expr_8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_7)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LSB or _la==D96Parser.RSB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 288
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr_8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.expr_9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_8)
                    self.state = 292
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 293
                    self.match(D96Parser.DOT)
                    self.state = 294
                    self.expr_9(0) 
                self.state = 299
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

        def expr_10(self):
            return self.getTypedRuleContext(D96Parser.Expr_10Context,0)


        def expr_9(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_9Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_9Context,i)


        def DCL(self):
            return self.getToken(D96Parser.DCL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_9" ):
                return visitor.visitExpr_9(self)
            else:
                return visitor.visitChildren(self)



    def expr_9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr_9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expr_10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_9)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    self.match(D96Parser.DCL)
                    self.state = 305
                    self.expr_9(3) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_10" ):
                return visitor.visitExpr_10(self)
            else:
                return visitor.visitChildren(self)




    def expr_10(self):

        localctx = D96Parser.Expr_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_10)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(D96Parser.NEW)
                self.state = 312
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.operands()
                pass


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


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operands)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.object_create()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.state = 323
            self.match(D96Parser.IDENTIFIER)
            self.state = 324
            self.match(D96Parser.LP)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LSB) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 325
                self.expr_list()


            self.state = 328
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
            self.state = 330
            self.expression(0)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 331
                self.match(D96Parser.CM)
                self.state = 332
                self.expression(0)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 56, self.RULE_literals)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.bool_lit()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 342
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
        self.enterRule(localctx, 58, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.ARRAY)
            self.state = 346
            self.match(D96Parser.LP)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 347
                self.array_list()


            self.state = 350
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
        self.enterRule(localctx, 60, self.RULE_array_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.arrayitemint_list()
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.arrayitemfloat_list()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.arrayitembool_list()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.arrayitemstring_list()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 356
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
        self.enterRule(localctx, 62, self.RULE_arrayitemint_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.INT_LIT)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 360
                self.match(D96Parser.CM)
                self.state = 361
                self.match(D96Parser.INT_LIT)
                self.state = 366
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
        self.enterRule(localctx, 64, self.RULE_arrayitemfloat_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.FLOAT_LIT)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 368
                self.match(D96Parser.CM)
                self.state = 369
                self.match(D96Parser.FLOAT_LIT)
                self.state = 374
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
        self.enterRule(localctx, 66, self.RULE_arrayitembool_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.bool_lit()
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 376
                self.match(D96Parser.CM)
                self.state = 377
                self.bool_lit()
                self.state = 382
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
        self.enterRule(localctx, 68, self.RULE_arrayitemstring_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(D96Parser.STRING_LIT)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 384
                self.match(D96Parser.CM)
                self.state = 385
                self.match(D96Parser.STRING_LIT)
                self.state = 390
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
        self.enterRule(localctx, 70, self.RULE_arrayitemarray_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.array_lit()
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 392
                self.match(D96Parser.CM)
                self.state = 393
                self.array_lit()
                self.state = 398
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
        self.enterRule(localctx, 72, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(D96Parser.ARRAY)
            self.state = 400
            self.match(D96Parser.LSB)
            self.state = 401
            self.element_type()
            self.state = 402
            self.match(D96Parser.CM)
            self.state = 403
            self.match(D96Parser.INT_LIT)
            self.state = 404
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
        self.enterRule(localctx, 74, self.RULE_element_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 406
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 407
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


    class Object_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_create" ):
                return visitor.visitObject_create(self)
            else:
                return visitor.visitChildren(self)




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.NEW)
            self.state = 411
            self.match(D96Parser.IDENTIFIER)
            self.state = 412
            self.match(D96Parser.LP)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LSB) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 413
                self.expression_list()


            self.state = 416
            self.match(D96Parser.RP)
            self.state = 417
            self.match(D96Parser.SM)
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
        self.enterRule(localctx, 78, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.expression(0)
            self.state = 420
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
        self.enterRule(localctx, 80, self.RULE_index_op)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(D96Parser.LSB)
                self.state = 423
                self.expression(0)
                self.state = 424
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(D96Parser.LSB)
                self.state = 427
                self.expression(0)
                self.state = 428
                self.match(D96Parser.RSB)
                self.state = 429
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
        self.enterRule(localctx, 82, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(D96Parser.LCB)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LSB) | (1 << D96Parser.LCB) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 434
                self.stmt_list()
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 440
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
        self.enterRule(localctx, 84, self.RULE_stmt_list)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.vardecl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.forin_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 447
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 448
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 449
                self.methodinvocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 450
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

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(D96Parser.Array_declContext,0)


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
        self.enterRule(localctx, 86, self.RULE_vardecl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 454
            self.varname_list()
            self.state = 455
            self.match(D96Parser.CL)
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 456
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 457
                self.array_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 460
                self.var_init()


            self.state = 463
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
        self.enterRule(localctx, 88, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(D96Parser.ASSIGN)
            self.state = 466
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
            return D96Parser.RULE_varname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarname_list" ):
                return visitor.visitVarname_list(self)
            else:
                return visitor.visitChildren(self)




    def varname_list(self):

        localctx = D96Parser.Varname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_varname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(D96Parser.IDENTIFIER)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 469
                self.match(D96Parser.CM)
                self.state = 470
                self.match(D96Parser.IDENTIFIER)
                self.state = 475
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
        self.enterRule(localctx, 92, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.assign_lhs()
            self.state = 477
            self.match(D96Parser.ASSIGN)
            self.state = 478
            self.assign_tail()
            self.state = 479
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
        self.enterRule(localctx, 94, self.RULE_assign_lhs)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        self.enterRule(localctx, 96, self.RULE_assign_tail)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.assign_lhs()
                self.state = 486
                self.match(D96Parser.ASSIGN)
                self.state = 487
                self.assign_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.expression(0)
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
        self.enterRule(localctx, 98, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(D96Parser.IF)
            self.state = 493
            self.match(D96Parser.LP)
            self.state = 494
            self.expression(0)
            self.state = 495
            self.match(D96Parser.RP)
            self.state = 496
            self.block_stmt()
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 497
                self.match(D96Parser.ELSEIF)
                self.state = 498
                self.match(D96Parser.LP)
                self.state = 499
                self.expression(0)
                self.state = 500
                self.match(D96Parser.RP)
                self.state = 501
                self.block_stmt()
                self.state = 507
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 508
                self.match(D96Parser.ELSE)
                self.state = 509
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
        self.enterRule(localctx, 100, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(D96Parser.FOREACH)
            self.state = 513
            self.match(D96Parser.LP)
            self.state = 514
            self.match(D96Parser.IDENTIFIER)
            self.state = 515
            self.match(D96Parser.IN)
            self.state = 516
            self.match(D96Parser.INT_LIT)
            self.state = 517
            self.match(D96Parser.DDOT)
            self.state = 518
            self.match(D96Parser.INT_LIT)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 519
                self.match(D96Parser.BY)
                self.state = 520
                self.match(D96Parser.INT_LIT)


            self.state = 523
            self.match(D96Parser.RP)
            self.state = 524
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
        self.enterRule(localctx, 102, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(D96Parser.BREAK)
            self.state = 527
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
        self.enterRule(localctx, 104, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(D96Parser.CONTINUE)
            self.state = 530
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
        self.enterRule(localctx, 106, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(D96Parser.RETURN)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LSB) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 533
                self.expression(0)


            self.state = 536
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

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodinvocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocation_stmt" ):
                return visitor.visitMethodinvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocation_stmt(self):

        localctx = D96Parser.Methodinvocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_methodinvocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(D96Parser.VAL)
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
        self.enterRule(localctx, 110, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
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
        self._predicates[14] = self.expression_sempred
        self._predicates[15] = self.expr_1_sempred
        self._predicates[16] = self.expr_2_sempred
        self._predicates[17] = self.expr_3_sempred
        self._predicates[18] = self.expr_4_sempred
        self._predicates[21] = self.expr_7_sempred
        self._predicates[22] = self.expr_8_sempred
        self._predicates[23] = self.expr_9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_1_sempred(self, localctx:Expr_1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_2_sempred(self, localctx:Expr_2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_3_sempred(self, localctx:Expr_3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_4_sempred(self, localctx:Expr_4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr_7_sempred(self, localctx:Expr_7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr_8_sempred(self, localctx:Expr_8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expr_9_sempred(self, localctx:Expr_9Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




