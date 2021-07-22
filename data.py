data_path = 'raw/'
vol_path = 'train/'
mask_path = 'mask/'
save_path = 'data/'

# create liver/mask path list
vol_names = os.listdir(vol_path)
mask_names = os.listdir(mask_path)

for vol_name in sorted(vol_names):
    vol_done.append(vol_name)

for mask_name in sorted(mask_names):
    mask_done.append(mask_name)

print('vol:', vol_done)
print('mask:', mask_done)

train_path_list = []
for train in vol_done:
    train_data_path = os.path.join(train_path, train)
    train_path_list.append(train_data_path)
print(train_path_list)

mask_path_list = []
for mask in mask_done:
    mask_data_path = os.path.join(mask_path, mask)
    mask_path_list.append(mask_data_path)
print(mask_path_list)


# create training data
vol_scans = np.array([process_scan(path) for path in sorted(train_path_list)])
print('ssss')
mask_scans = np.array([process_mask(path) for path in sorted(mask_path_list)])


# Split data for training and validation. 
x_train = np.concatenate((vol_scans[:105]), axis=0)
print('x_train done')
y_train = np.concatenate((mask_scans[:105]), axis=0)
print('y_train done')
x_val = np.concatenate((vol_scans[105:]), axis=0)
print('x_val done')
y_val = np.concatenate((mask_scans[105:]), axis=0)
print('y_val done')