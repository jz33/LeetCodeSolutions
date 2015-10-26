import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<String> findStrobogrammatic(int totalWidth){
        return rec(totalWidth, totalWidth);
    }

    List<String> rec(int currWidth, int totalWidth){
        if(currWidth == 0) 
            return new ArrayList<String>(Arrays.asList(""));
        if(currWidth == 1) 
            return new ArrayList<String>(Arrays.asList("0", "1", "8"));
    
        List<String> lower = rec(currWidth - 2, totalWidth);
        List<String> res = new ArrayList<String>();
        
        for (String s : lower){
            if (currWidth != totalWidth) res.add("0" + s + "0");
            res.add("1" + s + "1");
            res.add("6" + s + "9");
            res.add("8" + s + "8");
            res.add("9" + s + "6");
        }
        return res;
    }
}
