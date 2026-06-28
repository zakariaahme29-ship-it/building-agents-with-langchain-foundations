import streamlit as st
import asyncio
import time
from langchain.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Nova AI Travel", page_icon="🌌", layout="centered")

# --- 2. CSS متقدم (تصميم زجاجي، نبض، وحركة تفكير) ---
st.markdown("""
<style>
    /* خلفية الفضاء السحيق المتدرجة */
    .stApp {
        background-color: #05050f;
        background-image: 
            radial-gradient(at 10% 20%, rgba(45, 10, 89, 0.4) 0px, transparent 50%),
            radial-gradient(at 90% 80%, rgba(10, 60, 90, 0.5) 0px, transparent 50%);
        background-attachment: fixed;
        color: #e2e8f0;
    }

    /* تصميم العنوان اللامع */
    h1 {
        text-align: center;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
        font-weight: 900;
        letter-spacing: 1px;
    }

    /* رسائل الدردشة - التأثير الزجاجي */
    .stChatMessage {
        background: rgba(20, 25, 45, 0.45) !important;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .stChatMessage:hover {
        transform: translateY(-2px);
        border: 1px solid rgba(79, 172, 254, 0.3);
    }

    /* نبض أيقونة المساعد (Holo-Pulse) */
    @keyframes pulse-ring {
        0% { box-shadow: 0 0 0 0 rgba(79, 172, 254, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(79, 172, 254, 0); }
        100% { box-shadow: 0 0 0 0 rgba(79, 172, 254, 0); }
    }
    [data-testid="chatAvatarIcon-assistant"] {
        animation: pulse-ring 2s infinite cubic-bezier(0.215, 0.61, 0.355, 1);
        border-radius: 50%;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
    }

    /* صندوق إدخال النص */
    .stChatInputContainer {
        background: rgba(15, 20, 35, 0.8) !important;
        border: 1px solid rgba(79, 172, 254, 0.2) !important;
        border-radius: 20px !important;
        backdrop-filter: blur(12px);
    }
    .stChatInputContainer:focus-within {
        border: 1px solid rgba(79, 172, 254, 0.8) !important;
        box-shadow: 0 0 20px rgba(79, 172, 254, 0.15) !important;
    }

    /* تصميم النقاط القافزة للتفكير */
    .thinking-box {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 5px;
        color: #4facfe;
        font-weight: 600;
        font-family: monospace;
        font-size: 1.1em;
    }
    .dot {
        width: 8px; height: 8px;
        background-color: #4facfe;
        border-radius: 50%;
        animation: bounce 1.4s infinite ease-in-out both;
    }
    .dot1 { animation-delay: -0.32s; }
    .dot2 { animation-delay: -0.16s; }
    @keyframes bounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# --- 3. إعداد الوكيل الذكي ---
load_dotenv()

@st.cache_resource
def setup_agent():
    client = MultiServerMCPClient(
        {
            "kiwi-com-flight-search": {
                "transport": "sse",
                "url": "https://mcp.kiwi.com"
            }
        }
    )
    tools = asyncio.run(client.get_tools())
    return create_agent(
        model="gpt-5-nano",
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt="You are a highly advanced AI travel assistant. Help the user plan flights using the Kiwi platform. Be concise and friendly."
    )

agent = setup_agent()

# --- 4. واجهة المستخدم ---
st.title("🌌 Nova AI | Aviation Matrix")
st.markdown("<p style='text-align: center; color: #8b9bb4; margin-bottom: 30px;'>System initialized. Ready for global routing.</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# طباعة الرسائل السابقة
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    # استخدام أيقونة مخصصة للمساعد
    avatar_icon = "🧑‍🚀" if role == "user" else "✨"
    with st.chat_message(role, avatar=avatar_icon):
        st.markdown(message.content)

# إدخال رسالة جديدة
if prompt := st.chat_input("Where do you want to fly today?"):
    
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar="🧑‍🚀"):
        st.markdown(prompt)

    # إنشاء المربع الذي سيحتوي على حركة التفكير ثم الإجابة
    with st.chat_message("assistant", avatar="✨"):
        message_placeholder = st.empty()
        
        # كود HTML لمؤشر التفكير
        thinking_html = """
        <div class="thinking-box">
            <div class="dot dot1"></div>
            <div class="dot dot2"></div>
            <div class="dot dot3"></div>
            <span style="margin-left: 10px;">Computing flight vectors...</span>
        </div>
        """
        # عرض مؤشر التفكير
        message_placeholder.markdown(thinking_html, unsafe_allow_html=True)
        
        # تشغيل الوكيل في الخلفية
        async def get_response():
            response = await agent.ainvoke(
                {"messages": st.session_state.messages},
                config={"configurable": {"thread_id": "nova_premium_session"}}
            )
            return response["messages"][-1]

        ai_message = asyncio.run(get_response())
        
        # استبدال مؤشر التفكير بالرد الفعلي!
        message_placeholder.markdown(ai_message.content)

    st.session_state.messages.append(ai_message)