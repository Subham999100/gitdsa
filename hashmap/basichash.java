package hashmap;

import java.util.HashMap;
import java.util.Map;

public class basichash {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();

        // Adding elements
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);

        // Accessing elements
        System.out.println("Value for 'Two': " + map.get("Two"));

        // Removing an element
        map.remove("Three");

        // Iterating over the HashMap
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }
}
