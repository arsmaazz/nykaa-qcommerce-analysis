# nykaa-qcommerce-analysis
Competitive threat analysis identifying which Nykaa beauty categories are most vulnerable to quick commerce substitution (Blinkit, Zepto). Original dataset of 50 products across 5 categories. Python analysis with composite vulnerability scoring and price competitiveness comparison.

## Business Problem

Nykaa's business model depends on customers returning regularly to purchase 
low-consideration beauty products, creating opportunities to increase basket 
sizes through higher-margin purchases. As Blinkit and Zepto expand their 
beauty assortments with 10-minute delivery, they threaten to shift these 
routine purchase occasions away from Nykaa, potentially reducing repeat 
purchase revenue and weakening long-term customer retention.

This project investigates which beauty categories are most vulnerable to that 
shift by analyzing quick commerce penetration, exposed customer demand, and 
pricing competitiveness across five major product categories.

## Key Finding

While Moisturizers emerged as the most exposed category due to high repeat 
purchase frequency and strong quick commerce presence, Kajal & Eyeliner 
revealed an equally important strategic risk. Despite comparatively lower 
quick commerce penetration, its high SKU concentration indicates that 
penetration alone understates the true competitive threat — Lakmé 9to5 alone 
accounts for 81% of Kajal's exposed customer demand.

## Data Collection

**Original primary dataset — not sourced from Kaggle.**

50 products manually collected across 5 categories from Nykaa, Blinkit, 
and Zepto in July 2026. Products selected from Nykaa bestseller lists ranked 
by review count to capture high-frequency purchase behavior.

**Categories covered:**
- Moisturizers (10 products)
- Face Wash (10 products)
- Kajal & Eyeliner (10 products)
- Shampoo (10 products)
- Lip Care (10 products)

**Data points collected per product:**
- Nykaa MRP, selling price, size, price per unit, rating, review count
- Blinkit availability, size, MRP, selling price, price per unit
- Zepto availability, size, MRP, selling price, price per unit
- Purchase consideration classification (High/Low)

---

## Methodology

**Purchase Consideration Classification**
Products classified as Low consideration (habit/repeat purchase, brand already 
trusted) or High consideration (requires research before purchase). This 
classification determines which products are most vulnerable to quick commerce 
substitution.

**Composite Vulnerability Score**
Three metrics combined into a single score per category:
- Exposed purchase volume (40%) — review count on products available on 
  quick commerce, used as proxy for historical purchase frequency
- Quick commerce penetration (35%) — % of Low consideration products 
  available on Blinkit or Zepto
- Demand concentration (25%) — % of exposed reviews concentrated in the 
  top single SKU

**Limitations**
- Review count measures cumulative historical purchases, not current velocity
- Dataset covers top 10 bestsellers per category only — findings are 
  directional, not definitive
- No data on offline availability — products with strong offline presence 
  may overstate Nykaa-specific threat
- Prices and availability verified July 2026 — subject to change

---

## Key Results

| Category | Vulnerability Score | Blinkit Penetration | Nykaa Cheaper |
|---|---|---|---|
| Moisturizers | 89.4 | 80% | 37.5% of products |
| Shampoo | 77.3 | 60% | 16.7% of products |
| Kajal & Eyeliner | 71.8 | 40% | 50.0% of products |
| Face Wash | 56.4 | 60% | 66.7% of products |
| Lip Care | 30.2 | 40% | 25.0% of products |

---

## Recommendations

1. **Private label acceleration** — Prioritize Nykaa-branded alternatives 
   in Moisturizers and Face Wash. Private label products remain exclusive 
   to Nykaa, creating demand that quick commerce cannot replicate.

2. **SKU-level defense in Kajal** — Lakmé 9to5 accounts for 81% of Kajal's 
   exposed demand. Negotiate exclusive launch windows or bundle with 
   Nykaa-exclusive products to create switching friction on the single 
   highest-risk SKU.

3. **Subscription model for habit categories** — Introduce auto-replenishment 
   subscriptions for Moisturizers and Face Wash. Securing repeat purchases 
   before customers consider alternatives eliminates the convenience advantage 
   quick commerce holds.

---

## Tools Used

- **Python** — Pandas, Matplotlib, OpenPyXL
- **Data collection** — Manual research across Nykaa, Blinkit, Zepto
- **Excel** — Dataset construction and maintenance

---

## Author

Mohammed Maaz  
BE in AI & ML, Shetty Institute of Technology (VTU) 2026  
[LinkedIn](https://linkedin.com/in/mohammed-maazz-6-69-ars/) | 
[GitHub](https://github.com/Maaz18)

Data collected and analysis conducted: July 2026
