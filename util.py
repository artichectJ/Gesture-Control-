import numpy as np

def get_angle(a, b, c):
    """
    Returns the angle (in degrees) formed at point b by the points a-b-c.
    """
    try:
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(np.degrees(radians))
        if angle > 180:
            angle = 360 - angle
        return angle
    except:
        return 0.0

def get_distance(landmark_list):
    """
    Returns the Euclidean distance between two (x, y) landmarks, scaled to [0, 1000].
    """
    if len(landmark_list) < 2:
        return 0.0
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    distance = np.hypot(x2 - x1, y2 - y1)
    return np.interp(distance, [0, 1], [0, 1000])
