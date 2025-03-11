def 展普(obj, level=0):
  indent = "  " * level  # 用於格式化輸出層級
  if isinstance(obj, dict):
    for key, value in obj.items():
      #if isinstance(key, list):
      session_state['展普']+=f"{indent}{key}:\n"
      展普(value, level + 1)  # 遞迴解析子層
  elif isinstance(obj, list):
    for index, item in enumerate(obj):
      if len(item)==1 and isinstance(item, list):
        session_state['展普']+=f"{indent}[{item}]:\n"
      展普(item, level + 1)  # 遞迴解析列表中的元素
  else:
    session_state['展普']+=f"{indent}{obj}\n"

def 至巢典(csv_file_path):
    nested_dict = {}
    with open(csv_file_path) as csv_file:
        reader = DictReader(csv_file, delimiter='\t')
        for row in reader:
            #rndrCode([row])
            keys = row['Id'].split('.')
            current_level = nested_dict
            for key in keys[:-1]:  # 遍历中间层
                if not isinstance(current_level.get(key), dict):
                    current_level[key] = {}
                current_level = current_level[key]
            current_level[keys[-1]] = row['型']  # 最后一层设置为值
    return nested_dict

def 識遍歷(*args):
  #rndrCode([args])
  識別, 型=args[0]
  #for (識別, Type, 型) in 訊框.iterrows():
  keys = 識別.split('.')
  現層 = {}
  for key in keys[:-1]:  # 遍历中间层
    if not isinstance(現層.get(key), dict):
      現層[key] = {}
    現層 = 現層[key]
  現層[keys[-1]] = 型
  return 現層

def csv至杰森(file_path):
    # Attempt to detect delimiter
    with open(file_path, 'r', encoding='utf-8') as file:
      sample = file.read(1024)
      dialect = Sniffer().sniff(sample)
      delimiter = dialect.delimiter
    data = read_csv(file_path, sep=delimiter, encoding='utf-8')
    json_data = data.to_dict(orient='records')
    return json_data

def 徑型舊(*args):
  (識別, 型別), 識模, 骨模, 型模, 徑模, 資特普=args
  if 識徵:=識模.search(識別): 識=識徵.group()
  if 骨徵:=骨模.search(型別): 骨=骨徵.group()
  else: 骨=None
  if 型徵:=型模.search(型別): 型=型徵.group()
  徑=徑模.findall(識別)
  #try: 徑頭=session_state['徑頭'];x
  徑頭=session_state['徑頭']=f'徑{徑[0]}'
