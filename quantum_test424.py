import random
from collections import Counter
import math

def decimalToBinary(n): 
    return bin(n).replace("0b", "")

def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(0,255))
        #random_numbers.append( decimalToBinary(random.randint(0, 255)))
    return(random_numbers)

def calculate_statistics(numbers):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Calculate the smallest element
    smallest = sorted_numbers[0]
    
    # Calculate the largest element
    largest = sorted_numbers[-1]
    
    # Calculate the median
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    # Calculate the average
    average = sum(sorted_numbers) / n
    
    return smallest, largest, median, average

def calculate_entropy(int_list):
    # Count the occurrences of each integer in the list
    counts = Counter(int_list)
    # Calculate the total number of integers in the list
    total_count = len(int_list)
    
    # Calculate the probability of each integer
    probabilities = [count / total_count for count in counts.values()]
    
    # Calculate the entropy
    entropy = -sum(probability * math.log2(probability) for probability in probabilities)
    
    return entropy

# Generate 10 random numbers between 0 and 255
def random_genereration_trial(n):
    for i in range(n):
        random_numbers = generate_random_numbers(10)
        print("Iteration :", i+1)
        print(random_numbers)
        smallest, largest, median, average = calculate_statistics(random_numbers)
        print("Smallest:", smallest)
        print("Largest:", largest)
        print("Median:", median)
        print("Average:", average)
        print("Entropy:", calculate_entropy(random_numbers))
        print()

def quantum_trial(int_set, n):
    print("Iteration :", n)
    print(int_set)
    smallest, largest, median, average = calculate_statistics(int_set)
    print("Smallest:", smallest)
    print("Largest:", largest)
    print("Median:", median)
    print("Average:", average)
    print("Entropy:", calculate_entropy(int_set))
    print()

#random_genereration_trial(10)
quantum_set1 = [149, 68, 88, 152, 64, 12, 72, 205, 126, 49]
quantum_set2 = [188, 67, 13, 122, 46, 48, 52, 63, 110, 190]
quantum_set3 = [254, 37, 121, 126, 51, 146, 103, 38, 167, 158]
quantum_set4 = [208, 140, 54, 200, 240, 190, 41, 230, 77, 184]
quantum_set5 = [162, 81, 155, 138, 80, 177, 43, 145, 12, 232]
quantum_set6 = [127, 130, 247, 248, 146, 105, 1, 202, 36, 87]
quantum_set7 = [192, 44, 85, 70, 171, 185, 202, 227, 225, 106]
quantum_set8 = [142, 183, 51, 51, 182, 57, 49, 35, 42, 131]
#interesting that the same number occured twice in a set
quantum_set9 = [235, 45, 155, 247, 153, 123, 61, 241, 105, 105]
#interesting that the same number occured twice in a set again!
quantum_set10 = [22,154,201,242,202,202,217,145,175,213,142]

quantum_trial(quantum_set1, 1)
quantum_trial(quantum_set2, 2)
quantum_trial(quantum_set3, 3)
quantum_trial(quantum_set4,4 )
quantum_trial(quantum_set5, 5)
quantum_trial(quantum_set6, 6)
quantum_trial(quantum_set7, 7)
quantum_trial(quantum_set8, 8)
quantum_trial(quantum_set9, 9)
quantum_trial(quantum_set10, 10)




