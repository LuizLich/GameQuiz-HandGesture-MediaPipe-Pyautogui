import cv2
import numpy as np

def adjust_gamma(image, gamma=1.8):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

def preprocess_frame(frame):
    # Equalizacao de histograma para melhorar contraste
    frame_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    frame_yuv[:, :, 0] = cv2.equalizeHist(frame_yuv[:, :, 0])
    frame = cv2.cvtColor(frame_yuv, cv2.COLOR_YUV2BGR)

    # Correcao de gamma para iluminar imagem escura
    frame = adjust_gamma(frame, gamma=1.8)

    # Remocao de ruido
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    return frame