with open('recon.txt', 'r') as myfile:
  lines = myfile.readlines()

for line in lines:
  if line == '/n': #if the line is just a blank line we know its changing


