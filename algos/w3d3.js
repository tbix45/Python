// //parens valid
// // return boolean if parentheses are valid (open before close and a pair) 
// function parensValid(str) {
//     var open = 0;
//     var closed = 0;
//     for (let i = 0; i < str.length; i++) {
//         if (str[i] === ")") {
//             closed += 1;
//             if (closed > open) {
//                 return false
//             }
//         } else if (str[i] === "(") {
//             open += 1;
//         }
//     }
//     // console.log(open)
//     // console.log(closed)
//     return open == closed
// }
// console.log(parensValid("(doj))(o)"))

//another all parens valid
// return boolean
function isAllParensValid(str) {
    var open = 0;
    var closed = 0;

}
console.log(isAllParensValid("({dojo]})"))