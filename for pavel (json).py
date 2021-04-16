import json
import os
import glob

def process_gw_json_file(gw_json_file_path):
    out_file = open(gw_json_file_path + 'info_from_gw.txt', 'w')
    with open(glob.glob(os.path.join(gw_json_file_path + '*' + 'gw.json.j2'))[0], 'r') as json_file:
        data = json.load(json_file)
        for p in data['config']['endpoints']:
            endpoint = p['endpoint']
            try:
                method = p['method']
            except:
                method = '-'
            try:
                resource_type = p['extra_config']['git.omprussia.ru/auth/krakendpermissions']['resource_type']
            except:
                resource_type = '-'
            try:
                action = p['extra_config']['git.omprussia.ru/auth/krakendpermissions']['action']
            except:
                action = '-'
            try:
               if('git.omprussia.ru/auth/krakendaudit' in p['extra_config']):
                   audit = "yes"
            except:
                audit = 'no'
            if os.path.exists(gw_json_file_path + 'policy.json.j2'):  # Проверка на наличие файла policy.
                arr_policies = get_gw_policies(gw_json_file_path)
                roles = get_roles(arr_policies, resource_type, action)
                out_file.write(endpoint + ',' + method + ',' + resource_type + ',' + action + ',' + audit + ',' + roles + '\n')
            else:
                out_file.write(endpoint + ',' + method + ',' + resource_type + ',' + action + ',' + audit + ',' + '-' + '\n')
    json_file.close()
    out_file.close()


def get_gw_policies(gw_policy_file_path):
    arr = []
    arr_row = 0
    with open(glob.glob(os.path.join(gw_policy_file_path + 'policy.json.j2'))[0], 'r') as json_file:
        data = json.load(json_file)
        for p in data:
            arr.append([])
            try:
                arr[arr_row].append(p['subject'])
            except:
                print("Subject not found")
            try:
                arr[arr_row].append(p['resourceType'])
            except:
                print("Resource type not found")
            try:
                arr[arr_row].append(p['action'])
            except:
                print("Action not found")
            arr_row = arr_row + 1
    json_file.close()
    return arr

def get_roles(policies, resourceType, action):
    roles_arr = []
    for policy in policies:
        if policy[1].find(resourceType) != -1 and policy[2].find(action) != -1:
            roles_arr.append(policy[0])
    return "|".join(roles_arr)


#arr_policies = get_gw_policies('/home/user45/install-apps/inventories-appstore/config/gateways/ocs-appstore-admin-api-gw/policy.json.j2')
#process_gw_json_file('/home/user45/install-apps/inventories-appstore/config/gateways/ocs-appstore-admin-api-gw/ocs-appstore-admin-api-gw.json.j2', arr_policies)


folder = ''
for i in os.walk('resources'):
    folder += str(i) + '\n'
folder = folder.replace('(' , '')
folder = folder.replace(')' , '')
folder = folder.replace("'" , '')
folder = folder.replace('\\' , '/')
folder = folder.replace('//' , '/')

mass = folder.split('\n')
for i in mass:
    if '-gw.json.j2' in i:
        mass_dir = i.split(',')
        direction = mass_dir[0] + '/'
        print(direction)
        process_gw_json_file(direction)
