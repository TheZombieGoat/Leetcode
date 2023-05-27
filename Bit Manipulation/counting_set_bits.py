"""O(n) implementation where n = number of bits.
   Counts number of set bits.
"""
def count_bits(num):
	count = 0
	while num >= 1:
		count += num & 1
		num = num >> 1
	print(count)

if __name__ == '__main__':
	num = 0
	while num >= 0:
		num = int(input("What number do you want to count set bits of? (Enter -1 to exit) : "))
		count_bits(num)
