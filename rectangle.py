def make_square(box : list, margin, shift_center) :
    max_border = box[2] if box[2] > box[3] else box[3]
    face_center = [
        (int)((2*box[0]+box[2])/2), 
        (int)((2*box[1]+box[3])/2)
    ]
    new_size = (int)((1+margin)*max_border)
    shift_window_up = (int)(shift_center*new_size)
    face_center[1] = face_center[1] - shift_window_up
    
    half_size = (int)(new_size/2)
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