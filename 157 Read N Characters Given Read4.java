'''
Read N Characters Given Read4
https://leetcode.com/problems/read-n-characters-given-read4/
'''
public class Solution extends Reader4 {
    public int read(char[] output, int n) {
        char[] buf = new char[4];
        boolean eof = false;
        int i = 0;
        for(;i < n && !eof;){
            int r = read4(buf);
            if (r < 4) eof = true;
            int len = Math.min(r,n-i);
            System.arraycopy(buf,0,output,i,len);
            i += len;
        }
        return i;
    }
}
