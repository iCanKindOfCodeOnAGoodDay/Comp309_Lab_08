"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Lab #08
    Created on Wed Mar 13 18:46:23 2024
    Updated 22:20 Mar 15

    Description: 
    The program.... makes the finding that Python arrays are faster when using math.sin calculations 
    than Numpy arrays when USING MATH.sin. But NP Arrays can
    calculate np.sin in parallel, 
    making those calculations over 10x faster than math.sin calculations on python arrays.
        
    
    Inputs: 
        
    createPlot( xData, PythonArrayTiming, NumpyTiming )

    timeArray( problemSizesList, initialDx )
    
    timeNumpy( problemSizesList, initialDx )


    Returns: 
    
    timeArray- returns List of floating point numbers used for plotting results 
    
    timeNumpy- returns List of floating point numbers used for plotting results 


    Dependencies: time, math, array, plt, np

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""

#----Import all modules

import time, math, array
import matplotlib.pyplot as plt
import numpy as np


 
#----Define All Functions


def main():
    
    """
    
    Description
    ----------  
    Our main() is the entry point to our program, holds our constants, and runs program.

    Parameters
    ----------
    None.
            
    Returns
    -------
    None.

    """
        
    # Best to define your variables here.   
    N = 8192
    problemSizes = [ N, N * 4, N * 16, N * 64 ]
    dx = 0.0
    
    # Call some funcs    
    print( "Scott Quashen", time.asctime() )
    
    # perform our calculations and save the data
    retrievedArrayResults = timeArray( problemSizes,  dx)
    retrievedNumpyResults = timeNumpy( problemSizes, dx)
    
    # plot the results 
    createPlot(problemSizes, retrievedArrayResults, retrievedNumpyResults)
    
    return None

# end of main function


def createPlot( xData, PythonArrayTiming, NumpyTiming ):
    
    """
    
    Description
    ----------  
    createPlot() uses mathPlot to create a chart representing the time 
    taken to calculate sin using (1) numpy.sin vs. (2) math.sin on various problem sizes.

    Parameters
    ----------
        
    xData- List of integers representing our problem sizes
        
    yDataMath- List of floats representing our y-axis values Math.sin times in milliseconds
        
    yDataNumpy- List of floats representing our y-axis values Numpy.sin times in milliseconds

    Returns
    -------
    None.

    """
    
    X = [ str( t ) for t in xData ] # string values for x ticks
    X_axis = np.arange( len( xData ) ) 
    plt.xticks( X_axis, X )

    
    plt.bar( X_axis - 0.2, PythonArrayTiming, 0.4, label='Python Arrays', color='red' )
    plt.bar( X_axis + 0.2, NumpyTiming, 0.4, label='Numpy Arrays', color='black' )
    
    plt.title( "Numpy Arrays Vs. Python Array Runtimes" )
    plt.xlabel( 'Problem Size' )
    plt.ylabel( 'Time (seconds)' )
    plt.legend( [ "Python Arrays-  Math.sin", "Numpy Arrays-  Np.sin" ], loc=2 )    
    plt.savefig( "Scott Quashen_Lab_08.png", dpi=600 )   
    plt.show()

# end createPlot() func


def timeArray( problemSizesList, initialDx ):
        
    """
    Description
    ----------  
    timeArray() measures how long it takes to perform many calculations on data that
    is structured inside a python array measuring the results and creating a list
    of those results for plotting.

    Parameters
    ----------
    
    problemSizesList - List of integers which is our problem size
    
    initialDx- floating point number which is our initial value to perform calculation on
            
    Returns
    -------
    List of floating point numbers which are the measurements passed into our plot func
    
    None.
    
    """
    
    timeResult= []   # create an empty list
      
    problemSizes = problemSizesList
    
    dx = initialDx
    
    for nSize in problemSizes:
        
        a = array.array("f", [0] * nSize) # create your np array
  
        # calculate your data values
        for i in range( nSize ):
            a[ i ] = dx = dx + ( 2 * np.pi ) / ( nSize - 1 )
                     
        startTime = time.time() # start
        
        # loop over data calling math.sin on each value        
        for b in range( nSize ):     
            math.sin( a[ b ] )
                
        stopTime = time.time() # stop
        
        elapsedTime = stopTime - startTime # measure 
        
        timeResult.append(elapsedTime)
                                           
    return timeResult # list of floats

# end Python Array timing func


def timeNumpy( problemSizesList, initialDx ):
        
    """
    Description
    ----------  
    timeNumpy() is a clone of timeArray but using Numpy Array and Numpy calculation

    Parameters
    ----------
    
    problemSizesList - List of integers which is our problem size
    
    initialDx- floating point number which is our initial value to perform calculation on
            
    Returns
    -------
    List of floating point numbers which are the measurements passed into our plot func
    
    None.
    
    """
    
    timeResult = [] # hold measurements
    
    problemSizes = problemSizesList
    
    dx = initialDx
    
    for nSize in problemSizes:
        
        a = np.zeros( nSize ) #create np arrays

        # calculate your data values
        for i in range( nSize ):
            a[ i ] = dx = dx + ( 2 * np.pi ) / ( nSize - 1 )
                             
        startTime = time.time() # start 

        np.sin( a ) # calculate in parallel
        
        stopTime = time.time() # stop 
        
        elapsedTime = stopTime - startTime # measure
        
        timeResult.append( elapsedTime ) # add result
                                           
    return timeResult # data for plot

# end NP Python timing func

 


#----Entry point

if __name__ == "__main__":
    main()































