from streamlit import json, radio as stRadio, sidebar, data_editor, dataframe, checkbox, session_state, download_button
from glob import glob
from dbUtil import dbCLMN, runQuery, clmnDF
from stUtil import rndrCode
from streamlit import sidebar, session_state, radio as stRadio, columns as stCLMN, text_area, text_input, multiselect
#from jsnKEYs import rtrvFhirKeys
from streamlit import toggle as stToggle, markdown as stMarkdown, dataframe #slider, code as stCode, cache as stCache
from os.path import splitext
from pandas import read_csv, DataFrame
from pathlib import Path
from twUtil import flattenDset, mstSpprtParser, srchMust, pbasCLMN, chngCLMN

twcoreCLMN={'TWProcedure', 'TWMedication', 'Address', 'TWOrganization', 'Specimen', 'TWAllergyIntolerance', 'TWPatient', 'MedicationStatement', 'CodeableConcept', 'MedicationDispense', 'TWDiagnosticReport', 'TWMedicationDispense', 'TWEncounter', 'TWComposition', 'TWBundle', 'AllergyIntolerance', 'Goal', 'Location', 'DiagnosticReport', 'Organization', 'Practitioner', 'Device', 'DocumentReference', 'Bundle', 'Procedure', 'CareTeam', 'Extension', 'TWLocation', 'Medication', 'TWMessageHeader', 'Condition', 'PractitionerRole', 'Provenance', 'TWDocumentReference', 'MedicationRequest', 'TWObservation', 'Encounter', 'Immunization', 'Composition', 'TWMedicationRequest', 'TWPractitioner', 'MessageHeader', 'TWPractitionerRole', 'QuestionnaireResponse', 'RelatedPerson', 'Media', 'TWCondition', 'ServiceRequest', 'TWSpecimen', 'TWMedia', 'TWMedicationStatement', 'CarePlan', 'TWImagingStudy', 'Patient', 'Coverage', 'ImagingStudy', 'Observation', 'Coding'}
合併CLMN=['Id', 'Must Support?', 'Min', 'Max', 'Definition', 'Comments', 'Requirements', 'Default Value', 'Fixed Value', 'Pattern', 'Example', 'Minimum Value', 'Maximum Value', 'Maximum Length', 'Binding Strength']

MENU, 表單, FLIST=[], ['viewJSON', 'jsn2CSV', 'CSV', 'csv2XLS', 'xls2XLS', 'singleCSV', 'crudTwcore', 'dType', 'MustSupport', 'flattenData', 'lxmlParser', 'Encounter', 'PBASE', '對應'], ['definitions', 'fullIG', 'package']	#, '錯綜複雜', '二十四節氣'
from glob import glob
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  #menu=stRadio('', MENU, horizontal=True, index=0)
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  fhir類別=stRadio('fhir類別', FLIST, horizontal=True, index=0)
  #if fhir類別=='fullIG': JSN=glob(f'{fhir類別}/site/*.json')
  #else: JSN=glob(f'{fhir類別}/*.json')
  #jsn=stRadio('表', JSN, horizontal=True, index=0)
  #fhirLst=menu[1:]    #glob()
  #rndrCode(['fhirCat=', fhir類別])
if menu==len(表單):
  pass
elif menu==MENU[13]:     #'對應'
  核CLMN=stRadio('core欄位', twcoreCLMN, horizontal=True, index=0)
  併CLMN=multiselect('合併', 合併CLMN)
  leftPane, rightPane=stCLMN([1, 1])

  try: cmbndDF=session_state['cmbndDF']
  except: cmbndDF=session_state['cmbndDF']=read_csv('singleStructureDefinition.csv')

  with leftPane:
    if 併CLMN:
      cmbndDF[cmbndDF['Id'].str.contains(核CLMN, regex=True) & cmbndDF['Must Support?'].str.contains('Y')][併CLMN] #flags=IGNORECASE, 
  try: dfCLMN=session_state['dfCLMN']
  except: dfCLMN=session_state['dfCLMN']=pbasCLMN()

  欄位DF=DataFrame(dfCLMN, columns=['value'])
  欄位DF.loc[:, '對應欄位']=''

  with rightPane:
    data_editor(欄位DF, num_rows='dynamic', use_container_width=True, args=(session_state["dfCLMN"],), on_change=chngCLMN)
    下載=download_button(label="Download data as CSV", data=csv, file_name='large_df.csv', mime='text/csv')

  #with leftPane:
  #  pbas=multiselect('PBAS欄位', dfCLMN)
