text = "X-DSPAM-Confidence:    0.8475";
pos=text.find(' ')
text2=text[pos:]
text2=text2.strip()
text3=float(text2)
print(text3)
