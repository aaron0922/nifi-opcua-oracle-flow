import json

text = '''
[ {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11",
  "k2" : "-11644473600000",
  "k3" : "",
  "k4" : "2150957056"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機",
  "k2" : "-11644473600000",
  "k3" : "",
  "k4" : "2150957056"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/interfaceID",
  "k2" : "1569397759119",
  "k3" : "2222",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/status",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/statusCode",
  "k2" : "1569397759119",
  "k3" : "123",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/passQty",
  "k2" : "1569397759119",
  "k3" : "13",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/failQty",
  "k2" : "1569397759119",
  "k3" : "12",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/errorCnt",
  "k2" : "1569397759119",
  "k3" : "20",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/errorTimes",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/cycleTime",
  "k2" : "1569397759119",
  "k3" : "100",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/runningTime",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/waitingTime",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/selfCheck",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/inputQty",
  "k2" : "1569397759119",
  "k3" : "25",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/barcode",
  "k2" : "1569397759119",
  "k3" : "1234",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/model",
  "k2" : "1569397759119",
  "k3" : "111",
  "k4" : "0"
} ]
'''
text2 = '''
[ {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11",
  "k2" : "-11644473600000",
  "k3" : "",
  "k4" : "2150957056"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機",
  "k2" : "-11644473600000",
  "k3" : "",
  "k4" : "2150957056"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/interfaceID",
  "k2" : "1569397759119",
  "k3" : "2222",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/status",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/statusCode",
  "k2" : "1569397759119",
  "k3" : "123",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/passQty",
  "k2" : "1569397759119",
  "k3" : "13",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/failQty",
  "k2" : "1569397759119",
  "k3" : "12",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/errorCnt",
  "k2" : "1569397759119",
  "k3" : "20",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/errorTimes",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/cycleTime",
  "k2" : "1569397759119",
  "k3" : "100",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/runningTime",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/waitingTime",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/selfCheck",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/inputQty",
  "k2" : "1569397759119",
  "k3" : "25",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/barcode",
  "k2" : "1569397759119",
  "k3" : "1234",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動插件機/model",
  "k2" : "1569397759119",
  "k3" : "111",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機",
  "k2" : "-11644473600000",
  "k3" : "",
  "k4" : "2150957056"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/interfaceID",
  "k2" : "1569397759119",
  "k3" : "1111",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/status",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/statusCode",
  "k2" : "1569397759119",
  "k3" : "123",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/passQty",
  "k2" : "1569397759119",
  "k3" : "13",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/failQty",
  "k2" : "1569397759119",
  "k3" : "12",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/errorCnt",
  "k2" : "1569397759119",
  "k3" : "20",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/errorTimes",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/cycleTime",
  "k2" : "1569397759119",
  "k3" : "100",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/runningTime",
  "k2" : "1569397759119",
  "k3" : "50",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/waitingTime",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/selfCheck",
  "k2" : "1569397759119",
  "k3" : "0",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/inputQty",
  "k2" : "1569397759119",
  "k3" : "25",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/barcode",
  "k2" : "1569397759119",
  "k3" : "1234",
  "k4" : "0"
}, {
  "k1" : "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/model",
  "k2" : "1569397759119",
  "k3" : "111",
  "k4" : "0"
} ]
'''

#print(text)
obj = json.loads(text2)
# print(obj[0])

# idx = 0
# for o in obj:
#   idx += 1
  # print(o)
  # print(o['k1'])
  # print(o['k1'].split('/')[4])  

# line = obj[0]['k1'].split('/')[3]
# print(line)
# 1+(1+14)+(1+14)...index:1,16,31
# print(len(obj)) 31

newObj = {}
eqpNameList = []
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

# print(eqpNameList)
# print(hierarchyScopeId)
# print(newObj)
# print(json.dumps(newObj, indent=4))
print((eqpNameList))
print(len(eqpNameList))

# s = "ns=1;s=/MES OPC UA Data Provider/東莞二廠/產線-P11/自動上平車機/selfCheck"
# a = s.split('/')
# print(a)
# print(a[4])

