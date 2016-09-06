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
    # IMPORTANT: see ffmpeg documentation for guidance on quality settings.
    # here, '-crf 26' represents a high compression level, at the expense of slight degradation in video quality.
    # Normal "sane" range for -crf is 18 (visually lossless) to 28 (often 10x filesize reduction with acceptable quality)
    line = 'ffmpeg -i %s -crf 26 -threads 2 %s\n' %(n, n.replace(".MOV", ".mp4"))
    batch_text.write(line)
batch_text.close()
