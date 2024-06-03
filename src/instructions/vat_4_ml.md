# VAT 4 ML - Creating Training data for a species distribution model

This workflow is a contribution to the NFDI4Earth conference.

## Video

The video for this use case is coming soon!



## Summary

Welcome to the VAT 4 ML Use Case.

In this example we will label training data in VAT for Germany, transfer it to a Jupyter notebook using the unique workflow identifier, download the training data as a geodataframe and finally use a machine learning model to build a species distribution model.

For this use case, we will therefore use the frequency of *Arnica montana* occurrences from GBIF as the target variable together with weather data from *CHELSA*, land use classification from *Ökosystematlas* and topographic information as predictor variables.

<img src="images/vat_4_ml_1.png" width="100%" height="auto" alt="Introduction image VAT overview">

To begin, select the Data Catalogue in the top right-hand corner. Here we have several data catalogues to choose from.

In our case, we start by searching for the individual species in the GBIF data provider. The search function makes it easy to find the species, so we search for _Arnica montana_ and load the dataset by selecting it.

<img src="images/vat_4_ml_2.png" width="50%" height="auto" alt="Sidebar with data catalog. Currently the GBIF data provider is chosen and the search is opened with Arnica montana in the search field">

For the weather data we taking weather information from *CHELSA*. Here we choose the *Mean daily air temperature*, *Monthly moisture index* and the *Montly precipitation amount*.

<img src="images/vat_4_ml_3.png" width="50%" height="auto" alt="Sidebar with data catalog. Currently the data catalogue is opened with the CHELSA tab containing multiple weather layer">

**Caution: The weather data is a spatio-temporal data set. Always check the spatial and temporal extent in the metadata.

The weather datasets cover the whole earth and a time range from 01/01/1981 to 01/01/2011. We need to change the time in the time menu at the top right.

<img src="images/vat_4_ml_4.png" width="50%" height="auto" alt="Sidebar with time configuration menu, where the time can be set to address temporal boundaries of spatio-temporal data">

For the spatial selection we also need the German borders, which we found by searching for _Germany_ in the data catalogue.

<img src="images/vat_4_ml_5.png" width="50%" height="auto" alt="Sidebar with data catalog. Currently the data catalog is selected and the search function is used to search for the German boundaries">

To add topographic information to the predictor variables, we include the *SRTM* elevation model.

<img src="images/vat_4_ml_6.png" width="50%" height="auto" alt="Sidebar with data catalog. Currently the data catalog is selected with the SRTM tab">

Finally, we add land use classification data, which in this case is the *Oekosystemaltas*. It can be loaded by searching for it in the personal data catalogue. The personal data catalogue contains all the datasets that the user has uploaded, as well as a section with all datasets, which also contains datasets that are not listed.

<img src="images/vat_4_ml_7.png" width="50%" height="auto" alt="Sidebar with data catalog. Currently Personal data catalogue is selected search function is used to find the Oekosystematlas">

This gives us all the layers we need to create the training and prediction data.

<img src="images/vat_4_ml_8.png" alt="An overview map is visible which contain all the added layers">

We start to create the training data and prepare the prediction data by aggregating the spatio-temporal weather data. To do this, we use the *Temporal Raster Aggregation* operator. This allows us to aggregate temporal data by a moving window (i.e. 1 year). We use this operator for all weather data. While we choose the mean aggregation type for the temperature and the moisture index, we choose the sum aggregation type for the precipitation. For better readability it is recommended to name the datasets.

<img src="images/vat_4_ml_9.png" width="50%" height="auto" alt="Temporal raster aggregation operator">

In a second step, we spatially filter the GBIF occurrence data of *Arnica montana* using the _Point in Polygon Filter_ to restrict our occurrence data to Germany. 

<img src="images/vat_4_ml_10.png" width="50%" height="auto" alt="point in polygon operator">.

Finally, to create the training data, we join the prepared raster data to the vector data using the _Raster Vector Join Operator_, which takes the occurrence data as a vector and the other prepared raster data. This allows us to spatially join the occurrences with the value of the underlying raster cells.

<img src="images/vat_4_ml_11.png" width="50%" height="auto" alt="Raster Vector Join operator">

To create the prediction data, we then use the *Raster Stacker* operator to create a multi-layer raster containing all the raster data. This makes it easier to import it into Jupyter Notebook and work with it.

<img src="images/vat_4_ml_12.png" width="50%" height="auto" alt="Raster Stacker operator">

This brings us to the *Arnica montana* training data and the stacked prediction grid data.

<img src="images/vat_4_ml_13.png" alt="Overview of the map with the training and prediction data as well as all other layer visually hidden">

We now copy the Workflow ID for each layer to use in Jupyter Notebook.

<img src="images/vat_4_ml_14.png" width="50%" height="auto" alt="Layer menu showing the options for i.e. copy the workflow id to clipboard">

In Jupyter Notebook, we can use the geoengine package to first initialise the VAT API. We then import the training data workflow. We then round and group the data in Jupyter Notebook to create a frequency of *Arnica montana* occurrences for each predictor variable combination. The frequency is used as the target variable and the remaining columns are used for the predictor variables. We then split the dataset into training and test data and start training the RandomForestRegressor model using a GridSearchCV strategy for better results. The best resulting model has an r2 value of 0.07.

<img src="images/vat_4_ml_15.png" alt="Jupyter Notebook code used to train the species distribution model">

After model training we can import the prediction data workflow. The best RandomForestRegressor model is used for the final prediction 

<img src="images/vat_4_ml_16.png" alt="Jupyter Notebook code used to predict using the trained species distribution model">

Finally, the result is plotted using the matplotlib package.

<img src="images/vat_4_ml_17.png" alt="Jupyter Notebook code used to plot the result of the prediction">

<img src="images/vat_4_ml_18.png" alt="The plot, showing three maps, two with the distribution and one with the distribution of the training data">

Although the model did not show the best performance, it was possible to show how easy it is to create spatio-temporal training data for machine learning applications using the VAT and exporting the data directly into Python, where it can be used in typical formats such as geopandas GeoDataFrame or xarray DataArray. 