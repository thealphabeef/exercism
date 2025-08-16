import string
def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    sentence = sentence.strip()
    sentence = sentence.lower()
    nopunct = ''
    for char in sentence:
        if char not in punct:
            nopunct += char
    
    for char in alphabet:
        new = nopunct.find(char)
        if new != -1:
            pass
        else:
            return False
            
    return True
    