def sortAndFindMedian(numbers):
    # First, sort the list of numbers in ascending order
    sort(numbers)
    
    n = len(numbers)
    # If even number of elements, median is average of the two middle values
    # If odd, median is the middle value
    if (n % 2 == 0):
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]
    

def sort(numbers):
    # Using a simple Bubble Sort to arrange the list in ascending order
    n_len = len(numbers)
    for i in range(n_len):
        for j in range(0, n_len - i - 1):
            # Swap adjacent elements if they are out of order
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Example list to find the median of
numbers_list = [1, 5, 6, 2, 8, 9, 10]
m_value = sortAndFindMedian(numbers_list)
print(f'The Median for the numbers list of {numbers_list} is :', m_value)
