-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT
    g.name AS name,
    SUM(r.rate) AS rating
FROM
    tv_show_genres AS sg
JOIN
    tv_genres AS g ON sg.genre_id = g.id
JOIN
    tv_show_ratings AS r ON sg.show_id = r.show_id
GROUP BY
    g.name
ORDER BY
    rating DESC, name;
