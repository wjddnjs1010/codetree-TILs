def find_max_n(binary_str):
    max_value =0

    for i in range(len(binary_str)):

        if binary_str[i]== '0':
            modified_str = binary_str[:i]+'1'+binary_str[i+1:]
        else:
            modified_str = binary_str[:i]+'0'+binary_str[i+1:]
        
        modified_str = int(modified_str,2)

        max_value = max(max_value,modified_str)

    return max_value

a = input()

result = find_max_n(a)

print(result)