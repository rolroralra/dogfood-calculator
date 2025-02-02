import streamlit as st
import requests
import os
import webbrowser

# 🔹 Load environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = "http://localhost:8501"  # Streamlit's default port
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# 🔹 Streamlit UI
st.title("카카오톡 나에게 메시지 보내기")

# 1️⃣ 🔥 Open Kakao Login URL in browser
auth_url = f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=talk_message"

if st.button("카카오 로그인"):
    webbrowser.open(auth_url)  # Open login page

# 2️⃣ 🔥 Get Authorization Code from Query Params
query_params = st.query_params
auth_code = query_params.get("code", None)

if auth_code:
    st.success(f"인가 코드: {auth_code}")

    # 3️⃣ 🔥 Request Access Token
    token_url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(token_url, data=data)
    tokens = response.json()

    if "access_token" in tokens:
        access_token = tokens["access_token"]
        st.success(f"Access Token: {access_token}")

        # 4️⃣ 🔥 Async function to send KakaoTalk Message
        async def send_message():
            async with httpx.AsyncClient() as client:
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/x-www-form-urlencoded"
                }

                data = {
                    "template_object": '''{
                        "object_type": "text",
                        "text": "Hello, 카카오톡!",
                        "link": {"web_url": "https://developers.kakao.com"}
                    }'''
                }

                message_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
                response = await client.post(message_url, headers=headers, data=data)

                if response.status_code == 200:
                    st.success("✅ 메시지 전송 성공!")
                else:
                    st.error(f"❌ 메시지 전송 실패: {response.json()}")

        if st.button("카톡 보내기"):
            st.info("📨 메시지를 보내는 중...")
            asyncio.run(send_message())

else:
    st.warning("로그인 후, 인가 코드가 필요합니다.")
