# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense , Dropout
import os

path = "data2"
epochs = 35
sz = 128
model_path = 'model/model-bw'
    
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# Step 1 - Building the CNN

# Initializing the CNN
classifier = Sequential()

# First convolution layer and pooling
classifier.add(Convolution2D(32, (3, 3), input_shape=(sz, sz, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Second convolution layer and pooling
classifier.add(Convolution2D(64, (3, 3), activation='relu'))
# input_shape is going to be the pooled feature maps from the previous convolution layer
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Third convolution layer and pooling
classifier.add(Convolution2D(96, (3, 3), activation='relu'))
# input_shape is going to be the pooled feature maps from the previous convolution layer
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Fourth convolution layer and pooling
classifier.add(Convolution2D(128, (3, 3), activation='relu'))
# input_shape is going to be the pooled feature maps from the previous convolution layer
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening the layers
classifier.add(Flatten())

# Adding a fully connected layer
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.40))
classifier.add(Dense(units=96, activation='relu'))
classifier.add(Dropout(0.40))
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dropout(0.40))
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dropout(0.40))
classifier.add(Dense(units=26, activation='softmax')) # softmax for more than 2

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # categorical_crossentropy for more than 2

# Step 2 - Preparing the train/test data and training the model
classifier.summary()
# Code copied from - https://keras.io/preprocessing/image/
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator( rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(path + '/train', target_size=(sz, sz), batch_size=10, color_mode='grayscale', class_mode='categorical')

test_set = test_datagen.flow_from_directory(path + '/test', target_size=(sz , sz), batch_size=10, color_mode='grayscale', class_mode='categorical') 

classifier.fit(
    training_set, 
    steps_per_epoch=len(training_set)/10, 
    batch_size = 512, 
    epochs = epochs, 
    verbose = 1, 
    validation_data = (test_set),
    validation_steps=len(test_set) /10 )

# Saving the model
model_json = classifier.to_json()
with open(model_path + ".json", "w") as json_file:
    json_file.write(model_json)
print('Model Saved')
classifier.save_weights(model_path + '.h5')
print('Weights saved')