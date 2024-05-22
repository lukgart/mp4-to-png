import cv2
import os


# Function to extract frames and save them as PNG
def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Loop through frames and save as PNG
    while success:
        frame_filename = os.path.join(output_folder, f"frame_{count:04d}.png")
        cv2.imwrite(frame_filename, image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    return count

# Example usage
video_path = '##############.mp4'  # Path to the input video file in Google Drive
output_folder = '/content/frames'  # Folder to save the frames in the Colab environment

# Extract frames and save them as PNG
frame_count = extract_frames(video_path, output_folder)
print(f"Extracted {frame_count} frames.")
