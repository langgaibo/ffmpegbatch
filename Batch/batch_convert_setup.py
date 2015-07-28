# Written off the cuff by Gabe Langton 2015
from os import listdir
from os.path import isfile, join

# Make sure to specify the absolute path to /Batch in both places here.
contents = [ f for f in listdir('/Users/gabe/Movies/Bucket/Batch') if isfile(join('/Users/gabe/Movies/Bucket/Batch',f))]

print contents
print "\n\n"

# Modify these cleaners with the video file extension of your choice.
# Make sure to change the extension below, in the ffmpeg arguments %s substitution
cleaned = filter(lambda m: '.MOV' in m, contents)

# In my common use case, different apple devices result in different caps
# for the .mov extension... so this just normalizes them into a single list.
cleaned_lower = filter(lambda m: '.mov' in m, contents)
for f in cleaned_lower:
    upped = f.replace(".mov", ".MOV")
    cleaned.append(upped)

# Opens and overwrites the contents of the commands file
batch_text = open('staged_commands.txt', 'w')
for n in cleaned:
# This is my most common argument set for ffmpeg. Please review the ffmpeg
# documentation and substitute your own arguments for your own batch.
# Especially note that the ""-crf" option is not universal. There are other
# quality commands for other file types!!!
    line = 'ffmpeg -i %s -crf 30 -threads 2 %s\n' %(n, n.replace(".MOV", ".mp4"))
    batch_text.write(line)
batch_text.close()
