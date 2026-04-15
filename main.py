# main.py (도쿄 리전 배포용 - 경량 앱)

import streamlit as st
import streamlit.components.v1 as components

SEOUL_APP_URL = "https://clean-text-seoul-1097794617970.asia-northeast3.run.app"  # 서울 리전 URL

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

    st.warning(
        "이 도구를 사용하기 전 아래 내용을 확인하세요."
    )

    st.markdown("""
    - 입력 데이터는 서버에 저장되지 않습니다
    - 자동 비식별 처리가 적용되나, 완전한 비식별을 보장하지 않습니다
    - 실환자 데이터 입력 시 소속 기관의 정보보호 규정을 확인하세요
    - 본 도구 사용으로 발생하는 법적 책임은 사용자에게 있습니다
    """)

    if st.button("확인했습니다 →", type="primary", use_container_width=True):
        st.session_state["accepted"] = True
        st.rerun()

# --- Redirect ---
else:
    st.markdown("이동 중입니다...")

    components.html(
        f"""
        <script>
            window.location.replace("{SEOUL_APP_URL}");
        </script>
        """,
        height=0
    )

    # JS 차단 환경 fallback
    st.markdown(f"자동으로 이동하지 않으면 [여기를 클릭하세요]({SEOUL_APP_URL})")