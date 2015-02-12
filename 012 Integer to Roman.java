package roman;
/**
 * 12 Integer to Roman
 * https://oj.leetcode.com/problems/integer-to-roman/
 */
public class Integer2Roman {
	public static String dec2Roman(int input){
	    java.lang.StringBuffer buffer = new java.lang.StringBuffer();
	    while(input > 0){
            if ( input >= 1000){ 
                buffer.append("M");
                input -= 1000;
            } else if ( input >= 900){ 
                buffer.append("CM");
                input -= 900;
            } else if ( input >= 500){ 
                buffer.append("D");
                input -= 500;
            } else if ( input >= 400){ 
                buffer.append("CD");
                input -= 400;
            } else if ( input >= 100){ 
                buffer.append("C");
                input -= 100;
            } else if ( input >= 90){ 
                buffer.append("XC");
                input -= 90;
            } else if ( input >= 50){ 
                buffer.append("L");
                input -= 50;
            } else if ( input >= 40){ 
                buffer.append("XL");
                input -= 40;
            } else if ( input >= 10){ 
                buffer.append("X");
                input -= 10;
            } else if ( input >= 9){ 
                buffer.append("IX");
                input -= 9;
            } else if ( input >= 5){ 
                buffer.append("V");
                input -= 5; 
            } else if ( input >= 4){ 
                buffer.append("IV");
                input -= 4;
            } else if ( input >= 1){ 
                buffer.append("I");
                input -= 1;
            }
	    }
	    return buffer.toString();
	}
    
    public static void main(String args[]){
        System.out.println(dec2Roman(100));
    }
}