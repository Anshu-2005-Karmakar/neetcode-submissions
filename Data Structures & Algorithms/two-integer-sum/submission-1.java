class Solution {
    public static int[] twoSum(int[] nums, int target) {
        int sum = 0 ;
        for(int i = 0;i<nums.length;i++){
            int ind = 0 ;
            for(int j = i + 1 ; j < nums.length;j++){
                sum = nums[i]+nums[j];
                if(sum == target)
                    return new int[]{i,j};
            }
        }
      return new int[]{};
    }
    public static void main(String [] args){
        int [] arr = {2,3,4,4};
        int tar = 6 ;
        System.out.println(twoSum(arr,tar));
    }
}
