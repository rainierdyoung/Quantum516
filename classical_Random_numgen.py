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
        random_numbers = generate_random_numbers(4000)
        print("Iteration :", i+1)
        print(random_numbers)
        smallest, largest, median, average = calculate_statistics(random_numbers)
        print("Smallest:", smallest)
        print("Largest:", largest)
        print("Median:", median)
        print("Average:", average)
        print("Entropy:", calculate_entropy(random_numbers))
        print()

random_genereration_trial(1)





