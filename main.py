import streamlit as st
import streamlit.components.v1 as components

SEOUL_APP_URL = "https://clean-text-seoul-1097794617970.asia-northeast3.run.app"  # 서울 리전 URL

DISCLAIMER_TEXT = """
Clean Text는 의료 텍스트 정리와 검사 결과 구조화를 돕는 보조 도구입니다.

### 데이터 처리 방식
- 서울 서버는 앱 실행에 필요한 화면(UI)과 코드만 제공합니다.
- 실제 입력 데이터 처리는 사용자의 브라우저(로컬 환경)에서 수행됩니다.
- 텍스트 비식별화, 구조화, 엑셀 생성 과정은 모두 브라우저 내부에서 실행됩니다.
- 입력한 원문 텍스트와 처리 결과는 서버로 전송되거나 저장되지 않습니다.

### 사용 시 주의사항
- 자동 비식별화는 입력 형식과 내용에 따라 일부 정보를 완전히 제거하지 못할 수 있습니다.
- 민감정보가 포함된 자유서술 텍스트는 사용 전 직접 확인해 주세요.
- 실환자 데이터 입력 시에는 소속 기관의 규정 및 내부 지침을 먼저 확인해 주세요.
- 본 도구는 의료적 판단이나 기관의 보안 절차를 대체하지 않습니다.
"""

st.set_page_config(
    page_title="Clean Text",
    page_icon="🧼",
    layout="centered"
)

# --- Disclaimer ---
if not st.session_state.get("accepted"):
    st.markdown("## 🧼 Clean Text")
    st.markdown("##### 의료 텍스트 정리 및 구조화 도구")
    st.divider()

    st.info("서울 서버 앱으로 이동하기 전에 데이터 처리 방식을 확인해 주세요.")

    with st.expander("안내 및 주의사항 보기", expanded=True):
        st.markdown(DISCLAIMER_TEXT)

    st.divider()

    agreed = st.checkbox(
        "앱 코드는 서울 서버에서 제공되지만, 실제 입력 데이터 처리는 내 브라우저(로컬 환경)에서만 수행된다는 점과 자동 비식별화의 한계를 확인했습니다.",
        key="disclaimer_checked",
    )

    col1, col2 = st.columns([2, 1])
    with col1:
        st.caption("체크 후 아래 버튼을 누르면 서울 서버 앱으로 이동합니다.")
    with col2:
        if st.button(
            "확인 후 이동 →",
            type="primary",
            use_container_width=True,
            disabled=not agreed,
        ):
            st.session_state["accepted"] = True
            st.rerun()

# --- Redirect ---
else:
    st.markdown("서울 서버 앱으로 이동 중입니다...")

    components.html(
        f"""
        <script>
            window.parent.location.replace("{SEOUL_APP_URL}");
        </script>
        """,
        height=0
    )

    st.markdown(f"자동으로 이동하지 않으면 [여기를 클릭하세요]({SEOUL_APP_URL})")