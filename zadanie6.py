#Given some text, count and save how often each letter appears in it.
# Then print each letter and its count in alphabetic order.
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."\
       "Nam venenatis nisi eu hendrerit aliquet. Praesent euismod, "\
       "mauris vitae consequat luctus."

symbol = 'abcdefghijklmnopqrstuvwxyz'
charsCount = {} 

for element in symbol:
    count =  (text.count(element))
    charsCount[element] = count
    
print(charsCount)