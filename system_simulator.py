import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="System Logic Simulator", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:italic,wght@600&display=swap');
    
    .main { background-color: #fcfcfc; font-family: 'Inter', sans-serif; }
    h1 { font-family: 'Playfair Display', serif; color: #1a1a1a; font-size: 3rem !important; }
    .stMetric { background: rgba(255, 255, 255, 0.8); border-radius: 10px; padding: 15px; border: 1px solid #eee; }
    
    .quote-box {
        padding: 20px;
        border-left: 5px solid #1a1a1a;
        background: #f7f7f7;
        font-style: italic;
        margin: 20px 0;
        color: #444;
    }

    /* 阻力路径动画 */
    @keyframes resistance-pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(255, 75, 75, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }
    }
    .resistance-btn { animation: resistance-pulse 2s infinite; }
    
    .stButton>button { 
        border-radius: 2px; 
        height: 3.5em; 
        transition: all 0.3s; 
        border: 1px solid #ddd;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)


# initial state
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
    st.session_state.risk += c
    for attr in ['harmony', 'authenticity', 'stability', 'cost']:
        st.session_state[attr] = max(0, min(100, st.session_state[attr]))
    
    label = "RESISTANCE" if is_resistance else "COMPLIANCE"
    color = "red" if is_resistance else "green"
    st.session_state.log.append(f"<div style='color:{color};margin-bottom:10px;'><b>{prefix}</b> {msg}</div>")
    st.session_state.step += 1

st.title("🤓The Systemic Logic Simulator: Unraveling the Knot")
st.write("---")

with st.sidebar:
    st.header("🕵️ System Diagnostics")
    st.markdown('*System shape us by creating "paths of least resistance".*')
    st.write("---")
    
    st.metric("Social Harmony", st.session_state.harmony)
    st.metric("Personal Authenticity", st.session_state.authenticity)
    st.metric("System Stability", st.session_state.stability)
    st.metric("Social Cost Score", st.session_state.cost)
    st.write("---")
    st.write("**Simulation Log:**")
    for l in reversed(st.session_state.log):
        st.markdown(l, unsafe_allow_html=True)


# Scene 1: Chinese Family's Explicit expectations
if st.session_state.step == 0:
    st.subheader("Scenario 1: The Chinese New Year Dinner (China)")
    st.image('new_year_dinner.png', caption = 'A traditional Chinese Dinner Table Setting', use_container_width = True)
    st.info("Relative🙎🏻‍♀️: 'Allison, you are getting older. You should focus on finding a stable job near home to support your future family.'")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Smile and nod🙂‍↕️: 'I'll consider it, thank you.'"):
            make_choice(15, -10, 10, -5, "Path of Least Resistance: You maintained the family peace.")
    with c2:
        if st.button("Challenge😬: 'My career goals are not limited by my gender.'"):
            make_choice(-20, 20, -15, 20, "System Friction: Tension rises at the table.", True)

# Scene 2: American Work Environment Implicit bias
elif st.session_state.step == 1:
    st.subheader("Scenario 2: 🖥️The STEM Lab Meeting (USA)")
    st.image('lab.png', caption = 'A STEM Lab Setting', use_container_width = True)
    st.info("A male colleague repeats your idea from 5 minutes ago and the professor praises HIM for it.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("😶Stay silent to avoid being seen as 'aggressive'."):
            make_choice(10, -15, 10, -10, "Passive Acceptance: The system rewards your 'politeness'.")
    with c2:
        if st.button("Interject🤨: 'I'm glad you agree with the point I made earlier.'"):
            make_choice(-10, 15, -10, 15, "Subtle Resistance: You claimed your space.", True)

# Scene 3: Gendered praise
elif st.session_state.step == 2:
    st.subheader("Scenario 3: The 'Good Girl' Trap")    
    st.image('mentor.png', caption = 'A College Mentor Talking to You', use_container_width = True)
    st.info("A mentor says: 'I love how you are so helpful and never cause trouble in the department.'")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("😀Accept the compliment and offer to do more admin work."):
            make_choice(20, -20, 15, -15, "Self-Marginalization: You accepted the 'supportive' role.")
    with c2:
        if st.button("🧐Pivot: 'I'd rather focus on the leading my research project.'"):
            make_choice(-5, 20, -5, 10, "Reframing: You rejected the 'nurturer' label.", True)

# Scene 4: Emotional Labor
elif st.session_state.step == 3:
    st.subheader("Scenario 4: The Group Chat Conflict")
    st.image('emotion_support.png', caption = 'A Group of Friends are Out, and You are the Girl Sitting \
    in the Passenger Seat.', use_container_width = True)
    st.info("Two male friends are arguing. Everyone expects YOU to mediate and calm them down.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🙂Spend an hour mediating to keep the group together."):
            make_choice(15, -25, 10, -10, "Emotional Labor: You sacrificed your energy for the system.")
    with c2:
        if st.button("🙃Stay out of it: 'They are adults, they can fix it.'"):
            make_choice(-15, 15, -10, 5, "Boundary Setting: You refused unpaid emotional labor.", True)

# Scene 5: The Monopoly Paradox
elif st.session_state.step == 4:
    st.subheader("Scenario 5: The Glass Ceiling")
    st.image('promo.png', use_container_width = True)
    st.info("You are offered a promotion, but you're told to 'soften your leadership style' to better fit the culture.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("😶‍🌫️Adapt your personality to get the power."):
            make_choice(10, -30, 20, -5, "Strategic Compliance: You gained power but lost yourself.")
    with c2:
        if st.button("😎Refuse to perform gender: 'Judge me by my results.'"):
            make_choice(-30, 30, -20, 40, "Direct Confrontation: The system pushes back hard.", True)

# final radar plot 
else:
    st.header("🏁 Final Systemic Analysis")
    
    categories = ['Social Harmony', 'Authenticity', 'System Stability', 'Social Cost']
    values = [st.session_state.harmony, st.session_state.authenticity, 
              st.session_state.stability, st.session_state.cost]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]], 
        theta=categories + [categories[0]],
        fill='toself',
        name='Your Path',
        line_color='#1a1a1a',
        fillcolor='rgba(26, 26, 26, 0.2)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title="Your Identity Map within Patriarchy"
    )
    st.plotly_chart(fig, use_container_width = True)
    
    st.write("### Observation:")
    
    if st.session_state.stability > 60:
        st.error("SYSTEM STATUS: STABLE🙂. Your choices reinforced the 'Paths of Least Resistance'. The game of Monopoly continues.")
    else:
        st.warning("SYSTEM STATUS: AGITATED🥴. Your resistance has created friction. The rules are being questioned. But, what's next?")

    if st.button("Restart Simulation"):
        st.session_state.step = 0
        st.session_state.harmony = 50
        st.session_state.authenticity = 50
        st.session_state.stability = 50
        st.session_state.risk = 10
        st.session_state.log = []
        st.rerun()
