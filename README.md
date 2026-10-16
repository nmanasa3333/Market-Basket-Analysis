🛒 Market Basket Analysis Using the Apriori Algorithm

 📌 Project Overview

Market Basket Analysis is a data mining technique used to discover relationships between products frequently purchased together. This project analyzes online retail transaction data using the **Apriori algorithm** to identify frequent itemsets and generate association rules.

An interactive dashboard is developed using **Streamlit** to display visualizations and explore association rules based on minimum lift.

 🎯 Objectives

- Analyze online retail transaction data.
- Clean and preprocess the dataset.
- Identify frequently purchased products and product combinations.
- Apply the Apriori algorithm to generate frequent itemsets.
- Generate association rules using support, confidence, and lift.
- Visualize popular products and strong product associations.
- Develop an interactive dashboard for exploring the results.

 📂 Dataset Description

Dataset:Online Retail Dataset

The dataset contains transaction records from a UK-based online retailer.

Important columns include:

- `InvoiceNo` — Transaction or invoice number.
- `StockCode` — Product identification code.
- `Description` — Product name.
- `Quantity` — Quantity purchased.
- `InvoiceDate` — Date and time of the transaction.
- `UnitPrice` — Price per unit.
- `CustomerID` — Customer identification number.
- `Country` — Customer's country.

The original dataset contains 541,909 records and 8 columns.
 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Removed duplicate records.
2. Removed rows with missing product descriptions.
3. Excluded cancelled invoices.
4. Removed records with non-positive quantities or unit prices.
5. Filtered transactions to include the United Kingdom.
6. Grouped products by invoice number to create shopping baskets.

Missing customer IDs were retained because customer identification was not required for the invoice-based basket analysis.

 ⚙️ Technologies Used

- **Python** — Programming language.
- **Pandas** — Data manipulation and preprocessing.
- **mlxtend** — Apriori algorithm and association-rule mining.
- **Matplotlib** — Data visualization.
- **Streamlit** — Interactive dashboard development.
- **Google Colab** — Data analysis and experimentation.

 🔍 Methodology

 1. Frequent Itemset Mining

The Apriori algorithm was applied with a minimum support threshold of 0.02 (2%) to identify frequent product combinations.

 2. Association Rule Generation

Association rules were generated using a minimum confidence threshold of 0.30 (30%).

The rules were sorted by lift and confidence to identify strong product relationships.

 3. Evaluation Metrics

- **Support:** The proportion of transactions containing a product or product combination.
- **Confidence:** The proportion of transactions containing the antecedent that also contain the consequent.
- **Lift:** Measures the strength of an association relative to the expected co-occurrence under independence.

 📊 Visualizations

The project includes three graphs:

1. **Top 10 Most Purchased Products** — Displays frequently occurring products.
2. **Top 10 Associations by Lift** — Highlights strong relationships between products.
3. **Association Rule Confidence** — Compares the confidence values of association rules.

 🖥️ Interactive Dashboard

The Streamlit dashboard provides:

- A summary of the number of frequent itemsets and association rules.
- Three data visualizations.
- An association-rules table.
- A minimum-lift slider for filtering association rules.
- A frequent-itemsets table.
- A project conclusion.

 📈 Sample Finding

One strong association identified in the analysis was:

WOODEN STAR CHRISTMAS SCANDINAVIAN → WOODEN HEART CHRISTMAS SCANDINAVIAN

- Support: Approximately 0.0204 (2.04%).
- Confidence: Approximately 0.7683 (76.83%).
- Lift: Approximately 27.20.

This indicates a strong association between the two products in the analyzed transactions. Retailers could investigate this relationship for product recommendations and bundle offers.

 ▶️ How to Run the Project

 Prerequisites

Install Python on your computer.

Install the required libraries by running:

```bash
python -m pip install streamlit pandas
```

### Project Structure

Keep the following files together in the project directory:

```text
Market_Basket_Analysis/
├── app.py
├── frequent_itemsets.csv
├── association_rules.csv
├── ds graph1.png
├── ds graph2.png
└── ds graph3.png
```

The graph filenames shown above should match the filenames referenced in `app.py`.

 Run the Dashboard

Open Command Prompt in the project directory and run:

```bash
python -m streamlit run app.py
```

The dashboard should open in your browser. If it does not open automatically, visit:

`http://localhost:8501`

💡 Applications

- Product recommendation systems.
- Product bundling and promotional offers.
- Retail inventory and merchandising decisions.
- Understanding customer purchasing patterns.
- Cross-selling strategies.

 ⚠️ Limitations

- The results depend on the selected dataset, preprocessing steps and thresholds.
- The analysis identifies associations, not causal relationships.
- The UK-only filter limits the findings to the selected market.
- Rare product combinations may not be identified because of the minimum support threshold.

 🏁 Conclusion

This project demonstrates how Market Basket Analysis can extract useful purchasing patterns from retail transaction data. The Apriori algorithm identifies frequent itemsets, while association rules measure relationships between products using support, confidence and lift. The Streamlit dashboard makes the results easier to explore and interpret, supporting data-driven retail recommendations and merchandising decisions.

 👩‍💻 Project Type

Academic Data Analytics / Data Mining Project
