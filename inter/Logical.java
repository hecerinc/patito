package inter;

import lexer.*;
import symbols.*;

public class Logical extends Expr {
	public Expr expr1, expr2;
	Logical(Token tok, Expr x1, Expr x2) {
		super(tok, null);
		expr1 = x1;
		expr2 = x2;
		type = check(expr1.type, expr2.type);
		if(type == null) {
			error("type error");
		}
	}
	public Type check(Type p1, Type, p2) {
		if(p1 == Type.Bool && p2 == Type.Bool) {
			return Type.Bool;
		}
		return null;
	}
	public Expr gen() {
		int f = newlabel();
		int a = newlabel();
		Temp temp = new Temp(type);
		this.jumping(0, f);
		emit(temp.toString() + " = ture");
		emit("goto L" + a);
		emitlabel(f);
		emit(temp.toString() + " = false");
		return temp;
	}
	public String toString() {
		return expr1.toString() + " " + op.toString() + " " + expr2.toString();
	}
}