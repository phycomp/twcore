from streamlit import sidebar, radio as stRadio, download_button, multiselect, columns as stCLMN, session_state, data_editor, button, set_page_config as pageConfig, date_input, text_input, date_input
from glob import glob
from pandas import read_csv, DataFrame
from dbUtilNew import asyncExtractData, dbCLMN, clmnDF
from asyncio import run as asyncRun
from twUtil import pbasCLMN, twcoreCLMN, 合併CLMN, queryHIST #flattenDset, mstSpprtParser, srchMust, chngCLMN, 
from stUtil import rndrCode
pageConfig(page_title='欄位對應', layout='wide', initial_sidebar_state='expanded')

資料表=['PBASINFO', 'SOAP', 'CD']

MENU, 表單, CMPRSN=[], ['欄位對應', '搜尋', 'uniqHIST'], ['\>=', '\>', '==', '\<', '\<=']#, , FLIST=['definitions', 'fullIG', 'package']#, 'jsn2CSV', 'CSV', 'csv2XLS', 'xls2XLS', 'singleCSV', 'crudTwcore', 'dType', 'MustSupport', 'flattenData', 'lxmlParser', 'Encounter', 'PBASE', '對應', '錯綜複雜', '二十四節氣'
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  #menu=stRadio('', MENU, horizontal=True, index=0)
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  bdcTBL=stRadio('bdcTBL', 資料表, horizontal=True, index=0)
  srch=text_input('病歷號', '17476969') #搜尋
  sdbrLeft, sdbrRight=stCLMN([1, 1])
  with sdbrLeft:
    比較=stRadio('比較', CMPRSN, horizontal=True, index=0)
  with sdbrRight:
    startDate=date_input('startDate')
    endDate=date_input('endDate')
  #fhir類別=stRadio('fhir類別', FLIST, horizontal=True, index=0)

if menu==len(表單):
  pass
elif menu==MENU[2]:     #'對應'
  from hist import HIST
  leftPane, rightPane=stCLMN([1, 1])
  with leftPane:
    病歷號=stRadio('病歷號', HIST[:15], horizontal=True, index=0)
    rsltDF=queryHIST(病歷號)
    rsltDF.T
  with rightPane:
    pass
  #with sidebar:
  #MNPL=['Create', 'Read', 'Update', 'Delete']
  #with sidebar:
    #mnpl=stRadio('操作', MNPL, horizontal=True, index=0)
    #增加資料、刪除資料、查資料、改資料
  #query=f'''select distinct "PHISTNUM" from public."PBASINFO" where char_length("PHISTNUM")=8 limit 1000;'''
  #rsltQuery=asyncExtractData(query, db='pbase')
  #rsltQuery=asyncRun(rsltQuery)
  #rsltDF=DataFrame(rsltQuery, columns=['PHISTNUM'])
  #rsltDF
elif menu==MENU[1]:     #'對應'
  from fhirSvr.fhir搜尋 import FHIRResource
  from streamlit import json as stJson
  if srch:
    #rsltDF=queryHIST(srch)
    #rsltDF.T
    leftPane, rightPane=stCLMN([5, 5])
    with leftPane:
      #病歷號=stRadio('病歷號', HIST[:15], horizontal=True, index=0)
      rsltDF=queryHIST(srch)
      rsltDF.T
      rsltDF.columns
    with rightPane:
      fhirRsrc=FHIRResource()
      #if mnpl==len(MNPL): pass
      #elif mnpl==MNPL[0]:   #Create
      #rsltDF.PHISTNUM
      patDset={'resourceType':'Patient', 'TWPatient.identifier':rsltDF.PIDNO.values[0], 'TWPatient.name':rsltDF.PNAMEC.values[0]}
      pat=fhirRsrc.create('Patient', patDset)
      #create(self, resource_type, data):
      stJson(['pat', pat])
  #rndrCode([srch, startDate, endDate, pbasDF])
elif menu==MENU[0]:     #'對應'
  try: cmbndDF=session_state['cmbndDF']
  except: cmbndDF=session_state['cmbndDF']=read_csv('singleStructureDefinition.csv')
  paneLeft, paneRight=stCLMN([1, 5]) #midPane, 
  with paneRight:
    核CLMN=stRadio('core欄位', twcoreCLMN, horizontal=True, index=0)
  with paneLeft:
    併CLMN=multiselect('合併', 合併CLMN)
  #cmbndDF

  leftPane, rightPane=stCLMN([1, 1]) #midPane, 
  #leftPane, midPane, rightPane=stCLMN([1, 1, 1]) #midPane, 
  with leftPane:
  #with midPane:
    if 併CLMN:
      cmbndDF[cmbndDF['Path'].str.contains(核CLMN, regex=True) ][併CLMN] #flags=IGNORECASE, & cmbndDF['Must Support?' .str.contains('Y')
  try: dfCLMN=session_state['dfCLMN']
  except: dfCLMN=session_state['dfCLMN']=pbasCLMN()
  #pbasCLMN()

  欄位DF=DataFrame(dfCLMN, columns=['原本欄位'])
  欄位DF.loc[:, '對應欄位']=''

  with rightPane:
    edtrDF=data_editor(欄位DF, num_rows='dynamic', use_container_width=True)   #args=(session_state["dfCLMN"],), on_change=chngCLMN, 
    #if button('下載'):
    csvDF=edtrDF.to_csv(index=False).encode('utf-8')
    download_button(label="下載", data=csvDF, file_name=f'{bdcTBL}對應.csv', mime='text/csv')
      #newDF.to_csv(f'{bdcTBL}對應.csv', index=False)

  #with leftPane:
  #  pbas=multiselect('PBAS欄位', dfCLMN)
