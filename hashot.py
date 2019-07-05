import csv
from time import strptime

filename = 'july19'

with open(filename.rstrip('.tsv')+'.tsv', encoding='utf8') as infile, open('out.md', 'w', encoding='utf8') as outfile:
  reader = csv.reader(infile, delimiter='\t')
  outfile.write('<div dir="rtl" style="text-align: right;">')
  for row in reader:
    if row[0].startswith('תאריך'):
      continue
    date = row[0]
    if date[0].isdigit():
      date_split = date.split(' ',1)
      date = '%s/%d'%('-'.join(date_split[0].split('-')[::-1]), strptime(filename[:3],'%b').tm_mon)
      if len(date_split)>1:
        date = '%s %s'%(date, date_split[1])
    outfile.write('<strong>%s</strong> %s<br />\n'%(date,row[1]))
    if row[2]:
      outfile.write('%s<br />\n'%row[2])
    for url in row[3].split(' '):
      outfile.write('<a href="%s" target="_blank">%s</a><br />\n'%(url,url))
    outfile.write('<br />\n')