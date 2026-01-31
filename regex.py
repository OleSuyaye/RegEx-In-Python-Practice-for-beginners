import re
# Program that matches a string that has an 'a' followed by three 'b;

def textmatcher1 (text):
    pattern = 'ab{3}'
    if re.search(pattern, text, re.IGNORECASE):
        return "a and 3b's found"
    else:
        return "match not found"
print(textmatcher1("abbsAbBbs"))

# Python program that matches a string that has an a followed by two to three 'b'

def textmatcher2 (text):
    pattern = 'ab{2,3}'
    if re.search(pattern, text, re.IGNORECASE):
        return "a and two or three b's found"
    else:
        return "match not found"
print(textmatcher2("adffsABbbbdff"))

# Python program to find sequences of lowercase letters joined by an underscore.

def lowercase_underscore (text):
    pattern = '[a-z]+_[a-z]+'
    if re.findall(pattern, text):
        return re.findall(pattern, text)
    else:
        return "Match not found"
    
print(lowercase_underscore("Adsd_ssd3455df_ge"))

#Python program to find the sequences of one upper case letter followed by lower case letters.

def one_upper_and_lowercase (text):
    pattern = "[A-Z][a-z]+"
    if re.findall(pattern, text):
        return re.findall(pattern, text)
    else:
        return "Match not found"
    
print(one_upper_and_lowercase("AsdffAfdOddsdfLdsd"))

# Python program that matches a word at the beginning of a string.

def match_beginning (text):
    pattern = "^cat"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group()
    else:
        return "Match Not Found"
    
print(match_beginning("catholic"))