function reverseString(string) {
    var reversed = "";
    for (let i = string.length - 1; i >= 0; i--) {
        // console.log(string[i])
        reversed += string[i]
    }
    console.log(reversed)
}
reverseString('hello tom')
reverseString('car')
reverseString('welcome')



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