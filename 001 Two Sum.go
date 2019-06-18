// Hashmap method
func twoSum(nums []int, target int) []int{

    ref := make(map[int]int) // value : index

    for i, v := range nums {
        j, existed := ref[target - v]
        if existed {
            return []int{j, i}
        }
        ref[v] = i
    }
    return nil
}
