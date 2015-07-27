#test logic for executing a shell script to process a batch of .mov files
#with ffmpeg
from os import listdir
from os.path import isfile, join

contents = [ f for f in listdir('/Users/gabe/Movies/Batch') if isfile(join('/Users/gabe/Movies/Batch',f))]

print contents
print "\n\n\n\n"

cleaned = filter(lambda m: '.MOV' in m, contents)
cleaned_lower = filter(lambda m: '.mov' in m, contents)
for f in cleaned_lower:
    upped = f.replace(".mov", ".MOV")
    cleaned.append(upped)

batch_text = open('staged_commands.txt', 'w')

print "New contents of staged_commands.txt"

for n in cleaned:
    line = 'ffmpeg -i %s -crf 30 -threads 2 %s\n' %(n, n.replace(".MOV", ".mp4"))
    print line
    batch_text.write(line)

batch_text.close()
