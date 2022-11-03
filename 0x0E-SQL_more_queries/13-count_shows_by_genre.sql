-- lists genre names and count according to number of tv shows with genre and orders them highest to lowest count
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id ORDER BY number_of_shows DESC;
