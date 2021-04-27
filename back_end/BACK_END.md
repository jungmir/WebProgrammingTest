# Back-End
-   ## DB Structure
    -   user, ToDo List table 설계

            User Table : id, password, name, email, phone, birth, enroll_date
            ToDo list Table : user_id, priority, task, create date, deadline, is_deleted
    
    -   설계한 Table을 바탕으로 한 CRUD method 작성

    -   [참고](https://dbdiagram.io/)
            
-   ## query
    -  등록된 task를 완료한 유저 정보를 우선순위 순서로(오름차순 정렬) 출력

        e.g.)
        |priority|task|create_date|deadline|user info ...|
        |----|----|----|----|----|
        |1|'병원가기'|2021-04-27 12:00:00|2021-09-24 12:00:00| ...|
        ...

    -  가장 많이 등록된 task를 기준(내림차순)으로 정렬 후 해당 task가 얼마나 많은 유저에게 등록 되었는지와 해당 task를 사용자들이 얼마나 완료 했는지를 출력

        e.g.)  
        |총 등록|task|완료 한 유저 수|완료 비율|
        |---|---|---|---|
        |15 | '다이어트하기'|4| 26.67%|
        |8|'금연 하기'|1|12.5%|
        ...

    -  각 priority별로 등록된 task 수와, 해당 priority task를 완료한 사람, 완료한 비율을 출력

        e.g.)
        |priority|total_count|complete|complete_rate|
        |----|----|----|----|
        |1|2007|655|32.64%|
        |2|1498|479|31.98%|
        ...