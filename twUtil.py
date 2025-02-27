from streamlit import session_state
from dbUtilNew import dbCLMN, clmnDF, asyncExtractData, dbCLMN, clmnDF
from lxml import html as lxmlHTML
from asyncio import run as asyncRun
from pandas import DataFrame

def queryHIST(srch):
  query=f'''select * from public."PBASINFO" where "PHISTNUM"='{srch}' limit 5;'''
  rsltQuery=asyncExtractData(query, db='pbase')
  dfCLMN=asyncRun(dbCLMN(tblName='PBASINFO', db='pbase'))
  dfCLMN=clmnDF(dfCLMN)
  #rndrCode([query])
  rsltQuery=asyncRun(rsltQuery)
  pbasDF=DataFrame(rsltQuery, columns=dfCLMN)
  return pbasDF

twcoreCLMN={'TWProcedure', 'TWMedication', 'Address', 'TWOrganization', 'Specimen', 'TWAllergyIntolerance', 'TWPatient', 'MedicationStatement', 'CodeableConcept', 'MedicationDispense', 'TWDiagnosticReport', 'TWMedicationDispense', 'TWEncounter', 'TWComposition', 'TWBundle', 'AllergyIntolerance', 'Goal', 'Location', 'DiagnosticReport', 'Organization', 'Practitioner', 'Device', 'DocumentReference', 'Bundle', 'Procedure', 'CareTeam', 'Extension', 'TWLocation', 'Medication', 'TWMessageHeader', 'Condition', 'PractitionerRole', 'Provenance', 'TWDocumentReference', 'MedicationRequest', 'TWObservation', 'Encounter', 'Immunization', 'Composition', 'TWMedicationRequest', 'TWPractitioner', 'MessageHeader', 'TWPractitionerRole', 'QuestionnaireResponse', 'RelatedPerson', 'Media', 'TWCondition', 'ServiceRequest', 'TWSpecimen', 'TWMedia', 'TWMedicationStatement', 'CarePlan', 'TWImagingStudy', 'Patient', 'Coverage', 'ImagingStudy', 'Observation', 'Coding'}
合併CLMN=['Id', 'Must Support?', 'Min', 'Max', 'Definition', 'Comments', 'Requirements', 'Default Value', 'Fixed Value', 'Pattern', 'Example', 'Minimum Value', 'Maximum Value', 'Maximum Length', 'Binding Strength']
def flattenDset(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flattenDset(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def mstSpprtParser(htmlCntnt):
  #file_path = 'StructureDefinition-AllergyIntolerance-twcore.html'
  #with open(fname, 'r', encoding='utf-8') as f:
      #content = f.read()
  tree = lxmlHTML.fromstring(htmlCntnt)
  # XPath to find elements with mustSupport (S symbol in the HTML file)
  must_support_elements = tree.xpath('//span[@title="This element must be supported"]/ancestor::tr')
  # Iterate through the mustSupport elements and extract ID and Path
  msEle=set()
  for elem in must_support_elements:
      # Extract the ID and Path from the corresponding columns in the table row (tr)
      element_id = elem.xpath('.//td[1]/a/text()')
      element_path = elem.xpath('.//td[1]/a/@href')
      # Print the ID and Path
      msEle.add(f"{element_id[0] if element_id else 'N/A'}")
      #rndrCode([f"ID: {element_id[0] if element_id else 'N/A'}", f"Path: {element_path[0] if element_path else 'N/A'}\n"])
  return msEle

# Get all key-value pairs
def srchMust(data):
    mustSupportEle = {}
    def rcrsvSrch(d):
        if isinstance(d, dict):
            # If the key is "mustSupport" and value is True, collect the relevant details
            if 'mustSupport' in d and d.get('mustSupport', False):
                mustSupportEle[d.get('id', 'Unknown ID')] = d.get('path', 'Unknown Path')
            # Continue searching nested dictionaries
            for k, v in d.items():
                if isinstance(v, dict) or isinstance(v, list):
                    rcrsvSrch(v)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, dict) or isinstance(item, list):
                    rcrsvSrch(item)

    rcrsvSrch(data)
    return mustSupportEle
def pbasCLMN():
  coCLMN=dbCLMN(tblName='PBASINFO', db='pbase')
  #rndrCode(['CLMN=', CLMN])
  CLMN=asyncRun(coCLMN)
  dfCLMN=clmnDF(CLMN)
  return dfCLMN
def chngCLMN(欄位):
  session_state['dfCLMN']=欄位
