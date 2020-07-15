def spaces(diff):
  space=''
  for s in range(0,diff):
    space = space + ' '

  return space

def undercores(i):
  aux = ''
  for x in range(0,i):
    aux = aux + '-'
  return aux

def suma(sp):
  if sp[1] == '+':
    return int(sp[0]) + int(sp[2])
  else:
    return int(sp[0]) - int(sp[2])
  
def spaceSums(sums, spliter):
  for i in range(0, len(sums)):
    sums[i] = spaces(spliter[i] - len(sums[i])) + sums[i]

def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  top = list()
  botton = list()
  exp = '[0-9]+'
  spliter = list()
  sums = list()

  for i in problems:
    sp = i.split(' ')
    if sp[1] not in '+-':
      return "Error: Operator must be '+' or '-'."
    if len(sp[0]) > 4 or len(sp[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    if not sp[0].isdigit() or not sp[2].isdigit():
      return "Error: Numbers must only contain digits."
    
    tops=sp[0]
    bottons=sp[1]+sp[2]
    ltop = len(tops)
    lbotton = len(bottons)
    
    if ltop < lbotton:
      dif = (lbotton - ltop) +1
      tops = spaces(dif) + sp[0]
      bottons = sp[1]+ spaces(1) + sp[2]
    if lbotton < ltop:
      dif = ltop - lbotton
      bottons = sp[1]+ spaces(dif + 2) + sp[2]
      tops = spaces(dif) + sp[0]
    if lbotton == ltop:
      bottons = sp[1]+ spaces(2) + sp[2]
      tops = spaces(2) + sp[0]

    sums.append(str(suma(sp)))
    spliter.append(len(bottons))
    top.append(tops+'   ')
    botton.append(bottons+'   ')
    
  
  spaceSums(sums, spliter)
  top[len(top)-1] = top[len(top)-1].rstrip()
  botton[len(botton)-1] = botton[len(botton)-1].rstrip()

  split=''
  for i in spliter:
    split = split + undercores(i) + '    '

  arranged_problems = ' '.join(top) + '\n' + ' '.join(botton) + '\n' + split.rstrip()

  if solve: 
    arranged_problems = arranged_problems + '\n' +'    '.join(sums).rstrip()

  return arranged_problems