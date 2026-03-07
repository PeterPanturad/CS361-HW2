import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

def InsertionSort(A,n):				# Arguments: InsertionSort(Array, ArraySize)
	if n <= 1:				# If it is an array with 0 or 1 element, it is already sorted
		return
	for i in range(1, n):			# Loop starting from 1 to n elements of array
		key = A[i]			# Remember the current element (first iteration starts at 2nd element)
		j = i - 1			# j will be our iterator
		while j >= 0 and key < A[j]:	# 
			A[j + 1] = A[j]		# Move the element j one to the right (first iteration replaces the element we stored into key)
			j -= 1			# Move to left to the next element
		A[j + 1] = key			# Place key where it is in order

def HybridMergeSort(A, n, k):			# Arguments: HybridMergeSort(Array, ArraySize, Threshold)
	if n > k:				# If it is an array with <= k elements, use insertion sort instead
		mid = n // 2			# Divide array szie by half
		left = A[:mid]			# Create a left array containing items to left of mid
		right = A[mid:]			# Create a right array containing items to right of mid
	
		HybridMergeSort(left, len(left), k)		# Recurse for left and right arrays till we get to 1 element
		HybridMergeSort(right, len(right), k)
		
		i = j = idx = 0			# Create 3 iterators: i will be for left array, j for right array, k for return array
		while i < len(left) and j < len(right):	# Compare left and right arrays till one of them runs out of elements
			if left[i] < right[j]:		# If left is less than right, then insert that element into A
				A[idx] = left[i]	
				i += 1		
			else:				# Else insert right into A 
				A[idx] = right[j]		
				j += 1
			idx += 1
		while(i < len(left)):			# Handles edge cases
			A[idx] = left[i]
			i += 1
			idx += 1
		while(j < len(right)):
			A[idx] = right[j]
			j += 1
			idx += 1
	else:
		InsertionSort(A, n)
	return A

def avgTime(func, n, k, reps = 5): 		# Arguments: avgTime(SortFunction, Array, ArraySize, Threshold, repitition count)
	total = 0.0
	for _ in range(reps):			# Repeat the amount of counts	
		randA = list(np.random.randint(100, size=n))	# Create randArray and fill with values between 0-10 and the array has a size of arraySize
		start = time.perf_counter()	# Start timer
		func(randA, n, k)		# Run function
		end = time.perf_counter()	# End timer
		total += (end - start) * 1000	# Calculate delta time and put in total (*1000 changes it to miliseconds)
	return total / reps			# Calculate avg time for all repititions

def main():
	random.seed(42)				# Seeding rand
	
	nValues = [100, 5000, 10000]		# Create array storing test values for array sizes
	kValues = [1, 2, 4, 8, 16, 32, 64]	# Create array storing test values for threshold amounts
	
	results = {}				# Dictionary to store our results

	for n in nValues:			# Loop through the three array sizes
		runtimes = []			# Create array for runtimes
		print(f"--Testing array w/ size {n}--")	

		for k in kValues:		# Loop through all threshold test cases
			avg_t = avgTime(HybridMergeSort, n, k, reps = 5)	# Run and output avg time
			print(f"Threshold: {k}	| Average Runtime: {avg_t} ms")	
			runtimes.append(avg_t)	# Add avg run times to our run time array
		results[n] = runtimes		# Store all run time arrays into reuslts

	for n, times in results.items():
		plt.plot(kValues, times, label=f"Array Size n = {n}", marker='o')
	plt.title("Hybrid Merge Sort")
	plt.xlabel("Threshold (k)")
	plt.ylabel("Average runtime (ms)")
	plt.legend()
	plt.grid(True)
	plt.show()
	
if __name__ == "__main__":
#	if len(sys.argv) > 1:			# Check if user passed in a command line argument for array size. Else throw error and exit program
#		try:				# Try to set arraySize & threshold to command line arg as int
#			arraySize = int(sys.argv[1])
#			threshold = int(sys.argv[2])
#
#			if arraySize <= 0 or threshold <= 0:
#				print("Error: Please providea valid integer >= 0. Usage: python3 code.py <size> <thresold>")	# If user enters a number <= 0, throw error.
#				sys.exit()

#			print("Error: Please provide a valid integer for array size and threshold. Usage: python3 code.py <size> <threshold>")
#			sys.exit()
#	else:
#		print("Error: Please provide a valid integer for array size and threshold. Usage: python3 code.py <size> <threshold>")
#		sys.exit()

	main()
