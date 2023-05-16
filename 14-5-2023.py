def min_operations_to_delete(string):
    count = 0
    i = 0
    while i < len(string):
        if i == len(string) - 1:
            i += 1
            continue
        if string[i] == string[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count

# string = "aabbaa"
# string = "aabbbcccaacccaa"
string = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
min_ops = min_operations_to_delete(string)
print(min_ops) 
