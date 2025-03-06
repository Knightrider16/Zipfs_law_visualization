import matplotlib.pyplot as plt

with open('sample.txt','r') as f:
    file1 = f.read()

file1 = file1.lower()
words = {}
temp = "" 
punct = set([".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_", "..."]) 

for i in file1:
    if i in punct:
        continue
    elif i == " ":
        if temp not in words:
            words[temp] = 1
        else:
            words[temp]+=1
        temp = ""
    else:
        temp = temp+i

if temp:
    if temp not in words:
        words[temp] = 1
    else:
        words[temp] += 1

sorted_words = dict(sorted(words.items(), key = lambda item:item[1], reverse = True))

word_list = list(sorted_words.items())

x_values = [i + 1 for i in range(len(words))]

y_values = [i for i in sorted_words.values()]

print(sorted_words)

plt.plot(x_values, y_values, marker = 'o')
plt.title('Zipf\'s law visualization')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.show()