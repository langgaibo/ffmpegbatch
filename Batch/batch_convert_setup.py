# coding: utf8
# 朗盖博 2015
from os import listdir
from os.path import isfile, join

# Make sure to specify the absolute path to /Batch in both places here.
contents = [ f for f in listdir('.../Batch') if isfile(join('.../Batch',f))]

# Modify these cleaners with the video file extension of your choice.
# Mine handle capitalization and spaces, probably not elegantly
# Make sure to change the extension below, in the ffmpeg arguments %s substitution
cleaned = []

upper = filter(lambda m: '.MOV' in m, contents)

for f in upper:
    undered = f.replace(" ", "\ ")
    cleaned.append(undered)

# In my common use case, different apple devices result in different caps
# for the .mov extension... so this just normalizes them into a single list.
lower = filter(lambda m: '.mov' in m, contents)

for f in lower:
    undered = f.replace(" ", "\ ")
    cleaned.append(undered)

# Below is my most common argument set for ffmpeg. Please review the ffmpeg
# documentation and substitute your own arguments for your own batch.
# Especially note that the ""-crf" option is not universal. There are other
# quality commands for other file types!!!

# Opens and overwrites the contents of the commands file
batch_text = open('staged_commands.txt', 'w')
for n in cleaned:

    if ".MOV" in n:
        # Write the new output video to a subdirectory
        line = 'ffmpeg -i %s -crf 30 -threads 2 ./converted/%s\n' %(n, n.replace(".MOV", ".mp4"))
        batch_text.write(line)
        # And dump the original file into another subdirectory, so there's less management
        # or overwriting - alternatively you can just delete the originals here if you won't need
        # them again.
        sweep = 'mv %s ./originals/%s\n' % (n, n)
        batch_text.write(sweep)

    elif ".mov" in n:
        line = 'ffmpeg -i %s -crf 30 -threads 2 ./converted/%s\n' %(n, n.replace(".mov", ".mp4"))
        batch_text.write(line)
        sweep = 'mv %s ./originals/%s\n' % (n, n)
        batch_text.write(sweep)

batch_text.close()
