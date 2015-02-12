package roman;
/**
 * 13 Roman to Integer
 * https://oj.leetcode.com/problems/roman-to-integer/
 */
public class Roman2Integer {
	public static int roman2Dec(String input){
	    int res  = 0;
        for(int i = 0; i<input.length(); i++){
            switch(input.charAt(i)) {
            case 'M': res += 1000;break;
            case 'D': res += 500;break;
            case 'C':
                if(i < input.length()-1){
                    switch(input.charAt(i+1)){
                    case 'M': 
                        res += 900;
                        i++;break;                                
                    case 'D': 
                        res += 400;
                        i++;break;
                    default: 
                        res += 100;
                    }
                } else {
                    res += 100;
                }break;
            case 'L': res += 50;break;
            case 'X':
                if(i < input.length()-1){
                    switch(input.charAt(i+1)){
                    case 'C': 
                        res += 90;
                        i++;break;
                    case 'L': 
                        res += 40;
                        i++;break;
                    default: 
                        res += 10;
                    }
                } else {
                    res += 10;
                }break;
            case 'V': res += 5;break;
            case 'I':
                if(i < input.length()-1){
                    switch(input.charAt(i+1)){
                    case 'X': 
                        res += 9;
                        i++;break;
                    case 'V': 
                        res += 4;
                        i++;break;
                    default: 
                        res += 1;
                    } 
                } else {
                    res += 1;
                }break;
            }
        }
        return res;
	}
	
	 public static void main(String args[]){
	        System.out.println(roman2Dec("X"));
	 }
}
