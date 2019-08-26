
func minAddToMakeValid(S string) int {
    left := 0 // Number of left brackets
    right := 0 // Number of right brackets
    for _, c := range S {
        if c == '(' {
            left += 1
        } else {
            if left > 0 {
                left -= 1 // If left brackets are remaining, close the parentheses pair
            } else {
                right += 1 // Right brackets are outstanding, added to the total cost
            }
        }
    }
    return left + right
}
