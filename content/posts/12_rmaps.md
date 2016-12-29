Title: Making maps in R
Category: article
Date: 04-28-2016
Tags: R, GIS, map
Slug: rMaps
Template: article
Status: published


![rMaps](../images/rMaps.png)

I have been working on my population genetics project. One of the main thing is to plot the data in the context of the sampling locations. I have been searching all different kinds of solutions. One of the best for my application was to use the packages: maps, mapplots. 

Below are my R code for plotting the partial US and Argentina maps. 

```r
#! r code
library(mapplots)
library(maps)
library(mapdata)

par(mar = (c(4, 1, 4, 1) + 0.1), mfrow = c(1,2))
# prepare color from STRUCTURE and convert them into alpha .8
# color order: C1=Blue, C2=Purple
structureCol <- c("#0099e6", "#800080","#ff004d","#339933")
structureCol <- adjustcolor(structureCol, alpha = 0.8)

# read structure CLUMMP data along with GPS coordinates
struGpsData <- read.table("data/raw/struGPS.txt", header=TRUE, sep="\t")

# set radius size
for (i in struGpsData$Pop){
  subData <- subset(struGpsData, Pop==i)
  if (subData$PopSize < 5){
    struGpsData$popRadius[i] <- 0.35}
  else if (subData$PopSize > 5 && subData$PopSize < 10) {
    struGpsData$popRadius[i] <- 0.5}
  else if (subData$PopSize > 10 && subData$PopSize < 20) {
    struGpsData$popRadius[i] <- 0.6}
  else if (subData$PopSize > 20 && subData$PopSize < 55) {
    struGpsData$popRadius[i] <- 0.9}
  else if (subData$PopSize > 55) {
    struGpsData$popRadius[i] <- 1.2}
}

# plot Argentina and pie chart
argStruData <- struGpsData[struGpsData$country %in% c("Arg"),]
map("world", "argentina",mar=rep(0,4),boundary=TRUE)
for (i in argStruData$Pop){
  subData <- subset(argStruData, Pop==i)
  zValues <- c(subData$C1, subData$C2, subData$C3, subData$C4)
  xLong <- subData$longitude
  yLati <- subData$latitude
  # add pie chart to map
  add.pie(z=zValues, x=xLong, y=yLati, col=structureCol, labels=NA, 
          radius=subData$popRadius)
}

# plot US midwest 
usStruData <- struGpsData[struGpsData$country %in% c("USA","CAN"),]
map("state", xlim=c(-105,-76), boundary=TRUE, mar=rep(0,4))
# Draw pie plot in US map
for (i in usStruData$Pop){
  subData <- subset(usStruData, Pop==i)
  zValues <- c(subData$C1, subData$C2, subData$C3, subData$C4)
  xLong <- subData$longitude
  yLati <- subData$latitude
  # add pie chart to map
  add.pie(z=zValues, x=xLong, y=yLati, col=structureCol, labels=NA, 
          radius=subData$popRadius)
}

```


Other good resources have been found while I was searching solutions for this plot.

- [RMakingMaps - by K Gilbert](http://www.zoology.ubc.ca/~kgilbert/mysite/Miscellaneous_files/R_MakingMaps.pdf)
- [Molecular Ecologist Post R making Maps](http://www.molecularecologist.com/2012/09/making-maps-with-r/)
- [Interactive Maps in R](http://rmaps.github.io/)
- [rworldmap: Mapping Global Data](https://cran.r-project.org/web/packages/rworldmap/index.html)

