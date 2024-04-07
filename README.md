# AI-Powered CCTV Surveillance System

## Overview

The increasing rate of crimes in high footfall areas across India necessitates the implementation of advanced technological solutions for public safety and law enforcement. This project aims to address this pressing issue by developing an AI-powered CCTV surveillance system specifically tailored to detect crimes happening in real-time.

The proposed system leverages cutting-edge artificial intelligence and computer vision algorithms to analyze real-time video feeds from strategically placed cameras. By using anamoly detection, object detection, and predictive analysis, it is capable of identifying criminal activities such as theft, vandalism, violence, fires, car crashes, and incidents like a person falling which could signify an assault, theft, or robbery on a real-time basis.

## Functional Requirements

### Object Detection

Through advanced object detection techniques, the system identifies _"events"_ that could occur in the public and would require help from authorities as soon as possible. These include criminal activities such as theft, vandalism, violence, fires, car crashes, and suspicious behaviors.

## Event Types

The system detects three main event types:

1. **Fire**: Detection of fire incidents.
2. **Car Crash**: Identification of car accidents.
3. **Person Falling**: Signifies potential assaults, thefts, or robberies.

Based on the feasibility of this solution, more _"events"_ will be added and implemented to deal with more commonly occuring events in CCTV systems.

### Real-time Alerts

The technology sends real-time alerts to the nearest police officers, enabling rapid response to criminal incidents. Alerts contain information such as the type of event, timestamp, camera number, and location.

## Alerting Mechanism

When an event is detected, alerts are sent via two channels:

1. **Web Interface**: Alerts are displayed on the interface accessible to police officials. The alert includes the type of event, timestamp, camera number, and location. We also offer the feature to view and review _"events"_ that could have occured in the past. We also provide a 10 second clip of that event which the admin / police official could review in order to determine whether the event requires authorities to send help or not.
   
2. **Email Notification**: In case police officials are not actively monitoring the web interface, alerts are sent to a designated email address. 

It's important to note that the system is designed to alert authorities to potential criminal activities but does not trigger any immediate action. It is up to the police to review the footage and decide on the appropriate response.

## Technologies Used

- **Computer Vision / Machine Learning**: OpenCV, YOLOv9, Mediapipe, Tensorflow, scikit-learn, seaborn
- **Back-end**: Express, MongoDB
- **Front-end**: React, Tailwind

## Usage

To deploy the surveillance system:

1. Install the necessary dependencies as outlined in the installation guide.
2. To use the requirements.txt file, you can simply use the following command-
```
> pip install -r /path_to/requirements.txt
```
4. Configure the system to integrate with CCTV cameras.
5. Start the system to begin real-time monitoring and detection of criminal activities.
6. Monitor the web interface for alerts and take necessary actions based on the alerts received.

## Important Notes

- The system is designed to alert authorities to potential criminal activities but does not trigger any immediate action. It is up to the police to review the footage and decide on the appropriate response.
- Future extensions of the system may include identifying and tracking individuals with a history of criminal behavior or those on law enforcement watch lists.

## Contributors

- Alan Thomas
- Aditya Pratap Singh
- Ayush Kadam
- Bharath Mudduluru


Developed during DEVSOC, 42 hour hackathon.
Dated 17/03/2024

---

**Disclaimer:** The proposed system should be deployed and used responsibly, adhering to all applicable laws and regulations regarding surveillance and privacy.
