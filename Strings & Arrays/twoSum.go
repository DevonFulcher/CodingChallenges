func twoSum(nums []int, target int) []int {
    dict := map[int]int{};
    for i := 0; i < len(nums); i++ {
        dict[nums[i]] = i;
    }
    
    for i := 0; i < len(nums); i++ {
        index, ok := dict[target - nums[i]];
        if ok && i != index {
            return []int{i, index};
        }
    }
    return []int{};
}