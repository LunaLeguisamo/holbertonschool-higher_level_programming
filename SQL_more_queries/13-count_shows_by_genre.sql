-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name as genre, COUNT(*) as number_of_shows
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
