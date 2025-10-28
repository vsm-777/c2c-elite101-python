def count_vowels(a_string):
    count=0
    vowels=['a','e','i','o','u']
    for character in a_string.lower():
        if character in vowels:
            count+=1
    return count

print(count_vowels("Apple"))
print(count_vowels("python"))
print(count_vowels(''))
