# problem statement: 6.5 Write code using find() and string slicing(see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# Desired Output
# 0.8475

# code:

text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(":")
rpos = float(text[atpos+5:])
print(rpos)
