# problem statement:
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Desired Output:
# cwen@iupui.edu 5


# code:

fh = open("mbox-short.txt")
counts = dict()
for l1 in fh:
    line = l1.rstrip()
    if line == "":
        continue
    if line.startswith("From"):
        word = line.split()
        if(len(word) > 2):
            counts[word[1]] = counts.get(word[1], 0)+1

# find the most number of times an email has occured
largest = 0
biggest_email = None
for key, value in sorted(counts.items()):
    if value > largest:
        largest = value
        biggest_email = key

print(biggest_email, largest)
