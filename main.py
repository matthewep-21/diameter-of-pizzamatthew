"""

Declare variables

"""
# Ask for pizza diameter
diameter = game.ask_for_number("Pizza diameter?")
# Calculate subtotal
subtotal = 0.75 + 1 + 0.5 * diameter
# Add HST
total = subtotal * 1.13
# Round to 2 decimal places
rounded_total = Math.round(total * 100) / 100
# Show result
game.splash("Pizza Cost: $" + ("" + str(rounded_total)))