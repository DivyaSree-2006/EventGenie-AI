import streamlit as st
import base64

# PAGE CONFIG
st.set_page_config(
    page_title="EventGenie AI",
    layout="wide"
)

# LOAD LOCAL BACKGROUND IMAGE
with open("background.jpg", "rb") as img:
    bg = base64.b64encode(img.read()).decode()

# CSS
st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
background:
linear-gradient(rgba(255,255,255,0.12), rgba(255,255,255,0.12)),
url("data:image/jpg;base64,{bg}");

background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

section.main {{
background: transparent;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

.block-container {{
padding-top: 2rem;
max-width: 1200px;
}}

h1,h2,h3,p {{
color:white;
text-align:center;
}}

.hero-title {{
font-size:72px;
font-weight:800;
letter-spacing:1px;
font-family: "Segoe UI", Arial, sans-serif;
color:#dffcff;
text-align:center;
text-shadow:
0 0 8px rgba(0,255,255,.55),
0 0 18px rgba(0,255,255,.35);
margin-bottom:8px;
}}

.hero-sub {{
font-size:30px;
font-weight:500;
font-family:"Segoe UI", Arial, sans-serif;
color:white;
text-align:center;
text-shadow:
0 2px 8px rgba(0,0,0,.35);
margin-bottom:40px;
}}


.button-row{{
display:flex;
justify-content:center;
align-items:center;
gap:45px;
width:100%;
margin-top:35px;
margin-bottom:35px;
}}

.hero{{
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
text-align:center;

width:100%;

margin-top:30px;
margin-bottom:35px;
}}

.hero-title{{
font-size:72px;
font-weight:800;
color:#bffcff;

text-shadow:
0 0 12px #00ffff,
0 0 30px rgba(0,255,255,.35);

margin-bottom:12px;
}}

.hero-sub{{
font-size:34px;
font-weight:500;
color:white;

text-shadow:
0 2px 10px rgba(0,0,0,.35);

margin-bottom:35px;
}}

.btn{{
display:inline-block;
padding:32px 85px;     
min-width:380px;       
font-size:50px;        
font-weight:700;
border-radius:24px;
margin:0 18px;
color:white;
background:linear-gradient(
90deg,
rgba(70,80,255,.85),
rgba(190,60,220,.85)
);
border:2px solid rgba(255,255,255,.35);
box-shadow:
0 0 20px rgba(0,255,255,.25),
0 0 35px rgba(255,0,255,.18);
}}

.btn1 {{
background:linear-gradient(90deg,#5a63ff,#a33bbd);
}}

.btn2 {{
background:linear-gradient(90deg,#4a5dff,#7b46ff);
}}

.btn3 {{
background:linear-gradient(90deg,#ff7c5a,#b13bd3);
}}

 /* -----------------------
 AI INPUT
----------------------- */
.stTextInput > div > div > input {{
background:rgba(120,90,255,.28);
border:2px solid rgba(0,255,255,.6);
border-radius:34px;
font-size:30px;
font-weight:500;
font-family:"Segoe UI", Arial, sans-serif;
color:white;
padding:22px 32px;
box-shadow:
0 0 14px rgba(0,255,255,.35),
0 0 28px rgba(255,0,255,.18);
}}

.panel{{
max-width:900px;
margin:35px auto;
text-align:center;
background:rgba(255,255,255,0.18);
backdrop-filter:blur(18px);
-webkit-backdrop-filter:blur(18px);

border:1.5px solid rgba(255,255,255,0.35);
border-radius:30px;
padding:35px 50px;

box-shadow:
0 8px 40px rgba(0,0,0,.18),
0 0 30px rgba(255,255,255,.08);
}}

.section-title {{
font-size:42px;
font-weight:bold;
margin-bottom:15px;
}}

.item {{
font-size:26px;
line-height:1.8;
margin:3px 0;
}}

.schedule-item {{
font-size:26px;
line-height:1.7;
margin:2px 0;
}}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
   <div class="hero-title">🎉 EventGenie AI</div>
   <div class="hero-sub">  Your Smart Companion for Every Event ✨</div>
</div>
""", unsafe_allow_html=True)

# BUTTONS CENTERED
st.markdown("""
<div class="button-row">
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns([1.4,2,2,2,1.4])
with c2:
    suggest = st.button("🎯 Suggest Events", use_container_width=True)
with c3:
    schedule = st.button("🗓 Today's Schedule", use_container_width=True)
with c4:
    miss = st.button("🔥 Don't Miss", use_container_width=True)

# SEARCH BOX
user_input = st.text_input(
"",
placeholder="🔍 Ask anything about the event..."
)

# FEATURE 1
if suggest:
    st.markdown("""
    <div class='panel'>
    <div class='section-title'>
    🎯 Suggested Events For You
    </div>
    <div class='item'>AI/ML Workshop</div>
    <div class='item'>Hackathon Challenge</div>
    <div class='item'>Startup Pitch Competition</div>
    <div class='item'>Robotics Demo</div>
    <div class='item'>Cybersecurity Seminar</div>
    </div>
    """, unsafe_allow_html=True)

# FEATURE 2
if schedule:
    st.markdown("""
    <div class='panel'>
    <div class='section-title'>
    🗓 Today's Schedule
    </div>
    <div class='schedule-item'>9:00 AM — Opening Ceremony</div>
    <div class='schedule-item'>11:00 AM — AI Workshop</div>
    <div class='schedule-item'>1:00 PM — Startup Pitch</div>
    <div class='schedule-item'>3:00 PM — Robotics Demo</div>
    <div class='schedule-item'>5:00 PM — Closing Session</div>
    </div>
    """, unsafe_allow_html=True)

# FEATURE 3
if miss:
    st.markdown("""
    <div class='panel'>
    <div class='section-title'>
    🔥 Don't Miss
    </div>
    <div class='item'>Keynote by Industry Expert</div>
    <div class='item'>AI Startup Networking</div>
    <div class='item'>Prize Distribution</div>
    </div>
    """, unsafe_allow_html=True)

# AI ASSISTANT 
if user_input:
    if "techfest" in user_input.lower():
        st.markdown("""
<div class='panel'>
<div class='section-title'>
🤖 EventGenie AI
</div>
<div class='item'>
TechFest 2026 is a technology event featuring AI, hackathons,
startup pitches, workshops, demos and keynote speakers.
</div>
</div>
""", unsafe_allow_html=True)

# EVENT DETAILS
st.markdown("""
<div class='panel'>
<div class='section-title'>
📍 Event Details
</div>
<div class='item'>🏛 TechFest 2026</div>
<div class='item'>📌 Main Auditorium</div>
<div class='item'>⏰ 9 AM – 6 PM</div>
</div>
""", unsafe_allow_html=True)