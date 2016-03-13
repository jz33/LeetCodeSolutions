import java.util.*;

boolean isPalindromic(String a, String b){
    int la = a.length();
    int lb = b.length();
    if(la == 0 || lb == 0) return true;
    if(la <= lb){
        int i = 0, j = lb - 1;
        for(;i<la;i++,j--){
            if(a.charAt(i) != b.charAt(j)){
                return false;
            }
        }
        int bound = (lb - la) / 2;
        for(i = 0;i<bound;i++,j--){
            if(b.charAt(i) != b.charAt(j)){
                return false;
            }
        }
    } else {
        int i = 0, j = lb - 1;
        for(;j>-1;i++,j--){
            if(a.charAt(i) != b.charAt(j)){
                return false;
            }
        }
        int bound = (la - lb) / 2;
        for(j = la - 1;i<bound;i++,j--){
            if(a.charAt(i) != a.charAt(j)){
                return false;
            }
        }
    }
    return true;
}

public List<List<Integer>> palindromePairs(String[] words) {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    int l = words.length;
    for(int i = 0;i<l;i++){
        for(int j = i+1;j<l;j++){
            if(isPalindromic(words[i],words[j])){
                res.add(Arrays.asList(i,j));
            }
            if(isPalindromic(words[j],words[i])){
                res.add(Arrays.asList(j,i));
            }
        }
    }
    return res;
}
