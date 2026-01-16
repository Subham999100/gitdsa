class Solution {
    public boolean isPathCrossing(String path) {
        HashSet<String> map=new HashSet<>();
        int x=0;
        int y=0;
        for(char c:path.toCharArray()){
            map.add("0,0");
            if(c=='N'){
                y+=1;
            }else if(c=='S'){
                y-=1;
            }else if(c=='E'){
                x+=1;
            }else if(c=='W'){
                x-=1;
            }
            String ok=x+","+y;
            if(map.contains(ok)){
                return true;
            }
            map.add(ok);
        }
        return false;
    }
}