import image
import path
import argparse
import cv2


# Create the parser
parser = argparse.ArgumentParser(description="This is a program to crop faces for further neuronetwork training")

# Add the arguments
parser.add_argument('source', metavar='in', type=str, help='root directory for traversing photos')
parser.add_argument('output', metavar='out', type=str, help='output directory')
parser.add_argument('--resolution', metavar='resolution', type=int, default=512, help='required resolution')
parser.add_argument('--log', metavar='log', type=bool, default=False, help='create log file')
parser.add_argument('--margin', metavar='margin', type=float, default=0.4, help='percent of outbox margin')
parser.add_argument('--shift_center', metavar='shift_center', type=float, default=-0.1, help='percent to shift center')
parser.add_argument('--original_folder', metavar='original', type=str, default="original")
parser.add_argument('--scaled_folder', metavar='scaled', type=str, default='scaled')

# Execute the parse_args() method
args = parser.parse_args()

original_dir = path.join_folders(args.output, "\\original")
path.create_if_not_exist(original_dir)

scaled_dir = path.join_folders(args.output, f"\\scaled_{args.resolution}")
path.create_if_not_exist(scaled_dir)

already_processed_files = set(
        map(lambda file: path.get_filename_and_extension(file)[0].split('x')[0],
            path.find_files(scaled_dir)
            )
    )
for image_file in filter(
    lambda file: path.get_filename_and_extension(file)[0] not in already_processed_files, 
    path.find_files(args.source)):

    print("processing " + image_file)
    
    file_name, file_ext = path.get_filename_and_extension(image_file)
    sub_folder = path.get_subfolder(args.source, image_file)  

    img=cv2.imread(image_file)
    i = 1
    for face in image.detect_faces(img, args.resolution, args.margin, args.shift_center) :
        new_file_name = file_name + f"x{i}"
        new_dir = path.join_folders(original_dir, sub_folder)
        path.create_if_not_exist(new_dir)

        prefix= "" if face['is_square'] else "rect_"
        output_file = path.combine(new_dir, prefix+new_file_name, file_ext)
        cv2.imwrite(output_file, face['image']) 

        new_scaled_dir = path.join_folders(scaled_dir, sub_folder)
        path.create_if_not_exist(new_scaled_dir)
        scaled_file = path.combine(new_scaled_dir, new_file_name, file_ext)
        scaled_image = image.scale_image(face['image'], args.resolution)
        cv2.imwrite(scaled_file, scaled_image)

        if args.log :
            output_log_file = path.combine(new_dir, new_file_name, ".txt")
            with open(output_log_file, 'w') as f:
                f.write(f"Confidence: {face['confidence']}\n")
                f.write(f"Keypoints:\n {face['keypoints']}")
        i = i+1