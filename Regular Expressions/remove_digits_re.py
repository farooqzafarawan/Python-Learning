# Following code remove special characters optionally.

import re

def remove_special_characters(text, remove_digits=False):    
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'    
    text = re.sub(pattern, '', text) 
    
    return text
    
refText = remove_special_characters("Well this was fun! What do you think? 123#@!", remove_digits=True)

print(refText)
