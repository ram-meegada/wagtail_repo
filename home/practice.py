import re, json
def method1(string):
    s = re.sub(r'[^a-zA-Z0-9\s{}:,._@""()\[\]]', '', string)
    return s

def method2(string):
    special_character = ''.join([chr(i) for i in range(32, 127)])
    s = re.sub(fr'[^{special_character}]', '',string)   
    b = json.loads(s)
    return s

def problem1():
    # string = "rammmmm"
    a = b'{"terms_and_conditions":"<p>sdf</p>\\n","privacy":"<p>sdfsd</p>\\n","about_us":"<p>E-NILCON \xe2\x80\x98s history spans 25 years of integration of companies and business, allowing it provide a complete EPC solutions under a qualifies experienced and committed staff</p>\\n","legal":"<p>sdf</p>\\n","cms_email":"admin@enilcon.com","cms_phone":"6435347564","cms_country_code":"in","cms_country_iso_code":"91","executive_phone":"","executive_country_code":"","executive_country_iso_code":""}\x05\x05\x05\x05\x05'
    try:
        decrypted = a.decode('ascii')
    except:
        decrypted = a.decode('utf-8')    
# print(method2(decrypted))
# print(method1(decrypted))

def problem2(string):
    left, right = [0, 'n', 0], [len(string)-1,'n',0]
    left_required, right_required = 0, len(string)-1
    while (left[1] == 'n' or right[1] =='n') and left<right:
        if string[left[0]] != "[":
            left[0] += 1
        else:
            left[2] = left[0]
            left[1] = 'y'
        if string[right[0]] != "]":
            right[0] -= 1
        else:
            right[2] = right[0]
            right[1] = 'y'
    return string[left[2]:right[2]+1]


def problem2(string):
    left, right = 0, len(string)-1
    try:
        while string[left] != '[' and left < len(string)-1:
            left += 1
        while string[right] != ']' and right >= 0:
            right -= 1
    except Exception as e:
        return e
    print(left, right)
    return string[left:right+1]

string = "@@[1,2,3,4]*&+"
print(problem2(string))