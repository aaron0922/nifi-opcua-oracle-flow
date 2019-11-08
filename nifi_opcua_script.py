# replace com as XXX
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

class PyStreamCallback(StreamCallback):
  def __init__(self):
        pass
  def process(self, inputStream, outputStream):
    text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
    obj = json.loads(text)

    newObj = {}
    # eqpNameList = []
    eqpClassList = []
    eqpClassPropList = []
    eqpList = []
    eqpPropList = []
    eqpClassXEqpMappingList = []

    factory = obj[0]['k1'].split('/')[2]
    line = obj[0]['k1'].split('/')[3]
    # XXX-DG2-P11
    hierarchyScopeId = "".join(['XXX-', factory, '-', line])
    # EQP_CLASS
    eqpClassList.append({
      # "DESCRIPTION":"description",
      "ID":"STANDARD_TAGS",
      "SYSTEM_ID":"OPCUA-Data",
      "GROUP_KEY":"TAG_GROUP",
      "GROUP_TABLE":"STANDARD_TAGS"
      })

    for i in range(1, len(obj)):
      eqp = obj[i]['k1'].split('/')[4]
      if len(obj) >= 16 and i > 1 and i < 16: 
        key = obj[i]['k1'].split('/')[5]
        # EQP_CLASS_PROP
        eqpClassPropList.append({
          "ID":key, 
          "SYSTEM_ID":"OPCUA-Data", 
          "GROUP_KEY":key,
          "GROUP_TABLE":"STANDARD_TAGS",
          "PID_EQP_CLASS_PROP_EQP_CLASS_ID":"STANDARD_TAGS",
          "PID_EQP_CLASS_PROP_EQP_CLASS_SYSTEM_ID":"OPCUA-Data",
          "PID_EQP_CLASS_PROP_EQP_CLASS_GROUP_KEY":"TAG_GROUP",
          "PID_EQP_CLASS_PROP_EQP_CLASS_GROUP_TABLE":"STANDARD_TAGS"
          })

      if (i - 1) % 15 == 0:
        eqpNameList.append(eqp)
        # EQP
        eqpList.append({
          # "DESCRIPTION":"description",
          "ID":eqp,
          "SYSTEM_ID":"OPCUA-Data",
          "GROUP_KEY":eqp,
          "GROUP_TABLE":eqp,
          "FID_HIERARCHY_SCOPE_HIERARCHY_SCOPE_ID":hierarchyScopeId,
          "FID_HIERARCHY_SCOPE_HIERARCHY_SCOPE_SYSTEM_ID":"XXX-CORP",
          "FID_HIERARCHY_SCOPE_HIERARCHY_SCOPE_GROUP_KEY":hierarchyScopeId,
          "FID_HIERARCHY_SCOPE_HIERARCHY_SCOPE_GROUP_TABLE":"XXX-CORP-HIERARCHYSCOPE"
        })
        # EQP_CLASS_X_EQP_MAPPING
        eqpClassXEqpMappingList.append({
          "FID_EQP_CLASS_ID":"STANDARD_TAGS",
          "FID_EQP_CLASS_SYSTEM_ID":"OPCUA-Data",
          "FID_EQP_CLASS_GROUP_KEY":"TAG_GROUP",
          "FID_EQP_CLASS_GROUP_TABLE":"STANDARD_TAGS",
          "FID_EQP_ID":eqp,
          "FID_EQP_SYSTEM_ID":"OPCUA-Data",
          "FID_EQP_GROUP_KEY":eqp,
          "FID_EQP_GROUP_TABLE":eqp
        })
      else:
        key = obj[i]['k1'].split('/')[5]
        value = obj[i]['k3']
        # EQP_PROP
        eqpPropList.append({
          # "DESCRIPTION":"description",
          "VALUE":value,
          "ID":key,
          "SYSTEM_ID": "OPCUA-Data",
          "GROUP_KEY":eqp,
          "GROUP_TABLE":eqp,
          "PID_EQP_PROP_EQP_ID":eqp,
          "PID_EQP_PROP_EQP_SYSTEM_ID":"OPCUA-Data",
          "PID_EQP_PROP_EQP_GROUP_KEY":eqp,
          "PID_EQP_PROP_EQP_GROUP_TABLE":eqp
        })
    newObj['EQP_CLASS'] = eqpClassList
    newObj['EQP_CLASS_PROP'] = eqpClassPropList
    newObj['EQP'] = eqpList
    newObj['EQP_PROP'] = eqpPropList
    newObj['EQP_CLASS_X_EQP_MAPPING'] = eqpClassXEqpMappingList

    outputStream.write(bytearray(json.dumps(newObj, indent=4).encode('utf-8'))) 

flowFile = session.get()
eqpNameList = []
if (flowFile != None):
  flowFile = session.write(flowFile,PyStreamCallback())
  flowFile = session.putAttribute(flowFile, "Content Type", 'application/json')  
  flowFile = session.putAttribute(flowFile, "eqp-num", str(len(eqpNameList)))
  session.transfer(flowFile, REL_SUCCESS)