"""Counting bits. Brian Kernighan method. Only counts set bits."""
def count_bits(num):
	c = 0 #c accumulates the total bits set in num
	while num:
 		num &= num - 1 # clear the least significant bit set
 		c = c + 1
	print(c)

if __name__ == '__main__':
	num = int(input("What number do you want to count set bits of? (Enter -1 to exit) : "))
	while num >= 0:
		count_bits(num)
		num = int(input("What number do you want to count set bits of? (Enter -1 to exit) : "))
