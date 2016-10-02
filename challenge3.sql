SELECT DISTINCT created_at as month,(SELECT (
	(SELECT COUNT(DISTINCT user_id) FROM PURCHASES where MONTH(created_at) =  MONTH(month))
	- 
	(SELECT COUNT(DISTINCT user_id) FROM PURCHASES where created_at < month and user_id in (SELECT user_id FROM PURCHASES where MONTH(created_at) =  MONTH(month)))
	)
) as first_time_buyers,
	(SELECT COUNT(DISTINCT user_id) FROM PURCHASES where created_at < month and user_id in (SELECT user_id FROM PURCHASES where MONTH(created_at) =  MONTH(month))) as returned_buyers
from purchases;