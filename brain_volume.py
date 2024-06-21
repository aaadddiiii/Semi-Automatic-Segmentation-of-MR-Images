import nibabel as nib
import numpy as np

# Load the NIfTI file
nii_file = '/Users/aditya/Desktop/My Computer/AIIMS/WNet-master 3/Yoga/ss_anita_3.nii.gz'
nii_img = nib.load(nii_file)

# Get the data as a numpy array
brain_data = nii_img.get_fdata()

# Get the voxel dimensions from the header
voxel_dims = nii_img.header.get_zooms()
print(voxel_dims)
voxel_volume = np.prod(voxel_dims)  # Calculate the volume of a single voxel
print(voxel_volume)\
# Calculate the number of non-zero voxels (assuming non-zero voxels are part of the brain)
non_zero_voxels = np.count_nonzero(brain_data)

# Calculate the total brain volume
brain_volume = non_zero_voxels * voxel_volume
