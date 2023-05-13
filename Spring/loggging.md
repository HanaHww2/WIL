# logging 알아가기

## 스프링 부트의 디폴트 로깅 설정
- 참고) https://www.baeldung.com/spring-boot-logging
- 스프링 부트는 기본 로깅 설정을 갖추고 있다.
- spring-boot-starter-web 은 spring-boot-starter-logging을 의존하고 있으며, spring-jcl 라이브러리를 포함한다.
  - In the case of logging, the only mandatory dependency is Apache Commons Logging.
  - We need to import it only when using Spring 4.x (Spring Boot 1.x) since it's provided by Spring Framework’s spring-jcl module in Spring 5 (Spring Boot 2.x)

- 참고_공식문서) https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.logging
  - 콘솔에 출력하는 것이 기본 설정
  - 파일은 옵셔널, 기본적으로 생성하지 않는다.
 
- 스프링부트는 Slf4j(Simple Logging Facade for Java) 와 같은 인터페이스를 두고, 구현체를 선택해 사용할 수 있도록 지원한다. (파사드 패턴)

## logback
- starter를 사용하면 기본으로 logback을 활용한다고 하는데... 
> By default, if you use the “Starters”, Logback is used for logging.
  
### 
- org.springframework.boot.logging 이하에 로그백 설정 파일이 위치해 있다.

#### base.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!--
Base logback configuration provided for compatibility with Spring Boot 1.1
-->

<included>
	<include resource="org/springframework/boot/logging/logback/defaults.xml" />
	<property name="LOG_FILE" value="${LOG_FILE:-${LOG_PATH:-${LOG_TEMP:-${java.io.tmpdir:-/tmp}}}/spring.log}"/> <!--파일 관련 설정이 있음?-->
	<include resource="org/springframework/boot/logging/logback/console-appender.xml" />
	<include resource="org/springframework/boot/logging/logback/file-appender.xml" />
	<root level="INFO">
		<appender-ref ref="CONSOLE" />
		<appender-ref ref="FILE" /> <!--파일 관련 설정이 있음?-->
	</root>
</included>
```

#### defaults.xml
```xml
xml version="1.0" encoding="UTF-8"?>

<!--
Default logback configuration provided for import
-->

<included>
	<conversionRule conversionWord="clr" converterClass="org.springframework.boot.logging.logback.ColorConverter" />
	<conversionRule conversionWord="wex" converterClass="org.springframework.boot.logging.logback.WhitespaceThrowableProxyConverter" />
	<conversionRule conversionWord="wEx" converterClass="org.springframework.boot.logging.logback.ExtendedWhitespaceThrowableProxyConverter" />

	<property name="CONSOLE_LOG_PATTERN" value="${CONSOLE_LOG_PATTERN:-%clr(%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>
	<property name="CONSOLE_LOG_CHARSET" value="${CONSOLE_LOG_CHARSET:-${file.encoding:-UTF-8}}"/>
	<property name="FILE_LOG_PATTERN" value="${FILE_LOG_PATTERN:-%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}} ${LOG_LEVEL_PATTERN:-%5p} ${PID:- } --- [%t] %-40.40logger{39} : %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>
	<property name="FILE_LOG_CHARSET" value="${FILE_LOG_CHARSET:-${file.encoding:-UTF-8}}"/>

	<logger name="org.apache.catalina.startup.DigesterFactory" level="ERROR"/>
	<logger name="org.apache.catalina.util.LifecycleBase" level="ERROR"/>
	<logger name="org.apache.coyote.http11.Http11NioProtocol" level="WARN"/>
	<logger name="org.apache.sshd.common.util.SecurityUtils" level="WARN"/>
	<logger name="org.apache.tomcat.util.net.NioSelectorPool" level="WARN"/>
	<logger name="org.eclipse.jetty.util.component.AbstractLifeCycle" level="ERROR"/>
	<logger name="org.hibernate.validator.internal.util.Version" level="WARN"/>
	<logger name="org.springframework.boot.actuate.endpoint.jmx" level="WARN"/>
</included>
```

#### file-appender.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!--
File appender logback configuration provided for import, equivalent to the programmatic
initialization performed by Boot
-->

<included>
	<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
		<encoder>
			<pattern>${FILE_LOG_PATTERN}</pattern>
			<charset>${FILE_LOG_CHARSET}</charset>
		</encoder>
		<file>${LOG_FILE}</file>
		<rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
			<fileNamePattern>${LOGBACK_ROLLINGPOLICY_FILE_NAME_PATTERN:-${LOG_FILE}.%d{yyyy-MM-dd}.%i.gz}</fileNamePattern>
			<cleanHistoryOnStart>${LOGBACK_ROLLINGPOLICY_CLEAN_HISTORY_ON_START:-false}</cleanHistoryOnStart>
			<maxFileSize>${LOGBACK_ROLLINGPOLICY_MAX_FILE_SIZE:-10MB}</maxFileSize>
			<totalSizeCap>${LOGBACK_ROLLINGPOLICY_TOTAL_SIZE_CAP:-0}</totalSizeCap>
			<maxHistory>${LOGBACK_ROLLINGPOLICY_MAX_HISTORY:-7}</maxHistory>
		</rollingPolicy>
	</appender>
</included>
```
#### console-appender.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!--
Console appender logback configuration provided for import, equivalent to the programmatic
initialization performed by Boot
-->

