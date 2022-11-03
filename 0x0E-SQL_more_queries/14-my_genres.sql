-- returns the genres for Dexter tv show
SELECT name FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = "Dexter" ORDER BY name;
