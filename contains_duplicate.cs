'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> seenElements = new HashSet<int>();
        foreach(int num in nums)
        {
            if(seenElements.Contains(num)) return true;
            seenElements.Add(num);
        }

        return false;
    }
}
