import lexer.*;
import java.io.*;
import java.util.*;

public class Driver {
	public static void main(String[] args) throws IOException {
		Lexer lex = new Lexer();
		try {
			Token t;
			while(true) {
				t = lex.scan();
				Object value;
				if(t instanceof Word) {
					value = ((Word)t).lexeme;
				}
				else if(t instanceof Num) {
					value = ((Num)t).value;
				}
				else {
					value = null;
				}
				System.out.println("<" + t.tag + ", " + value + ">");
			}
		}
		catch(IOException ex) {
			System.out.println("Done");
		}
	}
}