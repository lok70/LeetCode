func twoSum(nums []int, target int) []int{
    numMap := make(map[int]int)
    for i, num := range nums{
        comp := target - num
        if index, found := numMap[comp]; found{
            return []int{index, i}
        }
        numMap[num] = i
    }
    return nil
}