import nibabel as nib
from scipy import ndimage

def read_nifti_file(filepath):
    """Read and load volume"""
    scan = nib.load(filepath)
    scan = scan.get_fdata()
    return scan


def normalize(volume):
    """Normalize the volume 0-255"""
    min = -1000
    max = 400
    volume[volume < min] = min
    volume[volume > max] = max
    volume = volume-min / max-min
    volume = volume.astype("float32")
    return volume


def transform_ctdata(img, windowWidth, windowCenter, normal=False):
    """
    return: trucated image according to window center and window width
    Liver: normal 50~70, fatty -20~120, 
    """
    minWindow = float(windowCenter) - 0.5*float(windowWidth)
    newimg = (img - minWindow) / float(windowWidth)
    newimg[newimg < 0] = 0
    newimg[newimg > 1] = 1
    if not normal:
        newimg = (newimg * 255).astype('float32')
    return newimg

def resize_volume(img):
    """Resize across z-axis"""
    # Set the desired depth
    desired_depth = 128
    desired_width = 128
    desired_height = 128
    # Get current depth
    current_depth = img.shape[-1]
    current_width = img.shape[0]
    current_height = img.shape[1]
    # Compute depth factor
    depth = current_depth / desired_depth
    width = current_width / desired_width
    height = current_height / desired_height
    depth_factor = 1 / depth
    width_factor = 1 / width
    height_factor = 1 / height
    # Rotate
    img = ndimage.rotate(img, 90, reshape=False)
    # Resize across z-axis
    img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=3)
    return img

def process_scan(path):
    """Read and resize volume"""

    volume = read_nifti_file(path)
    volume = resize_volume(volume)
    volume = normalize(volume)
    return volume


def process_mask(path):
    """Read and resize mask"""
    mask = read_nifti_file(path)
    mask = resize_volume(mask)   
    return mask


if __name__ == '__main__':

    # create training data
    vol_scans = np.array([process_scan(path) for path in sorted(train_path_list)])
    mask_scans = np.array([process_mask(path) for path in sorted(mask_path_list)])


# Split data for training and validation. 
x_train = np.concatenate((vol_scans[:105]), axis=0)
y_train = np.concatenate((mask_scans[:105]), axis=0)
x_val = np.concatenate((vol_scans[105:]), axis=0)
y_val = np.concatenate((mask_scans[105:]), axis=0)
print('All data had transferred')