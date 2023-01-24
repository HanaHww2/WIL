## @JsonFormat
- Jackson 라이브러리에서 제공하는 어노테이션
    - json 데이터의 직렬화/역직렬화에 활용한다.

### 사용시 설정 주의사항
- Jackson 라이브러리로 ZonedDateTime 시간 데이터를 매핑하는 경우, UTC 기준으로 데이터를 변환하는 것이 기본 설정이다.
```
# application.yml 파일 적용

  jackson:
    deserialization:
      ADJUST_DATES_TO_CONTEXT_TIME_ZONE: false # 타임존 UTC로 자동 변경 해제
```  
#### 참고
- https://stackoverflow.com/questions/59097664/timezone-of-zoneddatetime-changed-to-utc-during-auto-conversion-of-requestbody-w

## @DateTimeFormat
- 스프링에서 제공하는 어노테이션
    - 특히, Json 데이터가 아닌 RequestParameter 와 ModelAttribute 에서 활용한다.

#### 참고
- @DateTimeFormat vs. @JsonFormat :https://jojoldu.tistory.com/361
- 자바에서 적용 가능한 DateType 포맷 : https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html