# Shaping Boulders
Shaping Boulder is a browser app where you can define your own routes from a picture of any wall. 
It consists of a python script and three seperate browser applications:

## Module description
Disclaimer: At the moment the algorithmus is not clever enough to process any given picture. You may need to edit the preprocessed picture.
But no worries, a handy tool for that is included in the application (drawing.ipynb / editing.ipynb)! 

#### preparation.py 
If your setup is very slick this algorithmus recognizes holds on your wall for you. Possible commands are documented in the docstring.

Use python preparation.py -h in a console in the working directory to find out about it.

#### Drawing and editing 
This is used for holds that are not properly recognized by the algorithm. 
Because both tools do not work together in one application, drawing and editing should be done one after another. Both applications access the same geopandas dataframe, so editing can only start after saving the drawn shapes. More explanation is provided after startup.

##### drawing.ipynb
The application to draw shapes that are not properly recognized by the algorithm. This can be used right away - without using the algorithm first. This is recommended for very complicated/ cluttered wall setups.

##### editing.ipynb 
The application to edit / delete shapes that are not properly recognized by the alrorithm or wrongly drawn by an operator.

#### app.ipynb
The main application to define, show and explore your boulders.

##### How to use the app 
The app has two main functionalities: 
- Selecting boulders from a pre-defined list 

In the 'Select your Boulder' box, you can click on the boulders in the table and they will be displayed in the image of your wall. If you wanna see only boulders in a grade range you can adjust the sliders above the table and click 'Confirm Selection' to only see those.

- Defining new boulders (and add them to the list)
To define a new boulder on your wall, you have to define: 
  - the name of the boulder
  - the name of the setter 
  - the grade
  - the selection of holds on the image. To select the holds, you have to use the 'Tap' function in the image. Click and hold shift while selecting your holds, to select multiple holds.

All 4 variables need to be defined, otherwise a warning pops up. 

When you are happy with your boulder, click 'Confirm Selection' to save your boulder. It will pop up in the table on the right. 


At any point you can click the green button 'Clear Selection', to clear everything and have a clean setup again.

## How to setup your directory and start the applications
#### Default
The directory includes three example folders:
- 'ideal_ex' runs smooth (also with the recognition algorithm)
- 'real_ex' runs okay, but some holds are missing or wrongly recognized by the algorithm, so some more work is required (drawing/editing)
- 'fail_ex' shows a folder structure that is not sufficient to make the application work (**.jpeg' is missing)
#### Your own wall
To include your own wall add a folder including a picture (.jpeg) of your wall in the parent directory.
You have different options how to go on from here, either draw your own contours using drawing.ipynb, or use the recognition algorithm preparation.py.

#### How to run the recognition algorithm preparation.py
```
python preparation.py --input_folder ['ideal_ex'] --show [False]
```
arguments to set:
input_folder: path to folder where .jpeg of your wall is stored (default='ideal_ex')
show: True/False opens a browser tab with a picture of recognized hold contours (default=False)

#### How to start the different applications

Open a terminal, naviagte to the parrent directory (where you placed the source code of the app), and type:

```
panel serve app.ipynb --show --args DIRECTORY FROMSCRATCH
```
arguments to set:
DIRECTORY: path to folder where .jpeg (and most certainly also your .shp file) of your wall is stored
FROMSCRATCH: if you want to start drawing your holds from scratch set argument to TRUE, only needed for drawing.ipynb

Dependent on which application you want to use subsitute app.ipynb with editing.ipynb or drawing.ipynb
This will start a local host for the app in your preferred browser.
The application is now ready to use.

# Improvements to come
The basic functionality is provided but there are still bugs to be fix.


