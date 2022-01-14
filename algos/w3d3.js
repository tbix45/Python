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
    const bracesStack = [];
    const openBraces = "({[";
    const closeMatches = {
        ")": "(",
        "}": "{",
        "]": "[",
    };

    for (let i = 0; i < str.length; i++) {
        if (openBraces.includes(str[i])) {
            bracesStack.push(str[i]);
        } else if (str[i] in closeMatches) {
            if (closeMatches[str[i]] === bracesStack[bracesStack.length - 1]) {
                bracesStack.pop();
            } else {
                return false;
            }
        }
    }
    return bracesStack.length === 0;
}
console.log(isAllParensValid("({dojo})"))

