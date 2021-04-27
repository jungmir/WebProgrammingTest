# 1.
sql = ' \
    select todo.priority, todo.task, todo.create_date, todo.deadline, user.* \
    from db_test.todo \
    left join user on todo.user_id = user.id \
    where is_done = 1 \
    order by priority asc; \
';

# 2.
sql = ' \
    select count(*) as count, task, sum(is_done), concat(round(sum(is_done) / count(*) * 100, 2), "%") as complete_rate \
    from db_test.todo \
    where priority = 1 \
    group by task \
    order by count desc; \
    ';

# 3.
sql = ' \
    select priority, count(*) as count, sum(is_done) as complete, concat(round(sum(is_done) / count(*) * 100, 2), "%") as complete_rate \
    from db_test.todo \
    group by priority \
    order by priority asc; \
';