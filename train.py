import tensorflow as tf

train_loader = tf.data.Dataset.from_tensor_slices((x_train, y_train))
validation_loader = tf.data.Dataset.from_tensor_slices((x_val, y_val))

model = get_unet()

history = model.fit(train_loader, 
	batch_size=10, 
	epochs=20, 
	verbose=1, 
	shuffle=True,
	validation_data=validation_loader)