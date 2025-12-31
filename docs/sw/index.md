---
layout: default
title: SW (소프트웨어공학)
nav_order: 3
has_children: true
has_toc: false
permalink: /docs/sw
---

# SW (소프트웨어공학) <span class="page-title-with-cta__ctas"><a class="exam-top-cta" href="{{ site.baseurl }}/docs/sw/daily">🃏 데일리 암기 덱</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/sw/exam">📝 기출문제</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/sw/legacy">🗂️ 레거시</a></span>
{: .fs-9 .page-title-with-cta }

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
  top: 0;
  background: white;
  padding: 0.8rem 1rem;
  margin: 0 -1rem;
  z-index: 100;
  border-bottom: 2px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

<details open markdown="1">
<summary><strong>📋 목차 (주요 섹션)</strong></summary>

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
| RAD | 개발도구(CASE), 빠른개발 / 지라씨(JRAC) / JRP→JAD→Cut Over |

---

### 개발방법론

| 토픽 | 암기법 |
|:-----|:-------|
| 정보공학(IE) 방법론 | ISP/데이터중심 / ISPASS, 기술독립 |
| 구조적 개발 방법론 | 분할정복 / 요구사항분석→구조분석(DFD)→구조적설계→구조적 프로그래밍 |
| CBD | 재사용 비용절감 생산성 / 요구사항정의→영역분석→컴포넌트기반설계→조립→완성 |
| Product Line | Core Asset개발 재사용성 극대화 / 도에코 프리인 |
| 객체지향 프로그래밍 특징 | 속성, 메소드, 객체 / **캡추다정상** |
| ㄴ 캡슐화 | 메시지 |
| ㄴ 추상화 | 기데제 |
| ㄴ 다형성 | 로라 |
| ㄴ 정보은닉 | PPPD |
| ㄴ 상속성 | Extends |
| 객체지향 설계의 원리 | **SOLID**, 응집도↑ 결합도↓, 모듈화 |
| AOP | 관심사분리, 의존성주입 / 코조 위애포 어크 |
| 개발 방법론 테일러링 | 프로세스SW, 산출물 분석 / **특표상세문** |

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
| ISO/IEC/IEEE 42010 | ISCPK ADVM RCR / 식표디뷰 |
| SW Architecture 평가 | 시설 시뮬수경 |
| ㄴ ATAM | 아시비 협기상후 / 품질특성 trade off / 유틸리티트리 |
| ㄴ CBAM | ATAM기반, ROI, 경제성 평가 |

---

### MSA

| 토픽 | 암기법 |
|:-----|:-------|
| MSA | 도메인별 서비스 DB분리 API / DDD분석→설계개발→테스트/모니터링 |
| 이벤트 스토밍 | 이벤트→도메인→커맨드→외부시스템→액터→애그리게이트→컨텍스트경계→정책 |
| 헥사고날 아키텍처 | Drive Adapter, Application Core, Driven Adapter / Port, Adapter Layer |
| DDD (Domain Driven Design) | 모유 MDD, 유비쿼터스언어 / 전략적설계(분석)→전술적설계(구현) |
| SAGA 패턴 | 보상이벤트 비동기처리 원자성보장 / Choreography, Orchestration |
| CQRS 패턴 | CUD R분리 / 이메오폴 |
| 클린 아키텍처 | 룰엔유인프 / Entities→Use Cases→Interface Adapter→Framework |
| 서비스 메시 | Control Plane, Data Plane / Sidecar Proxy, Service Discovery, Circuit Breaker |
| EDA | Producer→채널→Processor→이벤트채널→이벤트프로세서 |
| SOA | 통사정매채 / SOAP, WSDL, UDDI, XML, ESB |

---

<div id="s-uml-pattern"></div>

### UML

`구행 CCDP USA I SCIT`

