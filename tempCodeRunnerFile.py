# Python program to find sequences of lowercase letters joined by an underscore.

def lowercase_underscore (text):
    pattern = '[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return "Match not found"
    
print(lowercase_underscore("Adsd_ssd"))