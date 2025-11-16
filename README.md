# asteroid_reddening_by_ZTF
## Analysis of the reddening of the spectra of small asteroids using ZTF data. 

# Studying the effect of space weathering with distance
• This set of programs can be used to study the space weathering of asteroids using the Zwicky Center data.
• First, the necessary data will be extracted from the ZTF .
• Then, for convenience, use the filter_separation.sql query program to separate the data by filters, having previously checked the data spread (this parameter can be changed in the last line of this query, in addition, you can add a third filter zr, but keep in mind that there is very little data for this filter). In addition to convenience, this query immediately calculates the color index.
Next, use the slope.py program to calculate the slope of the spectrum at given phase angles. It is not necessary to calculate the absolute magnitude, since this parameter does not depend on the distance, and the apparent index will be sufficient.

For own project, this method was applied to more than 150 objects to calculate the slope of the spectra within the families. For this purpose, three families were selected: Massalia, Eunomia and Carina (Coronis 2).
As a result, the dependence of space weathering on the distance from the Sun within each of the selected families was confirmed.

If you use this code for your own research, please include a link to this repository in your work: https://github.com/aili-s/asteroid_reddening_by_ZTF 
