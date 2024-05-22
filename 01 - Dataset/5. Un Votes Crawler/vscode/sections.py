import lxml
from lxml import etree
from lxml import html

file = open("dowloads/contents_221")
txt  = file.read()
file.close()
parser = etree.HTMLParser()
t=etree.fromstring(txt,parser)
count = -1
divs  = []
for e in t.iter():
    count = count + 1 
    if e.tag == "div":
        divs.append(e)

print(len(divs))
count = -1
for e in divs:
    count = count + 1
    match count:
        case 0:
            print("---------------------------title")
            print(e.getchildren()[1].text)
            print(count)   
        case 1:
            print("---------------------------Agenda")
            print(e.getchildren()[1].getchildren()[0].text) 
            print(count)   
        case 2:
            print("---------------------------resolution")
            print(e.getchildren()[1].getchildren()[0].text) 
            print(count)   
        case 7:
            print("---------------------------Summary")
            print(e.getchildren()[1].getchildren()[1].text) 
            print(count)   
        case 10:
            print("---------------------------DATE")
            print(e.getchildren()[1].text) 
        case 11:
            print("---------------------------Vote")
            data = html.tostring(e.getchildren()[1], method='text', encoding='unicode')
            # target   = e.getchildren()[1]
            # text     = e.text_content()
            print(data) 
            # print(e.getchildren()[1].getchildren()) 
            # br = e.getchildren()[1].getchildren()
            # i = 0
            # for b in br:
            #     b.getparent().remove(b)
            #     # print(b)
            #     # e.getchildren()[1].remove(b)
            #     i = i + 1
            # print(e.getchildren()[1].text)

        #     print(count)   
        # case 6:
        #     print("---------------------------2")
        #     print(e.tag) 
        #     print(count)   
        # case 7:
        #     print("---------------------------3")
        #     print(e.tag) 
        #     print(count)   
            
        # case 8:
        #     print("---------------------------4")
        #     print(e.tag) 
        #     print(count)   
        # case 9:
        #     print("---------------------------5")
        #     print(e.tag) 
        #     print(count)   
        # case 10:
        #     print("---------------------------6")
        #     print(e.tag) 
        #     print(count)  
        # case 11:
        #     print("---------------------------6")
        #     print(e.tag) 
        #     print(count)  
        # case 12:
        #     print("---------------------------6")
        #     print(e.tag) 
        #     print(count)  
        # case 13:
        #     print("---------------------------6")
        #     print(e.tag) 
        #     print(count)
        # case 14:
        #     print("---------------------------6")
        #     print(e.tag) 
        #     print(count)                            
        # Tenemos 11 div
            # 0 __ title
            # 1 __ tema
            # 2 __ sesion
            # 3 __ NO
            # 4 __ resid
            # 5 __ NO
            # 6 __ NO
            # 6 __ SUMMARY
            # 7 __ DATE
            # 8 __ NO
            # 9 __ VOTES
        



