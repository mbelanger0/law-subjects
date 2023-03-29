# law-subjects
## Purpose ##
The purpose of this project is to determine if Senators from states in different geographical regions of the United States favor the proposition of certain bill policy areas over. We obtained the data needed to answer this question by accessing the Congress API on bills and obtaining information on many of the bills proposed by the Senate during the 117th Congress. 

## Libraries ##
This project requires several libraries in order to run, including Pandas, Matplotlib, JSON, Geoplot, Geoplot.crs, Geopandas. Installation of Geoplot, Geoplot.crs, and Geopandas is required. Run the following code in terminal to install Geoplot and Geopandas:

`conda install geoplot -c conda-forge`

    *Installing Geoplot can take over 20 minutes. Be patient.

`conda install --channel conda-forge geopandas`


## Generating Identical Data and Plots ##
To generate identical data and plots, use `get_data` to get data from Congresses 117. The code should be `bills = get_data(117, 117, API_KEY)` to get data from just the 117th Congress.

Note: Titles cannot be added to the geospatial plots created using Geoplot and Geopandas so the titles of the plots are printed above the plots in text
