//parens valid
// return boolean if parentheses are valid (open before close and a pair) 
function parensValid(str) {
    var open = 0;
    var closed = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === ")") {
            closed += 1;
            if (closed > open) {
                return false
            }
        } else if (str[i] === "(") {
            open += 1;
        }
    }
    // console.log(open)
    // console.log(closed)
    if (open == closed) {
        return true
    } else {
        return false
    }
}
console.log(parensValid("(doj)(o)"))