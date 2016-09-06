# coding: utf8
# 朗盖博 2015
from os import listdir
from os.path import isfile, join

# list all the filenames in the source file directory.
# REPLACE '...' with the absolute path to the Batch directory in both places in this line!
contents = [ f for f in listdir('.../Batch') if isfile(join('.../Batch',f))]

# make an empty bucket to fill with normalized filenames
cleaned = []

# escape spaces in filenames
upper = filter(lambda m: '.MOV' in m, contents)
for f in upper:
    despaced = f.replace(" ", "\ ")
    cleaned.append(despaced)

# normalize lowercase filename extensions
lower = filter(lambda m: '.mov' in m, contents)
for f in lower:
    uppered = f.replace(".mov", ".MOV")
    despaced = uppered.replace(" ", "\ ")
    cleaned.append(despaced)

# open and overwrite a text file with a list of ffmpeg commands
batch_text = open('staged_commands.txt', 'w')
for n in cleaned:
<<<<<<< HEAD
    # IMPORTANT: see ffmpeg documentation for guidance on quality settings.
    # here, '-crf 26' represents a high compression level, at the expense of slight degradation in video quality.
    # Normal "sane" range for -crf is 18 (visually lossless) to 28 (often 10x filesize reduction with acceptable quality)
    line = 'ffmpeg -i %s -crf 26 -threads 2 %s\n' %(n, n.replace(".MOV", ".mp4"))
    batch_text.write(line)
=======

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

>>>>>>> 88450b322a58b6e88d661557490fea0565fc3f5f
batch_text.close()
