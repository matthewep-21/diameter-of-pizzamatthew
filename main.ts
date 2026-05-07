game.splash("welcome to PP's pizza!")
// Ask for pizza diameter
let diameter = game.askForNumber("How big do you want your pizza in inches?")
// Calculate subtotal
let subtotal = 0.75 + 1 + 0.5 * diameter
// Add HST
let total = subtotal * 1.13
// Round to 2 decimal places
let rounded_total = Math.round(total * 100) / 100
// Show result
game.splash("Your total is: $" + ("" + rounded_total) + " for " + diameter + " Inches")
