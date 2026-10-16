
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Market Basket Analysis")
st.write(
    "Discover products frequently purchased together "
    "using the Apriori algorithm."
)

folder = Path(__file__).parent

try:
    frequent_items = pd.read_csv(folder / "frequent_itemsets.csv")
    rules = pd.read_csv(folder / "association_rules.csv")

    col1, col2 = st.columns(2)
    col1.metric("Frequent Itemsets", len(frequent_items))
    col2.metric("Association Rules", len(rules))

    st.header("📊 Data Visualizations")

    for filename, title in [
        ("ds graph1.png", "Top 10 Most Purchased Products"),
        ("ds graph2.png", "Top 10 Associations by Lift"),
        ("ds graph3.png", "Association Rule Confidence")
    ]:
        image_path = folder / filename
        if image_path.exists():
            st.subheader(title)
            st.image(str(image_path), use_container_width=True)

    st.header("🔎 Explore Association Rules")

    if "lift" in rules.columns:
        max_lift = max(2.0, float(rules["lift"].max()))
        min_lift = st.slider(
            "Minimum lift",
            min_value=1.0,
            max_value=max_lift,
            value=1.0
        )
        filtered_rules = rules[rules["lift"] >= min_lift]
        st.dataframe(filtered_rules, use_container_width=True)
    else:
        st.dataframe(rules, use_container_width=True)

    st.header("📦 Frequent Itemsets")
    st.dataframe(frequent_items, use_container_width=True)

    st.header("💡 Conclusion")
    st.write(
        "The Apriori algorithm identified associations between "
        "products purchased in the same transactions. Retailers can "
        "use these patterns for product recommendations, bundle offers, "
        "and store planning. Association does not prove causation."
    )

except FileNotFoundError:
    st.error(
        "Could not find the required CSV files. Make sure both CSV files "
        "are in the same folder as app.py."
    )
