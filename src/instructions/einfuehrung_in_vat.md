# Introduction to VAT

## Video

<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wtGskNfGV_w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Summary

Welcome to the Introduction to VAT.

This first tutorial will introduce you to the VAT system, which can be used to easily load, transform and explore spatio-temporal datasets, such as in the context of ecological science. This tutorial will give you a tour, explain each menu and show the functionality in a simple first use case where we spatially join the minimum and maximum temperature with the GBIF occurrence data of _Aeshna affinis_.

Let the tour begin!

The most prominent area when opening the link https://vat.gfbio.org is the large map. Here you can visualise the spatio-temporal data. The extent of the map can be changed by dragging with the mouse or zooming with the scroll wheel.

<img src="images/einfuehrung_in_vat_1.png" width="100%" height="auto" alt="Introduction image VAT overview">

Next, in the top left-hand corner, is the layer selection menu, which allows you to view all the layers currently loaded, change the symbology or arrange the layers. You can also view the provenance, data table or download the layer.

<img src="images/einfuehrung_in_vat_2.png" width="50%" height="auto" alt="Layer selection">

In the top left hand corner you will find the GFBio Portal button which will take you back to the GFBio Search. Due to the deep integration between the VAT and the GFBio search, it is possible to load data directly from the GFBio search. This button will take you back to the GFBio search when you have finished your data exploration.

<img src="images/einfuehrung_in_vat_3.png" width="50%" height="auto" alt="GFBio Search">

Next to the GFBio button is a zoom manipulation menu. Next to the scroll wheel, the zoom level can be changed using the maximise and minimise buttons.

<img src="images/einfuehrung_in_vat_4.png" width="50%" height="auto" alt="Zoom buttons">

In the middle of the top bar is the time step selector. When viewing spatio-temporal data, you may wish to change the time by one time step. This menu can be used to move the current time step or to open the time selector, which we will see in a moment.

<img src="images/einfuehrung_in_vat_5.png" width="50%" height="auto" alt="Time step selector">

On the top bar you will find a series of icons, which we will visit next.

The first icon is the Account menu. Here you can log in with your GFBio account, which allows you to upload files or create, save or export a project. It also shows the session token, which can be used in Python to visit loaded files.

<img src="images/einfuehrung_in_vat_6.png" width="50%" height="auto" alt="Account menu">

The next menu is the data selection menu. Here you will find several data catalogues. The Data Catalogue contains datasets hosted by the GeoEngine, such as land use classification, climate information or orographic elevation maps. The Personal Catalogue contains all files and workflows, and the All Datasets Catalogue contains all hosted and uploaded datasets. Below these are the GBIF and GFBio ABCD data catalogues, which contain all datasets derived from the respective data providers. It is also possible to draw features or load a layer by inserting the workflow_id from a Python workflow.

<img src="images/einfuehrung_in_vat_7.png" width="50%" height="auto" alt="Data selection">

The cogwheel icon hides the operator selection menu. Here you will find a range of operators to manipulate, transform, merge or plot vector or raster data.

<img src="images/einfuehrung_in_vat_8.png" width="50%" height="auto" alt="Operator selection">

The plots are then displayed in the Plot Window. Here you can view the plot results and delete plots.

<img src="images/einfuehrung_in_vat_9.png" width="50%" height="auto" alt="Plot window">

The next menu is the time configuration menu. Here you can filter the spatio-temporal data. It is also possible to change the time step using the time step selector.

<img src="images/einfuehrung_in_vat_10.png" width="50%" height="auto" alt="Time configurator">

If you are logged in, the workspace settings allow you to save and load projects and change the spatial reference of your project.

<img src="images/einfuehrung_in_vat_11.png" width="50%" height="auto" alt="Workspace settings">

The last menu is the Help section. Here you will find initial information and links to the geoengine documentation, as well as further information about the VAT.

