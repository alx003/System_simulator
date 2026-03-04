
import streamlit as st
import plotly.graph_objects as go

# --- 1. 页面高级配置与样式 ---
st.set_page_config(page_title="System Logic Simulator", layout="wide")

st.markdown("""
    <style>
    /* 引入高级字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:italic,wght@600&display=swap');
    
    .main { background-color: #fcfcfc; font-family: 'Inter', sans-serif; }
    h1 { font-family: 'Playfair Display', serif; color: #1a1a1a; font-size: 2.8rem !important; margin-bottom: 0px; }
    .subtitle { font-style: italic; color: #666; margin-bottom: 2rem; }
    
    /* 指标卡片样式 */
    .stMetric { background: #ffffff; border-radius: 4px; padding: 15px; border: 1px solid #eaeaea; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    
    /* 精美的引用框 - 提取自你的作文 */
    .quote-box {
        padding: 25px;
        border-left: 3px solid #1a1a1a;
        background: #f9f9f9;
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 20px 0;
        color: #333;
    }
    .quote-author {
        display: block;
        margin-top: 10px;
        font-weight: 600;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 按钮美化 */
    .stButton>button { 
        border-radius: 2px; 
        height: 3.5em; 
        transition: all 0.3s; 
        border: 1px solid #ddd;
        font-weight: 500;
        background-color: white;
    }
    .stButton>button:hover {
        border-color: #1a1a1a;
        color: #1a1a1a;
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 初始化系统状态 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.harmony = 50      
    st.session_state.authenticity = 50 
    st.session_state.stability = 50    
    st.session_state.cost = 10         
    st.session_state.log = []

def make_choice(h, a, s, c, msg, is_resistance=False):
    st.session_state.harmony += h
    st.session_state.authenticity += a
    st.session_state.stability += s
    st.session_state.cost += c
    for attr in ['harmony', 'authenticity', 'stability', 'cost']:
        st.session_state[attr] = max(0, min(100, st.session_state[attr]))
    
    # 修正了你代码中的 prefix 错误，改成了 label
    label = "RESISTANCE" if is_resistance else "COMPLIANCE"
    color = "#d9534f" if is_resistance else "#4b9e5f"
    st.session_state.log.append(f"<div style='color:{color};margin-bottom:8px;font-size:0.85rem;'><b>[{label}]</b> {msg}</div>")
    st.session_state.step += 1

# --- 3. 侧边栏：系统诊断 ---
with st.sidebar:
    st.header("🕵️ System Diagnostics")
    st.markdown('*“Systems shape us by creating paths of least resistance.”* — Allan G. Johnson')
    st.write("---")
    st.metric("Social Harmony", f"{st.session_state.harmony}%")
    st.metric("Personal Authenticity", f"{st.session_state.authenticity}%")
    st.metric("System Stability", f"{st.session_state.stability}%")
    st.metric("Social Cost (Risk)", f"{st.session_state.cost}%")
    st.write("---")
    st.write("**Path Record:**")
    for l in reversed(st.session_state.log):
        st.markdown(l, unsafe_allow_html=True)

# --- 4. 主界面内容 ---
st.markdown("<h1>Unraveling the Knot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>An interactive exploration of systemic patriarchy and its 'paths of least resistance'</p>", unsafe_allow_html=True)

# 场景 1: 中国家庭的显性期待 (引用你的原文)
if st.session_state.step == 0:
    st.subheader("Scenario 1: The Cultural Script")
    st.image('new_year_dinner.png', use_container_width=True)
    st.markdown("""
    <div class='quote-box'>
    “In China, patriarchy often operates through clearly defined gender expectations... My high school teachers always praised girls for being <b>'quiet and careful'</b>, while praising boys for being <b>'decisive.'</b>”
    <span class='quote-author'>— Allison Xu, Essay</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Relative🙎🏻‍♀️: 'Allison, you are getting older. You should focus on finding a stable job near home to support your future family.'")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Follow the script: 'I'll consider it, thank you.'"):
            make_choice(15, -10, 10, -5, "You took the path of least resistance.")
    with c2:
        if st.button("Challenge the script: 'My goals are not limited by gender.'"):
            make_choice(-20, 25, -15, 20, "You created friction in the family system.", True)

