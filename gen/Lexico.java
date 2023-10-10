// Generated from C:/Users/Tobias Romano/Desktop/Compiladores/TPE_COMPILADORES_2023/Lexico.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class Lexico extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, END_IF=3, PRINT=4, CLASS=5, VOID=6, INT=7, ULONG=8, FLOAT=9, 
		WHILE=10, DO=11, MENORIGUAL=12, MAYORIGUAL=13, DISTINTO=14, ID=15, ERROR=16, 
		NUM_INT=17, NUM_ULONG=18, NUM_FLOAT=19, RETURN=20, CADENA=21, COMPIGUAL=22, 
		FIN=23, PLUS=24, MINUS=25, COMMA=26, DIVIDE=27, MULTIPLY=28, LEFT_PAREN=29, 
		RIGHT_PAREN=30, LESS_THAN=31, GREATER_THAN=32, SEMICOLON=33, EQUALS=34, 
		LEFT_BRACE=35, RIGHT_BRACE=36, DOUBLE_MINUS=37, DOT=38, WS=39;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IF", "ELSE", "END_IF", "PRINT", "CLASS", "VOID", "INT", "ULONG", "FLOAT", 
			"WHILE", "DO", "MENORIGUAL", "MAYORIGUAL", "DISTINTO", "ID", "ERROR", 
			"NUM_INT", "NUM_ULONG", "NUM_FLOAT", "RETURN", "CADENA", "COMPIGUAL", 
			"FIN", "PLUS", "MINUS", "COMMA", "DIVIDE", "MULTIPLY", "LEFT_PAREN", 
			"RIGHT_PAREN", "LESS_THAN", "GREATER_THAN", "SEMICOLON", "EQUALS", "LEFT_BRACE", 
			"RIGHT_BRACE", "DOUBLE_MINUS", "DOT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'IF'", "'ELSE'", "'END_IF'", "'PRINT'", "'CLASS'", "'VOID'", "'INT'", 
			"'ULONG'", "'FLOAT'", "'WHILE'", "'DO'", "'MENORIGUAL'", "'MAYORIGUAL'", 
			"'DISTINTO'", "'ID'", "'ERROR'", "'NUM_INT'", "'NUM_ULONG'", "'NUM_FLOAT'", 
			"'RETURN'", "'CADENA'", "'COMPIGUAL'", "'FIN'", "'+'", "'-'", "','", 
			"'/'", "'*'", "'('", "')'", "'<'", "'>'", "';'", "'='", "'{'", "'}'", 
			"'--'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "END_IF", "PRINT", "CLASS", "VOID", "INT", "ULONG", 
			"FLOAT", "WHILE", "DO", "MENORIGUAL", "MAYORIGUAL", "DISTINTO", "ID", 
			"ERROR", "NUM_INT", "NUM_ULONG", "NUM_FLOAT", "RETURN", "CADENA", "COMPIGUAL", 
			"FIN", "PLUS", "MINUS", "COMMA", "DIVIDE", "MULTIPLY", "LEFT_PAREN", 
			"RIGHT_PAREN", "LESS_THAN", "GREATER_THAN", "SEMICOLON", "EQUALS", "LEFT_BRACE", 
			"RIGHT_BRACE", "DOUBLE_MINUS", "DOT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	    from AnalizadorLexico.Token import Token
	    IF          : 'IF' { 500; };
	    ELSE        : 'ELSE' { setType(Token.ELSE); };
	    END_IF      : 'END_IF' { setType(Token.END_IF); };
	    PRINT       : 'PRINT' { setType(Token.PRINT); };
	    CLASS       : 'CLASS' { setType(Token.CLASS); };
	    VOID        : 'VOID' { setType(Token.VOID); };
	    INT         : 'INT' { setType(Token.INT); };
	    ULONG       : 'ULONG' { setType(Token.ULONG); };
	    FLOAT       : 'FLOAT' { setType(Token.FLOAT); };
	    WHILE       : 'WHILE' { setType(Token.WHILE); };
	    DO          : 'DO' { setType(Token.DO); };
	    MENORIGUAL  : 'MENORIGUAL' { setType(Token.MENORIGUAL); };
	    MAYORIGUAL  : 'MAYORIGUAL' { setType(Token.MAYORIGUAL); };
	    DISTINTO    : 'DISTINTO' { setType(Token.DISTINTO); };
	    ID          : 'ID' { setType(Token.ID); };
	    ERROR       : 'ERROR' { setType(Token.ERROR); };
	    NUM_INT     : 'NUM_INT' { setType(Token.NUM_INT); };
	    NUM_ULONG   : 'NUM_ULONG' { setType(Token.NUM_ULONG); };
	    NUM_FLOAT   : 'NUM_FLOAT' { setType(Token.NUM_FLOAT); };
	    RETURN      : 'RETURN' { setType(Token.RETURN); };
	    CADENA      : 'CADENA' { setType(Token.CADENA); };
	    COMPIGUAL   : 'COMPIGUAL' { setType(Token.COMPIGUAL); };
	    FIN         : 'FIN' { setType(Token.FIN); };
	    PLUS : '+' { setType(43; };
	    MINUS : '-' { setType(45); };
	    COMMA : ',' { setType(44); };
	    DIVIDE : '/' { setType(47); };
	    MULTIPLY : '*' { setType(42); };
	    LEFT_PAREN : '(' { setType(40); };
	    RIGHT_PAREN : ')' { setType(41); };
	    LESS_THAN : '<' { setType(60); };
	    GREATER_THAN : '>' { setType(62); };
	    SEMICOLON : ';' { setType(59); };
	    EQUALS : '=' { setType(61); };
	    LEFT_BRACE : '{';
	    RIGHT_BRACE : '}';
	    DOUBLE_MINUS : '--';
	    DOT : '.';
	    WS : [ \t\r\n]+ -> skip;


	public Lexico(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Lexico.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 0:
			IF_action((RuleContext)_localctx, actionIndex);
			break;
		case 1:
			ELSE_action((RuleContext)_localctx, actionIndex);
			break;
		case 2:
			END_IF_action((RuleContext)_localctx, actionIndex);
			break;
		case 3:
			PRINT_action((RuleContext)_localctx, actionIndex);
			break;
		case 4:
			CLASS_action((RuleContext)_localctx, actionIndex);
			break;
		case 5:
			VOID_action((RuleContext)_localctx, actionIndex);
			break;
		case 6:
			INT_action((RuleContext)_localctx, actionIndex);
			break;
		case 7:
			ULONG_action((RuleContext)_localctx, actionIndex);
			break;
		case 8:
			FLOAT_action((RuleContext)_localctx, actionIndex);
			break;
		case 9:
			WHILE_action((RuleContext)_localctx, actionIndex);
			break;
		case 10:
			DO_action((RuleContext)_localctx, actionIndex);
			break;
		case 11:
			MENORIGUAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 12:
			MAYORIGUAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 13:
			DISTINTO_action((RuleContext)_localctx, actionIndex);
			break;
		case 14:
			ID_action((RuleContext)_localctx, actionIndex);
			break;
		case 15:
			ERROR_action((RuleContext)_localctx, actionIndex);
			break;
		case 16:
			NUM_INT_action((RuleContext)_localctx, actionIndex);
			break;
		case 17:
			NUM_ULONG_action((RuleContext)_localctx, actionIndex);
			break;
		case 18:
			NUM_FLOAT_action((RuleContext)_localctx, actionIndex);
			break;
		case 19:
			RETURN_action((RuleContext)_localctx, actionIndex);
			break;
		case 20:
			CADENA_action((RuleContext)_localctx, actionIndex);
			break;
		case 21:
			COMPIGUAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 22:
			FIN_action((RuleContext)_localctx, actionIndex);
			break;
		case 23:
			PLUS_action((RuleContext)_localctx, actionIndex);
			break;
		case 24:
			MINUS_action((RuleContext)_localctx, actionIndex);
			break;
		case 25:
			COMMA_action((RuleContext)_localctx, actionIndex);
			break;
		case 26:
			DIVIDE_action((RuleContext)_localctx, actionIndex);
			break;
		case 27:
			MULTIPLY_action((RuleContext)_localctx, actionIndex);
			break;
		case 28:
			LEFT_PAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 29:
			RIGHT_PAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 30:
			LESS_THAN_action((RuleContext)_localctx, actionIndex);
			break;
		case 31:
			GREATER_THAN_action((RuleContext)_localctx, actionIndex);
			break;
		case 32:
			SEMICOLON_action((RuleContext)_localctx, actionIndex);
			break;
		case 33:
			EQUALS_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void IF_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			 500; 
			break;
		}
	}
	private void ELSE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			 setType(Token.ELSE); 
			break;
		}
	}
	private void END_IF_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			 setType(Token.END_IF); 
			break;
		}
	}
	private void PRINT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			 setType(Token.PRINT); 
			break;
		}
	}
	private void CLASS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			 setType(Token.CLASS); 
			break;
		}
	}
	private void VOID_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			 setType(Token.VOID); 
			break;
		}
	}
	private void INT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:
			 setType(Token.INT); 
			break;
		}
	}
	private void ULONG_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 7:
			 setType(Token.ULONG); 
			break;
		}
	}
	private void FLOAT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 8:
			 setType(Token.FLOAT); 
			break;
		}
	}
	private void WHILE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 9:
			 setType(Token.WHILE); 
			break;
		}
	}
	private void DO_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 10:
			 setType(Token.DO); 
			break;
		}
	}
	private void MENORIGUAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 11:
			 setType(Token.MENORIGUAL); 
			break;
		}
	}
	private void MAYORIGUAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 12:
			 setType(Token.MAYORIGUAL); 
			break;
		}
	}
	private void DISTINTO_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 13:
			 setType(Token.DISTINTO); 
			break;
		}
	}
	private void ID_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 14:
			 setType(Token.ID); 
			break;
		}
	}
	private void ERROR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 15:
			 setType(Token.ERROR); 
			break;
		}
	}
	private void NUM_INT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 16:
			 setType(Token.NUM_INT); 
			break;
		}
	}
	private void NUM_ULONG_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 17:
			 setType(Token.NUM_ULONG); 
			break;
		}
	}
	private void NUM_FLOAT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 18:
			 setType(Token.NUM_FLOAT); 
			break;
		}
	}
	private void RETURN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 19:
			 setType(Token.RETURN); 
			break;
		}
	}
	private void CADENA_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 20:
			 setType(Token.CADENA); 
			break;
		}
	}
	private void COMPIGUAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 21:
			 setType(Token.COMPIGUAL); 
			break;
		}
	}
	private void FIN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 22:
			 setType(Token.FIN); 
			break;
		}
	}
	private void PLUS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 23:
			 setType(43; 
			break;
		}
	}
	private void MINUS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 24:
			 setType(45); 
			break;
		}
	}
	private void COMMA_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 25:
			 setType(44); 
			break;
		}
	}
	private void DIVIDE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 26:
			 setType(47); 
			break;
		}
	}
	private void MULTIPLY_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 27:
			 setType(42); 
			break;
		}
	}
	private void LEFT_PAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 28:
			 setType(40); 
			break;
		}
	}
	private void RIGHT_PAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 29:
			 setType(41); 
			break;
		}
	}
	private void LESS_THAN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 30:
			 setType(60); 
			break;
		}
	}
	private void GREATER_THAN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 31:
			 setType(62); 
			break;
		}
	}
	private void SEMICOLON_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 32:
			 setType(59); 
			break;
		}
	}
	private void EQUALS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 33:
			 setType(61); 
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000\'\u0147\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001\"\u0001\""+
		"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001%\u0001%\u0001&\u0004&\u0142"+
		"\b&\u000b&\f&\u0143\u0001&\u0001&\u0000\u0000\'\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b"+
		"7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%K&M\'\u0001\u0000\u0001\u0003"+
		"\u0000\t\n\r\r  \u0147\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000"+
		"\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000"+
		")\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001"+
		"\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000"+
		"\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u0000"+
		"7\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001"+
		"\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000"+
		"\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000"+
		"E\u0001\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001"+
		"\u0000\u0000\u0000\u0000K\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000"+
		"\u0000\u0001O\u0001\u0000\u0000\u0000\u0003T\u0001\u0000\u0000\u0000\u0005"+
		"[\u0001\u0000\u0000\u0000\u0007d\u0001\u0000\u0000\u0000\tl\u0001\u0000"+
		"\u0000\u0000\u000bt\u0001\u0000\u0000\u0000\r{\u0001\u0000\u0000\u0000"+
		"\u000f\u0081\u0001\u0000\u0000\u0000\u0011\u0089\u0001\u0000\u0000\u0000"+
		"\u0013\u0091\u0001\u0000\u0000\u0000\u0015\u0099\u0001\u0000\u0000\u0000"+
		"\u0017\u009e\u0001\u0000\u0000\u0000\u0019\u00ab\u0001\u0000\u0000\u0000"+
		"\u001b\u00b8\u0001\u0000\u0000\u0000\u001d\u00c3\u0001\u0000\u0000\u0000"+
		"\u001f\u00c8\u0001\u0000\u0000\u0000!\u00d0\u0001\u0000\u0000\u0000#\u00da"+
		"\u0001\u0000\u0000\u0000%\u00e6\u0001\u0000\u0000\u0000\'\u00f2\u0001"+
		"\u0000\u0000\u0000)\u00fb\u0001\u0000\u0000\u0000+\u0104\u0001\u0000\u0000"+
		"\u0000-\u0110\u0001\u0000\u0000\u0000/\u0116\u0001\u0000\u0000\u00001"+
		"\u0119\u0001\u0000\u0000\u00003\u011c\u0001\u0000\u0000\u00005\u011f\u0001"+
		"\u0000\u0000\u00007\u0122\u0001\u0000\u0000\u00009\u0125\u0001\u0000\u0000"+
		"\u0000;\u0128\u0001\u0000\u0000\u0000=\u012b\u0001\u0000\u0000\u0000?"+
		"\u012e\u0001\u0000\u0000\u0000A\u0131\u0001\u0000\u0000\u0000C\u0134\u0001"+
		"\u0000\u0000\u0000E\u0137\u0001\u0000\u0000\u0000G\u0139\u0001\u0000\u0000"+
		"\u0000I\u013b\u0001\u0000\u0000\u0000K\u013e\u0001\u0000\u0000\u0000M"+
		"\u0141\u0001\u0000\u0000\u0000OP\u0005I\u0000\u0000PQ\u0005F\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RS\u0006\u0000\u0000\u0000S\u0002\u0001\u0000"+
		"\u0000\u0000TU\u0005E\u0000\u0000UV\u0005L\u0000\u0000VW\u0005S\u0000"+
		"\u0000WX\u0005E\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0006\u0001\u0001"+
		"\u0000Z\u0004\u0001\u0000\u0000\u0000[\\\u0005E\u0000\u0000\\]\u0005N"+
		"\u0000\u0000]^\u0005D\u0000\u0000^_\u0005_\u0000\u0000_`\u0005I\u0000"+
		"\u0000`a\u0005F\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0006\u0002\u0002"+
		"\u0000c\u0006\u0001\u0000\u0000\u0000de\u0005P\u0000\u0000ef\u0005R\u0000"+
		"\u0000fg\u0005I\u0000\u0000gh\u0005N\u0000\u0000hi\u0005T\u0000\u0000"+
		"ij\u0001\u0000\u0000\u0000jk\u0006\u0003\u0003\u0000k\b\u0001\u0000\u0000"+
		"\u0000lm\u0005C\u0000\u0000mn\u0005L\u0000\u0000no\u0005A\u0000\u0000"+
		"op\u0005S\u0000\u0000pq\u0005S\u0000\u0000qr\u0001\u0000\u0000\u0000r"+
		"s\u0006\u0004\u0004\u0000s\n\u0001\u0000\u0000\u0000tu\u0005V\u0000\u0000"+
		"uv\u0005O\u0000\u0000vw\u0005I\u0000\u0000wx\u0005D\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000yz\u0006\u0005\u0005\u0000z\f\u0001\u0000\u0000\u0000"+
		"{|\u0005I\u0000\u0000|}\u0005N\u0000\u0000}~\u0005T\u0000\u0000~\u007f"+
		"\u0001\u0000\u0000\u0000\u007f\u0080\u0006\u0006\u0006\u0000\u0080\u000e"+
		"\u0001\u0000\u0000\u0000\u0081\u0082\u0005U\u0000\u0000\u0082\u0083\u0005"+
		"L\u0000\u0000\u0083\u0084\u0005O\u0000\u0000\u0084\u0085\u0005N\u0000"+
		"\u0000\u0085\u0086\u0005G\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0006\u0007\u0007\u0000\u0088\u0010\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0005F\u0000\u0000\u008a\u008b\u0005L\u0000\u0000\u008b\u008c"+
		"\u0005O\u0000\u0000\u008c\u008d\u0005A\u0000\u0000\u008d\u008e\u0005T"+
		"\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0006\b\b"+
		"\u0000\u0090\u0012\u0001\u0000\u0000\u0000\u0091\u0092\u0005W\u0000\u0000"+
		"\u0092\u0093\u0005H\u0000\u0000\u0093\u0094\u0005I\u0000\u0000\u0094\u0095"+
		"\u0005L\u0000\u0000\u0095\u0096\u0005E\u0000\u0000\u0096\u0097\u0001\u0000"+
		"\u0000\u0000\u0097\u0098\u0006\t\t\u0000\u0098\u0014\u0001\u0000\u0000"+
		"\u0000\u0099\u009a\u0005D\u0000\u0000\u009a\u009b\u0005O\u0000\u0000\u009b"+
		"\u009c\u0001\u0000\u0000\u0000\u009c\u009d\u0006\n\n\u0000\u009d\u0016"+
		"\u0001\u0000\u0000\u0000\u009e\u009f\u0005M\u0000\u0000\u009f\u00a0\u0005"+
		"E\u0000\u0000\u00a0\u00a1\u0005N\u0000\u0000\u00a1\u00a2\u0005O\u0000"+
		"\u0000\u00a2\u00a3\u0005R\u0000\u0000\u00a3\u00a4\u0005I\u0000\u0000\u00a4"+
		"\u00a5\u0005G\u0000\u0000\u00a5\u00a6\u0005U\u0000\u0000\u00a6\u00a7\u0005"+
		"A\u0000\u0000\u00a7\u00a8\u0005L\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000"+
		"\u0000\u00a9\u00aa\u0006\u000b\u000b\u0000\u00aa\u0018\u0001\u0000\u0000"+
		"\u0000\u00ab\u00ac\u0005M\u0000\u0000\u00ac\u00ad\u0005A\u0000\u0000\u00ad"+
		"\u00ae\u0005Y\u0000\u0000\u00ae\u00af\u0005O\u0000\u0000\u00af\u00b0\u0005"+
		"R\u0000\u0000\u00b0\u00b1\u0005I\u0000\u0000\u00b1\u00b2\u0005G\u0000"+
		"\u0000\u00b2\u00b3\u0005U\u0000\u0000\u00b3\u00b4\u0005A\u0000\u0000\u00b4"+
		"\u00b5\u0005L\u0000\u0000\u00b5\u00b6\u0001\u0000\u0000\u0000\u00b6\u00b7"+
		"\u0006\f\f\u0000\u00b7\u001a\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005"+
		"D\u0000\u0000\u00b9\u00ba\u0005I\u0000\u0000\u00ba\u00bb\u0005S\u0000"+
		"\u0000\u00bb\u00bc\u0005T\u0000\u0000\u00bc\u00bd\u0005I\u0000\u0000\u00bd"+
		"\u00be\u0005N\u0000\u0000\u00be\u00bf\u0005T\u0000\u0000\u00bf\u00c0\u0005"+
		"O\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2\u0006\r"+
		"\r\u0000\u00c2\u001c\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005I\u0000"+
		"\u0000\u00c4\u00c5\u0005D\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c6\u00c7\u0006\u000e\u000e\u0000\u00c7\u001e\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c9\u0005E\u0000\u0000\u00c9\u00ca\u0005R\u0000\u0000\u00ca\u00cb"+
		"\u0005R\u0000\u0000\u00cb\u00cc\u0005O\u0000\u0000\u00cc\u00cd\u0005R"+
		"\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce\u00cf\u0006\u000f"+
		"\u000f\u0000\u00cf \u0001\u0000\u0000\u0000\u00d0\u00d1\u0005N\u0000\u0000"+
		"\u00d1\u00d2\u0005U\u0000\u0000\u00d2\u00d3\u0005M\u0000\u0000\u00d3\u00d4"+
		"\u0005_\u0000\u0000\u00d4\u00d5\u0005I\u0000\u0000\u00d5\u00d6\u0005N"+
		"\u0000\u0000\u00d6\u00d7\u0005T\u0000\u0000\u00d7\u00d8\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d9\u0006\u0010\u0010\u0000\u00d9\"\u0001\u0000\u0000\u0000"+
		"\u00da\u00db\u0005N\u0000\u0000\u00db\u00dc\u0005U\u0000\u0000\u00dc\u00dd"+
		"\u0005M\u0000\u0000\u00dd\u00de\u0005_\u0000\u0000\u00de\u00df\u0005U"+
		"\u0000\u0000\u00df\u00e0\u0005L\u0000\u0000\u00e0\u00e1\u0005O\u0000\u0000"+
		"\u00e1\u00e2\u0005N\u0000\u0000\u00e2\u00e3\u0005G\u0000\u0000\u00e3\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e4\u00e5\u0006\u0011\u0011\u0000\u00e5$\u0001"+
		"\u0000\u0000\u0000\u00e6\u00e7\u0005N\u0000\u0000\u00e7\u00e8\u0005U\u0000"+
		"\u0000\u00e8\u00e9\u0005M\u0000\u0000\u00e9\u00ea\u0005_\u0000\u0000\u00ea"+
		"\u00eb\u0005F\u0000\u0000\u00eb\u00ec\u0005L\u0000\u0000\u00ec\u00ed\u0005"+
		"O\u0000\u0000\u00ed\u00ee\u0005A\u0000\u0000\u00ee\u00ef\u0005T\u0000"+
		"\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f1\u0006\u0012\u0012"+
		"\u0000\u00f1&\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005R\u0000\u0000\u00f3"+
		"\u00f4\u0005E\u0000\u0000\u00f4\u00f5\u0005T\u0000\u0000\u00f5\u00f6\u0005"+
		"U\u0000\u0000\u00f6\u00f7\u0005R\u0000\u0000\u00f7\u00f8\u0005N\u0000"+
		"\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u00fa\u0006\u0013\u0013"+
		"\u0000\u00fa(\u0001\u0000\u0000\u0000\u00fb\u00fc\u0005C\u0000\u0000\u00fc"+
		"\u00fd\u0005A\u0000\u0000\u00fd\u00fe\u0005D\u0000\u0000\u00fe\u00ff\u0005"+
		"E\u0000\u0000\u00ff\u0100\u0005N\u0000\u0000\u0100\u0101\u0005A\u0000"+
		"\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102\u0103\u0006\u0014\u0014"+
		"\u0000\u0103*\u0001\u0000\u0000\u0000\u0104\u0105\u0005C\u0000\u0000\u0105"+
		"\u0106\u0005O\u0000\u0000\u0106\u0107\u0005M\u0000\u0000\u0107\u0108\u0005"+
		"P\u0000\u0000\u0108\u0109\u0005I\u0000\u0000\u0109\u010a\u0005G\u0000"+
		"\u0000\u010a\u010b\u0005U\u0000\u0000\u010b\u010c\u0005A\u0000\u0000\u010c"+
		"\u010d\u0005L\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000\u010e\u010f"+
		"\u0006\u0015\u0015\u0000\u010f,\u0001\u0000\u0000\u0000\u0110\u0111\u0005"+
		"F\u0000\u0000\u0111\u0112\u0005I\u0000\u0000\u0112\u0113\u0005N\u0000"+
		"\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0115\u0006\u0016\u0016"+
		"\u0000\u0115.\u0001\u0000\u0000\u0000\u0116\u0117\u0005+\u0000\u0000\u0117"+
		"\u0118\u0006\u0017\u0017\u0000\u01180\u0001\u0000\u0000\u0000\u0119\u011a"+
		"\u0005-\u0000\u0000\u011a\u011b\u0006\u0018\u0018\u0000\u011b2\u0001\u0000"+
		"\u0000\u0000\u011c\u011d\u0005,\u0000\u0000\u011d\u011e\u0006\u0019\u0019"+
		"\u0000\u011e4\u0001\u0000\u0000\u0000\u011f\u0120\u0005/\u0000\u0000\u0120"+
		"\u0121\u0006\u001a\u001a\u0000\u01216\u0001\u0000\u0000\u0000\u0122\u0123"+
		"\u0005*\u0000\u0000\u0123\u0124\u0006\u001b\u001b\u0000\u01248\u0001\u0000"+
		"\u0000\u0000\u0125\u0126\u0005(\u0000\u0000\u0126\u0127\u0006\u001c\u001c"+
		"\u0000\u0127:\u0001\u0000\u0000\u0000\u0128\u0129\u0005)\u0000\u0000\u0129"+
		"\u012a\u0006\u001d\u001d\u0000\u012a<\u0001\u0000\u0000\u0000\u012b\u012c"+
		"\u0005<\u0000\u0000\u012c\u012d\u0006\u001e\u001e\u0000\u012d>\u0001\u0000"+
		"\u0000\u0000\u012e\u012f\u0005>\u0000\u0000\u012f\u0130\u0006\u001f\u001f"+
		"\u0000\u0130@\u0001\u0000\u0000\u0000\u0131\u0132\u0005;\u0000\u0000\u0132"+
		"\u0133\u0006  \u0000\u0133B\u0001\u0000\u0000\u0000\u0134\u0135\u0005"+
		"=\u0000\u0000\u0135\u0136\u0006!!\u0000\u0136D\u0001\u0000\u0000\u0000"+
		"\u0137\u0138\u0005{\u0000\u0000\u0138F\u0001\u0000\u0000\u0000\u0139\u013a"+
		"\u0005}\u0000\u0000\u013aH\u0001\u0000\u0000\u0000\u013b\u013c\u0005-"+
		"\u0000\u0000\u013c\u013d\u0005-\u0000\u0000\u013dJ\u0001\u0000\u0000\u0000"+
		"\u013e\u013f\u0005.\u0000\u0000\u013fL\u0001\u0000\u0000\u0000\u0140\u0142"+
		"\u0007\u0000\u0000\u0000\u0141\u0140\u0001\u0000\u0000\u0000\u0142\u0143"+
		"\u0001\u0000\u0000\u0000\u0143\u0141\u0001\u0000\u0000\u0000\u0143\u0144"+
		"\u0001\u0000\u0000\u0000\u0144\u0145\u0001\u0000\u0000\u0000\u0145\u0146"+
		"\u0006&\"\u0000\u0146N\u0001\u0000\u0000\u0000\u0002\u0000\u0143#\u0001"+
		"\u0000\u0000\u0001\u0001\u0001\u0001\u0002\u0002\u0001\u0003\u0003\u0001"+
		"\u0004\u0004\u0001\u0005\u0005\u0001\u0006\u0006\u0001\u0007\u0007\u0001"+
		"\b\b\u0001\t\t\u0001\n\n\u0001\u000b\u000b\u0001\f\f\u0001\r\r\u0001\u000e"+
		"\u000e\u0001\u000f\u000f\u0001\u0010\u0010\u0001\u0011\u0011\u0001\u0012"+
		"\u0012\u0001\u0013\u0013\u0001\u0014\u0014\u0001\u0015\u0015\u0001\u0016"+
		"\u0016\u0001\u0017\u0017\u0001\u0018\u0018\u0001\u0019\u0019\u0001\u001a"+
		"\u001a\u0001\u001b\u001b\u0001\u001c\u001c\u0001\u001d\u001d\u0001\u001e"+
		"\u001e\u0001\u001f\u001f\u0001  \u0001!!\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}