| 토픽 | 암기법 |
|:-----|:-------|
| UML / Diagram 전체 | 구조(CCDP), 행위(USA I SCIT) |
| UML의 관계 | 연의GR 집복 |
| Class diagram | 관계유형, 접근제어(PPPP), 관계숫자 |
| Usecase diagram | 액유시, 액유다명 |
| Sequence diagram | 액터 활성객체 생명선 제어사각형, 메시지, 프레임 |
| Activity Diagram | 구시활선 분병종 / 구역,시작점,활동,선택,분리(fork),병합,종료,전이 |
| State Diagram | 상시전이조 / 상태,시작점,전이,이벤트,전이조건 |
| Interaction Diagram | 커뮤니케이션(액객링메프), 인터랙션오버뷰(액티비티→시퀀스) |
| MOF (Meta Object Facility) | RUMM / Runtime Instance, User Model, Meta Model, Meta Meta Model |

---

### 디자인 패턴

`생(추싱팩) 구(어퍼M) 행(전메템)`

| 토픽 | 암기법 |
|:-----|:-------|
| Design Pattern | **생구행** |
| Abstract Factory | <<interface>> Abstract Factory → Concrete Factory |
| Singleton | 전역변수, static, getInstance |
| Factory Method | Creator → Concrete Creator → Concrete Product |
| Adapter | 어댑터, 어댑티, 복합연관 |
| Facade | 인터페이스 통합, <<include>> |
| Memento | 스냅샷 |
| Strategy | 알고리즘 |
| Template Method | 알고리즘 골격, Final |
| MVC | Model, View, Controller |
| 서킷브레이커 | 상클오하 설최대예 / Close→Open→Half Open, fallback |

---

<div id="s-test-maint"></div>

### 테스트

`(원리) 결완초 정궤충집` · `(기법) 명구경`

| 토픽 | 암기법 |
|:-----|:-------|
| Test 일반 | 결함발견, 원리, 절차 |
| 테스트 원리 | 결함존재, 완벽테스트불가, 초기테스트, 정황의존, 오류부재궤변, 살충제패러독스, 오류집중 |
| 명세기반 테스팅 | 블동경의상 유분페원오 |
| 구조기반 테스트 | 화제루커 |
| 탐색적 테스팅 | 경험, 결함집중, 애자일 / 휴박 차박노요 |
| 경험기반/리스크기반 | 경탐오체분 펀인스서 |
| 성능 테스트 | 처시사 부과용 / 루스확티가 / 단복성 |
| BMT | 벤치오오 오공오일 일억조사 / 발수심참 발수상설 신계수결 |
| ISO 29119 | 개프독테키 조관동(프독) 명구경(테) / ISO 33063 |
| 키워드기반 테스트 | 생실결, SUT |
| Test Coverage | 구문 조건 결정 조결 엠조결 멀조결 |
| 몽키테스트 | 스크립트→실행→검증, 초기 설계, 프로토타입 |
| 회귀테스트 | 수정영실 리파사부 리셀프 |
| V모델 | Verification Validation / 화이트→그레이→블랙 / 인수(알파 베타 감마) |
| 임베디드 테스트 | Dess V, Multiple V |
| 테스트케이스 | 목방개 예실피 / 식테입출 환특의 |

---

### 유지보수

| 토픽 | 암기법 |
|:-----|:-------|
| 모듈화 | 응집도: 우논시절통순기 / 결합도: 내공외제스자메 |
| SW 리팩토링 | 중긴큰긴발분 / 결이분 응올내통 가리 |
| Lehman SW 변화 | 계자조친 피지증감 / SPE |
| 유지보수 | 시대원 / 응계예지 / 수완예적 |
| 3R | 재공학, 역공학, 재사용 |
| 역공학 | 논리적역공학, 자료역공학 / 추분문 |
| 재공학 | 재구조화, 재모듈화, 의미론적 정보추출 |
| Reuse | 분류, 디자인패턴, 모듈화, 객체지향, CBD, PL |

---

<div id="s-quality" class="sticky-header sticky-header-quality">🏆 소프트웨어 품질관리</div>

### SW 품질

