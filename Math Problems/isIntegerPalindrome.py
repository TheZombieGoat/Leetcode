class Solution:

	def lop(n,digits):
		sum_num = 0
		half_dig = digits // 2
		m = n
		for i in range(half_dig):				
			n = n // 10**(digits-1-i) #num_digits - 1 - i
			sum_num = sum_num + n*10**i # -(i + 1)
			m = m - n*10**(digits-1-i) #num_digits - 1 - i
			n = m
		return sum_num

	def isPalindrome(self, num: int) -> bool:
		if num < 0 or num == 10:
			print("It's not a Palindrome.")
			return False
		elif num < 10:
			print("It's a Palindrome")
			return True

		new_num = num
		digits = 1

		while num >= 10:
			num = num // 10
			digits += 1
		return Solution.lop(new_num,digits) == new_num % 10**(digits//2)

