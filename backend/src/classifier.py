import tensorflow as tf


def create_model():
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal'),
        tf.keras.layers.RandomRotation(0.2),
    ])

    preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
    rescale = tf.keras.layers.Rescaling(1./127.5, offset=-1)
    IMG_SHAPE = (256, 256, 3)
    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                   include_top=False,
                                                   weights='imagenet')

    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
    prediction_layer = tf.keras.layers.Dense(8)

    inputs = tf.keras.Input(shape=(256, 256, 3))
    x = data_augmentation(inputs)
    x = preprocess_input(x)
    x = base_model(x, training=False)
    x = global_average_layer(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = prediction_layer(x)
    model = tf.keras.Model(inputs, outputs)

    # Fine-tune from this layer onwards
    fine_tune_at = 100

    # Freeze all the layers before the `fine_tune_at` layer
    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False

    return model


def load_model():
    model = create_model()

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.legacy.RMSprop(
                      learning_rate=0.00001),
                  metrics=['accuracy'])

    model.load_weights("./model.h5")

    return model


classes = ['anger', 'contempt', 'disgust',
           'fear', 'happy', 'neutral', 'sad', 'surprise']


def classify(model: tf.keras.Model, x):
    probabilities = tf.keras.activations.softmax(
        tf.Variable(model.predict(x.reshape(-1, 256, 256, 3))))
    predictions = []
    for i in range(len(probabilities[0])):
        predictions.append(
            (classes[i], float(probabilities[0][i])))
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions
