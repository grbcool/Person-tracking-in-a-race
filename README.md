# Person-tracking-in-a-race
to get the co-ordinates in a frame at the end of a video following is the python command:

python3 get_cordinates.py -i paht-to-video

to run the model, run the following command:

python3 Run.py -i path-to-video -o path-to-save-file-to -s #skip_frames -c confidence -xy 4-points-stating-xy-co-ordinates-of-line
for example (python3 Run.py -i videos/sample1.mp4 -o output/output.mp4 -s 2 -c 0.1 -xy 236 225 248 122)


Improvements Need to be done:
1) Detector is unable to detect all persons in frame
2) I used the simple straight line equation to determine if the person has crossed a line or not but we can have bird view implementation using warp perspective from opencv and them implement the centroid tracking 
3) A good dataset
