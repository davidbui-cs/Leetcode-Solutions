def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    for element in array:
        if(i == len(sequence)):
            return True
        if(element == sequence[i]):
            i+=1
    return i == len(sequence)
