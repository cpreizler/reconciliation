
def main():
	yesterdayPos=[]
  todayPos=[]
  todayTrans=[]
	fillLists('recon.txt', yesterdayPos, todayPos, todayTrans)
	


def fillLists(fileName, yesterdayPos, todayPos, todayTrans):
  with open(fileName, 'r') as myfile:
    lines = myfile.readlines()

  length = len(lines)
  i=1
  while i < length: 
    if lines[i-1] =='D0-POS': #if the previous line was the header, we want to loop until the blank line and add it to correct list, Im sure theres a more efficient way to do this without nested loops in linear time instead of exponential but I did not have time to optimize
      while lines[i] !='\n' and i<length:
        yesterdayPos.append(lines[i])
        i+=1

    else if lines[i-1] =='D1-TRN': 
      while lines[i] !='\n' and i<length:
        todayTrans.append(lines[i])
        i+=1

    else if lines[i-1] =='D1-POS': 
      while lines[i] !='\n' and i<length:
        todayPos.append(lines[i])
        i+=1

    i+=1
    


