# DCF Stock Valuation Calculator

A comprehensive Python tool for valuing stocks using the Discounted Cash Flow (DCF) method with real-time data from Yahoo Finance.

## Features

- **Real-time Data**: Fetches financial data directly from Yahoo Finance
- **Comprehensive DCF Analysis**: Calculates intrinsic value using free cash flow projections
- **WACC Calculation**: Estimates Weighted Average Cost of Capital
- **Sensitivity Analysis**: Tests different growth rate scenarios
- **User-friendly Interface**: Interactive command-line interface
- **Professional Output**: Formatted analysis with buy/hold/sell recommendations

## Installation

1. Clone or download the files
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the main script for an interactive analysis:

```bash
python dcf_calculator.py
```

Then enter a stock ticker when prompted (e.g., AAPL, MSFT, GOOGL).

### Programmatic Usage

```python
from dcf_calculator import DCFCalculator

# Create calculator instance
calculator = DCFCalculator("AAPL")

# Run DCF analysis
results = calculator.calculate_dcf_value()

# Print formatted results
calculator.print_analysis(results)

# Run sensitivity analysis
run_sensitivity_analysis(calculator)
```

### Example Analysis

```python
# Analyze Apple Inc.
aapl = DCFCalculator("AAPL")
results = aapl.calculate_dcf_value(
    projection_years=10,
    growth_rate=0.10,  # 10% growth rate
    terminal_growth_rate=0.025  # 2.5% terminal growth
)

print(f"Fair Value: ${results['fair_value_per_share']:.2f}")
print(f"Current Price: ${results['current_price']:.2f}")
print(f"Upside/Downside: {results['upside_downside_percent']:+.1f}%")
```

## DCF Methodology

The calculator uses the following approach:

1. **Free Cash Flow Calculation**: FCF = Operating Cash Flow - Capital Expenditures
2. **Growth Rate Estimation**: Based on historical FCF growth rates
3. **WACC Calculation**: Weighted Average Cost of Capital using CAPM
4. **Projection Period**: 10 years of detailed projections
5. **Terminal Value**: Gordon Growth Model for perpetuity
6. **Discounting**: Present value calculation using WACC

## Key Metrics

- **Fair Value**: Intrinsic value per share based on DCF
- **Upside/Downside**: Percentage difference from current price
- **WACC**: Weighted Average Cost of Capital
- **Terminal Value**: Perpetuity value of future cash flows
- **Enterprise Value**: Total value of the company

## Assumptions

- **Risk-free Rate**: 4% (can be adjusted)
- **Market Return**: 10% (can be adjusted)
- **Tax Rate**: 25% (can be adjusted)
- **Terminal Growth**: Capped at 3%
- **Growth Rate**: Between 1% and 20%

## Limitations

- Historical data dependency
- Market volatility impact
- Assumption sensitivity
- Limited to publicly traded companies
- Yahoo Finance data availability

## Example Output

```
============================================================
DCF VALUATION ANALYSIS: AAPL
============================================================

📊 CURRENT METRICS:
Current Price: $150.25
Fair Value: $165.80
Upside/Downside: +10.3%
Recommendation: BUY

💰 VALUATION DETAILS:
Enterprise Value: $2,650,000,000,000
Market Cap: $2,400,000,000,000
Current FCF: $95,000,000,000

📈 ASSUMPTIONS:
Growth Rate: 8.5%
WACC: 9.2%
Terminal Growth: 2.5%

🔮 PROJECTED FCF (Next 5 Years):
Year 1: $103,075,000,000
Year 2: $111,836,375,000
Year 3: $121,343,067,875
Year 4: $131,657,228,045
Year 5: $142,848,091,729
```

## Files

- `dcf_calculator.py`: Main DCF calculator class
- `example_usage.py`: Example usage demonstrations
- `requirements.txt`: Python dependencies
- `README.md`: This documentation

## Contributing

Feel free to fork and improve this calculator. Some potential enhancements:

- Monte Carlo simulation for uncertainty
- Industry-specific adjustments
- More sophisticated WACC calculation
- Integration with other data sources
- Web interface

## Disclaimer

This tool is for educational and research purposes only. Not financial advice. Always consult with financial professionals before making investment decisions.

