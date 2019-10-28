#
## 36. Write a python program to find the longest word in given paragraph?
#

paragraph = '''
If adequate measures are not taken today to control environmental damages, the day is not far when earth will 
become an arid planet unable to sustain life. Uncontrolled environmental pollution will soon lead to extreme 
climatic conditions and natural disasters like floods, famine etc. The nations must realize the urgency to make 
necessary policy changes and to raise awareness, taking adequate measures towards slowing down environmental 
pollution. There could be hundreds of examples of human induced environmental pollution, but finding a solution 
to them, also lies only on humans.
'''

words    = paragraph.split()
longest  = ''
smallest = ''

for word in words:
    word.replace( '.|,', '')
    #print("INFO: The word is -", word, "-")
    if len(word) >= len(longest):
        longest = word
    elif len(word) < len(smallest):
        smallest = word
    elif len(smallest) == 0:
        smallest = word

print("The longest word in the given paragraph is of length  %2d: %s" % ( len(longest), longest))
print("The smallest word in the given paragraph is of length %2d: %s" % ( len(smallest), smallest))


