# Your imports go here
import logging
import re
import json

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    with open(dirpath + "/ocr.json","r",encoding='utf-8') as file:
        data = file.read()
        js = json.loads(data)
    json_text = ''
    for j in range(len(data['Blocks'])):

        try:

          if data['Blocks'][j]['Text']:

          json_text  += data['Blocks'][j]['Text'] + ' '
          
        except:
          pass
    detect = []
    if re.findall('CREDIT ([$]+[0-9\.]+)',json_text):
        detect = re.findall(r'CREDIT ([$]+[0-9\.]+)',json_text)
  
    elif re.findall('Total ([$]+[0-9\.]+)',json_text):
        detect = re.findall(r'Total ([$]+[0-9\.]+)',json_text)
  
    elif re.findall('TOTAL ([0-9\.]+)',json_text):
        detect = re.findall(r'TOTAL ([0-9\.]+)',json_text)

    elif re.findall('TOTAL ([$]+[0-9\.]+)',json_text):
        detect = re.findall(r'TOTAL ([$]+[0-9\.]+)',json_text)

    elif re.findall('Dance ([$]+[0-9\,\.]+)',json_text):
        detect = re.findall(r'Dance ([$]+[0-9\,\.]+)',json_text)

    elif re.findall('Total: ([$] +[0-9\,\.]+)',json_text):
        detect = re.findall(r'Total: ([$] +[0-9\,\.]+)',json_text)

    elif re.findall('AMOUNT PAID : ([$]+[0-9\,\.]+)',json_text):
        detect = re.findall(r'AMOUNT PAID : ([$]+[0-9\,\.]+)',json_text)

    elif re.findall('MasterCard ([$]+[0-9\,\.]+)',json_text):
        detect = re.findall(r'MasterCard ([$]+[0-9\,\.]+)',json_text)

    elif re.findall('USD ([0-9\.]+)',json_text):
        detect = re.findall(r'USD ([0-9\.]+)',json_text)

    elif re.findall('DEBIT ([$][0-9\.]+)',json_text):
        detect = re.findall(r'DEBIT ([$][0-9\.]+)',json_text)

    elif re.findall('Total USD ([0-9\.]+)',json_text):
        detect = re.findall(r'Total USD ([0-9\.]+)',json_text)

    elif re.findall('AMOUNT ([0-9\.]+)',json_text):
        detect = re.findall(r'AMOUNT ([0-9\.]+)',json_text)

    elif re.findall('Payment ([0-9\.]+)',json_text):
        detect = re.findall(r'Payment ([0-9\.]+)',json_text)

    elif re.findall('PAYEMENTS ([0-9\.]+)',json_text):
        detect = re.findall(r'PAYEMENTS ([0-9\.]+)',json_text)

    elif re.findall('([$]+[0-9\,\.]+)',json_text):
        detect = re.findall(r'([$]+[0-9\,\.]+)',json_text)
        
    amount = 0
    if detect[-1].split('$):
       amount = detect[i][-1].split('$')[-1] 
    else :
          amount = detect[-1]             
    return amount
