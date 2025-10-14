"""
Example usage of the DCF Calculator
"""

from dcf_calculator import DCFCalculator

def example_analysis():
    """Example of how to use the DCF calculator programmatically."""
    
    # Example 1: Apple Inc.
    print("🍎 Analyzing Apple Inc. (AAPL)")
    print("-" * 40)
    
    try:
        aapl = DCFCalculator("AAPL")
        results = aapl.calculate_dcf_value()
        aapl.print_analysis(results)
    except Exception as e:
        print(f"Error analyzing AAPL: {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 2: Microsoft Corporation
    print("🪟 Analyzing Microsoft Corporation (MSFT)")
    print("-" * 40)
    
    try:
        msft = DCFCalculator("MSFT")
        results = msft.calculate_dcf_value()
        msft.print_analysis(results)
    except Exception as e:
        print(f"Error analyzing MSFT: {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 3: Custom growth rate analysis
    print("🔍 Custom Growth Rate Analysis for GOOGL")
    print("-" * 40)
    
    try:
        googl = DCFCalculator("GOOGL")
        
        # Test different growth rates
        growth_rates = [0.08, 0.10, 0.12, 0.15]
        
        print(f"{'Growth Rate':<12} {'Fair Value':<12} {'Current Price':<15} {'Recommendation':<12}")
        print("-" * 60)
        
        for growth_rate in growth_rates:
            results = googl.calculate_dcf_value(growth_rate=growth_rate)
            if "error" not in results:
                print(f"{growth_rate:<12.1%} ${results['fair_value_per_share']:<11.2f} "
                      f"${results['current_price']:<14.2f} {results['recommendation']:<12}")
        
    except Exception as e:
        print(f"Error analyzing GOOGL: {e}")

if __name__ == "__main__":
    example_analysis()

