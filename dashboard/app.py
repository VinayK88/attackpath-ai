import streamlit as st

st.set_page_config(page_title="AttackPath AI", page_icon="◉", layout="wide", initial_sidebar_state="expanded")
METRICS=[("Synthetic events","936","fixture"),("Alerts","200","fixture"),("Held-out recall","90.2%","fixture"),("Mean detect time","4.0 min","fixture"),("Paths stopped early","100%","fixture"),("Critical paths","12","illustrative"),("Identity pivots","18","illustrative"),("Privilege edges","27","illustrative"),("Graph nodes","143","illustrative"),("Mitigations ranked","16","illustrative"),("Residual blast","0.31","illustrative"),("Auto-remediation","Off","review first")]
SIGNALS=[("Path coverage",.90),("Identity context",.88),("Graph explainability",.94),("Detection timeliness",.86),("Mitigation coverage",.91)]
st.markdown("""<style>html,body,[class*="css"]{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Arial,sans-serif;color:#1d1d1f}.stApp{background:#f5f5f7}[data-testid="stHeader"]{background:transparent}[data-testid="stSidebar"]{background:#fff;border-right:1px solid #e5e5ea}.block-container{max-width:1500px;padding:2rem 2.4rem 4rem}.hero{background:linear-gradient(135deg,#fff,#f7fbff);border:1px solid #e5e5ea;border-radius:32px;padding:38px 42px;margin-bottom:24px;box-shadow:0 14px 36px rgba(0,0,0,.045)}.eyebrow{color:#0071e3;font-size:.78rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase}.hero h1{font-size:3.35rem;letter-spacing:-.052em;margin:.22rem 0 .55rem}.hero p{max-width:900px;color:#6e6e73;font-size:1.12rem;line-height:1.55}.pill{display:inline-block;background:#eef6ff;color:#0066cc;border:1px solid #d8eaff;border-radius:999px;padding:.42rem .78rem;margin:.55rem .35rem 0 0;font-size:.76rem;font-weight:650}[data-testid="stMetric"]{background:#fff;border:1px solid #e5e5ea;border-radius:24px;padding:18px 20px;box-shadow:0 8px 26px rgba(0,0,0,.035);min-height:116px}[data-testid="stMetricLabel"]{color:#6e6e73;font-weight:600}[data-testid="stMetricValue"]{font-size:1.9rem;font-weight:700}.stTabs [data-baseweb="tab"]{background:#fff;border:1px solid #e5e5ea;border-radius:999px;padding:8px 16px}.card{background:#fff;border:1px solid #e5e5ea;border-radius:22px;padding:18px 20px}.note{background:#fff;border:1px solid #e5e5ea;border-radius:18px;padding:14px 18px;color:#6e6e73}</style>""",unsafe_allow_html=True)
with st.sidebar:
    st.markdown("## AttackPath AI"); st.caption("Identity & Agentic Attack Paths"); st.divider(); st.markdown("**Overview**\n\nPath posture\n\nIdentity pivots\n\nMitigations\n\nEvidence"); st.divider(); st.caption("Synthetic attack-path lab")
st.markdown("""<div class="hero"><div class="eyebrow">Identity &amp; Agentic Attack Paths</div><h1>AttackPath AI</h1><p>Detect and explain identity-centric attack paths, rank high-impact pivots, and measure mitigations before they become operational changes.</p><span class="pill">Identity graph</span><span class="pill">Attack paths</span><span class="pill">Risk ranking</span><span class="pill">Mitigation</span></div>""",unsafe_allow_html=True)
for s in range(0,len(METRICS),4):
    cols=st.columns(4)
    for c,(l,v,n) in zip(cols,METRICS[s:s+4]): c.metric(l,v,n)
st.subheader("Attack-path health")
l,r=st.columns([1.15,.85],gap="large")
with l:
    for n,v in SIGNALS: st.progress(v,text=f"{n} · {v:.0%}")
with r: st.markdown('<div class="card"><b>Relationships matter</b><br><br><span style="color:#6e6e73">The system prioritizes reachability, privilege, sequence, and blast radius rather than treating isolated findings as equally important.</span></div>',unsafe_allow_html=True)
t1,t2,t3,t4=st.tabs(["Path posture","Identity pivots","Mitigations","Evidence"])
with t1: st.dataframe([{"Path":"identity → admin role → model store","Risk":.94,"State":"Critical"},{"Path":"device → token → SaaS app","Risk":.86,"State":"High"},{"Path":"service principal → storage","Risk":.72,"State":"Review"}],use_container_width=True,hide_index=True)
with t2: st.dataframe([{"Pivot":"privileged role","Reach":31},{"Pivot":"refresh token","Reach":22},{"Pivot":"service principal","Reach":18}],use_container_width=True,hide_index=True)
with t3:
    for n,v in SIGNALS: st.progress(v,text=n)
with t4: st.info("All events, identities, graph nodes, paths, and KPIs are synthetic or explicitly illustrative. No cloud or identity control is modified.")
st.markdown('<div class="note"><b>Evaluation boundary.</b> Held-out metrics apply to the checked-in synthetic fixture only and are not production efficacy claims.</div>',unsafe_allow_html=True)
