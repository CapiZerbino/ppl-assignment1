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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0208\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\7\2p\n\2\f\2\16\2s")
        buf.write("\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\7\3\7\7\7\u0090\n\7\f\7\16\7\u0093\13\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u009f\n\t\f\t\16")
        buf.write("\t\u00a2\13\t\3\n\3\n\5\n\u00a6\n\n\3\13\3\13\3\13\5\13")
        buf.write("\u00ab\n\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b3\n")
        buf.write("\13\3\f\3\f\3\f\7\f\u00b8\n\f\f\f\16\f\u00bb\13\f\3\r")
        buf.write("\3\r\3\r\7\r\u00c0\n\r\f\r\16\r\u00c3\13\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\7\17\u00cd\n\17\f\17\16\17\u00d0")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00d8\n\20\f")
        buf.write("\20\16\20\u00db\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00e3\n\21\f\21\16\21\u00e6\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u00ee\n\22\f\22\16\22\u00f1\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\7\23\u00f9\n\23\f\23\16\23")
        buf.write("\u00fc\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0104")
        buf.write("\n\24\f\24\16\24\u0107\13\24\3\25\3\25\3\25\5\25\u010c")
        buf.write("\n\25\3\26\3\26\3\26\5\26\u0111\n\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u0118\n\27\f\27\16\27\u011b\13\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\7\30\u0123\n\30\f\30\16\30\u0126")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u012e\n\31\f")
        buf.write("\31\16\31\u0131\13\31\3\32\3\32\3\32\5\32\u0136\n\32\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u013c\n\33\3\34\3\34\3\34\5\34")
        buf.write("\u0141\n\34\3\34\3\34\3\35\3\35\3\35\7\35\u0148\n\35\f")
        buf.write("\35\16\35\u014b\13\35\3\36\3\36\3\36\3\36\3\36\5\36\u0152")
        buf.write("\n\36\3\37\3\37\3\37\5\37\u0157\n\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u0160\n \3!\3!\3!\7!\u0165\n!\f!\16!\u0168")
        buf.write("\13!\3\"\3\"\3\"\7\"\u016d\n\"\f\"\16\"\u0170\13\"\3#")
        buf.write("\3#\3#\7#\u0175\n#\f#\16#\u0178\13#\3$\3$\3$\7$\u017d")
        buf.write("\n$\f$\16$\u0180\13$\3%\3%\3%\7%\u0185\n%\f%\16%\u0188")
        buf.write("\13%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\5\'\u0193\n\'\3(\3(")
        buf.write("\3(\3(\5(\u0199\n(\3(\3(\3(\3)\3)\3*\3*\7*\u01a2\n*\f")
        buf.write("*\16*\u01a5\13*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01b2")
        buf.write("\n+\3,\3,\3,\3,\3,\5,\u01b9\n,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\7.\u01c3\n.\f.\16.\u01c6\13.\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\5\60\u01cf\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u01d6\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u01e3\n\62\f\62\16\62\u01e6\13\62\3\62\3\62")
        buf.write("\5\62\u01ea\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01f5\n\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\5\66\u0202\n\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\2\n\36 \"$&,.\608\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjl\2\13\3\2\27\30\4\2\31\31::\3\2\20\23\3\2-")
        buf.write(".\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\66\67\2\u020d\2q")
        buf.write("\3\2\2\2\4w\3\2\2\2\6}\3\2\2\2\b\u0082\3\2\2\2\n\u0088")
        buf.write("\3\2\2\2\f\u0091\3\2\2\2\16\u0094\3\2\2\2\20\u009b\3\2")
        buf.write("\2\2\22\u00a5\3\2\2\2\24\u00b2\3\2\2\2\26\u00b4\3\2\2")
        buf.write("\2\30\u00bc\3\2\2\2\32\u00c7\3\2\2\2\34\u00c9\3\2\2\2")
        buf.write("\36\u00d1\3\2\2\2 \u00dc\3\2\2\2\"\u00e7\3\2\2\2$\u00f2")
        buf.write("\3\2\2\2&\u00fd\3\2\2\2(\u010b\3\2\2\2*\u0110\3\2\2\2")
        buf.write(",\u0112\3\2\2\2.\u011c\3\2\2\2\60\u0127\3\2\2\2\62\u0135")
        buf.write("\3\2\2\2\64\u013b\3\2\2\2\66\u013d\3\2\2\28\u0144\3\2")
        buf.write("\2\2:\u0151\3\2\2\2<\u0153\3\2\2\2>\u015f\3\2\2\2@\u0161")
        buf.write("\3\2\2\2B\u0169\3\2\2\2D\u0171\3\2\2\2F\u0179\3\2\2\2")
        buf.write("H\u0181\3\2\2\2J\u0189\3\2\2\2L\u0192\3\2\2\2N\u0194\3")
        buf.write("\2\2\2P\u019d\3\2\2\2R\u019f\3\2\2\2T\u01b1\3\2\2\2V\u01b3")
        buf.write("\3\2\2\2X\u01bc\3\2\2\2Z\u01bf\3\2\2\2\\\u01c7\3\2\2\2")
        buf.write("^\u01ce\3\2\2\2`\u01d5\3\2\2\2b\u01d7\3\2\2\2d\u01eb\3")
        buf.write("\2\2\2f\u01f9\3\2\2\2h\u01fc\3\2\2\2j\u01ff\3\2\2\2l\u0205")
        buf.write("\3\2\2\2np\5\b\5\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2")
        buf.write("\2\2rt\3\2\2\2sq\3\2\2\2tu\5\4\3\2uv\7\2\2\3v\3\3\2\2")
        buf.write("\2wx\7\26\2\2xy\7\3\2\2yz\78\2\2z{\5\6\4\2{|\79\2\2|\5")
        buf.write("\3\2\2\2}~\7\4\2\2~\177\7\64\2\2\177\u0080\7\65\2\2\u0080")
        buf.write("\u0081\5R*\2\u0081\7\3\2\2\2\u0082\u0083\7\26\2\2\u0083")
        buf.write("\u0084\5\n\6\2\u0084\u0085\78\2\2\u0085\u0086\5\f\7\2")
        buf.write("\u0086\u0087\79\2\2\u0087\t\3\2\2\2\u0088\u008b\7:\2\2")
        buf.write("\u0089\u008a\7\63\2\2\u008a\u008c\7:\2\2\u008b\u0089\3")
        buf.write("\2\2\2\u008b\u008c\3\2\2\2\u008c\13\3\2\2\2\u008d\u0090")
        buf.write("\5\16\b\2\u008e\u0090\5\24\13\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\r\3\2\2\2\u0093\u0091\3\2\2")
        buf.write("\2\u0094\u0095\t\2\2\2\u0095\u0096\5\20\t\2\u0096\u0097")
        buf.write("\7\63\2\2\u0097\u0098\5\32\16\2\u0098\u0099\5\22\n\2\u0099")
        buf.write("\u009a\7\60\2\2\u009a\17\3\2\2\2\u009b\u00a0\7:\2\2\u009c")
        buf.write("\u009d\7\61\2\2\u009d\u009f\7:\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4")
        buf.write("\7\'\2\2\u00a4\u00a6\5\34\17\2\u00a5\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\23\3\2\2\2\u00a7\u00a8\t\3\2\2\u00a8")
        buf.write("\u00aa\7\64\2\2\u00a9\u00ab\5\26\f\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\7\65\2\2\u00ad\u00b3\5R*\2\u00ae\u00af\7\32\2\2\u00af")
        buf.write("\u00b0\7\64\2\2\u00b0\u00b1\7\65\2\2\u00b1\u00b3\5R*\2")
        buf.write("\u00b2\u00a7\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b3\25\3\2")
        buf.write("\2\2\u00b4\u00b9\5\30\r\2\u00b5\u00b6\7\60\2\2\u00b6\u00b8")
        buf.write("\5\30\r\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\27\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bc\u00c1\7:\2\2\u00bd\u00be\7\61\2\2")
        buf.write("\u00be\u00c0\7:\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c3\3")
        buf.write("\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\7\63\2\2\u00c5")
        buf.write("\u00c6\5\32\16\2\u00c6\31\3\2\2\2\u00c7\u00c8\t\4\2\2")
        buf.write("\u00c8\33\3\2\2\2\u00c9\u00ce\5\36\20\2\u00ca\u00cb\7")
        buf.write("\61\2\2\u00cb\u00cd\5\36\20\2\u00cc\u00ca\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\35\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\b\20")
        buf.write("\1\2\u00d2\u00d3\5 \21\2\u00d3\u00d9\3\2\2\2\u00d4\u00d5")
        buf.write("\f\4\2\2\u00d5\u00d6\t\5\2\2\u00d6\u00d8\5\36\20\5\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\37\3\2\2\2\u00db\u00d9\3\2")
        buf.write("\2\2\u00dc\u00dd\b\21\1\2\u00dd\u00de\5\"\22\2\u00de\u00e4")
        buf.write("\3\2\2\2\u00df\u00e0\f\4\2\2\u00e0\u00e1\t\6\2\2\u00e1")
        buf.write("\u00e3\5 \21\5\u00e2\u00df\3\2\2\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5!\3\2\2")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\b\22\1\2\u00e8\u00e9")
        buf.write("\5$\23\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f\4\2\2\u00eb")
        buf.write("\u00ec\t\7\2\2\u00ec\u00ee\5$\23\2\u00ed\u00ea\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0#\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3")
        buf.write("\b\23\1\2\u00f3\u00f4\5&\24\2\u00f4\u00fa\3\2\2\2\u00f5")
        buf.write("\u00f6\f\4\2\2\u00f6\u00f7\t\b\2\2\u00f7\u00f9\5&\24\2")
        buf.write("\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fa\u00fb\3\2\2\2\u00fb%\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\b\24\1\2\u00fe\u00ff\5(\25\2\u00ff")
        buf.write("\u0105\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102\t\t\2\2")
        buf.write("\u0102\u0104\5(\25\2\u0103\u0100\3\2\2\2\u0104\u0107\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\'")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7#\2\2\u0109")
        buf.write("\u010c\5(\25\2\u010a\u010c\5*\26\2\u010b\u0108\3\2\2\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c)\3\2\2\2\u010d\u010e\7\37\2")
        buf.write("\2\u010e\u0111\5*\26\2\u010f\u0111\5,\27\2\u0110\u010d")
        buf.write("\3\2\2\2\u0110\u010f\3\2\2\2\u0111+\3\2\2\2\u0112\u0113")
        buf.write("\b\27\1\2\u0113\u0114\5.\30\2\u0114\u0119\3\2\2\2\u0115")
        buf.write("\u0116\f\4\2\2\u0116\u0118\t\n\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3")
        buf.write("\2\2\2\u011a-\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d")
        buf.write("\b\30\1\2\u011d\u011e\5\60\31\2\u011e\u0124\3\2\2\2\u011f")
        buf.write("\u0120\f\4\2\2\u0120\u0121\7\62\2\2\u0121\u0123\5\60\31")
        buf.write("\2\u0122\u011f\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125/\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0127\u0128\b\31\1\2\u0128\u0129\5\62\32\2\u0129")
        buf.write("\u012f\3\2\2\2\u012a\u012b\f\4\2\2\u012b\u012c\7/\2\2")
        buf.write("\u012c\u012e\5\60\31\5\u012d\u012a\3\2\2\2\u012e\u0131")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\61\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0133\7\33\2\2\u0133")
        buf.write("\u0136\5\62\32\2\u0134\u0136\5\64\33\2\u0135\u0132\3\2")
        buf.write("\2\2\u0135\u0134\3\2\2\2\u0136\63\3\2\2\2\u0137\u013c")
        buf.write("\7:\2\2\u0138\u013c\5:\36\2\u0139\u013c\5\66\34\2\u013a")
        buf.write("\u013c\5N(\2\u013b\u0137\3\2\2\2\u013b\u0138\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013a\3\2\2\2\u013c\65\3\2\2\2\u013d")
        buf.write("\u013e\7:\2\2\u013e\u0140\7\64\2\2\u013f\u0141\58\35\2")
        buf.write("\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142\u0143\7\65\2\2\u0143\67\3\2\2\2\u0144\u0149")
        buf.write("\5\36\20\2\u0145\u0146\7\61\2\2\u0146\u0148\5\36\20\2")
        buf.write("\u0147\u0145\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u0149\u014a\3\2\2\2\u014a9\3\2\2\2\u014b\u0149")
        buf.write("\3\2\2\2\u014c\u0152\7;\2\2\u014d\u0152\7<\2\2\u014e\u0152")
        buf.write("\7=\2\2\u014f\u0152\7>\2\2\u0150\u0152\5<\37\2\u0151\u014c")
        buf.write("\3\2\2\2\u0151\u014d\3\2\2\2\u0151\u014e\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152;\3\2\2\2\u0153")
        buf.write("\u0154\7\16\2\2\u0154\u0156\7\64\2\2\u0155\u0157\5> \2")
        buf.write("\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u0159\7\65\2\2\u0159=\3\2\2\2\u015a\u0160")
        buf.write("\5@!\2\u015b\u0160\5B\"\2\u015c\u0160\5D#\2\u015d\u0160")
        buf.write("\5F$\2\u015e\u0160\5H%\2\u015f\u015a\3\2\2\2\u015f\u015b")
        buf.write("\3\2\2\2\u015f\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160?\3\2\2\2\u0161\u0166\7;\2\2\u0162")
        buf.write("\u0163\7\61\2\2\u0163\u0165\7;\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167A\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016e")
        buf.write("\7<\2\2\u016a\u016b\7\61\2\2\u016b\u016d\7<\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016fC\3\2\2\2\u0170\u016e\3\2\2")
        buf.write("\2\u0171\u0176\7=\2\2\u0172\u0173\7\61\2\2\u0173\u0175")
        buf.write("\7=\2\2\u0174\u0172\3\2\2\2\u0175\u0178\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177E\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179\u017e\7>\2\2\u017a\u017b\7\61\2\2")
        buf.write("\u017b\u017d\7>\2\2\u017c\u017a\3\2\2\2\u017d\u0180\3")
        buf.write("\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fG")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0186\5<\37\2\u0182")
        buf.write("\u0183\7\61\2\2\u0183\u0185\5<\37\2\u0184\u0182\3\2\2")
        buf.write("\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187I\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a")
        buf.write("\7\16\2\2\u018a\u018b\7\66\2\2\u018b\u018c\5L\'\2\u018c")
        buf.write("\u018d\7\61\2\2\u018d\u018e\7;\2\2\u018e\u018f\7\67\2")
        buf.write("\2\u018fK\3\2\2\2\u0190\u0193\5\32\16\2\u0191\u0193\7")
        buf.write("\16\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("M\3\2\2\2\u0194\u0195\7\33\2\2\u0195\u0196\7:\2\2\u0196")
        buf.write("\u0198\7\64\2\2\u0197\u0199\5\34\17\2\u0198\u0197\3\2")
        buf.write("\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b")
        buf.write("\7\65\2\2\u019b\u019c\7\60\2\2\u019cO\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019eQ\3\2\2\2\u019f\u01a3\78\2\2\u01a0\u01a2")
        buf.write("\5T+\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a7\79\2\2\u01a7S\3\2\2\2\u01a8")
        buf.write("\u01b2\5V,\2\u01a9\u01b2\5\\/\2\u01aa\u01b2\5b\62\2\u01ab")
        buf.write("\u01b2\5d\63\2\u01ac\u01b2\5f\64\2\u01ad\u01b2\5h\65\2")
        buf.write("\u01ae\u01b2\5j\66\2\u01af\u01b2\5l\67\2\u01b0\u01b2\5")
        buf.write("R*\2\u01b1\u01a8\3\2\2\2\u01b1\u01a9\3\2\2\2\u01b1\u01aa")
        buf.write("\3\2\2\2\u01b1\u01ab\3\2\2\2\u01b1\u01ac\3\2\2\2\u01b1")
        buf.write("\u01ad\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b0\3\2\2\2\u01b2U\3\2\2\2\u01b3\u01b4\t\2\2")
        buf.write("\2\u01b4\u01b5\5Z.\2\u01b5\u01b6\7\63\2\2\u01b6\u01b8")
        buf.write("\5\32\16\2\u01b7\u01b9\5X-\2\u01b8\u01b7\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\7\60\2")
        buf.write("\2\u01bbW\3\2\2\2\u01bc\u01bd\7\'\2\2\u01bd\u01be\5\34")
        buf.write("\17\2\u01beY\3\2\2\2\u01bf\u01c4\7:\2\2\u01c0\u01c1\7")
        buf.write("\61\2\2\u01c1\u01c3\7:\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("[\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\5^\60\2\u01c8")
        buf.write("\u01c9\7\'\2\2\u01c9\u01ca\5`\61\2\u01ca\u01cb\7\60\2")
        buf.write("\2\u01cb]\3\2\2\2\u01cc\u01cf\7:\2\2\u01cd\u01cf\5P)\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf_\3\2\2")
        buf.write("\2\u01d0\u01d1\5^\60\2\u01d1\u01d2\7\'\2\2\u01d2\u01d3")
        buf.write("\5`\61\2\u01d3\u01d6\3\2\2\2\u01d4\u01d6\5\36\20\2\u01d5")
        buf.write("\u01d0\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6a\3\2\2\2\u01d7")
        buf.write("\u01d8\7\b\2\2\u01d8\u01d9\7\64\2\2\u01d9\u01da\5\36\20")
        buf.write("\2\u01da\u01db\7\65\2\2\u01db\u01e4\5R*\2\u01dc\u01dd")
        buf.write("\7\t\2\2\u01dd\u01de\7\64\2\2\u01de\u01df\5\36\20\2\u01df")
        buf.write("\u01e0\7\65\2\2\u01e0\u01e1\5R*\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01dc\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e9\3\2\2\2\u01e6\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e8\7\n\2\2\u01e8\u01ea\5R*\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01eac\3\2\2\2\u01eb\u01ec")
        buf.write("\7\13\2\2\u01ec\u01ed\7\64\2\2\u01ed\u01ee\7:\2\2\u01ee")
        buf.write("\u01ef\7\17\2\2\u01ef\u01f0\7;\2\2\u01f0\u01f1\7\5\2\2")
        buf.write("\u01f1\u01f4\7;\2\2\u01f2\u01f3\7\34\2\2\u01f3\u01f5\7")
        buf.write(";\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f7\7\65\2\2\u01f7\u01f8\5R*\2\u01f8")
        buf.write("e\3\2\2\2\u01f9\u01fa\7\6\2\2\u01fa\u01fb\7\60\2\2\u01fb")
        buf.write("g\3\2\2\2\u01fc\u01fd\7\7\2\2\u01fd\u01fe\7\60\2\2\u01fe")
        buf.write("i\3\2\2\2\u01ff\u0201\7\24\2\2\u0200\u0202\5\36\20\2\u0201")
        buf.write("\u0200\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\3\2\2\2")
        buf.write("\u0203\u0204\7\60\2\2\u0204k\3\2\2\2\u0205\u0206\7\27")
        buf.write("\2\2\u0206m\3\2\2\2/q\u008b\u008f\u0091\u00a0\u00a5\u00aa")
        buf.write("\u00b2\u00b9\u00c1\u00ce\u00d9\u00e4\u00ef\u00fa\u0105")
        buf.write("\u010b\u0110\u0119\u0124\u012f\u0135\u013b\u0140\u0149")
        buf.write("\u0151\u0156\u015f\u0166\u016e\u0176\u017e\u0186\u0192")
        buf.write("\u0198\u01a3\u01b1\u01b8\u01c4\u01ce\u01d5\u01e4\u01e9")
        buf.write("\u01f4\u0201")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'main'", "'..'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
                     "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
                     "'::'", "';'", "','", "'.'", "':'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                      "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
                      "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "WRITELN", 
                      "PLUS", "MINUS", "STAR", "DIV", "MOD", "NOT", "ANDAND", 
                      "OROR", "EQ", "ASSIGN", "NE", "GT", "GE", "LS", "LE", 
                      "STR_CMP", "STR_CONCAT", "DCL", "SM", "CM", "DOT", 
                      "CL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                      "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "SDIGIT", "WS", "BLOCKCOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

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
    RULE_block_stmt = 40
    RULE_stmt_list = 41
    RULE_vardecl_stmt = 42
    RULE_var_init = 43
    RULE_varname_list = 44
    RULE_assign_stmt = 45
    RULE_assign_lhs = 46
    RULE_assign_tail = 47
    RULE_if_stmt = 48
    RULE_forin_stmt = 49
    RULE_break_stmt = 50
    RULE_continue_stmt = 51
    RULE_return_stmt = 52
    RULE_methodinvocation_stmt = 53

    ruleNames =  [ "program", "class_init", "body", "class_decl", "classname", 
                   "classbody", "attribute_decl", "attributename_list", 
                   "attribute_init", "method_decl", "parameter_list", "parameter", 
                   "primitive_types", "expression_list", "expression", "expr_1", 
                   "expr_2", "expr_3", "expr_4", "expr_5", "expr_6", "expr_7", 
                   "expr_8", "expr_9", "expr_10", "operands", "call_expr", 
                   "expr_list", "literals", "array_lit", "array_list", "arrayitemint_list", 
                   "arrayitemfloat_list", "arrayitembool_list", "arrayitemstring_list", 
                   "arrayitemarray_list", "array_decl", "element_type", 
                   "object_create", "index_expression", "block_stmt", "stmt_list", 
                   "vardecl_stmt", "var_init", "varname_list", "assign_stmt", 
                   "assign_lhs", "assign_tail", "if_stmt", "forin_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "methodinvocation_stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BREAK=4
    CONTINUE=5
    IF=6
    ELSEIF=7
    ELSE=8
    FOREACH=9
    TRUE=10
    FALSE=11
    ARRAY=12
    IN=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    STRING=17
    RETURN=18
    NULL=19
    CLASS=20
    VAL=21
    VAR=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    NEW=25
    BY=26
    WRITELN=27
    PLUS=28
    MINUS=29
    STAR=30
    DIV=31
    MOD=32
    NOT=33
    ANDAND=34
    OROR=35
    EQ=36
    ASSIGN=37
    NE=38
    GT=39
    GE=40
    LS=41
    LE=42
    STR_CMP=43
    STR_CONCAT=44
    DCL=45
    SM=46
    CM=47
    DOT=48
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
    BOOL_LIT=59
    STRING_LIT=60
    SDIGIT=61
    WS=62
    BLOCKCOMMENT=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

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
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 108
                    self.class_decl() 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 114
            self.class_init()
            self.state = 115
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
            self.state = 117
            self.match(D96Parser.CLASS)
            self.state = 118
            self.match(D96Parser.T__0)
            self.state = 119
            self.match(D96Parser.LCB)
            self.state = 120
            self.body()
            self.state = 121
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

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(D96Parser.T__1)
            self.state = 124
            self.match(D96Parser.LP)
            self.state = 125
            self.match(D96Parser.RP)
            self.state = 126
            self.block_stmt()
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
            self.state = 128
            self.match(D96Parser.CLASS)
            self.state = 129
            self.classname()
            self.state = 130
            self.match(D96Parser.LCB)
            self.state = 131
            self.classbody()
            self.state = 132
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
            self.state = 134
            self.match(D96Parser.IDENTIFIER)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 135
                self.match(D96Parser.CL)
                self.state = 136
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
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 141
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 139
                    self.attribute_decl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDENTIFIER]:
                    self.state = 140
                    self.method_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 145
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

        def attributename_list(self):
            return self.getTypedRuleContext(D96Parser.Attributename_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


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




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 147
            self.attributename_list()
            self.state = 148
            self.match(D96Parser.CL)
            self.state = 149
            self.primitive_types()
            self.state = 150
            self.attribute_init()
            self.state = 151
            self.match(D96Parser.SM)
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




    def attributename_list(self):

        localctx = D96Parser.Attributename_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributename_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(D96Parser.IDENTIFIER)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 154
                self.match(D96Parser.CM)
                self.state = 155
                self.match(D96Parser.IDENTIFIER)
                self.state = 160
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
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 161
                self.match(D96Parser.ASSIGN)
                self.state = 162
                self.expression_list()


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
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==D96Parser.CONSTRUCTOR or _la==D96Parser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.match(D96Parser.LP)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 167
                    self.parameter_list()


                self.state = 170
                self.match(D96Parser.RP)
                self.state = 171
                self.block_stmt()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(D96Parser.DESTRUCTOR)
                self.state = 173
                self.match(D96Parser.LP)
                self.state = 174
                self.match(D96Parser.RP)
                self.state = 175
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
        self.enterRule(localctx, 20, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.parameter()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 179
                self.match(D96Parser.SM)
                self.state = 180
                self.parameter()
                self.state = 185
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

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(D96Parser.IDENTIFIER)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 187
                self.match(D96Parser.CM)
                self.state = 188
                self.match(D96Parser.IDENTIFIER)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(D96Parser.CL)
            self.state = 195
            self.primitive_types()
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
        self.enterRule(localctx, 24, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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
        self.enterRule(localctx, 26, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expression(0)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 200
                self.match(D96Parser.CM)
                self.state = 201
                self.expression(0)
                self.state = 206
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
            self.state = 208
            self.expr_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 212
                    self.expression(3) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_1Context(ParserRuleContext):

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
            self.state = 219
            self.expr_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_1)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GE) | (1 << D96Parser.LS) | (1 << D96Parser.LE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.expr_1(3) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_2Context(ParserRuleContext):

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
            self.state = 230
            self.expr_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_2)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDAND or _la==D96Parser.OROR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 234
                    self.expr_3(0) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_3Context(ParserRuleContext):

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
            self.state = 241
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.expr_4(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_4Context(ParserRuleContext):

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
            self.state = 252
            self.expr_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.STAR) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.expr_5() 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_5Context(ParserRuleContext):

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




    def expr_5(self):

        localctx = D96Parser.Expr_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_5)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(D96Parser.NOT)
                self.state = 263
                self.expr_5()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NEW, D96Parser.MINUS, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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




    def expr_6(self):

        localctx = D96Parser.Expr_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_6)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(D96Parser.MINUS)
                self.state = 268
                self.expr_6()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NEW, D96Parser.IDENTIFIER, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
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
            self.state = 273
            self.expr_8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_7)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LSB or _la==D96Parser.RSB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_8Context(ParserRuleContext):

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



    def expr_8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr_8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expr_9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_8)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    self.match(D96Parser.DOT)
                    self.state = 287
                    self.expr_9(0) 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_9Context(ParserRuleContext):

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



    def expr_9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr_9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.expr_10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_9)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    self.match(D96Parser.DCL)
                    self.state = 298
                    self.expr_9(3) 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_10Context(ParserRuleContext):

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




    def expr_10(self):

        localctx = D96Parser.Expr_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_10)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(D96Parser.NEW)
                self.state = 305
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
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


        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operands)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.object_create()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):

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




    def call_expr(self):

        localctx = D96Parser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.IDENTIFIER)
            self.state = 316
            self.match(D96Parser.LP)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 317
                self.expr_list()


            self.state = 320
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):

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




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.expression(0)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 323
                self.match(D96Parser.CM)
                self.state = 324
                self.expression(0)
                self.state = 329
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
        self.enterRule(localctx, 56, self.RULE_literals)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.match(D96Parser.BOOL_LIT)
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
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
        self.enterRule(localctx, 58, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(D96Parser.ARRAY)
            self.state = 338
            self.match(D96Parser.LP)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 339
                self.array_list()


            self.state = 342
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
        self.enterRule(localctx, 60, self.RULE_array_list)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.arrayitemint_list()
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.arrayitemfloat_list()
                pass
            elif token in [D96Parser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.arrayitembool_list()
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.arrayitemstring_list()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
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
        self.enterRule(localctx, 62, self.RULE_arrayitemint_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(D96Parser.INT_LIT)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 352
                self.match(D96Parser.CM)
                self.state = 353
                self.match(D96Parser.INT_LIT)
                self.state = 358
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
        self.enterRule(localctx, 64, self.RULE_arrayitemfloat_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.FLOAT_LIT)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 360
                self.match(D96Parser.CM)
                self.state = 361
                self.match(D96Parser.FLOAT_LIT)
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
        self.enterRule(localctx, 66, self.RULE_arrayitembool_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.BOOL_LIT)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 368
                self.match(D96Parser.CM)
                self.state = 369
                self.match(D96Parser.BOOL_LIT)
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
        self.enterRule(localctx, 68, self.RULE_arrayitemstring_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(D96Parser.STRING_LIT)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 376
                self.match(D96Parser.CM)
                self.state = 377
                self.match(D96Parser.STRING_LIT)
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
        self.enterRule(localctx, 70, self.RULE_arrayitemarray_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.array_lit()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 384
                self.match(D96Parser.CM)
                self.state = 385
                self.array_lit()
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

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl




    def array_decl(self):

        localctx = D96Parser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(D96Parser.ARRAY)
            self.state = 392
            self.match(D96Parser.LSB)
            self.state = 393
            self.element_type()
            self.state = 394
            self.match(D96Parser.CM)
            self.state = 395
            self.match(D96Parser.INT_LIT)
            self.state = 396
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
        self.enterRule(localctx, 74, self.RULE_element_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 398
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 399
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




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(D96Parser.NEW)
            self.state = 403
            self.match(D96Parser.IDENTIFIER)
            self.state = 404
            self.match(D96Parser.LP)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 405
                self.expression_list()


            self.state = 408
            self.match(D96Parser.RP)
            self.state = 409
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression




    def index_expression(self):

        localctx = D96Parser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_listContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(D96Parser.LCB)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.LCB) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 414
                self.stmt_list()
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 420
            self.match(D96Parser.RCB)
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




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_list)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.vardecl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 424
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 425
                self.forin_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 426
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 427
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 428
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 429
                self.methodinvocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 430
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varname_list(self):
            return self.getTypedRuleContext(D96Parser.Varname_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


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




    def vardecl_stmt(self):

        localctx = D96Parser.Vardecl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_vardecl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 434
            self.varname_list()
            self.state = 435
            self.match(D96Parser.CL)
            self.state = 436
            self.primitive_types()
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 437
                self.var_init()


            self.state = 440
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_init




    def var_init(self):

        localctx = D96Parser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(D96Parser.ASSIGN)
            self.state = 443
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varname_listContext(ParserRuleContext):

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




    def varname_list(self):

        localctx = D96Parser.Varname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_varname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.IDENTIFIER)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 446
                self.match(D96Parser.CM)
                self.state = 447
                self.match(D96Parser.IDENTIFIER)
                self.state = 452
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




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.assign_lhs()
            self.state = 454
            self.match(D96Parser.ASSIGN)
            self.state = 455
            self.assign_tail()
            self.state = 456
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assign_lhs)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.index_expression()
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


    class Assign_tailContext(ParserRuleContext):

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




    def assign_tail(self):

        localctx = D96Parser.Assign_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assign_tail)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.assign_lhs()
                self.state = 463
                self.match(D96Parser.ASSIGN)
                self.state = 464
                self.assign_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
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
        self.enterRule(localctx, 96, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(D96Parser.IF)
            self.state = 470
            self.match(D96Parser.LP)
            self.state = 471
            self.expression(0)
            self.state = 472
            self.match(D96Parser.RP)
            self.state = 473
            self.block_stmt()
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 474
                self.match(D96Parser.ELSEIF)
                self.state = 475
                self.match(D96Parser.LP)
                self.state = 476
                self.expression(0)
                self.state = 477
                self.match(D96Parser.RP)
                self.state = 478
                self.block_stmt()
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 485
                self.match(D96Parser.ELSE)
                self.state = 486
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

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forin_stmt




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(D96Parser.FOREACH)
            self.state = 490
            self.match(D96Parser.LP)
            self.state = 491
            self.match(D96Parser.IDENTIFIER)
            self.state = 492
            self.match(D96Parser.IN)
            self.state = 493
            self.match(D96Parser.INT_LIT)
            self.state = 494
            self.match(D96Parser.T__2)
            self.state = 495
            self.match(D96Parser.INT_LIT)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 496
                self.match(D96Parser.BY)
                self.state = 497
                self.match(D96Parser.INT_LIT)


            self.state = 500
            self.match(D96Parser.RP)
            self.state = 501
            self.block_stmt()
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
        self.enterRule(localctx, 100, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.BREAK)
            self.state = 504
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
        self.enterRule(localctx, 102, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.CONTINUE)
            self.state = 507
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
        self.enterRule(localctx, 104, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(D96Parser.RETURN)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.STRING_LIT))) != 0):
                self.state = 510
                self.expression(0)


            self.state = 513
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
        self.enterRule(localctx, 106, self.RULE_methodinvocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(D96Parser.VAL)
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
         




