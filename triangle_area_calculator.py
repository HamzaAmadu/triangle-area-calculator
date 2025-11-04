def triangle_area_calculator():
    # Calculate area of triangle
    print("Triangle Area Calculator")
    
    # Get user input for base and height
    base = input("Enter the base of the triangle: ")
    height = input("Enter the height of the triangle: ")
    
    # Calculate area using formula: (base * height) / 2
    area = int(base) * int(height) / 2
    
    # Display the result
    print(f"The base is {base} and the height is {height} which makes the area of the triangle = {area}")

def main():
    # Main program function
    print("Welcome to the Triangle Area Calculator!")
    
    # Run triangle calculator
    triangle_area_calculator()

if __name__ == "__main__":
    main()
