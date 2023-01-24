# timestamp vs. datetime

- timestamp 와 datetime의 데이터 포맷은 유사하나, 내부적으로 몇 가지 차이점이 존재한다.
- 그러므로 개발자는 (혹은 DBA의 설계에 따라) 적절히 시간 데이터의 타입을 선택해서 활용할 필요성이 있다.
- mysql8 이상부터 시간 데이터를 저장할 때, 오프셋을 활용할 수 있다.
    - timestamp와 datetime 이 이 오프셋을 계산하는 기준이 다르다는 점에 유의한다.

## timestamp
> MySQL converts TIMESTAMP values from the current time zone to UTC for storage, and back from UTC to the current time zone for retrieval. (This does not occur for other types such as DATETIME.). : [From the MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)

- dbms의 지정된 타임존에 따라 시간 데이터를 변경하여 활용할 필요성이 있다면, timestamp를 활용할 수 있다.
    - 그러나, 썩 좋은 방도는 아니라는 의견이 스택오버플로우에 많았다.
- 4 Byte

### cons
- 사용 가능한 데이터 범위 : 1970-01-01 00:00:01 UTC
~ 2038-01-1903:14:07 UTC
- 오직 2038년까지의 데이터만 기록이 가능하다.
- DBMS 의 타임존에 의존하게 된다.

## datetime
- 사용 가능한 데이터 범위 : 1000-01-01 00:00:00
~ 9999-12-31 23:59:59
- 8 Byte

## 타임존 활용 방식
- 타임존 데이터를 저장해야 하는 경우에 아래와 같이 3가지 컬럼을 활용해서 데이터를 저장할 수도 있다.
    - local_time DATETIME
    - utc_time DATETIME
    - time_zone VARCHAR(X)

- 타임존을 저장할 때 오프셋 시간을 저장하는 방식도 권장하지 않는다. 
    - 특정 타임존에 따라 서머 타임(DST) 등의 특수한 계산이 필요한 경우가 발생하고, 이를 명확하게 계산하기 위해서는 타임존 명칭을 기록하고 활용하는 것이 낫다고 한다.

### 참고 자료
- https://stackoverflow.com/questions/19843203/how-to-store-a-datetime-in-mysql-with-timezone-info
- https://stackoverflow.com/questions/44965545/best-practices-with-saving-datetime-timezone-info-in-database-when-data-is-dep
- https://velog.io/@dion/mysql-5-7-datetime
- https://gngsn.tistory.com/166
