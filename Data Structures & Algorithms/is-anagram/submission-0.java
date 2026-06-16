class Solution {
        public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false ;
        char arr_s [] = s.toLowerCase().toCharArray();
        char arr_t [] = t.toLowerCase().toCharArray();
        for (int i = 0 ; i < arr_s .length ; i++){
            int count_s = 0 ;
            int count_t = 0 ;
            for(int j = 0 ; j < arr_t.length;j++){
                if(arr_s[i] == arr_s[j])
                    count_s++;
                if(arr_s[i] == arr_t[j])
                    count_t++;
            }
            if(count_s != count_t)
                return false ;
        }
        return true ;
    }
    public  static void main (String [] args){
        String s = "Racecar";
        String t = "Carrace";
        System.out.println(isAnagram(s,t));
    }
}