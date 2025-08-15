# India Quality Factor ETF Optimizer
Stage: 01 - Problem Framing & Scoping

## Problem Statement
The Indian ETF market is crowded with an abundance of commodity and standard index funds. To compete, our new ETF needs a distinct edge. We will achieve this by focusing on the 'Quality' factor and by aggressively lowering operational costs. While our ETF will track the Nifty200 Quality 30 index, a full replication is too expensive and inefficient.

This project will build an optimization model to create a smaller, 20-25 stock portfolio that significantly cuts transaction costs while maintaining minimal tracking error. This cost efficiency is our key advantage, allowing us to stand ahead of very close ETFs and provide a sharper, more attractive vehicle for investors.

***

## Stakeholder & User
* The CIO would be stakeholder, who decides ultimately in totality if the replication strategy is accurate and cheap enough for the product to be launched.
* The portfolio team, who uses the model's daily output (stock list and weights) to manage the live ETF with the superlative end user being a layman retail investor in India.

***

## Useful Answer & Decision
This project delivers an optimization model that produces a descriptive list of stocks and weights.

* **Decision:** Is this portfolio a viable, low-cost representation of the index?
* **Metric:** Annualized Tracking Error < 0.5% to be competitive.
* **Artifact:** A CSV file with NSE tickers and their corresponding weights.

***

## Assumptions & Constraints
The model assumes access to historical NSE data. It must comply with all SEBI regulations and account for the liquidity of the underlying stocks to ensure tradability. Now however we try to mimic the index, the transaction costs won't allow us in absoluteness to beat the index, if we do then it would be by fluke which makes our tracking error a bit on the higher side.

***

## Known Unknowns / Risks
* Real-world trading costs (market impact) may exceed the model's simulations.
* Any change in SEBI regulations during our year might hamper our assumptions, similar to point 1.
* The strategy must adapt to the index's semi-annual rebalancing without incurring high turnover costs.

***

## Lifecycle Mapping
Goal -> Stage -> Deliverable
* Scoping -> This README file.
* Data Prep -> Clean time-series of stock returns.
* Modeling -> Backtest report showing tracking error is < 0.5%.
* Deployment -> Production script for the portfolio management team.

***

## Repo Plan
Folders: `/data/`, `/src/`, `/notebooks/`, `/docs/`. Updates will be managed via review every fortnight.