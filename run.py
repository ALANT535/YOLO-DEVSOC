import subprocess
import torch
import os

def call_YOLO(detect_path,weights_path, source_path, confidence_threshold, device):
    # Construct the command along with the two parameter that will be passed to the model
    # the weights you want to use
    #for TOLOV9 we have 4 choices
        #gelan-c.pt
        #gelan-e.pt
        #yolov9-c.pt
        #yolov9-e.pt
    
    # secondly, the source which you want to process
    # this can be an image, a video, your webcam
    
    command = [
        "python",
        detect_path,
        "--weights",
        weights_path,
        "--conf",
        str(confidence_threshold),
        "--source",
        source_path,
        "--device",
        device
    ]


    subprocess.run(command)


#provide the path to the detect.py file here
#this is the file that calls on the YOLOv9 model
#As far as we are concerned this is how we interact with YOLO
current_directory = os.getcwd()
detect_path = os.path.join(current_directory,"YOLO MODEL","detect.py")

#change the weights you want here
weight = "gelan-c.pt"
current_directory = os.getcwd()
weights_path = os.path.join(current_directory,r"YOLO MODEL\weights",weight)
# r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\weights\yolov9-c.pt"

#change the image you want to process here
source_path = os.path.join(current_directory,"Resources","CRASH.jpeg")
# source_path = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\videos\road_vid.mp4"
confidence_threshold = 0.1
device = "cpu"

call_YOLO(detect_path,weights_path, source_path, confidence_threshold, device)