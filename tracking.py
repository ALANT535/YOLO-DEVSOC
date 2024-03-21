import cv2
import os
import matplotlib.pyplot as plt
import sys

#this is x,y,width,height
def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)


def displayRectangle(frame, bbox):
    plt.figure(figsize=(20, 10))
    frameCopy = frame.copy()
    drawRectangle(frameCopy, bbox)
    frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_RGB2BGR)
    plt.imshow(frameCopy)
    plt.axis("off")
    plt.show()


def drawText(frame, txt, location, color=(255, 0, 0)):
    cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)


tt_type = [
    "BOOSTING",
    "MIL",
    "CSRT",
    "TLD",
    "MEDIANFLOW",
    "GOTURN"
]

# Change the index to change the tracker type
tracker_type = "MIL"
# tracker = cv2.Tracker_create(tracker_type)
 
if tracker_type == "BOOSTING":
    tracker = cv2.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv2.TrackerMIL.create()
# elif tracker_type == "KCF":
#     tracker = cv2.TrackerKCF_create()
elif tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT.create()
elif tracker_type == "TLD":
    tracker = cv2.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv2.TrackerGOTURN.create(r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\goturn.prototxt")
else:
    tracker = cv2.legacy.TrackerMOSSE_create()

video_input_file_name = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\videos\twitter2_crop.mp4"
# video_input_file_name = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\videos\twitter_crop.mp4"
video = cv2.VideoCapture(video_input_file_name)
ok, frame = video.read()

# Exit if video not opened
if not video.isOpened():
    print("Could not open video")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_output_file_name = "race_car-" + tracker_type + ".mp4"
video_out = cv2.VideoWriter(video_output_file_name, cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height))

print(video_output_file_name)
bbox = (131,126,122,178)
# bbox = (334,128,373-334,149-128)
displayRectangle(frame, bbox)

ok = tracker.init(frame, bbox)

frame_count = 0  # Initialize frame counter

while True:
    ok, frame = video.read()

    if not ok:
        break
    
    frame_count += 1
    ok, bbox = tracker.update(frame)
        
    if frame_count % 3 != 0:
        continue

    # Process only every other frame

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if ok:
        drawRectangle(frame, bbox)
    else:
        drawText(frame, "Tracking failure detected", (80, 140), (0, 0, 255))

    # Display Info
    drawText(frame, tracker_type + " Tracker", (80, 60))
    drawText(frame, "FPS : " + str(int(fps)), (80, 100))
    displayRectangle(frame,bbox)

    # Write frame to video
    video_out.write(frame)
    cv2.waitKey(0)

video.release()
video_out.release()


# import cv2
# import sys
# if __name__ == '__main__':

#     # Set up tracker.
#     # Instead of MIL, you can also use

#     tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
#     tracker_type = tracker_types[6]

#     if int(major_ver) < 4 and int(minor_ver) < 3:
#         tracker = cv2.cv2.Tracker_create(tracker_type)
#     else:
#         if tracker_type == 'BOOSTING':
#             tracker = cv2.TrackerBoosting_create()
#         if tracker_type == 'MIL':
#             tracker = cv2.TrackerMIL_create()
#         if tracker_type == 'KCF':
#             tracker = cv2.TrackerKCF_create()
#         if tracker_type == 'TLD':
#             tracker = cv2.TrackerTLD_create()
#         if tracker_type == 'MEDIANFLOW':
#             tracker = cv2.TrackerMedianFlow_create()
#         if tracker_type == 'CSRT':
#             tracker = cv2.TrackerCSRT_create()
#         if tracker_type == 'MOSSE':
#             tracker = cv2.TrackerMOSSE_create()

#     # Read video
#     video = cv2.VideoCapture(0)

#     # Exit if video not opened.
#     if not video.isOpened():
#         print("Could not open video")
#         sys.exit()

#     # Read first frame.
#     ok, frame = video.read()
#     if not ok:
#         print('Cannot read video file')
#         sys.exit()

#     # Define an initial bounding box
#     bbox = (287, 23, 86, 320)

#     # Uncomment the line below to select a different bounding box
#     bbox = cv2.selectROI(frame, False)

#     # Initialize tracker with first frame and bounding box
#     ok = tracker.init(frame, bbox)

#     while True:
#         # Read a new frame
#         ok, frame = video.read()
#         if not ok:
#             break

#         # Start timer
#         timer = cv2.getTickCount()

#         # Update tracker
#         ok, bbox = tracker.update(frame)

#         # Calculate Frames per second (FPS)
#         fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

#         # Draw bounding box
#         if ok:
#             # Tracking success
#             p1 = (int(bbox[0]), int(bbox[1]))
#             p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
#             cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
#         else :
#             # Tracking failure
#             cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

#         # Display tracker type on frame
#         cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

#         # Display FPS on frame
#         cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

#         # Display result
#         cv2.imshow("Tracking", frame)

#         # Exit if ESC pressed
#         k = cv2.waitKey(1) & 0xff
#         if k == 27 : break


