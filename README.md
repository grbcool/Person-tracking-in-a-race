# Person-tracking-in-a-race

to run the model, run the following command
python3 Run.py -i videos/sample1.mp4 -o output/output.mp4 -s 2 -c 0.1 -xy 236 225 248 122


Improvements Need to be done:
1) Detector is unable to detect all persons in frame
2) I used the simple straight line equation to determine if the person has crossed a line or not but we can have bird view implementation using warp perspective from opencv and them implement the centroid tracking 
