def make_square(box : list, margin, max_width, max_height) :
    max_border = box[2] if box[2] > box[3] else box[3]
    new_size = (int)((1+margin)*max_border)
    
    face_center = [
        (int)((2*box[0]+box[2])/2), 
        (int)((2*box[1]+box[3])/2)
    ]

    face_box = make_square_of_size(face_center, new_size)

    return adjust_dimensions(face_box, max_width, max_height)

def make_square_of_size(face_center, size):
    half_size = (int)(size/2)
    face_box = [
        face_center[0]-half_size,
        face_center[1]-half_size,
        face_center[0]+half_size,
        face_center[1]+half_size
    ]

    if face_box[0] < 0 :
        face_box[2] += abs(face_box[0])
        face_box[0] = 0
    if face_box[1] < 0 :
        face_box[3] += abs(face_box[1])
        face_box[1] = 0
    return face_box

def adjust_dimensions(face_box, max_width, max_height):
    if max_width < face_box[2]:
        diff = face_box[2] - max_width
        face_box[2] = max_width
        face_box[1] = face_box[1] + (int)(diff/2)
        face_box[3] = face_box[3] - (int)(diff/2)
    elif max_height < face_box[3]:
        diff = face_box[3] - max_height
        face_box[3] = max_height
        face_box[0] = face_box[0] + (int)(diff/2)
        face_box[2] = face_box[2] - (int)(diff/2)
    return face_box