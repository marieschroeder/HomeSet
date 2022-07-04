# libraries we need
import numpy as np
import cv2
import csv
from matplotlib import pyplot as plt
from shapely.geometry import Polygon
import pandas as pd
import geopandas as gpd
import argparse
import sys

def mask(in_path='./OG_pictures/kilter_board_setting.jpeg', 
         out_path='./OG_pictures/foreground.jpeg', 
         showoutput=False
        ):
    '''
    Transform an image using threshold,
    dissect foreground from background and save
    foreground
    _______________________________
    Input
    in_path: path to input picture
    out_path: path to output picture
    showoutput: FALSE / TRUE
    _______________________________
    Output
    picture foreground
    '''
    #load image, flip it to get right coordinates and build binary
    img = cv2.imread(in_path)
    img = cv2.flip(img, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV +
                                cv2.THRESH_OTSU)
    
    # Noise removal using Morphological
    # closing operation
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                                kernel, iterations = 2)

    # Background area using Dilation
    bg = cv2.dilate(closing, kernel, iterations = 1)

    # Finding foreground area
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02
                            * dist_transform.max(), 255, 0)
    # save image
    cv2.imwrite(out_path, fg)
    
    # show image
    if showoutput == True:
        cv2.imshow('image', fg)
        # Exiting the window if 'q' is pressed on the keyboard.
        if cv2.waitKey(0) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
        
def contour_recognition(in_path='./OG_pictures/foreground.jpeg', 
                         out_path='./OG_pictures/contours.jpeg', 
                         showoutput=False
                       ):
    '''
    Find the co-ordinates of the contours detected in an image.
    _______________________________
    Input
    in_path: path to input picture
    out_path: path to output picture
    showoutput: FALSE / TRUE
    _______________________________
    Output
    picture with recognized shapes/contours
    ''' 
   
    #load image
    font = cv2.FONT_HERSHEY_COMPLEX
    img2 = cv2.imread(in_path, cv2.IMREAD_COLOR)

    # Reading same image in another 
    # variable and converting to gray scale.
    img = cv2.imread(in_path, cv2.IMREAD_GRAYSCALE)

    # Converting image to a binary image
    # ( black and white only image).
    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)

    # Detecting contours in image.
    contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Going through every contour found in the image.
    for cnt in contours :

        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

        # draws boundary of contours.
        cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 

        # Used to flatten the array containing
        # the co-ordinates of the vertices.
        n = approx.ravel()

    # save image
    cv2.imwrite(out_path, img2)
    
    # Showing the final image.
    if showoutput == True:
        cv2.imshow('Contour outlines recognized', img2) 
        # Exiting the window if 'q' is pressed on the keyboard.
        if cv2.waitKey(0) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
    return contours

#def main(pathtoOGpicture='./OG_pictures/kilter_board_setting.jpeg',
#         pathtoFGpicture='./OG_pictures/foreground.jpeg',
#         pathforgeopandasdf='./OG_pictures/geopandas_geometry_kilter_board_new.shp',
#         showoutput=False
#        ):

#default input and output paths
pathtoOGpicture='./OG_pictures/kilter_board_setting.jpeg'
pathtoFGpicture='./OG_pictures/foreground.jpeg'
pathforgeopandasdf='./OG_pictures/geopandas_geometry_kilter_board_new.shp'
showoutput=False


def main(pathtoOGpicture=pathtoOGpicture,
         pathtoFGpicture=pathtoFGpicture,
         pathforgeopandasdf=pathforgeopandasdf,
         showoutput=showoutput
        ):
    '''
    Main function to call picture preprocessing
    _______________________________
    Input
    pathtoOGpicture: path to input OG picture
    pathtoFGpicture: path to input FG picture
    pathforgeopandasdf: path to output geopandas dataframe
    showoutput: FALSE / TRUE
    _______________________________
    Output
    geopandas dataframe with geometries for hold contours
    ''' 
    # preprocess image
    # dissect foreground
    mask(in_path=pathtoOGpicture, showoutput=showoutput)
    # contour retrieval
    contours = contour_recognition(in_path=pathtoFGpicture, showoutput=showoutput)

    # load contours to geopandas dataframe
    
    # build list of polygons out of the contours 
    list_of_polygons = []
    for i in contours:
        list_of_polygons.append(Polygon(np.vstack(i)))
    
    # load this list to geopandas dataframe
    p = {'geometry': [i for i in list_of_polygons]}
    p = gpd.GeoDataFrame(p)
    
    # saving geopandas dataframe for later use
    p.to_file(pathforgeopandasdf,index=False)
    if showoutput == True:
        p.plot()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'possible input arguments for image preparation')
    parser.add_argument('--in_OG', help = "Path to original input picture, default './OG_pictures/kilter_board_setting.jpeg'")
    parser.add_argument('--in_FG', help = "optional: Path to preprepared foreground picture, default './OG_pictures/foreground.jpeg'")
    parser.add_argument('--out', help = "optional: Path to output geopandas dataframe, default './OG_pictures/geopandas_geometry_kilter_board_new.shp'")
    parser.add_argument('--show', help = "optional: show intermediate output steps: True/False, default 'False'")
    args = parser.parse_args(sys.argv[1:])
   
    #user-defined input and output paths
    if args.in_OG != None:
        pathtoOGpicture = args.in_OG
    if args.in_FG != None:
        pathtoFGpicture = args.in_FG
    if args.out != None:
        pathforgeopandasdf = args.out
    if args.show != None:
        showoutput = args.show
    
    #call to main function
    main(pathtoOGpicture=pathtoOGpicture,
         pathtoFGpicture=pathtoFGpicture,
         pathforgeopandasdf=pathforgeopandasdf,
         showoutput=showoutput)
    
    
    
    
    
    
    
    
    
    
    
    
    
