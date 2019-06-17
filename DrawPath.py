# @author : Nahel Chazot
# Draw methods for TSP problem

import matplotlib.pyplot as plt
import matplotlib.image  as mpimage

## subplot
#
# Call the 3-args matplotlib sublot function
#
# @parameter :
#   nrows : number of rows
#   ncols : number of colons
#   index : index of the sublot
#
# @return : nothing
def subplot(nrows, ncols, index):
    plt.subplot(nrows, ncols, index)
    img=mpimage.imread('patios2.jpg')
    plt.imshow(img, extent=(0, 3000, -700, 1100))


## draw
#
# Call the matplotlib show function
#
# @parameter :
#   nothing
#
# @return : nothing
def draw():
    plt.show()

## setPlotTitle
#
# Set the title of the current plot
#
# @parameter :
#   title : string value to set
#   fontsize : size of the font
# @return : nothing
def setPlotTitle(title, fontsize):
    plt.title(title, fontsize=fontsize)


## drawPoints
#
# Draw each point of the problem
#
# @parameter :
#   xini : initial point's x value
#   yini : initial point's y value
#   x : list of x values
#   y : list of y values
#   bat : list of batteries if there is one
#
# @return : nothing
def drawPoints(xini, yini, x, y, *bat):
    #Draw the initial point

    plt.scatter(xini, yini, s=100, c='r')
    for i in range(0, len(x)):
        if bat and bat[0][i] == 1 :
            plt.scatter(x[i], y[i], s=50, c='y')   #Yellow point if it is a batterie zone
            # plt.annotate(i, (x[i], y[i]), size=20)
        else:
            plt.scatter(x[i], y[i], s=50, c='b')   #else blue point
            # plt.annotate(i, (x[i], y[i]), size=20)
    # Set x axis label.
    plt.xlabel("Position", fontsize=10)

    # Set y axis label.
    plt.ylabel("Position", fontsize=10)

    # Set size of tick labels.
    plt.tick_params(axis='both', which='major', labelsize=9)


## drawBatteries
#
# Draw each battery point of the problem
#
# @parameter :
#   x : list of x values
#   y : list of y values
#
# @return : nothing
def drawBatteries(x, y):

    for i in range(0, len(x)):
        plt.scatter(x[i], y[i], s=100, c='y')   #Yellow point
        #plt.annotate(i, (x[i], y[i]), size=20)
    

## drawLines
#
# Draw lines joining points of a solution
#
# @parameter :
#   xini : initial point's x value
#   yini : initial point's y value
#   x : list of x values
#   y : list of y values
#   sol : vector representing the solution
#
# @return : nothing
def drawLines(xini, yini, x, y, sol):
    xNumberValues = []
    yNumberValues = []

    #Starting point
    xNumberValues.append(xini)
    yNumberValues.append(yini)

    # List to hold x values.
    for i in range(0, len(sol)):
        xNumberValues.append(x[sol[i]-1])

    # List to hold y values.
    for i in range(0, len(sol)):
        yNumberValues.append(y[sol[i]-1])

    #Going back to the starting point
    xNumberValues.append(xini)
    yNumberValues.append(yini)

    # Plot the number in the list and set the line thickness.
    plt.plot(xNumberValues, yNumberValues, linewidth=1)



############################ USE ########################

# Use plt.show() to display the plot in the matplotlib's viewer.

# To sublot, use subplot() before using the draw functions.


# Exemple for 2 subplots :

#
# subplot(2, 1, 1)
# setPlotTitle("Subplot 1", 19)
#
# drawPoints(xini, yini, x, y)
# drawLines(xini, yini, x, y, solution)
#
# subplot(2, 1, 2)
# setPlotTitle("Subplot 2", 19)
#
# drawPoints(xini, yini, x, y)
# drawLines(xini, yini, x, y, solution)
#
# draw()