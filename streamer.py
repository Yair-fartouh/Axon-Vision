import cv2

def streamer(video_path, output_queue):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        output_queue.put(frame)
    cap.release()
    output_queue.put(None)