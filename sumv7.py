#function that adds up numbers hidden in strings to one sum
#multiple-digit numbers have to be preserved

def number_sum(word):
    numbers = '1234567890'
    found_numbers = []
    counter = 0
    r = len(word)

    for i in range(r):
        if not word[i-1]:
            if word[i] in numbers:
                found_numbers.append(word[i])
        elif word[i-1] and word[i+1]:
            if (word[i] in numbers) and (word[i-1] in numbers):
                found_numbers[counter] += word[i]
            elif (word[i] in numbers) and (word[i-1] not in numbers):
                found_numbers.append(word[i])
                counter += 1
        elif not word[i+1]:
            if word[i] in numbers and word[i-1] not in numbers:
                found_numbers.append(word[i])
            elif word[i] in numbers and word[i-1] in numbers:
                found_numbers[counter] += word[i]

    print(found_numbers)

number_sum("hello25hi10x")