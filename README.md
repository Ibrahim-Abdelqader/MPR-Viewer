# MPR Viewer
<img src="https://github.com/user-attachments/assets/3e606e68-24dd-4f9c-b3b3-0e10bf4532d7" width="400" />
<img src="https://github.com/user-attachments/assets/0b89d867-3df1-42f4-9bd1-c251da12e808" width="400" />
A multi-planar reconstruction (MPR) program displays the 4 views for medical images: sagittal, coronal, axial, and 3D view.

---
## Table of content
- [Video](#video)
- [Features](#features)
- [Technologies](#technologies)
- [How to use](#how-to-use)

---

## video
<video src="https://github.com/user-attachments/assets/94c5e3e1-eb01-4c1e-bab5-1446492c8f22" width="0" controls>
  Your browser does not support the video tag.
</video>

---

## Features
- Open a medical data in (.mhd & .raw) format.
- Zoom (in-out) using the mouse.
- Scroll through slices in each view.
- Cine play/pause/stop in any viewer.
- Cine can run in multiple viewers simultaneously.
- Indicate each slice on the other planar viewers.
- Brightness-contrast control using the mouse.
- Ability to maximize each viewer and restore it.
- Ability to resize each viewer and swap them.

## Technologies
- Python
- PyQt5
- VTK

---

## How to use
#### Installation
```Terminal
$ pip install -r requirements.txt
```
#### Run Locally
Run python3 main.py in the terminal.
```Terminal
$ python3 main.py
```

---

## References

- [VTK](https://vtk.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)

---
