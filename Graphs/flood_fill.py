"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color. Return the modified image after performing the flood fill.
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        orig = image[sr][sc]
        image[sr][sc] = color
        helper(image,sc,sr,height,width,color,orig)
        return image

def helper(image,x,y,height,width,color,orig):
    #up
    if y-1 >= 0 and image[y-1][x] == orig:
        if orig != color:
            image[y-1][x] = color
            helper(image,x,y-1,height,width,color,orig)
    #down
    if y+1 < height and image[y+1][x] == orig:
        if orig != color:
            image[y+1][x] = color
            helper(image,x,y+1,height,width,color,orig)
    #left
    if x-1 >= 0 and image[y][x-1] == orig:
        if orig != color:
            image[y][x-1] = color
            helper(image,x-1,y,height,width,color,orig)
    #right
    if x+1 < width and image[y][x+1] == orig:
        if orig != color:
            image[y][x+1] = color
            helper(image,x+1,y,height,width,color,orig) 
    if image[y][x] == color:
        return
