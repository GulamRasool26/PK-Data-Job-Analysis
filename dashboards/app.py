import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pakistan vs Global Data Jobs", layout="wide")

st.title("Should a Pakistani Data Professional Go Local or Remote?")
st.caption("Analysis of 43 real Pakistan job postings + 1,344 global survey responses + 49K global salary records")

tab1, tab2, tab3 = st.tabs(["Local Skill Demand", "Global Skill Demand", "Pay & Remote ROI"])

with tab1:
    st.subheader("Pakistan — Skills Required (Rozee/Glassdoor postings, n=43)")
    local_skills = pd.DataFrame({
        "Skill": ["Excel", "SQL", "Python", "Tableau", "Power BI", "Machine Learning", "Statistics"],
        "% of Postings": [35, 35, 26, 19, 19, 14, 14]
    }).sort_values("% of Postings", ascending=True)
    st.bar_chart(local_skills.set_index("Skill"))
    st.info("Excel and SQL are near-universal locally. Big-data tools (Spark, Snowflake) barely register.")

with tab2:
    st.subheader("Global — Skills Used (Stack Overflow 2025, data roles, n=1,344)")
    global_skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "R", "PostgreSQL", "MySQL"],
        "% of Respondents": [68, 56, 18, 39, 23]
    }).sort_values("% of Respondents", ascending=True)
    st.bar_chart(global_skills.set_index("Skill"))
    st.info("Python dominates globally (68%) — a much bigger gap vs SQL than seen in the local market.")

with tab3:
    st.subheader("Median Salary (USD/year) by Experience & Work Mode")
    roi = pd.DataFrame({
        "Level": ["Entry", "Entry", "Mid", "Mid", "Senior", "Senior", "Executive", "Executive"],
        "Mode": ["Onsite", "Remote", "Onsite", "Remote", "Onsite", "Remote", "Onsite", "Remote"],
        "Median USD": [83000, 82000, 118000, 112400, 150000, 150000, 175000, 220000]
    })
    st.dataframe(roi, use_container_width=True)
    st.warning(
        "Remote pay is NOT a discount — it roughly matches onsite globally, and even entry-level "
        "remote pay is 5-10x typical Pakistan entry-level analyst salaries. But this reflects people "
        "already employed remotely — landing that first remote role is the real barrier, not the pay ceiling."
    )

st.divider()
st.subheader("Bottom line")
st.markdown("""
**Local hiring** rewards Excel + SQL fundamentals and moves faster.  
**Global remote** pays dramatically more but demands stronger Python and real competitive access.  

**Practical path:** build local credibility now with SQL/Excel/Power BI, keep deepening Python 
to leave the remote door open long-term.
""")