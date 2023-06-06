
import pickle
import os
import numpy as np
import cv2

def load_cifar_pickle(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f, encoding='bytes')
    images = dict[b'data']
    images = np.reshape(images, (10000, 3, 32, 32))
    labels = np.array(dict[b'labels'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels


def load_cifar_categories(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f, encoding='bytes')
    return dict[b'label_names']

def save_cifar_image(array, path):
    # array is 3x32x32. cv2 needs 32x32x3
    array = array.transpose(1, 2, 0)
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, array)


if __name__ == '__main__':
    base_dir = './data'
    n_classes = 10
    categories = []
    n_images = 0

    for file_name in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, file_name)):
            # try:
            if file_name == "batches.meta":
                categories = load_cifar_categories(base_dir, "batches.meta")
                print(categories)
                for i in range(n_classes):
                    cat = categories[labels[i]]
            else:
                images, labels = load_cifar_pickle(base_dir, file_name)
                if "data_batch" in file_name:
                    out_dir = os.path.join(base_dir, 'train')
                else:
                    out_dir = os.path.join(base_dir, 'train')

                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)

                for i in range(n_images, n_images + len(images)):
                    save_cifar_image(images[i], os.path.join(out_dir, 'image_{}.png'.format(i)))
                n_images += len(images)
            # except:
            #     print("data problem")