<included>
	<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>${CONSOLE_LOG_PATTERN}</pattern>
			<charset>${CONSOLE_LOG_CHARSET}</charset>
		</encoder>
	</appender>
</included>

```
### 의문점
- 디폴트 설정이 궁금하다. 왜 로그 파일을 생성하지 않는 걸까. 
  - 위 base.xml을 가져오는 logback-spring.xml을 파일을 생성하면, 로그 파일을 만들어주는 듯 하다.
  - 혹은 application.yml 파일에 파일 관련 설정을 넣어주면 로그 파일이 생성된다.
- 즉, base.xml은 디폴트 설정은 아닌 듯 하다. 디폴트는 로그백 설정이 맞는 걸까.
- 해당 라이브러리 이하의 자바 기본 설정을 따라가는 것으로 추측.. 
    - LogFile 등을 확인해보았을 때 로그 파일 관련 변수값이 없으면 파일 생성을 하지 않는 듯 하다.
- 나중에 심심할 때 디버거 찍어보는 걸로...
  
### 커스텀해보기
#### 1차 커스텀
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOG_TEMP" value="./logs"/>
    <include resource="org/springframework/boot/logging/logback/base.xml"/>
</configuration>
```
- logback-spring.xml 파일을 resources 디렉토리 이하에 생성
    - base.xml 그대로 가져오기
    - log 파일 생성 위치만 변경해주었다.

#### 2차 커스텀
- json appender 추가해보기
    - 기존 다른 로그백 어펜더를 참고해서 작성

```xml
<?xml version="1.0" encoding="UTF-8"?>

<included>
    <appender name="JSON" class="ch.qos.logback.core.rolling.RollingFileAppender">
<!--        <layout class="ch.qos.logback.contrib.json.classic.JsonLayout">-->
<!--            <jsonFormatter-->
<!--                    class="ch.qos.logback.contrib.jackson.JacksonJsonFormatter">-->
<!--                <prettyPrint>true</prettyPrint>-->
<!--            </jsonFormatter>-->
<!--            <timestampFormat>yyyy-MM-dd' 'HH:mm:ss.SSS</timestampFormat>-->
<!--        </layout>-->


        <!--아래 인코더 라이브러리는 위에 활용한 라이브러리를 의존한다. 로그 스태시용으로 래핑한 라이브러리라고 볼 수 있을 듯?-->
        <!--일단 예시가 좀 더 있고 뭔가 기능적으로 더 편해보여서 아래로 활용한다.-->
        <encoder class="net.logstash.logback.encoder.LogstashEncoder" >
            <includeContext>true</includeContext>
            <includeCallerData>true</includeCallerData>
            <timestampPattern>yyyy-MM-dd HH:mm:ss.SSS</timestampPattern>
            <fieldNames>
                <timestamp>timestamp</timestamp>
                <thread>thread</thread>
                <message>message</message>
                <stackTrace>exception</stackTrace>
                <mdc>context</mdc>
            </fieldNames>
        </encoder>
        <file>${JSON_FILE}</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>${JSON_FILE}.%d{yyyy-MM-dd}.%i.gz</fileNamePattern>
            <cleanHistoryOnStart>${LOGBACK_ROLLINGPOLICY_CLEAN_HISTORY_ON_START:-false}</cleanHistoryOnStart>
            <maxFileSize>${LOGBACK_ROLLINGPOLICY_MAX_FILE_SIZE:-10MB}</maxFileSize>
            <totalSizeCap>${LOGBACK_ROLLINGPOLICY_TOTAL_SIZE_CAP:-0}</totalSizeCap>
            <maxHistory>${LOGBACK_ROLLINGPOLICY_MAX_HISTORY:-7}</maxHistory>
        </rollingPolicy>
    </appender>
</included>
```

- logback-spring.xml 도 수정한다.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOG_TEMP" value="./logs" />
    <property name="JSON_FILE" value="${LOG_TEMP}/spring.log.json}"/>
    <include resource="org/springframework/boot/logging/logback/base.xml" />
    <include resource="json-appender.xml" />

    <root level="INFO">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="FILE" />
        <appender-ref ref="JSON" />
    </root>

    <springProfile name="prod">
        <root level="INFO">
            <appender-ref ref="JSON" />
        </root>
    </springProfile>
</configuration>
```