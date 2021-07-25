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

# print('vol:', vol_done)
# print('mask:', mask_done)

train_path_list = []
for train in vol_done:
    train_data_path = os.path.join(train_path, train)
    train_path_list.append(train_data_path)

mask_path_list = []
for mask in mask_done:
    mask_data_path = os.path.join(mask_path, mask)
    mask_path_list.append(mask_data_path)
