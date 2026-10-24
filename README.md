# AI MSME Cash Flow Forecaster

A practical demo tool for Indian Micro, Small, and Medium Enterprises (MSMEs) to forecast cash flow using transaction data. Helps founders and finance teams spot shortfalls early and take action on working capital.

## The Problem

Indian MSMEs face high cash flow volatility. Delayed receivables, GST payments, seasonal UPI inflows, and limited access to formal credit create frequent shortfalls. Manual tracking in spreadsheets or basic accounting tools misses predictive insights.

## The Solution

This starter tool analyzes historical bank/UPI transactions and invoices to:
- Compute running cash balances
- Forecast the next 30 days based on average daily patterns
- Flag potential shortfalls below a safety threshold
- Suggest simple actions (e.g., accelerate collections, delay payables, explore short-term working capital)

It is designed as a lightweight Python demo that can be extended with real AI models (LLM categorization, ML forecasting) or integrations (Account Aggregator, GSTN, Tally/Zoho).

## Features

- Sample transaction data mimicking Indian MSME patterns (UPI, invoices, GST)
- Running balance calculation
- Simple moving-average forecast
- Shortfall alerts with actionable recommendations
- Fully commented, easy to extend

## Usage

### Requirements
- Python 3.8+
- No external dependencies (pure stdlib)

### Run the demo
```bash
python cashflow_forecaster.py
```

### Sample Output
The script prints current balance, 30-day forecast summary, and any shortfall warnings with suggestions.

### Customize
Edit the `SAMPLE_TRANSACTIONS` list in the script or extend it to read from CSV (bank statements, UPI exports).

## Roadmap Ideas
- Integrate with Account Aggregator for real bank data
- Add LLM-based transaction categorization (using Indian GST/HSN context)
- GST liability forecasting
- WhatsApp/UPI payment reminder generation
- Working capital estimator (credit limit suggestions)

## Author
Built as a profile showcase for fintech tools targeting Indian MSMEs. Focused on AI cash-flow systems.

## License
MIT
