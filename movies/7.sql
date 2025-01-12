select movies.title , ratings.rating  from movies
join ratings on ratings.movie_id=movies.id and movies.year=2010
order by ratings.rating DESC, movies.title asc;

