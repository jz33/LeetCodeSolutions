/**
 * Reverse Words in a String
 * https://leetcode.com/problems/reverse-words-in-a-string/
 *
 */
public class _151
{
    public String reverseWords(String input)
    {
        input = input.trim();
        String arr[] = input.split("\\s+");
        StringBuffer sb = new StringBuffer();
        for(int i = arr.length - 1 ; i > 0;i--)
        {
            sb.append(arr[i]);
            sb.append(" ");
        }
        if(arr.length > 0) sb.append(arr[0]);
        return sb.toString();
    }
    
    public _151()
    {
        String input = "   the   sky   is   blue    ";
        System.out.println(reverseWords(input));
    }
    
    public static void main(String []args)
    {
        new _151();
    }
}
