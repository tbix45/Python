//generate coin change
function coinChange(input) {
    var pennies = 0;
    var nickels = 0;
    var dimes = 0;
    var quarters = 0;
    var updatedInput = Math.round(input * 100);
    while (updatedInput > 0) {
        if (updatedInput >= 25) {
            quarters++
            updatedInput -= 25;
        } else if (updatedInput >= 10) {
            dimes++
            updatedInput -= 10;
        } else if (updatedInput >= 5) {
            nickels++
            updatedInput -= 5;
        } else {
            pennies++
            updatedInput -= 1;
        }
    }
    var output = "Q: " + quarters + " Dimes " + dimes + " Nickels " + nickels + " Pennies " + pennies
    return output
}
console.log(coinChange(0.86))
console.log(coinChange(4.60))
console.log(coinChange(9.12))
console.log(coinChange(.77))