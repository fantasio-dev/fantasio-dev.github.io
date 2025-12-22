---
layout: default
title: SEC (정보보안)
nav_order: 5
has_children: true
permalink: /docs/sec
---

# SEC (정보보안)
{: .fs-9 }

정보보안 관련 학습 자료입니다. 총 **106개** 항목
{: .fs-6 .fw-300 }

{% assign sec_root = page.title %}
{% assign sec_topics = site.pages | where: "grand_parent", sec_root %}

{% assign crypto_all = site.pages | where: "parent", "1. 암호 기술" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign iam_all = site.pages | where: "parent", "2. 인증·접근통제·식별" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign netsec_all = site.pages | where: "parent", "3. 네트워크 보안" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign cloud_all = site.pages | where: "parent", "4. 클라우드/IoT/스마트 보안" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign attack_all = site.pages | where: "parent", "5. 사이버 공격·위협 분석" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign vuln_all = site.pages | where: "parent", "6. 보안 취약점" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign ops_all = site.pages | where: "parent", "7. 보안 운영·대응" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign forensic_all = site.pages | where: "parent", "8. 디지털 포렌식" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign privacy_all = site.pages | where: "parent", "9. 개인정보 보호" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign policy_all = site.pages | where: "parent", "10. 보안 정책·표준" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign devsec_all = site.pages | where: "parent", "11. 개발 보안/운영 보안" | where: "grand_parent", sec_root | sort: "nav_order" %}
{% assign trend_all = site.pages | where: "parent", "12. 보안 신기술/트렌드" | where: "grand_parent", sec_root | sort: "nav_order" %}

