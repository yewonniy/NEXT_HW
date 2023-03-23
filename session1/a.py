num = int(input())
k = num
num_reverse = 0

for i in range(len(str(num))):
    num_reverse = num_reverse*10 + k%10
    k = k//10

if num == num_reverse: 
    print('true')
else : 
    print('false')


a = input()
word = a.split(' ')
print(len(word))


