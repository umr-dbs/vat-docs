# Updates & Changes

#### ++ 25.10.2024 ++

- **Percentile estimate:** We added the option to calculate a percentile estimate over a raster time series in the *Temporal Raster Aggregation* operator.
- **Band neighborhood aggregate:** We added the operator *Band Neighborhood Aggregation*, which computes a function over neighboring bands for multiband raster data.
- **Fixes and UX improvements:** We fixed a number of issues with existing functionality, e.g., the loading of data from the GfBio Search Basket which previously failed in certain edge cases. We also improved the UX, e.g., by adding loading indicators and setting more sensible default values in dialogs.

#### ++ 19.06.2024 ++

- **Login improvements**: We have improved the login experience by fixing a bug where the login state was displayed incorrectly as well as by implementing an automatic authentication refresh mechanism which keeps your login session active for longer, requiring less frequent logins.
- **Introduction of GBIF Time:** We updated the GBIF data provider, so it now supports the time-component of the GBIF data. This way the user can benefit from spatio-temporal data, leveraging the strength of spatio-temporal visualization, analysis and transformation of the VAT.
- **Quantile calculations:** We added the option to calculate quantiles when editing the symbology of a raster layer. This allows you to create breakpoints of gradient colorizers adjusted to the underlying data distribution in addition to creating evenly spaced breakpoints between minimum and maximum values.
- **Color Scales:** We added many new color maps to the symbology editor, expanding the readily available options for data visualization.
