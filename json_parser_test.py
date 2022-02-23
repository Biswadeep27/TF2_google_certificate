import json
 
ip_jsn ='''{
        "indicator" : "products",
        "mapStatus" : 1,
        "jsonString" : 1,
        "delimiter" : "",
        "mapDetail" : {
            "vendorNumber" : "vendorNumber",
            "modelId" : "modelId",
            "itemNumber" : "itemNumber",
            "imageUrls[].key" : "imageKey",
            "imageUrls[].value" : "imageValue",
            "omniItemId" : "omniItemId",
            "type" : "type",
            "sqFoot" : "sqFoot",
            "storeAttributes[].t024ItemDescription" : "ItemDescription",
            "storeAttributes[].values.keys" : "storeKeys",
            "storeAttributes[].values.attr[].key.baseVal" : "baseVal",
            "storeAttributes.ecatname" : "ecatname",
            "productVariants.variants[].pdURL" : "variantURL",
            "productVariants.variants[].attributes[].value" : "value",
            "productVariants.parentId" : "parentId"
        },
        "filter" : {
            "productStatus" : "true",
            "lcomIndicator" : "Y"
        }
    }'''
 
'''ip_jsn = {
        "indicator" : "products",
        "mapStatus" : 1,
        "jsonString" : 1,
        "delimiter" : "",
        "mapDetail" : {
            "vendorNumber" : "vendorNumber",
            "modelId" : "modelId",
            "itemNumber" : "itemNumber",
            "omniItemId" : "omniItemId",
            "type" : "type",
            "sqFoot" : "sqFoot"
            }
        }'''
 
dict_data = json.loads(ip_jsn)
 
map_detail = dict_data['mapDetail']
 
map_list = []
ren_col_list = []
attri_list = []
#i=0
for key,value in map_detail.items():
    map_list.append((key,value))
    ren_col_list.append(value)
    attri_list.append(key)
    #i+=1
 
enum_map_list = list(enumerate(map_list))
 
print('the enum map list')
print(enum_map_list)
print('just like a waving flag')
#print(ren_col_list)
#print('old me')
#print(attri_list)
 
#to check if there is any nested hierarchy to parse
returnCnt = 0
for _iter in attri_list:
    if '.' in _iter:
        returnCnt+=1    
 
##parsing begins from here
seen = set()
seen_add = seen.add
 
df_parser_attri_list = []
parser_attri_dict = {}
columns = []
ren_col = {}
 
for i in range(len(enum_map_list)):
    first_attr = enum_map_list[i][1][0].split('.')[0]
    if '[' in first_attr:
        clean_attr = first_attr[:first_attr.index('[')]
        #parser_attri_dict['explode_attr'] = clean_attr
        columns.append(clean_attr)
        ren_col[clean_attr] = clean_attr
    else:
        columns.append(first_attr)
        if '.' in enum_map_list[i][1][0]:
            ren_col[first_attr] = first_attr
        else:
            ren_col[first_attr] = enum_map_list[i][1][1]
uniq_columns = [x for x in columns if not (x in seen or seen_add(x))]
 
#parser_attri_dict['index'] = enum_map_list[i][0]
 
parser_attri_dict['columns'] = uniq_columns
parser_attri_dict['rename'] = ren_col
parser_attri_dict['explode_attr'] = ''
 
df_parser_attri_list.append(parser_attri_dict)
 
if returnCnt == 0:
    print(df_parser_attri_list)
else:
    print('picture abhi baki hai mere dost!')
    print(df_parser_attri_list)
 
    #escape condition for while true loop
    break_dict = {attri_val.split('.')[0].strip('[]') : (0,0) for attri_val in attri_list if '.' in attri_val} 
    
 
    for _iter in enum_map_list:
        if '.' in _iter[1][0]:
            dot_count = _iter[1][0].count('.')
            key_val = _iter[1][0].split('.')[0].strip('[]')
            if dot_count > break_dict[key_val][1]:
                break_dict[key_val] = (_iter[0],dot_count)
 
    print(break_dict)
    print(break_dict.values())
    break_string = [x[1][1] for x in enum_map_list if x[0] == max(break_dict.values())[0]][0]
    print(break_string)