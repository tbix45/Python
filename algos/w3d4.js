// write a function that given an array return a string representing a book index. Combine consecutive pages to create ranges. 
// [1,2,3,5,7,8,10] 
// 1-3, 5, 7-8 ,10
function bookIndex(arr) {
    var string = "";
    for (let i = 0; i < arr.length; i++) {
        if (i < arr.length && i !== 0) {
            string += ", "
        }
        if (arr[i] + 1 === arr[i + 1]) {
            var start = arr[i]
            while (arr[i] + 1 === arr[i + 1]) {
                i++;
            }
            var end = arr[i];
            string += start + "-" + end;
        }
        else {
            string += arr[i];
        }
    }
    return string
}
console.log(bookIndex([1, 3, 4, 5, 7, 8, 10, 11]))