elif menu==MENU[12]:     #'Type'
  #CLMN=dbCLMN(tblSchm='public', tblName='PBASIFNO', db='pbase')   #
  dfCLMN=pbasCLMN()
  #rndrCode(dfCLMN)
  leftPane, rightPane=stCLMN([1, 1])
  #with sidebar:
  #  df=DataFrame(columns=dfCLMN)
  #for ndx, CLMN in enumerate(dfCLMN): clmn=checkbox(label=CLMN, key=ndx)
  with leftPane:
    pbas=multiselect('PBAS欄位', dfCLMN)
  with rightPane:
    rndrCode(clmn)
  #欄位=checkbox('欄位', value=df.columns)
  #dataframe(df)
  #CLMN=runQuery("select column_name from information_schema.columns where table_name='PBASINFO' and table_schema='public';", db='pbase')
  #rndrCode(['dfCLMN=', dfCLMN])

elif menu==MENU[11]:     #'Type'
  csv='CSV/StructureDefinition-Encounter-twcore.csv'
  encntrDF=read_csv(csv)
  encntrDF
elif menu==MENU[10]:     #'Type'
  DSET=glob('fullIG/site/StructureDefinition-*.html')
  #DSET='fullIG/site/StructureDefinition-AllergyIntolerance-twcore.html'
  for dset in DSET:
    with open(dset) as fin:
      htmlData=fin.read()
      try:
        msEle=mstSpprtParser(htmlData)
        if msEle:
          rndrCode([f"{dset.split('-')[1]}.{v}" for v in msEle])
      except:
        rndrCode(['htmlData Bytes', dset])
elif menu==MENU[9]:     #'Type'
  from json import loads as jsnLoads
  DSET=glob('fullIG/site/StructureDefinition-*.json')
  #DSET='fullIG/site/StructureDefinition-AllergyIntolerance-twcore.json'
  #msupportKEY=[]
  mSpprtID=session_state['mSpprtID']
  mSpprtID=mSpprtID.to_list()
  rndrCode(['mSpprtID', mSpprtID, len(mSpprtID)])
  count=0
  for dset in DSET:
    with open(dset) as fin:
      jsnData=fin.read()
      jsnDict=jsnLoads(jsnData)
      flttndJsn = flattenDset(jsnDict)
      mustSupportEle=srchMust(flttndJsn)
      for key in mustSupportEle.keys():
        count+=1
        try: mSpprtID.remove(key)
        except: rndrCode(['unknown', key])
      #rndrCode([dset, ', '.join(mustSupportEle.keys())])
  rndrCode(['remainKEY', mSpprtID, count])
elif menu==MENU[8]:     #'Type'
  sdtwDF=session_state['sdTwcore']
  mSpprt=sdtwDF[sdtwDF['Must Support?']=='Y']#['Id', 'Path', 'Must Support?']
  #mSpprt=sdtwDF[['Id', 'Path', 'Must Support?']]
  mSpprt[['Id', 'Must Support?', 'Min', 'Max', 'Definition', 'Comments', 'Requirements', 'Default Value', 'Fixed Value', 'Pattern', 'Example', 'Minimum Value', 'Maximum Value', 'Maximum Length', 'Binding Strength']].T #'Path', 'Meaning When Missing', 
  session_state['mSpprtID']=mSpprt['Id']
  #Example, Minimum Value, Maximum Value, Maximum Length,
  #dataframe()   #.str.extractall('(\w+)')[0].unique()
  #rndrCode(['CLMN', mSpprt.columns])
