import subprocess
import torch

def call_YOLO(weights_path, source_path, confidence_threshold, device):
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
        r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\detect.py",
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


#change the weights you want here
weights_path = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\weights\yolov9-c.pt"

#change the image you want to process here
source_path = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\images\CRASH.jpeg"
# source_path = r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\YOLOV9\yolov9\videos\road_vid.mp4"
confidence_threshold = 0.1
device = "cpu"

call_YOLO(weights_path, source_path, confidence_threshold, device)