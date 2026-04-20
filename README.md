# acc102-roe-analysis-to
# ACC102 Track4: Listed Company ROE Comparison Tool
## 1. Problem & Target User
This tool helps business students and retail investors quickly compare the ROE (Return on Equity) and revenue trends of Apple and Microsoft, solving the pain point of manually sorting and visualizing financial data.

## 2. Data Source
- Source: Sample financial data of Apple and Microsoft (2020-2023)
- Access date: 2026-04-20
- Key fields: company name, year, ROE, revenue

## 3. Methods (Core Python Steps)
1. Load and read CSV data using pandas
2. Filter data based on user selection (company and year)
3. Calculate average ROE for key insights
4. Create interactive line and bar charts using plotly
5. Build user interface using Streamlit

## 4. Key Findings
- Microsoft has a higher average ROE than Apple from 2020 to 2023, staying above 35%
- Both companies' revenue grew steadily from 2020 to 2022, with a slight decline in 2023
- Apple's ROE showed a steady upward trend from 2020 to 2022

## 5. How to Run Locally
1. Clone this repository to your computer
2. Open the command line and enter the project folder
3. Install dependencies: `pip install streamlit pandas numpy plotly openpyxl`
4. Run the app: `streamlit run app.py`
5. View the tool in your browser

## 6. Demo Video Link
你的演示视频链接

## 7. Limitations & Next Steps
- Limitations: Only covers two companies, data is sample data, no real-time update
- Next steps: Add more companies, use real Yahoo Finance data, add more financial indicators
