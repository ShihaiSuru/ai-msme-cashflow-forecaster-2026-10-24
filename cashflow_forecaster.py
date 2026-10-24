#!/usr/bin/env python3
"""
AI MSME Cash Flow Forecaster
Starter demo for Indian MSMEs — analyzes sample transactions and forecasts shortfalls.

Practical, dependency-free Python script.
Extend with real data (CSV bank/UPI exports), ML models, or APIs.
"""

from datetime import datetime, timedelta
from collections import defaultdict
import statistics

# Sample transactions mimicking a small Indian trading/manufacturing MSME
# Positive = inflow, Negative = outflow. Dates in YYYY-MM-DD.
SAMPLE_TRANSACTIONS = [
    {"date": "2026-10-01", "amount": 45000, "description": "UPI from customer A - invoice 101"},
    {"date": "2026-10-02", "amount": -12000, "description": "GST payment"},
    {"date": "2026-10-03", "amount": 28000, "description": "UPI from customer B"},
    {"date": "2026-10-05", "amount": -8500, "description": "Supplier payment - raw materials"},
    {"date": "2026-10-07", "amount": 52000, "description": "Invoice 102 settled"},
    {"date": "2026-10-10", "amount": -15000, "description": "Salary advance"},
    {"date": "2026-10-12", "amount": 19000, "description": "UPI partial payment"},
    {"date": "2026-10-15", "amount": -22000, "description": "Rent + utilities"},
    {"date": "2026-10-18", "amount": 61000, "description": "Customer C - bulk order"},
    {"date": "2026-10-20", "amount": -9500, "description": "GST TDS"},
    {"date": "2026-10-22", "amount": 33000, "description": "UPI from regular buyer"},
    {"date": "2026-10-23", "amount": -18000, "description": "Supplier settlement"},
]

SAFETY_THRESHOLD = 20000  # INR — alert if projected balance falls below this
FORECAST_DAYS = 30

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def calculate_daily_net(transactions):
    """Group net cash flow by day."""
    daily = defaultdict(float)
    for tx in transactions:
        daily[parse_date(tx["date"])] += tx["amount"]
    return daily

def get_average_daily_flow(daily_net):
    """Simple average of daily nets for forecasting."""
    if not daily_net:
        return 0
    values = list(daily_net.values())
    return statistics.mean(values)

def forecast_cashflow(transactions, forecast_days=FORECAST_DAYS, threshold=SAFETY_THRESHOLD):
    """Main forecasting logic."""
    daily_net = calculate_daily_net(transactions)
    if not daily_net:
        print("No transactions found.")
        return

    # Current balance: sum of all historical nets
    current_balance = sum(daily_net.values())
    avg_daily = get_average_daily_flow(daily_net)

    print(f"=== AI MSME Cash Flow Forecaster ===")
    print(f"Current estimated balance: ₹{current_balance:,.0f}")
    print(f"Average daily net cash flow: ₹{avg_daily:,.0f}")
    print(f"Forecast horizon: {forecast_days} days")
    print("-" * 40)

    projected = current_balance
    shortfalls = []
    today = max(daily_net.keys()) if daily_net else datetime.now()

    for day in range(1, forecast_days + 1):
        projected += avg_daily
        forecast_date = today + timedelta(days=day)
        if projected < threshold:
            shortfalls.append((forecast_date, projected))

    if shortfalls:
        print("⚠️  Potential shortfalls detected:")
        for date, bal in shortfalls[:5]:  # Show first few
            print(f"  - {date.strftime('%Y-%m-%d')}: projected ₹{bal:,.0f}")
        print("\nRecommended actions:")
        print("  • Accelerate collections on overdue invoices (send UPI payment links)")
        print("  • Delay non-critical supplier payments by 7-15 days")
        print("  • Explore short-term working capital (invoice discounting / NBFC line)")
        print("  • Review GST liability timing to free up cash")
    else:
        print("✅ No shortfalls projected in the next 30 days under current average.")
        print("Consider building a buffer or exploring growth financing.")

    print(f"\nFinal projected balance after {forecast_days} days: ₹{projected:,.0f}")

if __name__ == "__main__":
    forecast_cashflow(SAMPLE_TRANSACTIONS)
