from glob import glob
from streamlit import sidebar, text_input, radio as stRadio, set_page_config as pageConfig, columns as stCLMN, multiselect
from pandas import read_csv, unique
from stUtil import rndrCode

MENU, 表單=[], ['twpas', 'allProf', '卦爻辭', '錯綜複雜', '二十四節氣']
pageConfig(page_title='twcoreAllFhir', layout='wide', initial_sidebar_state='expanded')    #page_icon=None, menu_items=None, layout='centered', initial_sidebar_state="expanded", theme='dark'

for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  srch=text_input('搜尋', '')
if menu==len(表單):
  pass
elif menu==MENU[1]:
  allProfile='twpas/site/all-profiles.csv'
  allProfDF=read_csv(allProfile)
  事審欄位=allProfDF.columns
  CLMN=multiselect('事審欄位', 事審欄位)
  leftPane, rightPane=stCLMN([1, 1])
  #uniqProf=allProfDF['Profile'].unique()
  if CLMN:
    with leftPane:
      uniqProf=unique(allProfDF[CLMN].values)#[CLMN]
      uniqProf
  all欄位='''
  ApplyModel
  Bundle-response-twpas
  Bundle-twpas
  Claim-twpas
  ClaimResponse-self-assessment-twpas
  ClaimResponse-twpas
  Coverage-twpas
  DiagnosticReport-image-twpas
  DiagnosticReport-twpas
  DocumentReference-twpas
  Encounter-twpas
  ImagingStudy-twpas
  Media-twpas
  MedicationRequest-apply-twpas
  MedicationRequest-treat-twpas
  Observation-cancer-stage-twpas
  Observation-diagnostic-twpas
  Observation-laboratory-result-twpas
  Observation-pat-assessment-twpas
  Observation-tx-assessment-twpas
  Operationoutcome-twpas
  Organization-genetic-testing-twpas
  Organization-twpas
  Patient-twpas
  Practitioner-twpas
  Procedure-twpas
  ResponseModel
  Specimen-twpas
  Substance-twpas
  extension-claim-encounter
  extension-requestedService
  '''
  #with rightPane:
  #  rndrCode(all欄位)
  #sutraCLMN=queryCLMN(tblSchm='public', tblName=tblName, db='sutra')
  #rndrCode(sutraCLMN)
  #fullQuery=f'''select {','.join(sutraCLMN)} from {tblName} where 章節~'中庸';'''
  #rsltQuery=runQuery(fullQuery, db='sutra')
  ##rndrCode([fullQuery, rsltQuery])
  #rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, index=None, columns=sutraCLMN)
  #[rsltDF['章節']=='中庸']
elif menu==MENU[0]:
  sutraCLMN=['章節', '內容']
  CSV=glob('twpas/site/StructureDefinition*.csv')
  Cat=['StructureDefinition']   #['ValueSet', 'medical', 'all', 'medication', 'marital', , 'observations', 'health', 'CodeSystem']
  #Cat=['ValueSet', 'medical', 'all', 'medication', 'marital', 'StructureDefinition', 'observations', 'health', 'CodeSystem']
  from csv2XLS import singleCSV#, xls2XLS
  for cat in Cat:
  #  CSV=glob(f'XLS/{cat}*')
    #csv2XLS(CSV)
    #rndrCode([cat, CSV])
    cmbndDF=singleCSV(cat, CSV)
    cmbndDF
