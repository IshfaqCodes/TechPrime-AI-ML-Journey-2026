"""Landing screen shown first when the dashboard opens.

Usage (see src/dashboard.py):
    if not st.session_state.get("entered"):
        render_landing(cfg)   # draws the screen and stops the script until the user clicks Open
"""
import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Manrope:wght@400;500;600&display=swap');

.fd-hero {
    background: #0F1B2D;
    color: #F2F5F9;
    border-radius: 18px;
    padding: 56px 56px 44px 56px;
    margin: 4px 0 28px 0;
    font-family: 'Manrope', system-ui, sans-serif;
}
.fd-hero h1 {
    font-family: 'Bricolage Grotesque', 'Manrope', system-ui, sans-serif;
    font-weight: 800;
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    line-height: 1.05;
    letter-spacing: -0.02em;
    margin: 0 0 18px 0;
    padding: 0;
    max-width: 16ch;
    color: #F2F5F9;
}
.fd-hero p.lead {
    font-size: 1.12rem;
    line-height: 1.6;
    max-width: 56ch;
    margin: 0 0 40px 0;
    color: #B9C4D4;
}

/* the risk scale: the one memorable element */
.fd-scale { position: relative; max-width: 760px; }
.fd-bar { display: flex; height: 18px; border-radius: 9px; overflow: hidden; }
.fd-bar span:nth-child(1) { width: 30%; background: #2F8F6B; }
.fd-bar span:nth-child(2) { width: 40%; background: #E0A526; }
.fd-bar span:nth-child(3) { width: 30%; background: #C8402F; }
.fd-ticks { position: relative; height: 22px; margin-top: 8px; font-size: 0.82rem; color: #8FA0B6; }
.fd-ticks i { position: absolute; font-style: normal; transform: translateX(-50%); }
.fd-marker {
    position: absolute; left: 82%; top: -34px; transform: translateX(-50%);
    background: #F2F5F9; color: #0F1B2D; font-weight: 600; font-size: 0.82rem;
    padding: 4px 10px; border-radius: 6px; white-space: nowrap;
}
.fd-marker:after {
    content: ""; position: absolute; left: 50%; bottom: -5px; margin-left: -5px;
    border: 5px solid transparent; border-top-color: #F2F5F9; border-bottom: 0;
}
.fd-bands { display: flex; gap: 28px; flex-wrap: wrap; margin-top: 14px; font-size: 0.95rem; color: #B9C4D4; }
.fd-bands b { color: #F2F5F9; font-weight: 600; }

.fd-point h3 { font-family: 'Bricolage Grotesque', system-ui, sans-serif; font-size: 1.2rem; margin-bottom: 4px; }
.fd-point p { margin: 0; line-height: 1.55; opacity: 0.85; }

@media (max-width: 640px) { .fd-hero { padding: 36px 24px 30px 24px; } }
</style>
"""

HERO = """
<div class="fd-hero">
  <h1>Catch card fraud before the money moves.</h1>
  <p class="lead">
    Every transaction gets a risk score from 0 to 100, a Low, Medium or High band,
    and a plain list of the factors that pushed it there.
  </p>
  <div class="fd-scale">
    <div class="fd-marker">Example transaction: 82, High</div>
    <div class="fd-bar"><span></span><span></span><span></span></div>
    <div class="fd-ticks"><i style="left:0%">0</i><i style="left:30%">30</i><i style="left:70%">70</i><i style="left:100%">100</i></div>
    <div class="fd-bands">
      <span><b>Low</b> passes through</span>
      <span><b>Medium</b> worth a second look</span>
      <span><b>High</b> flagged for review</span>
    </div>
  </div>
</div>
"""


def _enter():
    st.session_state["entered"] = True


def render_landing(cfg: dict) -> None:
    """Draw the landing screen, then stop the script until the user clicks Open."""
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(HERO, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")
    c1.markdown(
        '<div class="fd-point"><h3>Check the test results</h3>'
        "<p>See how many real fraud cases land in each band on transactions the model never saw.</p></div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        '<div class="fd-point"><h3>Score a transaction</h3>'
        "<p>Load a random legit or fraud case, or type your own values, and get the score instantly.</p></div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        '<div class="fd-point"><h3>See why it was flagged</h3>'
        "<p>Each score comes with the top factors, red for fraud signals and blue for legit ones.</p></div>",
        unsafe_allow_html=True,
    )

    st.write("")
    left, _ = st.columns([1, 3])
    left.button("Open dashboard", type="primary", use_container_width=True, on_click=_enter)
    st.caption(
        f"Current thresholds: Low below {cfg['t_low']:.4f}, High from {cfg['t_high']:.4f} "
        "(fraud probability). You can change them inside the dashboard."
    )
    st.stop()