elif menu==MENU[7]:     #'Type'
  #twcoreAllFhir
  #singleCSVStructureDefinition.csv
  sdtwDF=session_state['sdTwcore']
  rndrCode(['CLMN', sdtwDF.columns])
  #sdtwDF['Type']
  #from pandas import unique
  #rndrCode([unique(sdtwDF['Type(s)'].str.extractall('(\w+)'))])
  #rndrCode([])
  dataframe(sdtwDF['Type(s)'].str.extractall('(\w+)')[0].unique())
  sdtwDF['Type(s)'].str.extractall('(\w+)')[0].unique().tofile('uniqDatatype.csv', sep=',')     #,format='%10.5f'
  #欄位名稱==>"""Id, Path, Slice Name, Alias(s), Label, Min, Max, Must Support?, Is Modifier?, Is Summary?, Type(s), Short, Definition, Comments, Requirements, Default Value, Meaning When Missing, Fixed Value, Pattern, Example, Minimum Value, Maximum Value, Maximum Length, Binding Strength, Binding Description, Binding Value Set, Code, Slicing Discriminator, Slicing Description, Slicing Ordered, Slicing Rules, Base Path, Base Min, Base Max, Condition(s), Constraint(s), Mapping: TW Core IG, Mapping: RIM Mapping, Mapping: FiveWs Pattern Mapping, Mapping: HL7 v2 Mapping, Mapping: Workflow Pattern, Mapping: SNOMED CT Concept Domain Binding, Mapping: SNOMED CT Attribute Binding, Mapping: DICOM Tag Mapping, Mapping: ServD, Mapping: UDI Mapping, Mapping: CDA (R2), Mapping: Ontological RIM Mapping, Mapping: LOINC code for the element, Mapping: FHIR DocumentReference, Mapping: vCard Mapping, Mapping: Mapping to NCPDP SCRIPT 10.6, Mapping: V3 Pharmacy Dispense RMIM, Mapping: FHIR Composition, Mapping: XDS metadata equivalent, Mapping: Quality Improvement and Clinical Knowledge (QUICK), Mapping: Canadian Dental Association eclaims standard, Mapping: Canadian Pharmacy Associaiton eclaims standard, Mapping: W3C PROV, Mapping: FHIR AuditEvent Mapping"""
elif menu==MENU[6]:
  #try: 
  rndrCode(['總欄位數', len(twcoreCLMN)])
  with sidebar:
    twCLMN=stRadio('欄位', twcoreCLMN, horizontal=True, index=0)
  try:
    sdtwDF=session_state['sdTwcore']=read_csv('singleCSVStructureDefinition.csv')
    rndrCode(set([v[0] for v in sdtwDF['Id'].str.split('.')]))
  except: sdtwDF=session_state['sdTwcore']
  with sidebar:
    srchPttrn=text_input('搜尋', '')  #'輸入欄位'
  if twCLMN:
    srchDF=sdtwDF[sdtwDF.Id.str.contains(twCLMN, case=False)]   #srchPttrn fullmatch contains
    #srchDF=sdtwDF['Id'==srchPttrn]
    revDF=data_editor(srchDF, num_rows='dynamic', use_container_width=True)#, on_change=change_state2, args=(session_state["cso_df"],))
    revDF
elif menu==MENU[5]:
  from re import IGNORECASE
  #mSpprt[].T #'Path', 'Meaning When Missing', 
  核CLMN=stRadio('core欄位', twcoreCLMN, horizontal=True, index=0)
  併CLMN=multiselect('合併', 合併CLMN)
  Cat=['StructureDefinition']
  from csv2XLS import singleCSV
  for cat in Cat:
    CSV=glob(f'CSV/{cat}*.csv')
    #csv2XLS(CSV)
    #rndrCode([cat, CSV])
    cmbndDF=singleCSV(cat, CSV)
    #cmbndDF[cmbndDF['Id'].str.contains('Encounter')]
  leftPane, rightPane=stCLMN([1, 1])
  with leftPane:
    if 併CLMN:
      cmbndDF[cmbndDF['Id'].str.contains(核CLMN, regex=True) & cmbndDF['Must Support?'].str.contains('Y')][併CLMN] #flags=IGNORECASE, 
  with rightPane:
    dfCLMN=pbasCLMN()
    #dfCLMN
    data_editor(dfCLMN, num_rows='dynamic')
    #cmbndDF[]#['Id']
