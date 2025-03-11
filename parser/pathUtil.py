from streamlit import session_state, write as stWrite
from stUtil import rndrCode

def 展普(obj, level=0):
  indent = "  " * level  # 用於格式化輸出層級
  if isinstance(obj, dict):
    for key, value in obj.items():
      #if isinstance(key, list):
      session_state['展普']+=f"{indent}{key[1:]}:\n"
      展普(value, level + 1)  # 遞迴解析子層
  elif isinstance(obj, list):
    for index, item in enumerate(obj):
      if len(item)==1 and isinstance(item, list): session_state['展普']+=f"{indent}[{item}]:\n"
      展普(item, level + 1)  # 遞迴解析列表中的元素
  else:
    session_state['展普']+=f"{indent}{obj[1:]}\n"

def init普法(模):  #徑頭, 骨
  #if 骨: return session_state[徑頭]
  #else:
  #原本=[]#,
  #rndrCode(['init徑=', session_state.get('徑頭')])
  sssnInfo=[]
  for k in session_state.keys():
    #原本.append(k)
    if k.find(模)!=-1:  #徑
      sssnInfo.append(k)
      del session_state[k]
  #rndrCode(['sssnInfo=', sssnInfo])
  #return session_state['徑頭']

def 找徑(資特普, 徑頭, 骨, 徑): #
  if 骨 and session_state.get(徑頭):
    if 資特普.split('-')[0][1:]==徑頭[1:]:
      session_state[資特普].append(session_state[徑頭])
      展普(session_state[徑頭])
      stWrite([session_state['展普']])
    init普法(徑頭[0])
  徑長=len(徑)
  if 徑長==2:
    頭, 尾=徑
    徑頭, 徑尾=f'徑{頭}', f'徑{尾}' #例如 ==> 徑extension, 徑age
    if 原尾:=session_state.get(徑頭): #例如['徑id', '徑nationality']
      #徑尾.append(尾) #已經是[]
      if isinstance(原尾, list):
        if not 原尾.count(徑尾):
          原尾.append(徑尾)
      session_state[徑頭]=原尾
      return {徑頭:原尾}
    else:
      session_state[徑頭]=[徑尾]
      return {徑頭:徑尾}
  elif 徑長>2:
    頭, 尾=徑[0], 徑[1:]
    徑頭=f'徑{頭}'
    if 徑尾:=session_state.get(徑頭):
      尾果=找徑(資特普, 徑頭, 骨, 尾) #骨,
      if isinstance(徑尾, list):
        徑尾=徑尾[:-1]
        徑尾.append(尾果)
        session_state[徑頭]=徑尾
        return {徑頭:徑尾}
      elif isinstance(徑尾, dict):
        for k, 新尾 in 徑尾.items(): pass #新尾.append(v)
        rndrCode(['k, 新尾=', k, 新尾])
        try: 新尾.append(尾果)
        except: pass
        session_state[徑頭]=新尾
        return {徑頭:新尾}
    else:
      徑尾=找徑(資特普, 徑頭, 骨, 尾)
      session_state[徑頭]=徑尾
    return {徑頭:徑尾}
  elif 徑長==1:
    session_state[徑頭]=[]
    return {徑頭:None}

def 徑型(*args):
  (識別, 型別), 識模, 骨模, 型模, 徑模, 資特普=args
  if 識徵:=識模.search(識別): 識=識徵.group()
  if 骨徵:=骨模.search(型別): 骨=骨徵.group()
  else: 骨=None
  if 型徵:=型模.search(型別): 型=型徵.group()
  徑=徑模.findall(識別)
  #try: 徑頭=session_state['徑頭'];x
  徑頭=session_state['徑頭']=f'徑{徑[0]}'
  #資特普=f'資{特普}'
  #rndrCode(['徑', 徑, '徑頭', 徑頭])
  #if 骨: session_state[徑頭]=[]
  if not 骨: 型=型.capitalize()+'Type'
  徑果=找徑(資特普, 徑頭, 骨, 徑) #
  session_state['型'].append(型)
  return str(徑果), str(型), 徑頭

def rtrv兩欄(*args):  #識別, 型, 識模, 型模
  (識別, 型別), 識模, 骨模, 型模, 徑模, 特普, 資特普=args
  #session_state['計數']+=1
  if 識徵:=識模.search(識別): 識=識徵.group()
  if 骨徵:=骨模.search(型別): 骨=骨徵.group()
  else: 骨=None
  if 型徵:=型模.search(型別): 型=型徵.group()
  徑=徑模.findall(識別)
  try: 徑頭=session_state['徑頭'];x
  except: 徑頭=session_state['徑頭']=f'徑{徑[0]}'
  #資特普=f'資{特普}'
  #rndrCode(['徑', 徑, '徑頭', 徑頭])
  徑果=找徑(資特普, 徑頭, 骨, 徑) #
  if not 骨: 型=型.capitalize()+'Type'
  #型=型.capitalize()+'Type' if not 骨 else 型.capitalize()
  #if 型=='Backboneelement': 型='BackboneElement'
  if session_state.get(識): session_state[識]+=({識別:型}, ) #有找到包
  else: session_state[識]=({識別:型}, )    # assign識包
  if 骨:
    #rndrCode([f"del 鍵值={', '.join(sssnInfo)}", f'KEY={", ".join(原本)}'])  #, [k for k in 原本]
    if session_state.get('頭包'):  #處理 1. 設定頭
      session_state[特普].append(session_state['頭包'])
    #if session_state.get('Pth包'):
      #rndrCode(['頭包', session_state['頭包']] )
    session_state['頭包']=[]  #2. 清空
    session_state['頭包'].extend(session_state[識])
    #session_state['徑果']=徑果
    #session_state[f'資{特普}'].append(session_state[徑頭])#.append(session_state['Pth包'])
    #session_state['Pth包']=[]  #2. 清空
    #session_state['Pth包'].extend(徑果)  #session_state[徑頭]
    #rndrCode(['資特普', session_state['Pth包'], session_state[f'資{特普}']])
  else:
    #session_state['Pth包'].extend(session_state[徑頭])
    #rndrCode(['資特普', session_state[f'資{特普}']])
    #session_state['徑果']=徑果
    #session_state[f'資{特普}'].append(徑果)#.append(session_state['Pth包'])
    #rndrCode(['Pth包=', session_state['徑包']])
    if len(session_state[識])>session_state['多識']:  #處理多識情形
      #session_state['頭包']=session_state['頭包'][:session_state['計數']-len(session_state[識])].extend(session_state[識])
      #if session_state['多識']:
      #  pass
      #  session_state['頭包'].append(session_state[識][-1])
      #else:
      session_state['頭包']=session_state['頭包'][:-1]
      session_state['頭包'].append(session_state[識])
    else:
      session_state['頭包'].extend(session_state[識]) #單一識
  session_state['型'].append(型)
  session_state['多識']=len(session_state[識])
  return str(骨), str(型), str(徑果)#str(session_state['Pth包']), str(session_state[f'資{特普}']), f'資{特普}', str(識)    #str(session_state[識]), str(session_state['頭包'])#str(徑),
