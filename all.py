print("Введите число")
n = int(input())
k = 2
summa = 0

while n > 0:
        if k < 1:
            break
        summa = summa + n%10
        k = k-1
        n = n // 10
 
print("Сумма цифр:", summa)






print("Введите слово")
word = input()
word.split(' ')
print(word)
vowels = set("аеоуиыюяaeiouy")
fail = (' ', ',')
word_set = set(word.lower())
letter = 0
new_line = ''
for i in word:
    if i not in fail:
        print(sum(letter in vowels for letter in i))
print(sum(letter in vowels for letter in word))



import random
 
class customArr:
  N = 0
  M = 0
  zeroValue = 0
  values = [0,1,2,3]
  data = []
 
  def __init__(self, N, M, zeroValue = 0):    
    self.data = []
    self.N = N
    self.M = M
    self.zeroValue = zeroValue
   
    for i in range(self.N):
      self.data.append([])
      for j in range(self.M):
        self.data[i].append(self.zeroValue)
   
  def getValueFromKeyboard(self, i, j):
    while True:
      fromInput = int(input('Enter (' + i + ', ' + j + '):'))
      if fromInput in self.values:
        return fromInput
       
  def fillFromKeyboard(self):
    for i in range(0, self.N):
      for j in range(0, self.M):
        self.data[i][j] = self.getValueFromKeyboard(str(i), str(j))
   
  def fillRandom(self):
    for i in range(0, self.N):
      for j in range(0, self.M):
        self.data[i][j] = random.choice(self.values)
       
  def printOnScreen(self):
    self.printTop()
    for i in range(0, self.N):
      self.printLine(self.data[i], i)
     
  def printTop(self):
    print('i/j', end = ' ')
    for i in range(0, self.M):
      print(i, end = ' ')
    print('');
     
  def printLine(self, line, num):
    print(num, end = ' ')
    for i in range(0, self.M):
      print(line[i], end = ' ')
    print('');
   
  def getFours(self):
    return ''
   
a = customArr(1,3,3)