<img src="images/einfuehrung_in_vat_12.png" width="50%" height="auto" alt="Help section including Provenance">

After this brief tour, let us start with an example workflow to demonstrate the capabilities of the VAT.

First we go to the data selection menu and search for _Aeshna affinis_ in the GBIF data catalogue. Clicking on the file loads the layer into the map.

<img src="images/einfuehrung_in_vat_13.png" width="50%" height="auto" alt="GBIF Search">

To link the occurrence data with the mean temperature, we search for the _Minimum Temperature_ dataset in the data catalogue.

<img src="images/einfuehrung_in_vat_14.png" width="50%" height="auto" alt="Minimum temperature search">

The _Minimum Temperature_ dataset is a spatio-temporal dataset and therefore has a spatial and temporal extent. This can be found in the metadata of the dataset.

<img src="images/einfuehrung_in_vat_15.png" width="50%" height="auto" alt="Minimum temperature spatiotemporal extent">

To adjust the time range, change the time in the time configuration menu.

<img src="images/einfuehrung_in_vat_16.png" width="50%" height="auto" alt="Minimum temperature time configuration">

We also load the _Maximum Temperature_ dataset.

<img src="images/einfuehrung_in_vat_17.png" width="50%" height="auto" alt="Maximum temperature search">

As the visual appearence of the temperature datasets are not appealing, we change the symbology of the raster layer.

<img src="images/einfuehrung_in_vat_18.png" width="50%" height="auto" alt="Edit symbology button">

When we clicked on _Edit Symbology_ we were taken to the Edit Symbology menu. Here we scroll down, select a different colour map such as _VIRIDIS_ or _MAGMA_ and click on _Create colour map_. Finally, we confirm the change with the _Apply_ button at the bottom of the menu.

<img src="images/einfuehrung_in_vat_19.png" width="50%" height="auto" alt="Edit symbology menu">

After loading the data, we want to spatially join the occurrence data of _Aeshna affinis_ with the _Minimum Temperature_ and _Maximum Temperature_ datasets using the raster vector join operator. For better readability it is recommended to name the datasets.

<img src="images/einfuehrung_in_vat_20.png" width="50%" height="auto" alt="Raster Vector Join">

The result is that the vector data is spatially linked to the raster data by position. Therefore, new columns are added to the vector data table containing the information.

<img src="images/einfuehrung_in_vat_21.png" width="100%" height="auto" alt="Data table Aeshna affinis oekosystematlas">

The _Histogram_ operator can be used to visualise the distribution of occurrence data as a function of temperature.

<img src="images/einfuehrung_in_vat_22.png" width="50%" height="auto" alt="Histogram">

The graphs then show the distribution of occurrences of _Aeshna affinis_ as a function of the minimum and maximum temperatures on 1 January 1990.

<img src="images/einfuehrung_in_vat_23.png" width="100%" height="auto" alt="Overview Aeshna affinis final">

When you are finished manipulating the data, you can download the raster data as a .tif file and the vector data as a .shp file from the layer selection menu.

<img src="images/einfuehrung_in_vat_24.png" width="50%" height="auto" alt="Download layer button">

In the menu it is also possible to display the origin, which will then appear in the data table area at the bottom of the VAT.

<img src="images/einfuehrung_in_vat_25.png" width="100%" height="auto" alt="Show Provenance data table">

This was the first introductory tour of the VAT system. If you want to learn more, you can do so by watching the videos or exploring the use cases in this documentation.

**Warning** The VAT system is designed primarily for data exploration. Changing the extent of the visual map will recalculate the workflow and may change the results! This must be taken into account when working scientifically with the VAT system. There is also a new window in the bottom left corner. This window must be present when working scientifically with the VAT system, as it allows reproducibility!

**Tip**: The layers have several options. They can be downloaded to work with the data in other systems. The layers also always have a workflow tree and the _workflow_id_ can be copied to import the workflow directly into Python.