elif menu==MENU[4]:
  Cat=['ValueSet', 'medical', 'all', 'medication', 'marital', 'StructureDefinition', 'observations', 'health', 'CodeSystem']
  from csv2XLS import xls2XLS
  for cat in Cat:
    CSV=glob(f'XLS/{cat}*')
    #csv2XLS(CSV)
    #rndrCode([cat, CSV])
    xls2XLS(cat, CSV)
elif menu==MENU[3]:
  from csv2XLS import csv2XLS, df2XLS
  類別=['Bundle', 'codesystem', 'fragment', 'StructureDefinition', 'valueset']
  for cat in 類別:
    CSV=glob(f'CSV/{cat}*')
    #csv2XLS(CSV)
    #rndrCode([cat, CSV])
    df2XLS(cat, CSV)
elif menu==MENU[2]:
  with sidebar:
    CSV=glob('CSV/*')
    csvFNAME=map(lambda x:splitext(x)[0], CSV)
    csvFNAME=list(csvFNAME)
    #rndrCode(['csvFNAME', csvFNAME])
    csv=stRadio('CSV', CSV, horizontal=True, index=0)
  newCSV=map(lambda x:x.split('/')[-1], csvFNAME)
  #rndrCode(['menu2 newCSV', set(newCSV)])
  #with open('twcoreAllFhir.csv', 'w') as fout:
    #[fout.write(fname+'\n') for fname in set(newCSV) ]
    #for fname in set(newCSV): fout.write(fname+'\n')
    #fout.close()
  dfCSV=read_csv(csv)
  rndrCode(['dfCSV欄位', ', '.join(dfCSV.columns)])
  revDF=data_editor(dfCSV, num_rows='dynamic', use_container_width=True)#, on_change=change_state2, args=(session_state["cso_df"],))
  # Show the updated DataFrame after editing
  rndrCode("Updated DataFrame:")
  #if revDF.any():
  revDF.to_csv('dummy.csv', index=False)
elif menu==MENU[1]:
  def mkFhirCSV(jsn):
    jsnPth=Path(jsn)
    rndrCode(['absolute, stem=',  ])
    with open(jsn) as fin:   #'ImplementationGuide-tw.gov.mohw.nhi.pas.json'
      fullJsn=fin.read()
      fhirKEYs=rtrvFhirKeys(fullJsn)
      rndrCode(['fhirKEYs=', fhirKEYs])
      with open(f'{jsnPth.parent}/{jsnPth.stem}.csv', 'w') as fout:
        [fout.write(fhirkey+'\n') for fhirkey in fhirKEYs]
  for jsn in JSN:
    mkFhirCSV(jsn)
elif menu==MENU[0]:
  pass
#{'definitions':['OperationDefinition', 'ImplementationGuide', 'ConceptMap', 'ValueSet', 'StructureDefinition', 'CodeSystem', 'SearchParameter', 'CapabilityStatement']}
#{'package':['package.json', 'OperationDefinition', 'CapabilityStatement', 'StructureDefinition', 'ValueSet', 'SearchParameter', 'ImplementationGuide', 'ConceptMap', 'CodeSystem']}
#uniqJSN=map(lambda x:x.split('-')[0], JSN)
#rndrCode(['uniqJSN', set(uniqJSN)])
#if jsn:
#  rndrCode(['jsn=', jsn])
#  jsnPth=Path(jsn)
#  rndrCode(['absolute, stem=',  ])
#  with open(jsn) as fin:   #'ImplementationGuide-tw.gov.mohw.nhi.pas.json'
#    fullJsn=fin.read()
#    fhirKEYs=rtrvFhirKeys(fullJsn)
#    rndrCode(['fhirKEYs=', fhirKEYs])
#    with open(f'{jsnPth.parent}/{jsnPth.stem}.csv', 'w') as fout:
#      [fout.write(fhirkey+'\n') for fhirkey in fhirKEYs]
#    json(fullJsn)
