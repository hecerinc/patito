import java.io.*;

public class Postfix {
	public static void main(String[] args) throws Exception {
		Parser p = new Parser();
		p.expr(); // Start with the starting symbol
		System.out.println();
	}
}