# 场景 2: 美国 STEM 实验室 (引用你提到的 "Intense" 评价)
elif st.session_state.step == 1:
    st.subheader("Scenario 2: The 'Progressive' Regulation")
    st.image('lab.png', use_container_width=True)
    st.markdown("""
    <div class='quote-box'>
    “In the US... when I spoke assertively, I felt a subtle shift in tone, raised eyebrows, and joking comments about being <b>too 'intense.'</b> The boundary between confidence and 'too much' felt narrow.”
    <span class='quote-author'>— Allison Xu, Essay</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("A male colleague repeats your idea and gets the credit. You feel the urge to speak up.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Soften your voice to avoid being seen as 'aggressive'."):
            make_choice(10, -20, 10, -10, "You adapted to the 'narrow boundary'.")
    with c2:
        if st.button("Directly claim credit: 'That was the point I just made.'"):
            make_choice(-10, 20, -10, 25, "You felt the 'subtle shift in tone' in the room.", True)

# 场景 3: 社会信号与惩罚 (引用你文中提到的 awkward silence)
elif st.session_state.step == 2:
    st.subheader("Scenario 3: The Social Signal")
    st.image('mentor.png', use_container_width=True)
    st.markdown("""
    <div class='quote-box'>
    “The consequences are diffuse: <b>an awkward silence, a strained smile</b>, or a shift in group dynamics that is difficult to name but easy to feel... these small social signals teach us which behaviors are rewarded.”
    <span class='quote-author'>— Allan G. Johnson / Essay</span>
    </div>
    """, unsafe_allow_html=True)

    st.info("Your mentor praises you for 'never causing trouble' and asks you to handle some administrative tasks for the men in the lab.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Accept the 'Good Girl' role to maintain the smile."):
            make_choice(20, -25, 15, -15, "Compliance rewarded with social comfort.")
    with c2:
        if st.button("Reject: 'I'd rather focus on my research project.'"):
            make_choice(-15, 20, -10, 20, "A strained smile follows. You feel the social cost.", True)

# 场景 4: 大富翁游戏隐喻 (总结性思考)
elif st.session_state.step == 3:
    st.subheader("Scenario 4: The Monopoly Paradox")
    st.image('promo.png', use_container_width=True)
    st.markdown("""
    <div class='quote-box'>
    “No matter how kind the players are, the structure of the game pushes them toward <b>accumulation and domination</b>... asking players to be nicer cannot fundamentally alter the game.”
    <span class='quote-author'>— Allan G. Johnson (Chapter 4)</span>
    </div>
    """, unsafe_allow_html=True)

    st.info("You've reached a leadership position, but to stay there, you must adopt the same aggressive tactics that the system uses to exclude others.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Play the game by its rules to win."):
            make_choice(10, -35, 25, -5, "Strategic compliance. You won the game but reinforced it.")
    with c2:
        if st.button("Propose new rules: Redistribution of power."):
            make_choice(-35, 40, -30, 45, "The system views you as if you 'lost your mind'.", True)

# 最终分析图表与金句总结
else:
    st.header("🏁 Systemic Audit Result")
    
    categories = ['Social Harmony', 'Authenticity', 'System Stability', 'Social Cost']
    values = [st.session_state.harmony, st.session_state.authenticity, 
              st.session_state.stability, st.session_state.cost]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]], 
        theta=categories + [categories[0]],
        fill='toself',
        name='Your Journey',
        line_color='#1a1a1a',
        fillcolor='rgba(26, 26, 26, 0.1)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        margin=dict(l=80, r=80, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class='quote-box' style='background: white; border: 1px solid #eee;'>
    <b>Final Observation:</b><br>
    Your Authenticity score is <b>{st.session_state.authenticity}%</b>. <br><br>
    “If we always carry the system rules within us, then change cannot rely solely on personal intention or geographic relocation. 
    Leaving one cultural context did not mean stepping outside patriarchy; it meant encountering a different version.”
    <span class='quote-author'>— Allison Xu, Concluding Insight</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Restart the System Simulation"):
        st.session_state.step = 0
        st.session_state.harmony = 50
        st.session_state.authenticity = 50
        st.session_state.stability = 50
        st.session_state.cost = 10
        st.session_state.log = []
        st.rerun()
