# Leetcode
Leetcode-Python-Soultion
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
public class MajorityElement {
    public static int majorityElement(int[] nums){
        Map<Integer,Integer> h = new HashMap<>();
        for (int i=0; i<nums.length;i++){
            if (h.get(nums[i]) != null){
                h.put(nums[i],h.get(nums[i])+1);
            }
            else {
                h.put(nums[i],1);
            }
        }
        Iterator h1 = h.keySet().iterator();
        int ans = 0;
        while (h1.hasNext()){
            Object key = h1.next();
            if (h.get(key) > nums.length/2){
                ans = (int)(key);
                 break;
            }
        }
        return ans;
    }
}
