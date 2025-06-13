import cv2

def find_available_cameras():
    """
    Checks for available camera indices.
    Uses CAP_DSHOW for better compatibility on Windows.
    """
    print("Searching for available cameras...")
    available_indices = []
    index = 0
    while index < 10:  # Check up to 10 indices
        # Use cv2.CAP_DSHOW for more stable camera detection on Windows
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.isOpened():
            print(f"  [+] Camera found at index {index}")
            available_indices.append(index)
            cap.release()
        index += 1

    if not available_indices:
        print("\n  [!] No cameras were found.")
    else:
        print(f"\n  Available camera indices are: {available_indices}")
    return available_indices

if __name__ == "__main__":
    find_available_cameras()