<div class="sec-matrix">
  <div class="sec-matrix__grid">
    <!-- ① 공격기법 (침해사고, 위협) -->
    <section class="sec-card">
      <div class="sec-card__header">① 공격기법 (침해사고, 위협)</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/05-cyber-attack">공격 기법/프레임워크</a></div>
          <div class="nw-sub__content">
            {% assign atk_framework = attack_all | where_exp: "p", "p.url contains '/mitre-attack' or p.url contains '/cyber-kill-chain' or p.url contains '/apt'" %}
            {% assign atk_methods = attack_all | where_exp: "p", "p.url contains '/dos-ddos' or p.url contains '/ransomware' or p.url contains '/raas' or p.url contains '/supply-chain-attack' or p.url contains '/social-engineering' or p.url contains '/infostealer'" %}
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">공격 기법</div>
                <div class="nw-links">
                  {% for item in atk_methods %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">프레임워크</div>
                <div class="nw-links">
                  {% for item in atk_framework %}
                    <a class="nw-link nw-link--blue nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/06-vulnerability">취약점</a></div>
          <div class="nw-sub__content">
            {% assign vuln_sw = vuln_all | where_exp: "p", "p.url contains '/owasp-top10' or p.url contains '/injection' or p.url contains '/xss' or p.url contains '/csrf' or p.url contains '/ssrf'" %}
            {% assign vuln_platform = vuln_all | where_exp: "p", "p.url contains '/cloud' or p.url contains '/iot' or p.url contains '/smart-' or p.url contains '/metaverse' or p.url contains '/blockchain' or p.url contains '/ai' or p.url contains '/mec' or p.url contains '/uam'" %}
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">SW(OWASP)</div>
                <div class="nw-links">
                  {% for item in vuln_sw %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">플랫폼</div>
                <div class="nw-links">
                  {% for item in vuln_platform %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 보안기술 (암호화 등) -->
    <section class="sec-card">
      <div class="sec-card__header">② 보안기술 (암호화 등)</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/01-cryptography">암호 기술</a></div>
          <div class="nw-sub__content">
            {% assign crypto_basic = crypto_all | where_exp: "p", "p.url contains '/encryption' or p.url contains '/block-cipher' or p.url contains '/hash' or p.url contains '/mac-mdc'" %}
            {% assign crypto_pk = crypto_all | where_exp: "p", "p.url contains '/diffie-hellman' or p.url contains '/rsa' or p.url contains '/digital-signature'" %}
            {% assign crypto_new = crypto_all | where_exp: "p", "p.url contains '/homomorphic-encryption' or p.url contains '/zero-knowledge-proof' or p.url contains '/fpe' or p.url contains '/ope'" %}
            {% assign crypto_quantum = crypto_all | where_exp: "p", "p.url contains '/qkd' or p.url contains '/pqc' or p.url contains '/qubit'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">기본</div>
                <div class="nw-links">
                  {% for item in crypto_basic %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">공개키/서명</div>
                <div class="nw-links">
                  {% for item in crypto_pk %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">최신</div>
                <div class="nw-links">
                  {% for item in crypto_new %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">양자</div>
                <div class="nw-links">
                  {% for item in crypto_quantum %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/02-iam">인증·접근통제·식별(IAM)</a></div>
          <div class="nw-sub__content">
            {% assign iam_auth = iam_all | where_exp: "p", "p.url contains '/pki' or p.url contains '/digital-envelope' or p.url contains '/fido' or p.url contains '/ldap'" %}
            {% assign iam_access = iam_all | where_exp: "p", "p.url contains '/access-control' or p.url contains '/sso'" %}
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">인증</div>
                <div class="nw-links">
                  {% for item in iam_auth %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">접근통제</div>
                <div class="nw-links">
                  {% for item in iam_access %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ 정보보호 (보안 엔지니어링 등) -->
    <section class="sec-card">
      <div class="sec-card__header">③ 정보보호 (보안 엔지니어링 등)</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/03-network-security">네트워크 보안</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in netsec_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/04-cloud-iot-smart">클라우드/IoT/스마트 보안</a></div>
          <div class="nw-sub__content">
            {% assign cloud_core = cloud_all | where_exp: "p", "p.url contains '/casb' or p.url contains '/sase' or p.url contains '/cloud-vulnerability'" %}
            {% assign smart_core = cloud_all | where_exp: "p", "p.url contains '/iot-security' or p.url contains '/aiot-security' or p.url contains '/mec-security' or p.url contains '/metaverse-security' or p.url contains '/blockchain-security'" %}
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">클라우드</div>
                <div class="nw-links">
                  {% for item in cloud_core %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">IoT/스마트</div>
                <div class="nw-links">
                  {% for item in smart_core %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ 보안시스템 + 기술적 수단 -->
    <section class="sec-card">
      <div class="sec-card__header">④ 보안시스템 + 기술적 수단</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/07-security-operations">탐지/대응(D&R)</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in ops_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/11-devsecops">DevSecOps/개발보안</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in devsec_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 포렌식 (사고대응) -->
    <section class="sec-card">
      <div class="sec-card__header">⑤ 포렌식 (사고대응) <span class="nw-badge-hot">🔥</span></div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/08-digital-forensics">디지털 포렌식</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in forensic_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑥ 개인정보보호 -->
    <section class="sec-card">
      <div class="sec-card__header">⑥ 개인정보보호 및 활용</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/09-privacy">개인정보 보호</a></div>
          <div class="nw-sub__content">
            {% assign p_law = privacy_all | where_exp: "p", "p.url contains '/data-3-laws' or p.url contains '/privacy-breach-report' or p.url contains '/pia'" %}
            {% assign p_pet = privacy_all | where_exp: "p", "p.url contains '/pet' or p.url contains '/anonymization' or p.url contains '/de-identification' or p.url contains '/privacy-model' or p.url contains '/pseudonymization'" %}
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">법·제도</div>
                <div class="nw-links">
                  {% for item in p_law %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">PET</div>
                <div class="nw-links">
                  {% for item in p_pet %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑦ 관리적 보안 (보안정책, 절차) -->
    <section class="sec-card">
      <div class="sec-card__header">⑦ 관리적 보안 (정책/표준) <span class="nw-badge-hot">🔥</span></div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/10-policy-standard">정책·표준</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in policy_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title">기출문제</div>
          <div class="nw-sub__content">
            <div class="nw-links">
              <a class="nw-link nw-link--red nw-link--strong" href="{{ site.baseurl }}/docs/sec/exam">📝 기출문제 (114문제)</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 최근 보안 이슈/트렌드 -->
    <section class="sec-card">
      <div class="sec-card__header">최근 보안 이슈 & 트렌드</div>
      <div class="sec-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sec/12-security-trends">보안 신기술/트렌드</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in trend_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>

