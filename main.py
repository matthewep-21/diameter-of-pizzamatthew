game.splash("welcome to PP's pizza!")
# Ask for pizza diameter
diameter = game.ask_for_number("How big do you want your pizza in inches?")
# Calculate subtotal
subtotal = 0.75 + 1 + 0.5 * diameter
# Add HST
total = subtotal * 1.13
# Round to 2 decimal places
rounded_total = Math.round(total * 100) / 100
# Show result
game.splash("Your total is: $" + ("" + str(rounded_total)) + " for " + str(diameter) + " Inches")