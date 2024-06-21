import xml.etree.ElementTree as ET 
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    rootElm = tree.getroot() 

    print(f"Root: {rootElm}")
  
    # # create empty list for news items 
    headerItems = [] 
  
    # iterate news items 
    for item in rootElm.findall('./DIV1/HEAD'): 
        
        print(item.text)

        # # empty news dictionary 
        # news = {} 
  
        # # iterate child elements of item 
        # for child in item: 
  
        #     # special checking for namespace object content:media 
        #     if child.tag == '{http://search.yahoo.com/mrss/}content': 
        #         news['media'] = child.attrib['url'] 
        #     else: 
        #         news[child.tag] = child.text.encode('utf8') 
  
        # # append news dictionary to news items list 
        # headerItems.append(news) 
      
    # return news items list 
    return headerItems 

def main(): 

    # parse xml file 
    headerItems = parseXML('data/ecfr/title-14-tiny.xml')
    # parseXML('title-14.xml') 
    print(headerItems)
  

if __name__ == "__main__": 
  
    # calling main function 
    main() 