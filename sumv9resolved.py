#function that adds up numbers hidden in strings to one sum
#multiple-digit numbers have to be preserved

def number_sum(word):
    numbers = '1234567890'
    found_numbers = []
    counter = 0
    r = len(word)

    for i in range(r):
        if i == 0:
            if word[i] in numbers:
                found_numbers.append(word[i])
        else:
            if (word[i] in numbers) and (word[i-1] not in numbers) and (found_numbers == []):
                found_numbers.append(word[i])
            elif (word[i] in numbers) and (word[i-1] not in numbers) and (found_numbers != []):
                found_numbers.append(word[i])
                counter += 1
            elif (word[i] in numbers) and (word[i-1] in numbers):
                found_numbers[counter] += word[i]

    print(sum(map(int, found_numbers)))


