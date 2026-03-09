import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

def MergeSort(A, n):			# Arguments: MergeSort(Array, ArraySize)
	if n <= 1:
		return A, 0
	else:
		totalInversions = 0;
		mid = n // 2			# Divide array szie by half
		left = A[:mid]			# Create a left array containing items to left of mid
		right = A[mid:]			# Create a right array containing items to right of mid
	
		_, leftInversions = MergeSort(left, len(left))		# Recurse for left and right arrays till we get to 1 element
		_, rightInversions =  MergeSort(right, len(right))
			
		totalInversions = leftInversions + rightInversions

		i = j = idx = 0			# Create 3 iterators: i will be for left array, j for right array, k for return array
		while i < len(left) and j < len(right):	# Compare left and right arrays till one of them runs out of elements
			if left[i] < right[j]:		# If left is less than right, then insert that element into A
				A[idx] = left[i]	
				i += 1		
			else:				# Else insert right into A 
				A[idx] = right[j]		
				j += 1
				totalInversions += (len(left) - i)
			idx += 1
		while(i < len(left)):			# Handles edge cases
			A[idx] = left[i]
			i += 1
			idx += 1
		while(j < len(right)):
			A[idx] = right[j]
			j += 1
			idx += 1

		return A, totalInversions

def main(arraySize):
	random.seed(42)				# Seeding rand
	randA = list(np.random.randint(100, size=arraySize))
	print(f"Size: {arraySize}\nArray: {randA}\n")
	sortedArray, inversions = MergeSort(randA, arraySize)
	print(f"Sorted Array: {sortedArray}\n{inversions} inversions")
	
if __name__ == "__main__":
	if len(sys.argv) > 1:			# Check if user passed in a command line argument for array size. Else throw error and exit program
		try:				# Try to set arraySize
			arraySize = int(sys.argv[1])

			if arraySize <= 0:
				print("Error: Please providea valid integer >= 0. Usage: python3 code.py <size>")	# If user enters a number <= 0, throw error.
				sys.exit()
		except ValueError:	
			print("Error: Please providea valid integer >= 0. Usage: python3 code.py <size>")	# If user enters a number <= 0, throw error.
			sys.exit()
	else:
		print("Error: Please provide a valid integer for array size and threshold. Usage: python3 code.py <size>")
		sys.exit()

	main(arraySize)
