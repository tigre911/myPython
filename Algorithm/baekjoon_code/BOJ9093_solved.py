t = int(input())
sentence = []
for i in range(t):
    sentence.append(input())

print(f'sentence : {sentence}')

print(f'split : {sentence[0].split()}')

print(f'split[::-1] : {sentence[0][::-1].split()}')

for j in range(t):
    a = sentence[j][::-1].split()
    print(f'a : {a}')
    print(f'a[::-1] : {a[::-1]}')
    print((' ').join(a[::-1]))
