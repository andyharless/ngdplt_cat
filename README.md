# ngdplt_cat
Chia Asset Token for US Nominal GDP

### The Greypaper

NOTE: Since USDS turns out not to be a reliable proxy for USD, I will be pricing peg offers in XCH instead, using a point-in-time price quote, probably the most recent available quote at the time the advance GDP report is released.

Background
- My preferred monetary policy is Nominal GDP Level Path Targeting at about 5%/year using 2007Q4 as a base
- This would roughly extrapolate NGDP from the 2 decades leading to 2007
- Actual policy targets since 2008 have been much less aggressive, too disinflationary, and ineffective, in part because the weak targets encouraged money hoarding. [To be clear, "too disinflationary" *on average*; obviously recently there has been a lot of dollar inflation, but in my view, it hasn't been enough to make up for the weak US nominal growth since 2008 so as to create a precedent that would discourage future money hoarding.]
- I can't really do anything about US monetary policy, but at least I can model what I would prefer it to be

Purpose of Token
- speculative/hedging vehicle for those with opinions or interest in US GDP
- signal of where US GDP is headed, for planning/policy purposes
- standard of value rooted in productive capacity
- possible target for monetary policy????
- possible anchor for money-like crypto tokens not tied directly to fiat

Defined Value
- Start with $1 in 2007Q4
- Increase NGDPLT value by actual US Nominal GDP growth since then
- Reduce NGDPLT by 5% per year (to give "normal" inflation rate relative to production)
- This is what the value of a dollar would be if the Fed had successfully pursued a 5% nominal GDP path since 2007Q4 and real GDP had followed its actual historical path
- This value is the implicit USD value of 1 NGDPLT. For pegging purposes, values will be calculated from the Advance [GDP](https://www.bea.gov/data/gdp/gross-domestic-product) Estimate when [released](https://www.bea.gov/news/schedule) (e.g., July 27, 2023 for 2023Q2), and after the pegging period (probably 1 week) expires, values will be allowed to float until the next advance report in the subsequent quarter.  (Note that NGDP is Line 1 of Table 3, so [for example](https://www.bea.gov/sites/default/files/2023-07/gdp2q23_adv.pdf) it was $26835.0 billion in the advance report for 2023Q2. The level of NGDP is not usually reported in the headline of a news release, but the table can normally be found under "Full Release and Tables", which should be a link under the "Related Materials" tab of the "News Release" page or in the "Current Release" box of the "Gross Domestic Product" page.)
- ~Use Stably USDS stablecoin as proxy for actual US Dollars~ For pegging purposes, calcuate value of NGDPLT in XCH using the XCHUSD rate reported by [CoinGecko](https://www.coingecko.com/en/coins/chia) as of the time the Advance GDP Report is released.
- INGDP (Inverse NGDP token) value defined so that 1 INGDP and 1 NGDPLT have a combined value of $2 ~USDS~ [based on XCHUSD exchange rate applied] ~USDS~
- NGDPLT value calculated as of 2021Q4:
```
2007Q4 NGDP = $14715 billion (base)
2021Q4 NGDP = $23992 billion (current)
Inflation factor = 1.05 per year
Number of years = 14
Target price = (23992/14715)/(1.05^14) = 0.8235 USDS
```
- [Python script to calculate target value in XCH](calc_price.py)

Why both NGDPLT and INGDP?
- enables speculation/hedging in both directions without requiring short sales
- enables issuer to remain neutral (or to choose an orientation on the bullish/bearish spectrum rather than being implicitly always bearish, as would be the case with only the NGDPLT token)
- facilitates initial distribution of tokens by providing a ~USDS~ dollar-linked anchor against which to measure issuing offer prices for matched pairs


How to Enforce Value
- During the week after quarterly GDP report, keep standing buy/sell offers
- Eventually, hopefully, this could be done with oracles and smartcoins

Optionality
- Holder has option to sell at a set price during the peg week or hold
- This option involves risk for the issuer
- Ultimately, like any option, it should be priced, with premium reflected in issue price (along with, in the other direction, time value of wealth)

Bias
- If (likely given Fed's target) NGDP rises less that 5%/year in the long run, value of NGDPLT will predictably go down, and value of INGDP will go up. [This is less clear now, as of 2023. It's possible that the inflation rate will be higher than 2% going forward or that real growth will be as high as 3%, but given slow underlying labor force growth and the Fed's impliict commitment to its inflation target, both of these possibilities still seem unlikely to me, at least in the longer run assuming that the Fed won't explicitly change its inflation target.]
- Maybe ultimately need to offer interest payments on NGDPLT ("staking" in a very rough sense).  If interest rates remain significantly above zero, we should ultimately expect both tokens to earn interest (but with a higher rate on NGDPLT), since the pair can in theory be arbitraged with interest-bearing US dollar instruments.

Avoiding Deflation
- Limit circulation and keep a large uncirculated reserve to credibly avoid exceeding peg price

StellaCoin (STDG, flagship coin for the ecosystem where the NGDPLT token arose)
- partakes of the quantum mechanical joke/money duality that is characteristic of altcoins
- original idea was just "People like dog coins; let's make one."
- Bias for Action: "Let's make this coin. We'll figure out later what to do with it."
- Current idea is to have a loose and variable peg to the NGDPLT token (loose & variable, e.g. like RMB vs $ in recent decades)
- Peg would presumably be revised upward as adoption increases and then stabilize
- Keep a large uncirculated reserve to stabilize value and credibly avoid deflation after wide adoption
- Considering creating a variable-issuance CAT, to be pegged directly to StellaCoin, to enable greater elasticity in use
- Would ultimately require an L2 channel for small transactions, presumably we can piggyback on what gets developed for XCH

Other Associated CATs
- Mostly experimental
- Note that fractional token issuance, even just 1 mojo (which makes it non-fungible) is possible
