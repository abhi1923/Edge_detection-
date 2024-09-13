# Line Segment Detection and DXF Export

This edge detection algotithm performs line segment detection on images using OpenCV's Line Segment Detector (LSD) and exports the detected lines to a DXF file format using the `ezdxf` library. This is useful for applications requiring conversion of image lines into a vector format for further processing or CAD applications.

## Features
- Detects line segments in images using OpenCV's LSD.
- Filters out short lines based on a minimum length threshold.
- Exports the detected lines to a DXF file for use in CAD or other vector-based applications.

## Requirements

- Python 3.x
- OpenCV
- `ezdxf` library

## Installation
pip install opencv-python ezdxf

