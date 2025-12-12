package hashmap;

import java.util.*;

public class word {
    static boolean pattern(String s,String word){
        HashMap<Character,String>fre1=new HashMap<>();
        HashMap<String,Character>fre2=new HashMap<>();
        String[] kk=word.split(" ");

        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            String w=kk[i];
            if(fre1.containsKey(ch)){
                if(!fre1.get(ch).equals(w)){
                    return false;
                }
            }
            if(fre1.containsKey(w)){
                if(fre2.get(w)!=ch){
                    return false;
                }
            }
            fre1.put(ch,w);
            fre2.put(w,ch);
            

        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String kk=sc.nextLine();
        if(pattern(s, kk)){
            System.out.println("Yes there is a pattern");
        }else{
            System.out.println("No there is not a pattern");
        }
    }
}
