# Duration and Convexity

## Definition
**Duration** and **Convexity** are measures used in fixed income analysis to assess how sensitive a bond’s price is to changes in interest rates.

- **Duration** measures the **average time** it takes to receive the bond’s cash flows (both coupon and principal) and indicates the bond’s **price sensitivity** to interest rate changes.
- **Convexity** measures the **curvature** in the relationship between bond prices and yields — it improves the accuracy of duration-based estimates for large interest rate changes.

---

## Duration

### 1. Macaulay Duration
\[
D_M = \frac{\sum_{t=1}^{n} t \times \frac{CF_t}{(1 + y)^t}}{\sum_{t=1}^{n} \frac{CF_t}{(1 + y)^t}}
\]

- **CFₜ** = Cash flow at time *t*  
- **y** = Yield to maturity (YTM)  
- **n** = Number of periods  

Measures the **weighted average time** to receive cash flows.

---

### 2. Modified Duration
\[
D_{mod} = \frac{D_M}{1 + y}
\]

Estimates the **percentage change in price** for a **1% change in yield**.

\[
\frac{\Delta P}{P} \approx -D_{mod} \times \Delta y
\]

- **ΔP/P** = Approximate percentage price change  
- **Δy** = Change in yield  

---

## Convexity

### Formula
\[
Convexity = \frac{1}{P} \times \sum_{t=1}^{n} \frac{CF_t \times t (t + 1)}{(1 + y)^{t + 2}}
\]

- **P** = Bond price  

Convexity accounts for the **non-linear** relationship between bond prices and yields, refining the duration estimate for larger yield changes.

---

## Combined Price Change Estimate
When interest rates change, both duration and convexity can be used to estimate price change more accurately:

\[
\frac{\Delta P}{P} \approx -D_{mod} \times \Delta y + \frac{1}{2} \times Convexity \times (\Delta y)^2
\]

---

## Key Insights
- **Higher duration** → greater sensitivity to interest rate changes.  
- **Higher convexity** → bond price increases more when yields fall and decreases less when yields rise.  
- **Zero-coupon bonds** have the **highest duration** for a given maturity (since all cash flows occur at maturity).  

---

## Example
A bond has:
- Price = \$1,000  
- Modified Duration = 5  
- Convexity = 40  
- Yield increases by 1% (Δy = 0.01)

\[
\frac{\Delta P}{P} \approx -5(0.01) + \frac{1}{2}(40)(0.01)^2 = -0.05 + 0.002 = -0.048
\]

Price change ≈ **-4.8%**, so the new price ≈ **\$952**.

---