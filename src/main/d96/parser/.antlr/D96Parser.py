# Generated from /Users/tieuviettrongnghia/Documents/Document/HỌC TẬP/ĐẠI HỌC BÁCH KHOA/212/PPL/Assignment/Assignment 1/initial copy/src/main/d96/parser/D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u01a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4y\n\4\f\4\16\4|\13\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u0089\n\6\3\7\3\7\7\7\u008d")
        buf.write("\n\7\f\7\16\7\u0090\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\5\n\u009c\n\n\3\13\3\13\3\f\3\f\3\f\7\f\u00a3")
        buf.write("\n\f\f\f\16\f\u00a6\13\f\3\f\3\f\3\f\7\f\u00ab\n\f\f\f")
        buf.write("\16\f\u00ae\13\f\5\f\u00b0\n\f\3\r\3\r\3\r\5\r\u00b5\n")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bd\n\r\3\16\3\16\3\16")
        buf.write("\7\16\u00c2\n\16\f\16\16\16\u00c5\13\16\3\17\3\17\3\17")
        buf.write("\7\17\u00ca\n\17\f\17\16\17\u00cd\13\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u00d7\n\20\3\21\3\21\3")
        buf.write("\21\5\21\u00dc\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00e5\n\22\3\23\3\23\3\23\7\23\u00ea\n\23\f\23\16")
        buf.write("\23\u00ed\13\23\3\24\3\24\3\24\7\24\u00f2\n\24\f\24\16")
        buf.write("\24\u00f5\13\24\3\25\3\25\3\25\7\25\u00fa\n\25\f\25\16")
        buf.write("\25\u00fd\13\25\3\26\3\26\3\26\7\26\u0102\n\26\f\26\16")
        buf.write("\26\u0105\13\26\3\27\3\27\3\27\7\27\u010a\n\27\f\27\16")
        buf.write("\27\u010d\13\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\5\32\u011a\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\35\3\35\5\35\u0125\n\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\5\"\u0133\n\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\7#\u013b\n#\f#\16#\u013e\13#\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\5$\u0149\n$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\7&\u0154\n&\f&\16&\u0157\13&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u0169\n(\f(\16(\u016c")
        buf.write("\13(\3(\3(\5(\u0170\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\5)\u017e\n)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\5\60\u0193\n\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\7\62\u019b\n\62\f\62\16\62\u019e\13\62")
        buf.write("\3\62\3\62\3\62\2\2\63\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\t")
        buf.write("\3\2\21\23\3\2\30\31\4\2\32\32==\3\2\21\24\4\2\37!##\4")
        buf.write("\2$&..\4\2\'\')-\2\u019d\2g\3\2\2\2\4m\3\2\2\2\6s\3\2")
        buf.write("\2\2\b\177\3\2\2\2\n\u0085\3\2\2\2\f\u008e\3\2\2\2\16")
        buf.write("\u0091\3\2\2\2\20\u0097\3\2\2\2\22\u009b\3\2\2\2\24\u009d")
        buf.write("\3\2\2\2\26\u00af\3\2\2\2\30\u00bc\3\2\2\2\32\u00be\3")
        buf.write("\2\2\2\34\u00c6\3\2\2\2\36\u00d6\3\2\2\2 \u00d8\3\2\2")
        buf.write("\2\"\u00e4\3\2\2\2$\u00e6\3\2\2\2&\u00ee\3\2\2\2(\u00f6")
        buf.write("\3\2\2\2*\u00fe\3\2\2\2,\u0106\3\2\2\2.\u010e\3\2\2\2")
        buf.write("\60\u0110\3\2\2\2\62\u0119\3\2\2\2\64\u011b\3\2\2\2\66")
        buf.write("\u0120\3\2\2\28\u0124\3\2\2\2:\u0126\3\2\2\2<\u0128\3")
        buf.write("\2\2\2>\u012a\3\2\2\2@\u012c\3\2\2\2B\u012e\3\2\2\2D\u0137")
        buf.write("\3\2\2\2F\u0148\3\2\2\2H\u014a\3\2\2\2J\u0150\3\2\2\2")
        buf.write("L\u0158\3\2\2\2N\u015d\3\2\2\2P\u0171\3\2\2\2R\u0182\3")
        buf.write("\2\2\2T\u0184\3\2\2\2V\u0186\3\2\2\2X\u0188\3\2\2\2Z\u018a")
        buf.write("\3\2\2\2\\\u018d\3\2\2\2^\u0190\3\2\2\2`\u0196\3\2\2\2")
        buf.write("b\u0198\3\2\2\2df\5\b\5\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2")
        buf.write("\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2jk\5\4\3\2kl\7\2\2\3l")
        buf.write("\3\3\2\2\2mn\7\27\2\2no\7\3\2\2op\7\65\2\2pq\5\6\4\2q")
        buf.write("r\7\66\2\2r\5\3\2\2\2st\7\4\2\2tu\7\61\2\2uv\7\62\2\2")
        buf.write("vz\7\65\2\2wy\5F$\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3")
        buf.write("\2\2\2{}\3\2\2\2|z\3\2\2\2}~\7\66\2\2~\7\3\2\2\2\177\u0080")
        buf.write("\7\27\2\2\u0080\u0081\5\n\6\2\u0081\u0082\7\65\2\2\u0082")
        buf.write("\u0083\5\f\7\2\u0083\u0084\7\66\2\2\u0084\t\3\2\2\2\u0085")
        buf.write("\u0088\7=\2\2\u0086\u0087\79\2\2\u0087\u0089\7=\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\13\3\2\2\2\u008a")
        buf.write("\u008d\5\16\b\2\u008b\u008d\5\30\r\2\u008c\u008a\3\2\2")
        buf.write("\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\r\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0092\5\24\13\2\u0092\u0093\5\26\f\2\u0093")
        buf.write("\u0094\79\2\2\u0094\u0095\5\20\t\2\u0095\u0096\7\67\2")
        buf.write("\2\u0096\17\3\2\2\2\u0097\u0098\t\2\2\2\u0098\21\3\2\2")
        buf.write("\2\u0099\u009a\7(\2\2\u009a\u009c\5D#\2\u009b\u0099\3")
        buf.write("\2\2\2\u009b\u009c\3\2\2\2\u009c\23\3\2\2\2\u009d\u009e")
        buf.write("\t\3\2\2\u009e\25\3\2\2\2\u009f\u00a4\7>\2\2\u00a0\u00a1")
        buf.write("\78\2\2\u00a1\u00a3\7>\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a6")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00b0\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00ac\7?\2\2")
        buf.write("\u00a8\u00a9\78\2\2\u00a9\u00ab\7?\2\2\u00aa\u00a8\3\2")
        buf.write("\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af")
        buf.write("\u009f\3\2\2\2\u00af\u00a7\3\2\2\2\u00b0\27\3\2\2\2\u00b1")
        buf.write("\u00b2\t\4\2\2\u00b2\u00b4\7\61\2\2\u00b3\u00b5\5\32\16")
        buf.write("\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\u00b7\7\62\2\2\u00b7\u00bd\5b\62\2\u00b8")
        buf.write("\u00b9\7\33\2\2\u00b9\u00ba\7\61\2\2\u00ba\u00bb\7\62")
        buf.write("\2\2\u00bb\u00bd\5b\62\2\u00bc\u00b1\3\2\2\2\u00bc\u00b8")
        buf.write("\3\2\2\2\u00bd\31\3\2\2\2\u00be\u00c3\5\34\17\2\u00bf")
        buf.write("\u00c0\7\67\2\2\u00c0\u00c2\5\34\17\2\u00c1\u00bf\3\2")
        buf.write("\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\33\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00cb")
        buf.write("\7=\2\2\u00c7\u00c8\78\2\2\u00c8\u00ca\7=\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00ce\u00cf\79\2\2\u00cf\u00d0\5\20\t\2\u00d0\35\3\2")
        buf.write("\2\2\u00d1\u00d7\7@\2\2\u00d2\u00d7\7G\2\2\u00d3\u00d7")
        buf.write("\7H\2\2\u00d4\u00d7\7I\2\2\u00d5\u00d7\5 \21\2\u00d6\u00d1")
        buf.write("\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\37\3\2\2\2\u00d8")
        buf.write("\u00d9\7\17\2\2\u00d9\u00db\7\61\2\2\u00da\u00dc\5\"\22")
        buf.write("\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\7\62\2\2\u00de!\3\2\2\2\u00df\u00e5")
        buf.write("\5$\23\2\u00e0\u00e5\5&\24\2\u00e1\u00e5\5(\25\2\u00e2")
        buf.write("\u00e5\5*\26\2\u00e3\u00e5\5,\27\2\u00e4\u00df\3\2\2\2")
        buf.write("\u00e4\u00e0\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e3\3\2\2\2\u00e5#\3\2\2\2\u00e6\u00eb")
        buf.write("\7@\2\2\u00e7\u00e8\78\2\2\u00e8\u00ea\7@\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00f3\7G\2\2\u00ef\u00f0\78\2\2\u00f0\u00f2\7G\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4\'\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write("\2\u00f6\u00fb\7H\2\2\u00f7\u00f8\78\2\2\u00f8\u00fa\7")
        buf.write("H\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc)\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fe\u0103\7I\2\2\u00ff\u0100\78\2\2\u0100\u0102")
        buf.write("\7I\2\2\u0101\u00ff\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104+\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u010b\5 \21\2\u0107\u0108\78\2\2")
        buf.write("\u0108\u010a\5 \21\2\u0109\u0107\3\2\2\2\u010a\u010d\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c-")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\t\5\2\2\u010f")
        buf.write("/\3\2\2\2\u0110\u0111\7\17\2\2\u0111\u0112\7\63\2\2\u0112")
        buf.write("\u0113\5\62\32\2\u0113\u0114\78\2\2\u0114\u0115\7:\2\2")
        buf.write("\u0115\u0116\7\64\2\2\u0116\61\3\2\2\2\u0117\u011a\5.")
        buf.write("\30\2\u0118\u011a\7\17\2\2\u0119\u0117\3\2\2\2\u0119\u0118")
        buf.write("\3\2\2\2\u011a\63\3\2\2\2\u011b\u011c\7\17\2\2\u011c\u011d")
        buf.write("\7\63\2\2\u011d\u011e\7:\2\2\u011e\u011f\7\64\2\2\u011f")
        buf.write("\65\3\2\2\2\u0120\u0121\7\5\2\2\u0121\67\3\2\2\2\u0122")
        buf.write("\u0125\7=\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0124\u0123\3\2\2\2\u01259\3\2\2\2\u0126\u0127\t\6\2")
        buf.write("\2\u0127;\3\2\2\2\u0128\u0129\t\7\2\2\u0129=\3\2\2\2\u012a")
        buf.write("\u012b\7/\2\2\u012b?\3\2\2\2\u012c\u012d\t\b\2\2\u012d")
        buf.write("A\3\2\2\2\u012e\u012f\7\34\2\2\u012f\u0130\7=\2\2\u0130")
        buf.write("\u0132\7\61\2\2\u0131\u0133\5D#\2\u0132\u0131\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\7")
        buf.write("\62\2\2\u0135\u0136\7\67\2\2\u0136C\3\2\2\2\u0137\u013c")
        buf.write("\5\66\34\2\u0138\u0139\78\2\2\u0139\u013b\5\66\34\2\u013a")
        buf.write("\u0138\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013dE\3\2\2\2\u013e\u013c\3\2\2")
        buf.write("\2\u013f\u0149\5H%\2\u0140\u0149\5L\'\2\u0141\u0149\5")
        buf.write("N(\2\u0142\u0149\5P)\2\u0143\u0149\5Z.\2\u0144\u0149\5")
        buf.write("\\/\2\u0145\u0149\5^\60\2\u0146\u0149\5`\61\2\u0147\u0149")
        buf.write("\5b\62\2\u0148\u013f\3\2\2\2\u0148\u0140\3\2\2\2\u0148")
        buf.write("\u0141\3\2\2\2\u0148\u0142\3\2\2\2\u0148\u0143\3\2\2\2")
        buf.write("\u0148\u0144\3\2\2\2\u0148\u0145\3\2\2\2\u0148\u0146\3")
        buf.write("\2\2\2\u0148\u0147\3\2\2\2\u0149G\3\2\2\2\u014a\u014b")
        buf.write("\5\24\13\2\u014b\u014c\5J&\2\u014c\u014d\79\2\2\u014d")
        buf.write("\u014e\5\20\t\2\u014e\u014f\7\67\2\2\u014fI\3\2\2\2\u0150")
        buf.write("\u0155\7>\2\2\u0151\u0152\78\2\2\u0152\u0154\7>\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156K\3\2\2\2\u0157\u0155\3\2\2")
        buf.write("\2\u0158\u0159\5\66\34\2\u0159\u015a\7(\2\2\u015a\u015b")
        buf.write("\5\66\34\2\u015b\u015c\7\67\2\2\u015cM\3\2\2\2\u015d\u015e")
        buf.write("\7\t\2\2\u015e\u015f\7\61\2\2\u015f\u0160\5\66\34\2\u0160")
        buf.write("\u0161\7\62\2\2\u0161\u016a\5b\62\2\u0162\u0163\7\n\2")
        buf.write("\2\u0163\u0164\7\61\2\2\u0164\u0165\5\66\34\2\u0165\u0166")
        buf.write("\7\62\2\2\u0166\u0167\5b\62\2\u0167\u0169\3\2\2\2\u0168")
        buf.write("\u0162\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016b\u016f\3\2\2\2\u016c\u016a\3")
        buf.write("\2\2\2\u016d\u016e\7\13\2\2\u016e\u0170\5b\62\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170O\3\2\2\2\u0171")
        buf.write("\u0172\7\f\2\2\u0172\u0173\7\61\2\2\u0173\u0174\5R*\2")
        buf.write("\u0174\u0175\7\20\2\2\u0175\u0176\5T+\2\u0176\u0177\7")
        buf.write("\6\2\2\u0177\u017d\5V,\2\u0178\u0179\7\61\2\2\u0179\u017a")
        buf.write("\7\35\2\2\u017a\u017b\5X-\2\u017b\u017c\7\62\2\2\u017c")
        buf.write("\u017e\3\2\2\2\u017d\u0178\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0180\7\62\2\2\u0180\u0181")
        buf.write("\5b\62\2\u0181Q\3\2\2\2\u0182\u0183\7\30\2\2\u0183S\3")
        buf.write("\2\2\2\u0184\u0185\7\30\2\2\u0185U\3\2\2\2\u0186\u0187")
        buf.write("\7\30\2\2\u0187W\3\2\2\2\u0188\u0189\7\30\2\2\u0189Y\3")
        buf.write("\2\2\2\u018a\u018b\7\7\2\2\u018b\u018c\7\67\2\2\u018c")
        buf.write("[\3\2\2\2\u018d\u018e\7\b\2\2\u018e\u018f\7\67\2\2\u018f")
        buf.write("]\3\2\2\2\u0190\u0192\7\25\2\2\u0191\u0193\5\66\34\2\u0192")
        buf.write("\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0195\7\67\2\2\u0195_\3\2\2\2\u0196\u0197\7\30")
        buf.write("\2\2\u0197a\3\2\2\2\u0198\u019c\7\65\2\2\u0199\u019b\5")
        buf.write("b\62\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a0\7\66\2\2\u01a0c\3\2\2\2\"g")
        buf.write("z\u0088\u008c\u008e\u009b\u00a4\u00ac\u00af\u00b4\u00bc")
        buf.write("\u00c3\u00cb\u00d6\u00db\u00e4\u00eb\u00f3\u00fb\u0103")
        buf.write("\u010b\u0119\u0124\u0132\u013c\u0148\u0155\u016a\u016f")
        buf.write("\u017d\u0192\u019c")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'main'", "'expr'", "'..'", 
                     "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
                     "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
                     "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'==.'", "'+.'", "'::'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "WRITELN", "PLUS", "MINUS", "STAR", "DIV", 
                      "MOD", "NOT", "ANDAND", "OROR", "EQ", "ASSIGN", "NE", 
                      "GT", "GE", "LS", "LE", "EQD", "PDOT", "DCL", "LP", 
                      "RP", "LSB", "RSB", "LCB", "RCB", "SM", "CM", "CL", 
                      "SDIGIT", "WS", "BLOCKCOMMENT", "IDENTIFIER", "ID_normal", 
                      "ID_static", "INT_LIT", "DecimalConstant", "OctalConstant", 
                      "HexadecimalConstant", "BinaryConstant", "HexadecimalPrefix", 
                      "HexadecimalDigit", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "ERROR_CHAR", "STR_CHAR" ]

    RULE_program = 0
    RULE_class_init = 1
    RULE_body = 2
    RULE_class_decl = 3
    RULE_classname = 4
    RULE_classbody = 5
    RULE_attribute_decl = 6
    RULE_datatype = 7
    RULE_attribute_init = 8
    RULE_attributetype = 9
    RULE_attributename_list = 10
    RULE_method_decl = 11
    RULE_parameter_list = 12
    RULE_parameter = 13
    RULE_literals = 14
    RULE_array_lit = 15
    RULE_array_list = 16
    RULE_arrayitemint_list = 17
    RULE_arrayitemfloat_list = 18
    RULE_arrayitembool_list = 19
    RULE_arrayitemstring_list = 20
    RULE_arrayitemarray_list = 21
    RULE_primitive_types = 22
    RULE_array_decl = 23
    RULE_element_type = 24
    RULE_array_element = 25
    RULE_expression = 26
    RULE_factor = 27
    RULE_arith_operator = 28
    RULE_bool_operator = 29
    RULE_concat_operator = 30
    RULE_rela_operator = 31
    RULE_object_decl = 32
    RULE_expression_list = 33
    RULE_stmt_list = 34
    RULE_varconstdecl_stmt = 35
    RULE_varconstname_list = 36
    RULE_assign_stmt = 37
    RULE_if_stmt = 38
    RULE_forin_stmt = 39
    RULE_scalar_var = 40
    RULE_expr1 = 41
    RULE_expr2 = 42
    RULE_expr3 = 43
    RULE_break_stmt = 44
    RULE_continue_stmt = 45
    RULE_return_stmt = 46
    RULE_methodinvocation_stmt = 47
    RULE_block_stmt = 48

    ruleNames =  [ "program", "class_init", "body", "class_decl", "classname", 
                   "classbody", "attribute_decl", "datatype", "attribute_init", 
                   "attributetype", "attributename_list", "method_decl", 
                   "parameter_list", "parameter", "literals", "array_lit", 
                   "array_list", "arrayitemint_list", "arrayitemfloat_list", 
                   "arrayitembool_list", "arrayitemstring_list", "arrayitemarray_list", 
                   "primitive_types", "array_decl", "element_type", "array_element", 
                   "expression", "factor", "arith_operator", "bool_operator", 
                   "concat_operator", "rela_operator", "object_decl", "expression_list", 
                   "stmt_list", "varconstdecl_stmt", "varconstname_list", 
                   "assign_stmt", "if_stmt", "forin_stmt", "scalar_var", 
                   "expr1", "expr2", "expr3", "break_stmt", "continue_stmt", 
                   "return_stmt", "methodinvocation_stmt", "block_stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BREAK=5
    CONTINUE=6
    IF=7
    ELSEIF=8
    ELSE=9
    FOREACH=10
    TRUE=11
    FALSE=12
    ARRAY=13
    IN=14
    INT=15
    FLOAT=16
    BOOLEAN=17
    STRING=18
    RETURN=19
    NULL=20
    CLASS=21
    VAL=22
    VAR=23
    CONSTRUCTOR=24
    DESTRUCTOR=25
    NEW=26
    BY=27
    WRITELN=28
    PLUS=29
    MINUS=30
    STAR=31
    DIV=32
    MOD=33
    NOT=34
    ANDAND=35
    OROR=36
    EQ=37
    ASSIGN=38
    NE=39
    GT=40
    GE=41
    LS=42
    LE=43
    EQD=44
    PDOT=45
    DCL=46
    LP=47
    RP=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    SM=53
    CM=54
    CL=55
    SDIGIT=56
    WS=57
    BLOCKCOMMENT=58
    IDENTIFIER=59
    ID_normal=60
    ID_static=61
    INT_LIT=62
    DecimalConstant=63
    OctalConstant=64
    HexadecimalConstant=65
    BinaryConstant=66
    HexadecimalPrefix=67
    HexadecimalDigit=68
    FLOAT_LIT=69
    BOOL_LIT=70
    STRING_LIT=71
    ERROR_CHAR=72
    STR_CHAR=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

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




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.class_decl() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 104
            self.class_init()
            self.state = 105
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_initContext(ParserRuleContext):

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




    def class_init(self):

        localctx = D96Parser.Class_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(D96Parser.CLASS)
            self.state = 108
            self.match(D96Parser.T__0)
            self.state = 109
            self.match(D96Parser.LCB)
            self.state = 110
            self.body()
            self.state = 111
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

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
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.T__1)
            self.state = 114
            self.match(D96Parser.LP)
            self.state = 115
            self.match(D96Parser.RP)
            self.state = 116
            self.match(D96Parser.LCB)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__2) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.LCB))) != 0):
                self.state = 117
                self.stmt_list()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):

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




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(D96Parser.CLASS)
            self.state = 126
            self.classname()
            self.state = 127
            self.match(D96Parser.LCB)
            self.state = 128
            self.classbody()
            self.state = 129
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassnameContext(ParserRuleContext):

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




    def classname(self):

        localctx = D96Parser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(D96Parser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 132
                self.match(D96Parser.CL)
                self.state = 133
                self.match(D96Parser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):

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




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 136
                    self.attribute_decl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDENTIFIER]:
                    self.state = 137
                    self.method_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 142
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributetype(self):
            return self.getTypedRuleContext(D96Parser.AttributetypeContext,0)


        def attributename_list(self):
            return self.getTypedRuleContext(D96Parser.Attributename_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.attributetype()
            self.state = 144
            self.attributename_list()
            self.state = 145
            self.match(D96Parser.CL)
            self.state = 146
            self.datatype()
            self.state = 147
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_datatype




    def datatype(self):

        localctx = D96Parser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN))) != 0)):
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


    class Attribute_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_init




    def attribute_init(self):

        localctx = D96Parser.Attribute_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 151
                self.match(D96Parser.ASSIGN)
                self.state = 152
                self.expression_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributetypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributetype




    def attributetype(self):

        localctx = D96Parser.AttributetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
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


    class Attributename_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_normal(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_normal)
            else:
                return self.getToken(D96Parser.ID_normal, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def ID_static(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_static)
            else:
                return self.getToken(D96Parser.ID_static, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attributename_list




    def attributename_list(self):

        localctx = D96Parser.Attributename_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attributename_list)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID_normal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(D96Parser.ID_normal)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 158
                    self.match(D96Parser.CM)
                    self.state = 159
                    self.match(D96Parser.ID_normal)
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.ID_static]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(D96Parser.ID_static)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 166
                    self.match(D96Parser.CM)
                    self.state = 167
                    self.match(D96Parser.ID_static)
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class Method_declContext(ParserRuleContext):

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




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.CONSTRUCTOR or _la==D96Parser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.match(D96Parser.LP)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 177
                    self.parameter_list()


                self.state = 180
                self.match(D96Parser.RP)
                self.state = 181
                self.block_stmt()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(D96Parser.DESTRUCTOR)
                self.state = 183
                self.match(D96Parser.LP)
                self.state = 184
                self.match(D96Parser.RP)
                self.state = 185
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




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.parameter()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 189
                self.match(D96Parser.SM)
                self.state = 190
                self.parameter()
                self.state = 195
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

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(D96Parser.IDENTIFIER)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 197
                self.match(D96Parser.CM)
                self.state = 198
                self.match(D96Parser.IDENTIFIER)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(D96Parser.CL)
            self.state = 205
            self.datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(D96Parser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(D96Parser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(D96Parser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literals)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(D96Parser.BOOL_LIT)
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
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




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(D96Parser.ARRAY)
            self.state = 215
            self.match(D96Parser.LP)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 13)) & ~0x3f) == 0 and ((1 << (_la - 13)) & ((1 << (D96Parser.ARRAY - 13)) | (1 << (D96Parser.INT_LIT - 13)) | (1 << (D96Parser.FLOAT_LIT - 13)) | (1 << (D96Parser.BOOL_LIT - 13)) | (1 << (D96Parser.STRING_LIT - 13)))) != 0):
                self.state = 216
                self.array_list()


            self.state = 219
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):

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




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_list)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.arrayitemint_list()
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.arrayitemfloat_list()
                pass
            elif token in [D96Parser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.arrayitembool_list()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.arrayitemstring_list()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
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




    def arrayitemint_list(self):

        localctx = D96Parser.Arrayitemint_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arrayitemint_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.INT_LIT)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 229
                self.match(D96Parser.CM)
                self.state = 230
                self.match(D96Parser.INT_LIT)
                self.state = 235
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




    def arrayitemfloat_list(self):

        localctx = D96Parser.Arrayitemfloat_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrayitemfloat_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(D96Parser.FLOAT_LIT)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 237
                self.match(D96Parser.CM)
                self.state = 238
                self.match(D96Parser.FLOAT_LIT)
                self.state = 243
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.BOOL_LIT)
            else:
                return self.getToken(D96Parser.BOOL_LIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayitembool_list




    def arrayitembool_list(self):

        localctx = D96Parser.Arrayitembool_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arrayitembool_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.BOOL_LIT)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 245
                self.match(D96Parser.CM)
                self.state = 246
                self.match(D96Parser.BOOL_LIT)
                self.state = 251
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




    def arrayitemstring_list(self):

        localctx = D96Parser.Arrayitemstring_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayitemstring_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(D96Parser.STRING_LIT)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 253
                self.match(D96Parser.CM)
                self.state = 254
                self.match(D96Parser.STRING_LIT)
                self.state = 259
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




    def arrayitemarray_list(self):

        localctx = D96Parser.Arrayitemarray_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayitemarray_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.array_lit()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 261
                self.match(D96Parser.CM)
                self.state = 262
                self.array_lit()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typesContext(ParserRuleContext):

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




    def primitive_types(self):

        localctx = D96Parser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
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


    class Array_declContext(ParserRuleContext):

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

        def SDIGIT(self):
            return self.getToken(D96Parser.SDIGIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl




    def array_decl(self):

        localctx = D96Parser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.ARRAY)
            self.state = 271
            self.match(D96Parser.LSB)
            self.state = 272
            self.element_type()
            self.state = 273
            self.match(D96Parser.CM)
            self.state = 274
            self.match(D96Parser.SDIGIT)
            self.state = 275
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element_type




    def element_type(self):

        localctx = D96Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_element_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 277
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 278
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


    class Array_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def SDIGIT(self):
            return self.getToken(D96Parser.SDIGIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element




    def array_element(self):

        localctx = D96Parser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(D96Parser.ARRAY)
            self.state = 282
            self.match(D96Parser.LSB)
            self.state = 283
            self.match(D96Parser.SDIGIT)
            self.state = 284
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_expression




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(D96Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_factor




    def factor(self):

        localctx = D96Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_factor)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class Arith_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def STAR(self):
            return self.getToken(D96Parser.STAR, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arith_operator




    def arith_operator(self):

        localctx = D96Parser.Arith_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arith_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.PLUS) | (1 << D96Parser.MINUS) | (1 << D96Parser.STAR) | (1 << D96Parser.MOD))) != 0)):
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


    class Bool_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def ANDAND(self):
            return self.getToken(D96Parser.ANDAND, 0)

        def OROR(self):
            return self.getToken(D96Parser.OROR, 0)

        def EQD(self):
            return self.getToken(D96Parser.EQD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_bool_operator




    def bool_operator(self):

        localctx = D96Parser.Bool_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_bool_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOT) | (1 << D96Parser.ANDAND) | (1 << D96Parser.OROR) | (1 << D96Parser.EQD))) != 0)):
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


    class Concat_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PDOT(self):
            return self.getToken(D96Parser.PDOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_concat_operator




    def concat_operator(self):

        localctx = D96Parser.Concat_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_concat_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(D96Parser.PDOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rela_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NE(self):
            return self.getToken(D96Parser.NE, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_rela_operator




    def rela_operator(self):

        localctx = D96Parser.Rela_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_rela_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GE) | (1 << D96Parser.LS) | (1 << D96Parser.LE))) != 0)):
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


    class Object_declContext(ParserRuleContext):

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
            return D96Parser.RULE_object_decl




    def object_decl(self):

        localctx = D96Parser.Object_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_object_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(D96Parser.NEW)
            self.state = 301
            self.match(D96Parser.IDENTIFIER)
            self.state = 302
            self.match(D96Parser.LP)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__2:
                self.state = 303
                self.expression_list()


            self.state = 306
            self.match(D96Parser.RP)
            self.state = 307
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):

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




    def expression_list(self):

        localctx = D96Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expression()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 310
                self.match(D96Parser.CM)
                self.state = 311
                self.expression()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varconstdecl_stmt(self):
            return self.getTypedRuleContext(D96Parser.Varconstdecl_stmtContext,0)


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




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_list)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.varconstdecl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.forin_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 321
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 322
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 323
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 324
                self.methodinvocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 325
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varconstdecl_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributetype(self):
            return self.getTypedRuleContext(D96Parser.AttributetypeContext,0)


        def varconstname_list(self):
            return self.getTypedRuleContext(D96Parser.Varconstname_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varconstdecl_stmt




    def varconstdecl_stmt(self):

        localctx = D96Parser.Varconstdecl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_varconstdecl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.attributetype()
            self.state = 329
            self.varconstname_list()
            self.state = 330
            self.match(D96Parser.CL)
            self.state = 331
            self.datatype()
            self.state = 332
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varconstname_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_normal(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_normal)
            else:
                return self.getToken(D96Parser.ID_normal, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_varconstname_list




    def varconstname_list(self):

        localctx = D96Parser.Varconstname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_varconstname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(D96Parser.ID_normal)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 335
                self.match(D96Parser.CM)
                self.state = 336
                self.match(D96Parser.ID_normal)
                self.state = 341
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expression()
            self.state = 343
            self.match(D96Parser.ASSIGN)
            self.state = 344
            self.expression()
            self.state = 345
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

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




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D96Parser.IF)
            self.state = 348
            self.match(D96Parser.LP)
            self.state = 349
            self.expression()
            self.state = 350
            self.match(D96Parser.RP)
            self.state = 351
            self.block_stmt()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 352
                self.match(D96Parser.ELSEIF)
                self.state = 353
                self.match(D96Parser.LP)
                self.state = 354
                self.expression()
                self.state = 355
                self.match(D96Parser.RP)
                self.state = 356
                self.block_stmt()
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 363
                self.match(D96Parser.ELSE)
                self.state = 364
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def scalar_var(self):
            return self.getTypedRuleContext(D96Parser.Scalar_varContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr1(self):
            return self.getTypedRuleContext(D96Parser.Expr1Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_forin_stmt




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.FOREACH)
            self.state = 368
            self.match(D96Parser.LP)
            self.state = 369
            self.scalar_var()
            self.state = 370
            self.match(D96Parser.IN)
            self.state = 371
            self.expr1()
            self.state = 372
            self.match(D96Parser.T__3)
            self.state = 373
            self.expr2()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LP:
                self.state = 374
                self.match(D96Parser.LP)
                self.state = 375
                self.match(D96Parser.BY)
                self.state = 376
                self.expr3()
                self.state = 377
                self.match(D96Parser.RP)


            self.state = 381
            self.match(D96Parser.RP)
            self.state = 382
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_var




    def scalar_var(self):

        localctx = D96Parser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2




    def expr2(self):

        localctx = D96Parser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3




    def expr3(self):

        localctx = D96Parser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.BREAK)
            self.state = 393
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.CONTINUE)
            self.state = 396
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

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




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(D96Parser.RETURN)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__2:
                self.state = 399
                self.expression()


            self.state = 402
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methodinvocation_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodinvocation_stmt




    def methodinvocation_stmt(self):

        localctx = D96Parser.Methodinvocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodinvocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(D96Parser.LCB)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.LCB:
                self.state = 407
                self.block_stmt()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





