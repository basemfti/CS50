select avg(rating) from ratings
join movies on ratings.movie_id=movies.id and movies.year=2012;
