import java.io.*;

public class Parser {

	char lookahead;

	public Parser() throws Exception {
		lookahead = (char)System.in.read();
	}
	void expr() throws Exception {
		term();
		rest();
	}

	void rest() throws Exception {
		if( lookahead == '+') {
			match('+');
			term();
			System.out.print('+');
			rest();
		}
		else if(lookahead == '-') {
			match('-');
			term();
			System.out.print('-');
			rest();
		}
		else {}
	}
	void term() throws Exception {
		if("0123456789".indexOf(lookahead) > -1) {
			char t = lookahead;
			match(lookahead);
			System.out.print(t);
		}
		else {
			throw new Exception("Syntax error.");
		}
	}
	void match(char t) throws Exception {
		if(lookahead == t) {
			lookahead = (char) System.in.read();
		}
		else {
			throw new Exception("Syntax error");
		}
	}
}