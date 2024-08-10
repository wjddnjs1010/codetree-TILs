def rect_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

def overlap_area(x1, y1, x2, y2, x3, y3, x4, y4):
    overlap_x1 = max(x1, x3)
    overlap_y1 = max(y1, y3)
    overlap_x2 = min(x2, x4)
    overlap_y2 = min(y2, y4)
    
    if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
        return rect_area(overlap_x1, overlap_y1, overlap_x2, overlap_y2)
    else:
        return 0

# Input
a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

# Areas of rectangles A and B
area_a = rect_area(a_x1, a_y1, a_x2, a_y2)
area_b = rect_area(b_x1, b_y1, b_x2, b_y2)

# Overlapping areas
overlap_a = overlap_area(a_x1, a_y1, a_x2, a_y2, m_x1, m_y1, m_x2, m_y2)
overlap_b = overlap_area(b_x1, b_y1, b_x2, b_y2, m_x1, m_y1, m_x2, m_y2)

# Remaining areas of A and B after subtracting overlap
remaining_a = area_a - overlap_a
remaining_b = area_b - overlap_b

# Output
print(remaining_a + remaining_b)