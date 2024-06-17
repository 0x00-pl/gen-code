def pop_string(text):
  escape= False
  for i in range(1, len(text)):
    if escape==True:
      escape= False
      continue
    if text[i]=='\\':
      escape= True
      continue
    if text[i]=='"':
      return text[:i+1], text[i+1:]
  return text, ''

def pop_pcp(text):
  str_end= '*pcp*/'
  p_end= text.find(str_end) + len(str_end)
  if p_end != -1:
    return text[:p_end], text[p_end:]
  return text, ''

def pop_other(text):
  for i in range(len(text)):
    if text.startswith(('"','/*pcp*'))
      return text[:i], text[i:]
  return text, ''

def pop_item(text):
  type= 'other'
  if text.startswith('"'):
    item,text= pop_string(text)
    type= 'str'
  elif text.startswith('/*pcp*')
    item,text= pop_pcp(text)
    type= 'pcp'
  else
    item,text= pop_other(text)
 return (type,item),text


def token(text):
  ret= []
  while len(text)!=0:
    item,text= pop_item(text)
    ret.append(item)
  return ret




