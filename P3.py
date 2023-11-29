text = input("Enter a text: ")


def replace(input_text):
    vowels = "AEIOUaeiou"  
    result = [] 

    for char in input_text:
        if char in vowels:
            result.append('*')  
        else:
            result.append(char)  

    
    return ''.join(result)

modified_text = replace(text)


print("Modified Text:", modified_text)
