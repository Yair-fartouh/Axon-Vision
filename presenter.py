import cv2
from datetime import datetime
from logger import Logger

logger = Logger.get_logger(__name__)

def presenter(input_queue):
    logger.info("Starting presenter process")

    while True:
        logger.debug("Waiting for processed frame...")
        item = input_queue.get()
        if item is None:
            break
        frame, boxes = item
        for (x, y, w, h) in boxes:
            roi = frame[y:y+h, x:x+w]
            blurred = cv2.GaussianBlur(roi, (21, 21), 0)
            frame[y:y+h, x:x+w] = blurred
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        timestamp = datetime.now().strftime("%H:%M:%S")
        cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Video Pipeline", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    logger.info(f"Presenter process completed. Total frames displayed: {frame_count}")
