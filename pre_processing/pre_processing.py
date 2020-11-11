#Necessary packages
import os
import json
import argparse

#My packages
from data_helper import data_path, traffic_path, result_path, txt_path
from data_helper import imageWidth, imageHeight
from utils import check_exist_folder




def main(args):
    #Flag 
    create_labels_txt = args.create_labels_txt
    create_train_txt = args.create_train_txt

    # Code
    with open(traffic_path) as json_file:
        data = json.load(json_file)

    list_images = [image['id'] for image in data['images']]


    # Create /labels/*.txt
    if create_labels_txt:
        check_exist_folder(result_path)

        for id_image in list_images:
            string_info = []
            for img_name in data['annotations']:
                if img_name['image_id'] == id_image:
                    x1 = img_name['bbox'][0]
                    y1 = img_name['bbox'][1]
                    w  = img_name['bbox'][2]
                    h  = img_name['bbox'][3]

                    #Caculation x,y center
                    x1_center = x1 + w/2
                    y1_center = y1 + h/2

                    # Normalization
                    x1_scale = abs(x1_center) / imageWidth
                    y1_scale = abs(y1_center) / imageHeight
                    w_scale =  abs(w) / imageWidth
                    h_scale = abs(h) / imageHeight

                    # labels when running yolo start from index 0
                    label = img_name['category_id'] - 1
                    string_info.append(str(label) + ' ' + str(x1_scale) + ' '
                                        + str(y1_scale) + ' ' + str(w_scale) + ' '
                                        + str(h_scale) + '\n')

            file = open(os.path.join(result_path, "{}.txt".format(id_image)), 'w')
            file.writelines(string_info)
            file.close()
        

    if create_train_txt:
        check_exist_folder(txt_path)

        list_path = [os.path.join('data/images', image_path) + '\n' for image_path in os.listdir(data_path)]
        file = open(os.path.join(txt_path, 'train.txt'), 'w')
        file.writelines(list_path)
        file.close()
        
        # Doan nay se code sau chia train.txt va val.txt theo ti le 80:20 theo suffered = True
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--create_labels_txt',
        help = 'create labels txt file',
        default = False,
        type = bool
    )
    parser.add_argument(
        '--create_train_txt',
        help = 'create train txt file',
        default = False,
        type = bool
    )

    args = parser.parse_args()


    #Call the main function
    main(args)