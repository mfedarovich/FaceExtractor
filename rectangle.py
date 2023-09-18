def make_square(box : list) :
    maxBorder = box[2] if box[2] > box[3] else box[3]
    faceCenter = [
        (int)((2*box[0]+box[2])/2), 
        (int)((2*box[1]+box[3])/2)
    ]
    halfSize = (int)(1.3*maxBorder/2)
    faceBox = [
        faceCenter[0]-halfSize,
        faceCenter[1]-halfSize,
        faceCenter[0]+halfSize,
        faceCenter[1]+halfSize
    ]

    if faceBox[0] < 0 :
        faceBox[2] += abs(faceBox[0])
        faceBox[0] = 0
    if faceBox[1] < 0 :
        faceBox[3] += abs(faceBox[1])
        faceBox[1] = 0
    
    return faceBox