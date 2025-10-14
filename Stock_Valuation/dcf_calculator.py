"""
Discounted Cash Flow (DCF) Valuation Calculator

This module provides a comprehensive DCF valuation model for stock analysis.
The DCF method values a company based on its projected future cash flows,
discounted back to present value.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class DCFCalculator:
    
    def __init__(
        self,
        company_name: str,
        current_fcf: float,
        growth_rates: List[float],
        terminal_growth_rate: float,
        discount_rate: float,
        shares_outstanding: float,
        cash: float = 0,
        debt: float = 0
    ):
        self.company_name = company_name
        self.current_fcf = current_fcf
        self.growth_rates = growth_rates
        self.terminal_growth_rate = terminal_growth_rate
        self.discount_rate = discount_rate
        self.shares_outstanding = shares_outstanding
        self.cash = cash
        self.debt = debt
        
        # Results storage
        self.projected_fcf = []
        self.pv_fcf = []
        self.terminal_value = 0
        self.pv_terminal_value = 0
        self.enterprise_value = 0
        self.equity_value = 0
        self.intrinsic_value_per_share = 0
        
    def project_fcf(self) -> List[float]:
        fcf = self.current_fcf
        self.projected_fcf = []
        
        for growth_rate in self.growth_rates:
            fcf = fcf * (1 + growth_rate)
            self.projected_fcf.append(fcf)
        
        return self.projected_fcf
    
    def calculate_terminal_value(self) -> float:
        final_year_fcf = self.projected_fcf[-1]
        self.terminal_value = (
            final_year_fcf * (1 + self.terminal_growth_rate) /
            (self.discount_rate - self.terminal_growth_rate)
        )
        return self.terminal_value
    
    def discount_to_present_value(self) -> Tuple[List[float], float]:
        # Discount projected FCF
        self.pv_fcf = []
        for year, fcf in enumerate(self.projected_fcf, start=1):
            pv = fcf / ((1 + self.discount_rate) ** year)
            self.pv_fcf.append(pv)
        
        # Discount Terminal Value
        years = len(self.growth_rates)
        self.pv_terminal_value = self.terminal_value / ((1 + self.discount_rate) ** years)
        
        return self.pv_fcf, self.pv_terminal_value
    
    def calculate_intrinsic_value(self) -> float:
        # Calculate Enterprise Value
        self.enterprise_value = sum(self.pv_fcf) + self.pv_terminal_value
        
        # Calculate Equity Value
        self.equity_value = self.enterprise_value + self.cash - self.debt
        
        # Calculate Intrinsic Value per Share
        self.intrinsic_value_per_share = self.equity_value / self.shares_outstanding
        
        return self.intrinsic_value_per_share
    
    def run_valuation(self) -> Dict:
        # Step 1: Project FCF
        self.project_fcf()
        
        # Step 2: Calculate Terminal Value
        self.calculate_terminal_value()
        
        # Step 3: Discount to Present Value
        self.discount_to_present_value()
        
        # Step 4: Calculate Intrinsic Value
        self.calculate_intrinsic_value()
        
        return self.get_results()
    
    def get_results(self) -> Dict:
        results = {
            'company_name': self.company_name,
            'assumptions': {
                'current_fcf': self.current_fcf,
                'growth_rates': self.growth_rates,
                'terminal_growth_rate': self.terminal_growth_rate,
                'discount_rate': self.discount_rate,
                'shares_outstanding': self.shares_outstanding,
                'cash': self.cash,
                'debt': self.debt
            },
            'projections': {
                'projected_fcf': self.projected_fcf,
                'pv_fcf': self.pv_fcf
            },
            'terminal_value': {
                'terminal_value': self.terminal_value,
                'pv_terminal_value': self.pv_terminal_value
            },
            'valuation': {
                'enterprise_value': self.enterprise_value,
                'equity_value': self.equity_value,
                'intrinsic_value_per_share': self.intrinsic_value_per_share
            }
        }
        return results
    
    def print_summary(self):
        results = self.get_results()
        
        print(f"\n{'='*70}")
        print(f"DCF VALUATION SUMMARY: {self.company_name}")
        print(f"{'='*70}\n")
        
        print("ASSUMPTIONS:")
        print(f"  Current Free Cash Flow: ${self.current_fcf:,.2f}M")
        print(f"  Discount Rate (WACC): {self.discount_rate*100:.2f}%")
        print(f"  Terminal Growth Rate: {self.terminal_growth_rate*100:.2f}%")
        print(f"  Shares Outstanding: {self.shares_outstanding:,.2f}M")
        print(f"  Cash: ${self.cash:,.2f}M")
        print(f"  Debt: ${self.debt:,.2f}M")
        
        print("\n" + "-"*70)
        print("PROJECTED FREE CASH FLOWS:")
        print("-"*70)
        print(f"{'Year':<10}{'Growth Rate':<15}{'FCF ($M)':<20}{'PV of FCF ($M)':<20}")
        print("-"*70)
        
        for i, (growth, fcf, pv) in enumerate(zip(self.growth_rates, self.projected_fcf, self.pv_fcf), start=1):
            print(f"{i:<10}{growth*100:>6.2f}%{fcf:>20,.2f}{pv:>23,.2f}")
        
        print("\n" + "-"*70)
        print("TERMINAL VALUE:")
        print("-"*70)
        print(f"  Terminal Value: ${self.terminal_value:,.2f}M")
        print(f"  PV of Terminal Value: ${self.pv_terminal_value:,.2f}M")
        
        print("\n" + "-"*70)
        print("VALUATION RESULTS:")
        print("-"*70)
        print(f"  Sum of PV of FCF: ${sum(self.pv_fcf):,.2f}M")
        print(f"  PV of Terminal Value: ${self.pv_terminal_value:,.2f}M")
        print(f"  Enterprise Value: ${self.enterprise_value:,.2f}M")
        print(f"  Plus: Cash: ${self.cash:,.2f}M")
        print(f"  Less: Debt: ${self.debt:,.2f}M")
        print(f"  Equity Value: ${self.equity_value:,.2f}M")
        print(f"\n  {'*'*50}")
        print(f"  INTRINSIC VALUE PER SHARE: ${self.intrinsic_value_per_share:,.2f}")
        print(f"  {'*'*50}\n")
        
        print(f"{'='*70}\n")
    
    def sensitivity_analysis(
        self,
        discount_range: Tuple[float, float] = (0.08, 0.14),
        terminal_range: Tuple[float, float] = (0.02, 0.04),
        steps: int = 5
    ) -> pd.DataFrame:
        discount_rates = np.linspace(discount_range[0], discount_range[1], steps)
        terminal_rates = np.linspace(terminal_range[0], terminal_range[1], steps)
        
        results = []
        
        for dr in discount_rates:
            for tr in terminal_rates:
                # Create temporary calculator with new rates
                temp_calc = DCFCalculator(
                    company_name=self.company_name,
                    current_fcf=self.current_fcf,
                    growth_rates=self.growth_rates,
                    terminal_growth_rate=tr,
                    discount_rate=dr,
                    shares_outstanding=self.shares_outstanding,
                    cash=self.cash,
                    debt=self.debt
                )
                temp_calc.run_valuation()
                
                results.append({
                    'Discount Rate': f"{dr*100:.1f}%",
                    'Terminal Growth': f"{tr*100:.1f}%",
                    'Intrinsic Value': f"${temp_calc.intrinsic_value_per_share:.2f}"
                })
        
        df = pd.DataFrame(results)
        pivot = df.pivot(index='Terminal Growth', columns='Discount Rate', values='Intrinsic Value')
        
        return pivot


def example_valuation():
    print("\n" + "="*70)
    print("EXAMPLE: DCF VALUATION OF TECH COMPANY XYZ")
    print("="*70)
    
    # Create DCF calculator with example data
    dcf = DCFCalculator(
        company_name="Tech Company XYZ",
        current_fcf=1000,  # $1,000M current FCF
        growth_rates=[0.15, 0.12, 0.10, 0.08, 0.06],  # Declining growth over 5 years
        terminal_growth_rate=0.025,  # 2.5% perpetual growth
        discount_rate=0.10,  # 10% WACC
        shares_outstanding=500,  # 500M shares
        cash=2000,  # $2,000M cash
        debt=1500   # $1,500M debt
    )
    
    # Run the valuation
    dcf.run_valuation()
    
    # Print summary
    dcf.print_summary()
    
    # Perform sensitivity analysis
    print("\nSENSITIVITY ANALYSIS:")
    print("="*70)
    sensitivity = dcf.sensitivity_analysis()
    print(sensitivity)
    print("\n")
    
    return dcf


if __name__ == "__main__":
    # Run example valuation
    example_valuation()

