(
    Select u.name as results from Users u join MovieRating m
    on u.user_id = m.user_id group by m.user_id
    order by count(m.user_id) desc, u.name limit 1
)
UNION ALL
(
    Select m.title as results FROM MovieRating as r, Movies as m
    where m.movie_id = r.movie_id
    and r.created_at like "2020-02-%"
    GROUP BY r.movie_id
    ORDER BY avg(r.rating) desc, m.title limit 1
);