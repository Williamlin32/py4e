

str =  'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
number = float(str[ipos + 1:])
print(number)
