func isPalindrome(x int) bool {
    reverse := 0
    for num := x; num > 0;{
        rem := num % 10
        reverse = reverse * 10 + rem
        num = num / 10
    }
    if x != reverse{
        return false
    }
    return true
}