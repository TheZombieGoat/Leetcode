class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        orig = image[sr][sc]
        helper(image,sr,sc,height,width,color,orig)
        return image

def helper(image,x,y,height,width,color,orig):
    #up
    if y-1 >= 0 and image[x][y-1] == orig:
        image[x][y-1] = color
        helper(image,x,y-1,height,width,color,orig)
    #down
    if y+1 < height and image[x][y+1] == orig:
        image[x][y+1] = color
        helper(image,x,y+1,height,width,color,orig)
    #left
    if x-1 >= 0 and image[x-1][y] == orig:
        image[x-1][y] = color
        helper(image,x-1,y,height,width,color,orig)
    if x+1 < width and image[x+1][y] == orig:
        image[x+1][y] = color
        helper(image,x+1,y,height,width,color,orig) 
    if image[x][y] != orig:
        return
    return
