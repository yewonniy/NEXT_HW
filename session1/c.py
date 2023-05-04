w = "to be or not to be, that is the question"
D = {}

w = w.split(' ')
for j in range(len(w)):
  w[j] = w[j].strip(',')
for i in range(len(w)):
  D[w[i]] = w.count(w[i])
  
print(D)