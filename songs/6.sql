SELECT name FROM songs where artist_id =
(select id from artists where name ='Post Malone')
