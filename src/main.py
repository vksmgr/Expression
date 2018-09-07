import re




f = open("/home/lab/HadoopProject/Expression/data/input.txt",'r')
f_o = open("/home/lab/HadoopProject/Expression/data/output.txt",'+w')

# regular expressions

## Email Id
email = r'([\w\._]+)@([\w\._]+)'

## Email with Text
email_txt = r'[a-zA-Z0-9.-]+\[?(at|@|At|AT)\]?[a-zA-Z]+(\[?(\.|Dot|dot|DOT)\]?[a-zA-Z]*)+'

##Date
date=r'(([0-2]\d)|([0-9])|([0]\d))[\.|\/|-](([0][0-9])|([0-1][0-2])|[0-9])[\.|\/|-](([0-9][0-9][0-9][0-9])|[0-9][0-9])'

##Mobile
mobile_no = r'(\(?\+?\s?(91)?\s?\))?\s?\d{10}'

##landline
landline = r'(\(?\s?\d{3}\s?\)?)?\s?\d{5}'

##Currency
currency = r'\$?\s?\d+(\,)?\d*\.\d+\s?(dollars)?'

##URL
url = r'(https://)?www\.[a-zA-z0-9.-]+\.[a-zA-z0-9.-]*'

for line in f.readlines():
    #EMAIL
    match = re.finditer(email, line)
    for mt in match:
        if mt:
            print(mt.group())
            f_o.write("\n")
            f_o.write(mt.group())

    #DATE
    match = re.finditer(date, line)
    for mt in match:
        if mt:
            print(mt.group())
            f_o.write("\n")
            f_o.write(mt.group())

    #MOBILE NO.
    match = re.finditer(mobile_no, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

    #Landline NO.
    match = re.finditer(landline, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

    #Currency.
    match = re.finditer(currency, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

    #email_txt.
    match = re.finditer(email_txt, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

    #email_txt.
    match = re.finditer(email_txt, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

    #URL.
    match = re.finditer(url, line)
    for mt in match:
        if mt:
            print(mt.group().strip())
            f_o.write("\n")
            f_o.write(mt.group().strip())

