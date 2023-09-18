import image
import path
import argparse
import cv2


# Create the parser
parser = argparse.ArgumentParser(description="This is a program to crop faces for further neuronetwork training")

# Add the arguments
parser.add_argument('Source', metavar='in', type=str, help='root directory for traversing photos')
parser.add_argument('Output', metavar='out', type=str, help='output directory')
parser.add_argument('--resolution', metavar='resolution', type=int, default=512, help='required resolution')

# Execute the parse_args() method
args = parser.parse_args()

for image_file in path.find_files(args.Source):
    print("processing " + image_file)
    
    file_name, file_ext = path.get_filename_and_extension(image_file)
    sub_folder = path.get_subfolder(args.Source, image_file)  

    img=cv2.imread(image_file)
    i = 1
    for face in image.detect_faces(img, args.resolution) :
        new_file_name = file_name + f"_{i}"
        new_dir = path.join_folders(args.Output, sub_folder)
        path.create_if_not_exist(new_dir)

        output_file = path.combine(new_dir, new_file_name, file_ext)
        output_log_file = path.combine(new_dir, new_file_name, ".txt")
        cv2.imwrite(output_file, face["image"]) 

        scaled_file = path.combine(new_dir, new_file_name+f"{args.resolution}x{args.resolution}", file_ext)
        scaled_image = image.scale_image(face['image'], args.resolution)
        cv2.imwrite(scaled_file, scaled_image)

        # with open(output_log_file, 'w') as f:
        #     f.write(f"Confidence: {face['confidence']}\n")
        #     f.write(f"Keypoints:\n {face['keypoints']}")

        i = i+1