def calculate_total_area(n, coordinates):
    # Create a 201x201 plane initialized with 0s
    plane = [[0] * 201 for _ in range(201)]
    
    # Fill the plane with squares of paper
    for x, y in coordinates:
        for i in range(x + 100, x + 108):
            for j in range(y + 100, y + 108):
                plane[i][j] = 1
    
    # Calculate the total area covered by the papers
    total_area = sum(sum(row) for row in plane)
    
    return total_area

# Read input
n = int(input().strip())
coordinates = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Calculate and print the total area
print(calculate_total_area(n, coordinates))