f = open('scores.csv','r')
l = f.read()
l = l.split('\n')
for item in l:
  x = item.split(',')
  sum += int(x[2])
print(sum)
