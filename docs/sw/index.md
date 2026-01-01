---
layout: default
title: SW (소프트웨어공학)
nav_order: 3
has_children: true
has_toc: false
permalink: /docs/sw
---

# SW (소프트웨어공학)
{: .fs-9 }

<style>
/* 진행률 바 */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 0%;
  height: 4px;
  background: linear-gradient(90deg, #1e3a5f, #2563eb, #4f46e5);
  z-index: 9999;
  transition: width 0.1s;
}

/* SDLC 흐름도 */
.sdlc-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.25rem;
  flex-wrap: wrap;
  margin: 1.5rem 0 2rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
  border-radius: 16px;
  border: 1px solid #cbd5e1;
}
.sdlc-flow__title {
  width: 100%;
  text-align: center;
  font-weight: 700;
  font-size: 0.9rem;
  color: #475569;
  margin-bottom: 1rem;
  letter-spacing: 0.05em;
}
.sdlc-step {
  display: flex;
  align-items: center;
  gap: 0.15rem;
  padding: 0.65rem 1rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.85rem;
  color: #fff;
  text-decoration: none !important;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}
.sdlc-step:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}
.sdlc-step__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background: rgba(255,255,255,0.25);
  border-radius: 50%;
  font-size: 0.75rem;
  margin-right: 0.3rem;
}
.sdlc-arrow {
  font-size: 1.2rem;
  color: #64748b;
  margin: 0 0.15rem;
}
.sdlc-step--req { background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%); }
.sdlc-step--analysis { background: linear-gradient(135deg, #0369a1 0%, #0ea5e9 100%); }
.sdlc-step--design { background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%); }
.sdlc-step--impl { background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%); }
.sdlc-step--test { background: linear-gradient(135deg, #6d28d9 0%, #8b5cf6 100%); }
.sdlc-step--deploy { background: linear-gradient(135deg, #475569 0%, #64748b 100%); }
.sdlc-step--maint { background: linear-gradient(135deg, #334155 0%, #475569 100%); }

/* Sticky 섹션 헤더 */
.sticky-header {
  position: sticky;
  top: 60px; /* 상단 네비게이션 바 높이 */
  background: white;
  padding: 0.8rem 1rem;
  margin: 0 -1rem;
  z-index: 100;
  border-bottom: 2px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
@media (max-width: 768px) {
  .sticky-header {
    top: 56px; /* 모바일 네비게이션 바 높이 */
  }
}
.sticky-header-sdlc {
  background: linear-gradient(135deg, #0f766e 0%, #0369a1 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-quality {
  background: linear-gradient(135deg, #1e3a5f 0%, #1d4ed8 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-mgmt {
  background: linear-gradient(135deg, #374151 0%, #4b5563 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-advanced {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: #fff;
  border-bottom: none;
}

/* 암기법 코드 스타일 */
.mnemonic-code {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border: 1px solid #fcd34d;
  border-radius: 6px;
  font-family: 'D2Coding', monospace;
  font-weight: 700;
  font-size: 0.9rem;
  color: #92400e;
}

/* 토픽 테이블 스타일 */
.topic-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 1rem 0;
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
}
.topic-table thead th {
  text-align: left;
  font-size: 0.85rem;
  color: #0f172a;
  background: #f8fafc;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #e5e7eb;
}
.topic-table tbody td {
  vertical-align: top;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #eef2f7;
  color: #0f172a;
}
.topic-table tbody tr:last-child td { border-bottom: none; }
</style>

<!-- 진행률 바 -->
<div class="progress-bar" id="progressBar"></div>
<script>
window.addEventListener('scroll', function() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById('progressBar').style.width = scrolled + '%';
});
</script>

<details markdown="1">
<summary><strong>📋 목차</strong></summary>

- **SDLC (개발 생명주기)**
  - [개발 모델 / 방법론](#s-sdlc)
  - [요구사항 / 아키텍처](#s-req-arch)
  - [UML / 디자인패턴](#s-uml-pattern)
  - [테스트 / 유지보수](#s-test-maint)
- **소프트웨어 품질관리**
  - [품질 표준 / 안전성](#s-quality)
- **소프트웨어 사업 관리**
  - [발주 / 비용 / 감리](#s-mgmt)
- **심화 토픽**
  - [고급 개념](#s-advanced)

</details>

---

<div id="s-sdlc" class="sticky-header sticky-header-sdlc">🔄 SDLC (Software Development Life Cycle)</div>

<div class="sdlc-flow">
  <div class="sdlc-flow__title">소프트웨어 개발 생명주기</div>
  <div class="sdlc-step sdlc-step--req">
    <span class="sdlc-step__icon">C</span>요구사항 정의
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--analysis">
    <span class="sdlc-step__icon">C</span>분석
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--design">
    <span class="sdlc-step__icon">C</span>설계
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--impl">
    <span class="sdlc-step__icon">C</span>구현
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--test">
    <span class="sdlc-step__icon">C</span>테스트
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--deploy">
    <span class="sdlc-step__icon">C</span>배포
  </div>
  <span class="sdlc-arrow">→</span>
  <div class="sdlc-step sdlc-step--maint">
    <span class="sdlc-step__icon">C</span>유지보수
  </div>
</div>

<p style="text-align: center; margin-top: -0.5rem;"><span class="mnemonic-code">요분설구테배유</span></p>

---

### SDLC / 프로젝트 개발 모델

`폭 프 S 반 증 진 R`

| 토픽 | 암기법 |
|:-----|:-------|
| 폭포수 모델 | 순차적, 고전적 / 계요설개단통시인설 / 고단순탑V후 |
| 프로토타이핑 모델 | 가시화, 초기모형, 의사소통, 검토평가, POC |
| Spiral 모델 | Suggested reviewers |
| 반복적 개발 모델 (Iteration) | 범위분해, 반복개발 완성 |
| 증분형 개발 모델 (Incremental) | 병렬, 스피드, 인도물중심 |
| 진화형 개발 모델 (Evolutional) | 핵심요구사항, 기능추가 |
| RAD | 개발도구(CASE), 빠른개발 / 지라씨(JRAC) / JRP: Joint Requirment Planning(분석,모델링,1~2주), JAD: Joint Application Design(설계,개발,평가,3~5주), Cut Over: 테스트,인수 |

---

### 개발방법론

| 토픽 | 암기법 |
|:-----|:-------|
| 정보공학(IE) 방법론 | ISP/데이터중심 / ISPASS, 기술독립 |
| 구조적 개발 방법론 | 분할정복 / 요구사항분석(데이터업무) 구조분석(전략적설계, DFD) 구조적설계(전술적설계), 구조적 프로그래밍(분할, 반복개발) |
| CBD | 재사용 비용절감 생산성 / 도메인분석→도메인설계→컴포넌트추출→컴포넌트설계→컴포넌트구현→컴포넌트인증→레파지토리저장 / 요구사항정의→영역분석→컴포넌트기반설계→컴포넌트조립→시스템완성 |
| Product Line | Core Asset개발 재사용성 극대화 / 도에코 프리인 / 도메인엔지니어링(도메인분석, 코어에셋추출), 애플리케이션엔지니어링(코어에셋조립, 시스템완성), 코어에셋(핵심업무기능, 재사용, 레파지토리생성) |
| 객체지향 프로그래밍 특징 | 속성, 메소드, 객체 / **캡추다정상** |
| ㄴ 캡슐화 (encapsulation) | 메시지 |
| ㄴ 추상화 (Abstraction) | 기데제 |
| ㄴ 다형성 (Polymorphism) | 로라 |
| ㄴ 정보은닉 (Information Hiding) | PPPD |
| ㄴ 상속성 (Inheritance) | Extends |
| 객체지향 설계의 원리 | **SOLID**, 응집도를 높이고 결합도 낮춤, 모듈화 |
| AOP | 관심사분리, 의존성주입 / 코조 위애포 어크 |
| 개발 방법론 테일러링 (Tailoring) | 프로세스SW, 산출물 분석 표준생성 최적화 / **특표상세문** / 프로젝트특성추출→표준프로세스 수립 및 검증→상위커스터마이징(SDLC)→상세커스터마이징(WBS, 일정)→문서화(테일러링문서) |

---

<div id="s-req-arch"></div>

### 요구사항 정의

| 토픽 | 암기법 |
|:-----|:-------|
| 기능/비기능 요구사항 | 성장인데 보품관지 테제 |
| 성능/품질 요구사항 | 속처용가 신사유이 |
| 요구사항 상세화 실무 가이드 | 기펑성규 기무품 |

---

### SW Architecture

| 토픽 | 암기법 |
|:-----|:-------|
| SW Architecture | 컴포넌트, 인터페이스 / 요참모프배 RMCPL |
| ISO/IEC/IEEE 42010 (구 IEEE1471) | ISCPK ADVM RCR / 식표디뷰 |
| SW Architecture 평가 | 시설 시뮬수경 |
| ㄴ ATAM | 아시비 협기상후 / 품질특성 trade off평가 / 유틸리티트리(유틸리티,품질속성,품질속성세분화,시나리오) / 브레인스토밍 / 아키텍처(변경성,시험성,적응성,일치성,대체성) 시스템(상호운영성,보안성,회복성,정밀성) 비즈니스(적합성,준거성,이해성,습득성) / 협력과 준비→기본평가(td)→상세평가(bu)→후속조치 |
| ㄴ CBAM | ATAM기반, ROI, 경제성 평가 / 시나리오 수집→정제→우선순위 / 반응예측→효용성분석 / 효용예측분석→반응값 예측→예상효율→이익계산→ROI분석→결과검증 |

---

### MSA

| 토픽 | 암기법 |
|:-----|:-------|
| MSA | 도메인별 서비스 DB분리 API통한 데이터 송수신 / DDD분석(이벤트스토밍,분해,이벤트맵)→비즈니스설계개발(인프라,헥사고날,PoC)→테스트 및 모니터링(CICD검증,아키텍처검증,모니터링검증,장애대응력) / Client REST/SOAP, Application APIGW, LB, Persistence DB, 서비스 |
| 이벤트 스토밍 | 이벤트도출→도메인도출→커맨드도출→외부시스템→액터도출→애그리게이트 도출→컨텍스트 경계도출→정책설정 |
| 헥사고날 아키텍처 | Drive Adapter, Application Core, Driven Adapter / Port Application Layer, Adapter Layer |
| DDD (Domain Driven Design) | 모유 MDD, 유비쿼터스언어 / 전략적설계(분석단계, 이벤트 커맨드 애그리게잇 바운디드 컨텍스트 MSA도출), 전술적설계(MSA내부설계, 계구모 계층구조 Client Application, 도메인,인프라, 구현(엔티티 객체, 도메인이벤트, 커맨드), 모델관리 Module, Refactoring) |
| SAGA 패턴 | 보상이벤트 비동기처리 원자성보장 / Choreography(APP간 메시지전송, MOM카프카), Orchestration(SAGA마스터를 통한 데이터 처리) |
| CQRS 패턴 (Command and Query Responsibility Segregation) | CUD R분리, Command API, Read API, MOM Polyglot DB / 이메오폴(Event Sourcing, Message Queuing, ORM, Polyglot) |
| 클린 아키텍처 (Clean Architecture) | 룰엔유인프 매커니즘과 정책분리 / Dependency Rule / Entities→Use Cases→Interface Adapter→Framework&Driver |
| 서비스 메시 | Control Plane, Data Plane Sidecar Proxy, Service Discovery, Circuit Breaker, Business Logic |
| EDA | Producer 채널, Processor, 중계자 메시지큐 중재자 이벤트프로세서 이벤트채널, 이벤트프로세서 이벤트채널 |
| SOA | 통사정매채 / 서비스통합관리 서비스간 데이터처리 / 통신 SOAP, 사용 WSDL, 정의 UDDI, 메시지 XML, 채널 ESB / 중재자 중계자 서비스제공자 서비스 사용자 |

---

<div id="s-uml-pattern"></div>

### UML

`구행 CCDP USA I SCIT`

| 토픽 | 암기법 |
|:-----|:-------|
| UML / Diagram 전체 | UML 구조 / 구행 CCDP USA I SCIT |
| UML의 관계 (Relationship) | 연의GR 집복 |
| Class diagram | 관계유형, 접근제어, 관계숫자 |
| Usecase diagram | 액유시, 액유다명 |
| 시퀀스, 액티비티, State, 컴포넌트, 배치 | - |
| MOF (Meta Object Facility) | UML의 문법과 필수요소, 작성방법 메타모델 / RUMM Runtime Instance, User Model, Meta Model, Meta Meta Model |
| Sequence diagram | 액터 활성객체 생명선 제어사각형, 메시지, 프레임 |
| Activity Diagram | 구시활선 분병종 구역 / 시작점 활동 선택 분리(fork), 병합, 종료, 전이 |
| State Diagram | 상시전이조 / 상태 시작점 전이 이벤트 전이조건 |
| Interaction Diagram | 커뮤니케이션(액객링메프, 액터 객체 링크 메시지 프레임), 인터랙션오버뷰(액티비티→시퀀스) |

---

### 디자인 패턴

`생(추싱팩) 구(어퍼M) 행(전메템)`

| 토픽 | 암기법 |
|:-----|:-------|
| Design Pattern | **생구행** |
| ㄴ Abstract Factory 패턴 | <<interface>> Abstract Factory, Concrete Factory |
| ㄴ Singleton 패턴 | 전역변수, static, getInstance |
| ㄴ Factory method 패턴 | Creator, Concrete Creator, Concrete Product |
| ㄴ Adaptor 패턴 | 어댑터, 어댑티, 복합연관 |
| ㄴ Facade 패턴 | 인터페이스 통합, <<include>> |
| ㄴ Memento 패턴 | 스냅샷 |
| ㄴ Strategy pattern | 알고리즘 |
| ㄴ Template Method | 알고리즘골격, Final |
| ㄴ MVC 패턴 | Model, View, Control |
| ㄴ 서킷브레이커 | 상클오하 설최대예 / 상태 Close Open Half Open, fallback / 설정 최대실패, 대기시간, 예외이벤트 |

---

<div id="s-test-maint"></div>

### 테스트

`(원리) 결완초 정궤충집` · `ISO 29119 - 개프독테키 조관동` · `(기법) 명구경 → 블동경의상 유분페원오 / 화제루커 / 경탐오체분 펀인스서 → 휴박 차박노요` · `KDT - 생실결` · `성능테스트 - 처시사 부과용 / 루스확티가 단복성`

| 토픽 | 암기법 |
|:-----|:-------|
| Test 일반 | 결함발견, 원리, 절차 |
| 테스트 원리 | 결함존재, 완벽테스트불가, 초기테스트, 정황에의존, 오류부재궤변, 살충제패러독스, 오류집중 |
| 명세기반 테스팅 기법 | 블동경의상 유분페원오 |
| 구조기반테스트 | 화제루커 |
| 탐색적 테스팅 | 경험, 결함집중, 애자일 / 휴박 차박노요 |
| 경험기반 기법 리스크기반 | 경탐오체분 펀인스서 |
| 성능 테스트 | 처리지표(TPS,Throughput,가용성), 시간지표(Response Time, Think Time, Request Interval Time), 사용자지표(Named User, Concurrent User, Active User) / 부하, 과부하, 용량 / 루프백, 스파이크, 티어, 확장성, 가용성 / 목적: 단위복합성능 |
| BMT (Benchmark Test) | 벤치오오 오공오일 일억조사 / 발수심참 발수상설 신계수결 |
| ISO 29119 | 개프독테키 조관동(프독) 명구경(테) / ISO 33063 |
| 키워드기반 테스트 | 생실결, SUT, ISO29119 |
| Test Coverage | 구문 조건 결정 조결 엠조결 멀조결 / 1100 1110 1010 문장, 조건 결정 커버리지율 |
| 몽키테스트 | 스크립트→실행→검증, 초기 설계, 프로토타입 |
| 회귀테스트 | 수정영실 리파사부 리셀프 / 수정→영향도파악→실행 / Ripple Effect(파급), Side Effect(부작용), Retest all, Selective Test, Priority Test |
| V모델 | verification Validation / 개발자와 테스트의 영역구분 확인과 검증의 절차 / 화이트→그레이→블랙 / 인수(알파 베타 감마) |
| 임베디드 테스트 | Dess V(상위,하위), Multiple V(모델,프로토타입,finalProduct), SW(상태,위험,명세,멀티v), HW(그레이,블랙,경계스캔,연기테스트) |
| 테스트케이스 | 목방개 예실피 / 테스트목적, 테스트방법 및 절차, 테스트케이스개발 테스트예측결과작성, 테스트실행, 결과피드백 / 식테입출 환특의 / 식별자, 테스트항목 입력명세, 출력명세 테스트환경 특수요구사항, 의존성 |

---

### 유지보수

| 토픽 | 암기법 |
|:-----|:-------|
| 모듈화 | 우연적 논리적 시간적 절차적 통신적 순차적 기능적 / 내부적 공통적 외부적 제어 스탬프 자료 메시지 |
| 소프트웨어 리팩토링 (SW Refactoring) | 중긴큰긴발분 중복소스 긴메소드 큰클래스 긴파라미터 변경의 발산, 변경의분산 / 결이분 응올내통 가리 / 결합도 이동 분리, 응집도 올림 내림 통합(inline), 가독성 rename |
| Lehman 소프트웨어 변화 | 계자조친 피지증감 / 계속적변경 자가규제 조직적 안정화 친근함유지 피드백 시스템, 지속적 성장, 복잡도증가, 품질감소 / SPE Specification Procedure Environment |
| 유지보수 | 시대원 시점 응계예지 응급계획예방지연 / 대상 시스템, 데이터, 프로그램, 문서 / 원인 수완예적 수정정 완전적 예방적 적응적 |
| 3R | 재공학 역공학 재사용 |
| 역공학 (Reverse Engineering) | 논리적역공학(물리설계), 자료역공학(DB) / 추분문 코드추출 코드분석 역공학문서화 |
| 재공학 (Re-Engineering) | 재구조화, 재모듈화, 의미론적 정보추출 / 역공학 재구조화 구현 |
| Reuse | 분류, 디자인패턴, 모듈화, 객체지향, CBD, PL / 순공학 재사용 역공학 순공학 재사용 |

---

<div id="s-quality" class="sticky-header sticky-header-quality">🏆 소프트웨어 품질관리</div>

### SW 품질

| 토픽 | 암기법 |
|:-----|:-------|
| ISO 25000 (SQuaRE, Systems and software Quality Requirements and Evaluation) | 요모관측평 31024 / 품질특성 기~ |
| ISO/IEC 25041 (ISO 14598) | 품질평가프로세스 표준 / 개관 개구평모 / 요명설수결 |
| ISO/IEC 25051 (ISO 12119) | 품질 요구사항, 테스트 / 제사실 / 제사실기보 |
| 프로젝트 형상관리 | 식통감기 기물목정 / 계요설구통운 / 기분설시제운 |
| CMMI / CMMI 2.0 | 카캐프레 4 9 20 두메인임 / 초관정량체 |
| SPICE | 기지조 고공지관조 / 불수관확예최 |
| ASPICE (Automotive SPICE) (ISO/IEC 33020) | 기지조 획공소시지 관재프 / 불수관확예혁 |
| GS(Good SW)인증 | 235141 / 기신사효유이호보일 |
| SP(SW Process)인증 | 프개지 프조프개지 |

---

### SW 안전성

| 토픽 | 암기법 |
|:-----|:-------|
| SW 안전성 요구사항 도출 절차 | 개범위명안 |
| SW 안전성/분석 개념 | 일기간 기소설테 목단분 |
| FMEA | SOD RPN DRP |
| FTA | 탑조다 정량대 |
| HAZOP | 이공가 사장외 특일 / 없증감반 부분기 |

---

<div id="s-mgmt" class="sticky-header sticky-header-mgmt">📋 소프트웨어 사업 관리</div>

### 발주 프로세스

| 토픽 | 암기법 |
|:-----|:-------|
| 제안요청서 작성 가이드 | 기방제입 작체확 / 기술제안내용 입찰방법 및 계약조건 제안안내서 입찰공고문 작성 체크리스트 수정 및 확인 입찰공고문 |
| 제안서 기술성평가 | 기술제안서 전기성 관지상하 / 전략 기술/기능 성과/품질 프로젝트관리 프로젝트지원 상생협력 하도급계약 적정성 / 기신사효유이공 |
| 기술평가표 (technical evaluation sheet) | 일반부분, 기술부분, 관리부문, 지원부분 |
| 기술 가치 평가 | 기술이전 사업화 가치 평가 / 기술성분석 권리성분석 시장성분석 사업성분석 / 수익접근법 시장접근법 비용접근법 |
| 상용SW 직접구매 제도 (SW 분리발주) | 분리54 3억이상 5천만원 조달청, GS인증 / 예외 민간형소프트웨어사업, 현저성 / 파조예발 SW사업비 및 사업유형 파악 사용SW 구매조사, 사업예외여부파악, SW사업발주 |
| SW 분할발주 | 공정분할, 기능분할, 부품분할 |
| SW 단계별 발주 | 선행사업기획 요구분석, 논리적설계 → 후행사업기획 상세설계, 구현, 테스트, 인수 |
| SW영향평가제 | 민간43 민간침해검토 / 사검민필종 사업계획서 작성, 사업계획서 검토, 민간침해검토, 사업필요성 및 공공성 검토, 종합의견작성 / 예외: 국방 및 치안관련 프로젝트, 현저성, 민간투자형 SW사업, 상용SW구매사업 |
| 민간투자형 SW사업제도 | 민간자본 50%이상 투자, 운영비 또는 사용료→투자금 분할 상환 / 소프트웨어 진흥법 40조, 소프트웨어 진흥법 시행령 32조 / 개발형(임대형, 수익형), 구매형 / 사업계획서/ISP→사전검토/적격성조사→SW사업고시→사업자선정→계약→사업 |

---

### SW 비용산정

| 토픽 | 암기법 |
|:-----|:-------|
| McCabe 회전 복잡도 | 영화조 |
| LOC 방법 | 베타분포계산 |
| 하드웨어 규모산정 | 수참시 |
| 공공SW사업 과업변경 | 변소50 4547 요구심통작금 |

---

### 오픈소스

| 토픽 | 암기법 |
|:-----|:-------|
| 오픈소스 SW | 공자배2 수차분 동포중 |
| License | 허약강 |
| 양립성 | 신재양탄 전특특추 |
| 오픈소스 거버넌스 | 정획적운개 위측관참활 |

---

### FP (Function Point)

| 토픽 | 암기법 |
|:-----|:-------|
| SW사업 대가산정 가이드 | 간이법 유범이의데이트 규연성호보 후직소 |
| 정규법 | - |

---

### 감리

| 토픽 | 암기법 |
|:-----|:-------|
| 감리 프레임워크 | 제3자, 점검, 개선 / 기현 이목관 업기정 / 시응대 시운 / 데데품 / 제지 유지보수 |
| 감리 조건/절차 | 요설종 예현조 |
| 단계별감리절차 | 준실감 감착감 보종보 / 준시작보 |
| 감리산출물 및 목차 | 근목대점 일보행 / 종과감별 / 계결과감 |
| 감리결과 보고서 작성 | 종과감별 개시과 / 유정논객 명간적준완 / 성실충 기무편안 보효준일 계절준 |
| 상주감리원/PMO | 제3자, 집중사업관리 / 전정 피6478, 감옥칠일 |

---

### TDD / DevOps / SRE

| 토픽 | 암기법 |
|:-----|:-------|
| DevOps | 품프도 품질 프로세스 도구 / 품질 품질유지, 테스트자동화 / 프로세스 짧은배포주기, 릴리즈와 배포분리, 배포자동화, 지속적완성 / 도구 CI/CD 프로비저닝, Application Release |
| 무중단 배포 | 지속적 배포를 위한 배포시 무중단 시스템 / Rolling Update LB에서 조금씩 전환 / Blue Green Deployment 별도 인스턴스, 한번에 이관 / Canary Release 일부사용자 점진적용 |
| TDD (Test Driven Development) | 요테코리체 / 요구사항 분석→테스트코드작성→코딩→리펙토링→check out |
| SRE (Site Reliability Engineering) | MC변장문 IO |

---

<div id="s-advanced" class="sticky-header sticky-header-advanced">🚀 심화 토픽</div>

| 토픽 | 암기법 |
|:-----|:-------|
| 소프트웨어 위기 | HW더빠름, SW특징(비기마제무 복복), 공자표품 |
| 주 공정법(CPM) | 프로젝트 최소기간, 프로젝트 일정 네트워크 분석 기법 / 절차 - 정순기 전후 분추 |
| WBS의 구성요소와 작성원칙 | 범위관리, 최소 업무 단위, 가시성 / 구성요소(APD), 작성원칙(WPL방) |
| 공공소프트웨어사업 과업심의 가이드 | SW법 50 47 1 / 유형(확변), 대상 / 확정 시 판단기준(내기상재), 확정 시 절차(요심통확) / 변경 시 판단기준(제기합), 변경 시 절차(요심통작재) |
| 정보시스템 감리 | 종합적 점검하고 문제점 개선 과정 / 유형(단계상주), 2설구 3요설구, 20억 6개월, 산출물 |
| Function Point | 유범 데트 미계결 / 데트보 |
| SW 사업 대가산정 가이드 | 발주, 계약 시 적정 대가 산정 가이드 / 절차(사이전사) / 유형별 가이드(유운재 응상공보 소보) |
| 대형 소프트웨어사업 전문평가제도 | 전문성 제고, 품질 보완 / 주요내용(8인, 40%) / 평가기준(기보데디, 전구운조/설준운조/설이관보/전활운조) |
| 프로젝트 요구사항 | 요구사항 조건(정명완일 중검수추, 830→29148) / 요구사항 수집기법(수분표의데프컨) / 요구사항 명세서 구성요소(서개용 요아사모 부색) |
| ISO/IEC/IEEE 29148 | 요구사항명세서작성 국제표준(SRS) / 요구사항 명세서 구성요소(서개용 요아사모 부색) / 요구사항 작성원칙(정명완일 중검수추, 830→29148) |
| 성능 요구사항 | 달성 최고, 최저 능력 처리량, 자원 사용치 기술 / 목적(만족성, 효율성) / 성능요구사항(속처용가) / 품질요구사항(신사유이) / 요구사항 상세화절차(요모최모) |
| 소프트웨어 아키텍처 드라이버 | 아키텍처설계원칙으로 사용되는 요구사항들의 집합 / 구성요소(비기제우) |
| V모델과 RTM | V모델 = 시험자(Verification), 사용자(Validation) 지원하는 test model / 특징(추확신품) / 테스트유형(단통시인설) / RTM = 요구사항-구현 관계 매트릭스 / 추적성(순역양) / 구성요소(요설테프배단통사ID) |
| SAFe(Scaled Agile Framework) | 대규모 조직 애자일 도입 프레임워크(6.0) / 4대 가치(정존개투) / 10대 원칙(경시변점 작중케 동분가) |
| 디미터의 법칙(Law of Demeter) | Object 최소 지식 원칙, 제한된 정보 소유, 설계 기법, MSA의 기초사상 / 등장배경(종속성, 다중점지양) / 규정성(오메초 변전) |
| 인터랙션 오버뷰 다이어그램 | 표기법 - 액시 AIDT 활메제 |
| 클래스 다이어그램 | 구성요소 - 클스 / 접근제어자 - PPPP / 관계 - 연직집 복의일실 |
| 샌드위치테스트, 빅뱅테스트 | 샌드위치 혼합식(상하), 빅뱅 동시식 / 비교(순모통 오수규시비) |
| Shift-left | 초기결함발견집중 통한 품질관리 / 법칙(초결궤) / 한계(불살정) |
| MSA | 모놀리식(하나의 코드 베이스), MSA(큰 App 을 여러 개의 작은 App) / 비교(개목특기요 표장단사 배개디수) / MSA 문제점(장트R테) / DDD(설계-구현 계속 수정 반복) / DDD 설계절차(유도서 바컨도) |
| MSA 트랜잭션 관리 방법 | MSA 단일 트랜잭션 정합성, 원자성 보장 어려움 (2PC, SAGA 패턴) / 2PC = 모든 노트 커밋, 롤백 / 구성요소(서정지커클) / 트랜잭션관리방법(PC) / SAGA패턴 = 여러 작은 로컬 트랜잭션, 보상 트랜잭션 / 유형(CO) / 트랜잭션관리방법(CO) |

