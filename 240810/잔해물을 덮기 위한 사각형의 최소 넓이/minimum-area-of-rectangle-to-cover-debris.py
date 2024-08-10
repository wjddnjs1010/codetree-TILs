def calculate_min_cover_area(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    # Create a 2001x2001 plane initialized with 0s
    plane = [[0] * 2001 for _ in range(2001)]
    
    # Fill the plane with the first rectangle
    for i in range(x1_1 + 1000, x2_1 + 1000):
        for j in range(y1_1 + 1000, y2_1 + 1000):
            plane[i][j] = 1
    
    # Remove the area covered by the second rectangle
    for i in range(x1_2 + 1000, x2_2 + 1000):
        for j in range(y1_2 + 1000, y2_2 + 1000):
            plane[i][j] = 0
    
    # Find the bounds of the remaining area covered by the first rectangle
    min_x = 2001
    max_x = -1
    min_y = 2001
    max_y = -1
    
    for i in range(2001)
        for j in range(2001):
            if plane[i][j] == 1:
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)
    
    # If no remaining area, the area to cover is 0
    if min_x > max_x or min_y > max_y:
        return 0
    
    # Calculate the width and height of the covering rectangle
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    return width * height

# Read input
x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

# Calculate and print the minimum covering area
print(calculate_min_cover_area(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2))