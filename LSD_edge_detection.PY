import cv2
import ezdxf

def save_lines_as_dxf(lines, output_dxf_path):

    doc = ezdxf.new()
    msp = doc.modelspace()

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            msp.add_line(start=(x1, y1), end=(x2, y2))

    doc.saveas(output_dxf_path)
    print(f"Saved {output_dxf_path}")

def filter_long_lines(lines, min_length):
  
    filtered_lines = []
    for line in lines:
        x1, y1, x2, y2 = line
        line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if line_length >= min_length:
            filtered_lines.append(line)
    return filtered_lines

def lsd_lines(image, min_length=20):

    lsd = cv2.createLineSegmentDetector(0)
    lines = lsd.detect(image)[0]  

    if lines is not None:
        lines = [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in lines[:, 0]]
        lines = filter_long_lines(lines, min_length)
    
    return lines

def detect_and_save_lsd(image_path, output_dxf_path, min_length=50):
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    lines = lsd_lines(image, min_length)

    save_lines_as_dxf(lines, output_dxf_path)

image_path = "IMAGE_PATH"
output_dxf_path = "lsd_output_path.dxf"

detect_and_save_lsd(image_path, output_dxf_path, min_length=20)  