| 토픽 | 암기법 |
|:-----|:-------|
| ISO 25000 (SQuaRE) | 요모관측평 31024 / 품질특성 기~ |
| ISO/IEC 25041 | 품질평가프로세스 / 개관 개구평모 / 요명설수결 |
| ISO/IEC 25051 | 품질 요구사항, 테스트 / 제사실 / 제사실기보 |
| 형상관리 | 식통감기 기물목정 / 계요설구통운 / 기분설시제운 |
| CMMI 3.0 | 카캐프레 4 9 20 / 초관정량체 |
| SPICE | 기지조 고공지관조 / 불수관확예최 |
| ASPICE | 기지조 획공소시지 관재프 / 불수관확예혁 |
| GS인증 | 235141 / 기신사효유이호보일 |
| SP인증 | 프개지 프조프개지 |

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
| 제안요청서 작성 가이드 | 기방제입 작체확 |
| 제안서 기술성평가 | 전기성 관지상하 / 기신사효유이공 |
| 기술평가표 | 일반부분, 기술부분, 관리부문, 지원부분 |
| 기술 가치 평가 | 기술성분석 권리성분석 시장성분석 사업성분석 / 수익·시장·비용접근법 |
| 상용SW 직접구매 제도 | 분리54 3억이상 5천만원 조달청, GS인증 / 파조예발 |
| SW 분할발주 | 공정분할, 기능분할, 부품분할 |
| SW 단계별 발주 | 선행(요구분석,논리설계) → 후행(상세설계,구현,테스트,인수) |
| SW 영향평가제 | 민간43 / 사검민필종 |
| 민간투자형 SW사업 | 민간자본 50%이상 / 진흥법40조 / 개발형(임대/수익), 구매형 |

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
| 감리 프레임워크 | 제3자, 점검, 개선 / 기현 이목관 업기정 / 시응대 시운 / 데데품 |
| 감리 조건/절차 | 요설종 예현조 |
| 단계별 감리절차 | 준실감 감착감 보종보 / 준시작보 |
| 감리산출물 | 근목대점 일보행 종과감별 계결과감 |
| 감리결과보고서 | 종과감별 개시과 / 유정논객 명간적준완 / 성실충 기무편안 보효준일 |
| 상주감리원/PMO | 제3자, 집중사업관리 / 전정 피6478, 감옥칠일 |

---

### TDD / DevOps / SRE

| 토픽 | 암기법 |
|:-----|:-------|
| DevOps | 품프도 / 품질유지, 테스트자동화 / 짧은배포주기, 배포자동화, 지속적완성 |
| 무중단 배포 | Rolling Update, Blue-Green, Canary Release |
| TDD | 요테코리체 / 요구사항분석→테스트코드→코딩→리펙토링→check out |
| SRE | MC변장문 IO |

---

<div id="s-advanced" class="sticky-header sticky-header-advanced">🚀 심화 토픽</div>

| 토픽 | 암기법 |
|:-----|:-------|
| 소프트웨어 위기 | HW더빠름, SW특징(비기마제무 복복), 공자표품 |
| 주 공정법(CPM) | 프로젝트 최소기간 / 정순기 전후 분추 |
| WBS 구성요소/작성원칙 | 범위관리, 최소업무단위, 가시성 / APD, WPL방 |
| 공공SW사업 과업심의 | SW법 50 47 1 / 유형(확변), 확정(내기상재), 변경(제기합) |
| 정보시스템 감리 | 유형(단계상주), 2설구 3요설구, 20억 6개월 |
| Function Point | 유범 데트 미계결 / 데트보 |
| ISO 29148 | 요구사항명세서(SRS) / 서개용 요아사모 부색 / 정명완일 중검수추 |
| 성능 요구사항 | 속처용가, 품질(신사유이), 절차(요모최모) |
| SAFe 6.0 | 대규모 애자일 / 4대가치(정존개투), 10대원칙(경시변점 작중케 동분가) |
| 디미터의 법칙 | 최소지식원칙, MSA 기초사상 / 오메초 변전 |
| Shift-left | 초기결함발견 / 초결궤, 한계(불살정) |
| MSA 트랜잭션 관리 | 2PC(모든노드 커밋/롤백), SAGA(보상트랜잭션) |

