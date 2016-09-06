### About ###
This is a quick, uncomplicated self-contained directory for batch conversion of videos via the ffmpeg tool.

### Dependencies ###
ffmpeg should be installed. I used Homebrew on OSX.
For compiling on other OS,  see ffmpeg compilation guide here: https://trac.ffmpeg.org/wiki/CompilationGuide

### Setup ###
1. Put the containing folder "Batch" in a convenient directory you will use for converting video files in batch form.
2. Modify the batch_convert_setup.py script to include your absolute path to the Batch folder.
3. Make sure the ffmpeg command to be applied in the python script is correct for the file types you'll be converting.
4. Modify the shell script batch_time.sh to include the absolute path to the Batch directory.
5. Chmod u+x the shell script and put it somewhere in your PATH if you wish to run from anywhere in the CLI.

### How to use this ###
1. Follow the Setup above, making sure to set the absolute path to the Batch folder. 
Do this at all the indicated lines in the batch_convert_setup.py file.
2. Drop any .mov files you wish to convert into the Batch folder (If you wish to convert a different type of video file, make sure to modify batch_convert_setup.py appropriately).
3. Run the batch_time.sh script. Your finished converted files will be written to the "converted" subdirectory, and the originals will be moved to the "originals" directory. This way you can just "dump and run" without moving files around, and delete / manage the originals at your leisure without reconverting them. Treat the Batch folder as a general hopper/bucket, run the script, and deal with the original and converted files at your leisure.

The python script is very simple.
It's set up to convert .mov files to .mp4, mostly for file size reduction.
My comments explain where to modify the python and shell scripts for different file types etc.
Check the ffmpeg documentation for your desired conversion, and just make sure the command in the script matches what you want before running.
