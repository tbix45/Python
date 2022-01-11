//is palindrome?
function isPalindrome(string) {
    for (let i = 0; i < string.length / 2; i++) {
        // console.log(string[i])
        // console.log(string[string.length - 1 - i])
        if (string[i] != string[string.length - 1 - i]) {
            return false
        }
    }
    return true
}
console.log(isPalindrome("racecar"))
console.log(isPalindrome("racexcar"))
console.log(isPalindrome("dud"))


//another way 
function isAnotherPalindrome(string) {
    var reversed = "";
    for (let i = string.length - 1; i >= 0; i--) {
        reversed += string[i];
    }
    // console.log(reversed)
    return string.toLowerCase() === reversed.toLowerCase()
}
console.log(isAnotherPalindrome("racecar"))
console.log(isAnotherPalindrome("raxcecar"))
console.log(isAnotherPalindrome("taCocat"))