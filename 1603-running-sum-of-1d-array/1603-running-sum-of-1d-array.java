class Solution {
    public int[] runningSum(int[] nums) {
    int[] dub = new int[nums.length];
    int summ = 0;
    for (int i = 0; i < nums.length; i++) {
        summ += nums[i];
        dub[i] = summ;
    }
    return dub;
}
}