import pydicom as dicom
import os
import cv2
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = "dcm_ims"

# Specify the output jpg/png folder path
jpg_folder_path = "output"

images_path = os.listdir(folder_path)

# get a single pic and store its pixels in a variable
ds = dicom.dcmread(os.path.join(folder_path, images_path[0]))
im = cv2.resize(ds.pixel_array, (896, 1152))
