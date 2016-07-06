
## Collaborative Filtering - Netflix movie reviews
<p align="center">
	<img src="https://github.com/jaimeps/collaborative-filtering-netflix/blob/master/images/logo.png" width="150">
</p>

### Description

This project consists of a collaborative filtering algorithm to predict movie reviews ratings from a dataset of Netflix ratings. 

### Data

The dataset corresponds to a subset of the original movie ratings data from the [Netflix Prize](http://www.netflixprize.com/)
Each row in the txt represents an observation with three fields: Movie ID, Customer ID, Rating. 

### Methods

The similarity measure used is Pearson coefficient. Given users *i* and *j*, let *I<sub>i</sub>* be the set of movies that user *i* has rated
<img src="https://github.com/jaimeps/collaborative-filtering-netflix/blob/master/images/pearson.png" width="400"> <br />
where 
<img src="https://github.com/jaimeps/collaborative-filtering-netflix/blob/master/images/avg_rating.png" width="150">
is the average rating for user *i*

Let  *R<sub>ik</sub>* be the rating of user *i* on movie *k*, the prediction is generated according to the following formula
<img src="https://github.com/jaimeps/collaborative-filtering-netflix/blob/master/images/prediction.png" width="400">

### Instructions

To run the code and build the predictions, simply type in the terminal

```
python cf.py --train data/training.txt --test data/testing.txt
```

### References
- Yannet Interian - *Advance Machine Learning - Course notes*
- Jure Leskovec, Anand Rajaraman and Jeffrey D. Ullman - *Mining of Massive Datasets*