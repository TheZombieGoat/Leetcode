def isPalindrome(num):
	if num < 0:
		return False
	y = 0
	q = num
	while q != 0:
		y = 10 * y + q % 10
		q //= 10
	return num == y 

