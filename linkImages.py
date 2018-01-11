import os
import dicom

# get current working directory
cwd = os.getcwd()


directory = os.fsencode(str(cwd))
print(directory)

dicomFiles = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".dcm"):

        #DICOMFile = dicom.read_file(str(filename))
        dicomFiles = [dicomFiles filename]


        continue

    else:
        continue