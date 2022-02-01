function reverseString(string) {
    var reversed = "";
    for (let i = string.length - 1; i >= 0; i--) {
        // console.log(string[i])
        reversed += string[i]
    }
    console.log(reversed)
}
reverseString('hello tom')
// reverseString('car')
// reverseString('welcome')
function reverseWord(word) {
    var revWord = "";
    for (let i = word.length - 1; i >= 0; i--) {
        revWord += word[i]
    }
    console.log(revWord)
}
reverseWord("car")


//reverse array 
function reverseArray(arr) {
    for (var left = 0; left < Math.floor(arr.length / 2); left++) {
        var right = arr.length - 1 - left;
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }
    return arr
}
console.log(reverseArray([1, 2, 3]))

if (2 === "2") {
    console.log(true)
} else {
    console.log(false)
}

// var myVar = 1;
var myVar = null;
if (myVar) {
    console.log('myVar is not null')
} else {
    console.log("myVar is null")
}
function isPrime(n) {
    if (n < 2) {
        return `${n} is not a prime number`
    }
    for (let i = 2; i < n; i++) {
        if (n % i === 0) {
            return `${n} is not a prime number`
        }
    }
    return `${n} is a prime number`
}
console.log(isPrime(4))
console.log(isPrime(17))
console.log(isPrime(133))
console.log(isPrime(123))
