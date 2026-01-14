class Solution {
    public String destCity(List<List<String>> paths) {
        HashSet<String> freq=new HashSet<>();
        for(List<String> p:paths){
            freq.add(p.get(0));
        }
        for(List<String> a:paths){
            String dest=a.get(1);
            if(!freq.contains(dest)){
                return dest;
            }
        }
        return"";
    }
}