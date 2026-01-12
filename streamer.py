import cv2
from logger import Logger

logger = Logger.get_logger(__name__)


def streamer(video_path, output_queue):
    logger.info(f"Starting streamer process for video: {video_path}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logger.error(f"Failed to open video file: {video_path}")
        output_queue.put(None)
        return

    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    logger.info(f"Video opened successfully. FPS: {fps}")

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.info(f"End of video reached. Total frames processed: {frame_count}")
            break

        frame_count += 1
        output_queue.put(frame)

        if frame_count % 100 == 0:
            logger.debug(f"Streamed {frame_count} frames")

    cap.release()
    output_queue.put(None)
    logger.info("Streamer process completed :)")