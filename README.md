# shaping_boulders
Shaping Boulder is a browser app where you can define your own routes from a picture of any wall. 
It consists of a python script and three seperate browser applications:
- preparation.py : if your setup is very slick this algorithmus recognizes holds on your wall for you. Possible commands are documented in the docstring - use python preparation.py -h in a console in the working directory to find out about it.
- drawing.ipynb : the application to draw shapes that are not properly recognized by the algorithmus
- editing.ipynb : the application to edit / delete shapes that are not properly recognized by the alrorithmus or wrongly drawn by an operator 
- app.ipynb : the actual app to define and display boulders

# Usage 
Disclaimer: At the moment the algorithmus is not clever enough to process any given picture. You may need to edit the preprocessed picture.
But no worries, a handy tool for that is included in the application (drawing.ipynb / editing.ipynb)! 

## How to start the app

Open a terminal, naviagte to the parrent directory (where you placed the source code of the app), and type:

```
panel serve app.ipynb
```
Dependent on which application you want to use subsitute app.ipynb with editing.ipynb or drawing.ipynb
This will start a local host for the app and you can now copy/paste the provided link in your preferred browser.
(The link looks something like: 'http://localhost:5006/app')
Now you can use the app.


## How to use the app 
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
