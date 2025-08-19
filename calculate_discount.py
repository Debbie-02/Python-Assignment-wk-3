# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount if 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied


# Main program
# Get inputs from the user
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount_percent)

# Print results
print("Original Price: $", original_price)
print("Final Price after discount: $", final_price)