import cv2
from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Path to the video file
video_path = 'videoplayback.mp4'
output_video_path = 'output_videoplayback.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Set up video writer to save the output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the current frame
    results = model(frame)
    annotated_frame = results[0].plot()  # Get the annotated frame with detections

    # Write the annotated frame to the output video
    out.write(annotated_frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Object detection completed. The output video is saved as {output_video_path}")
