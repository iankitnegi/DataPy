# Create a funn that replaces all vowels in a string with a specified vowel
# vow_replace("apples and bananas","u")     => "upplus and bununus"

def vow_replace(str, ch):
    new_str=""
    replace="aeiou"
    for i in str:
        if i in replace:
            new_str += ch
        else:
            new_str += i
    return new_str

print(vow_replace("apples and bananas","u"))