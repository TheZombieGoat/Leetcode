class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        orig = image[sr][sc]
        helper(image,sr,sc,height,width,color,orig)
        image[sr][sc] = color
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
    #down
    if x+1 < width and image[y][x+1] == orig:
        if orig != color:
            image[y][x+1] = color
            helper(image,x+1,y,height,width,color,orig) 
    if image[y][x] == color:
        return
