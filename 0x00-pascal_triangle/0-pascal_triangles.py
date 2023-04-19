#!/usr/bin/python3

"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Returns a triangle of Pascal's triangle of n
    """
    if n <= 0:
        return
    yield [1]
    prev_row = [1]
    for i in range(1, n):
        cur_row = [1]
        for j in range(1, (i+1)//2):
            cur_val = prev_row[j-1] + prev_row[j]
            cur_row.append(cur_val)
        if i % 2 == 0:
            cur_row.extend(cur_row[:-1][::-1])
        else:
            cur_row.extend(cur_row[::-1])
        yield cur_row
        prev_row = cur_row
