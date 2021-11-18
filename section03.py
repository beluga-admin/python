# Section03
# python virtualenv understanding and pip with vscode


#package installation test
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

#simplejson 
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))