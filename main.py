# main.py (도쿄 리전 배포용 - 경량 앱)

import streamlit as st
import streamlit.components.v1 as components

SEOUL_APP_URL = "https://clean-text-seoul-1097794617970.asia-northeast3.run.app"  # 서울 리전 URL

DISCLAIMER_TEXT = """
이 도구는 의료 데이터 처리 보조 도구입니다. 사용 전 아래 내용을 확인하세요.

[데이터 처리 방식]
- 입력 데이터는 국내 서버(서울 리전)에서만 처리됩니다
- 처리된 데이터는 서버에 저장되지 않습니다
- 자동 비식별 처리가 적용됩니다 (환자 등록번호, 날짜, 진료과, 작성자 정보 제거)
- 비식별 처리의 완전성을 보장하지 않습니다

[사용자 책임]
- 실환자 데이터 입력 시 소속 기관의 정보보호 규정을 확인하세요
- 본 도구 사용으로 발생하는 법적·행정적 책임은 사용자에게 있습니다
- 개발자는 사용자의 입력 데이터에 대한 책임을 지지 않습니다

[도구 특성]
- 본 도구는 비상업적 의료 보조 목적으로 제작되었습니다
- 소스코드는 공개되어 있으며 투명하게 운영됩니다
- 의료적 판단을 대체하지 않습니다
"""

st.set_page_config(
    page_title="Clean Text",
    page_icon="🧼",
    layout="centered"
)

# --- Disclaimer ---
if not st.session_state.get("accepted"):
    st.markdown("## 🧼 Clean Text")
    st.markdown("##### EMR 구조화 솔루션")
    st.divider()

    st.warning("사용 전 아래 내용을 확인하세요.")
    
    with st.expander("📋 전문 보기", expanded=True):
        st.markdown(DISCLAIMER_TEXT)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption("확인 버튼 클릭 시 위 내용에 동의한 것으로 간주합니다.")
    with col2:
        if st.button("확인했습니다 →", type="primary", use_container_width=True):
            st.session_state["accepted"] = True
            st.rerun()

# --- Redirect ---
else:
    st.markdown("이동 중입니다...")

    components.html(
        f"""
        <script>
            window.parent.location.replace("{SEOUL_APP_URL}");
        </script>
        """,
        height=0
    )

    st.markdown(f"자동으로 이동하지 않으면 [여기를 클릭하세요]({SEOUL_APP_URL})")