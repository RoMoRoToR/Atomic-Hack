import tensorflow as tf
from model import create_model
from utils import load_data, preprocess_data

# Загрузка и предобработка данных
train_images, train_labels, test_images, test_labels = load_data('data/')
train_images, train_labels = preprocess_data(train_images, train_labels)
test_images, test_labels = preprocess_data(test_images, test_labels)

# Создание и компиляция модели
model = create_model()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Сохранение модели
model.save('model/weld_defect_model.h5')
