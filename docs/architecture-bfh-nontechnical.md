Custom ERP System — Overview for Begal Farm Harvest (BFH)
Date: August 2025
Prepared by: Analytics Business Centre

About This Document
This is a simple, non-technical overview of the new ERP system we are setting up for BFH. It explains what the system does, how the pieces fit together, and what benefits you will see day to day.

1) What the System Does
- Finance: Tracks income, expenses, bank reconciliations, and provides Profit & Loss and Balance Sheet.
- Inventory: Shows stock levels across warehouses, supports stock transfers, and keeps accurate item costs.
- Manufacturing: Plans and tracks feed production and poultry batches, with costs per batch and per bird.
- Sales: Manages customers, quotations, orders, deliveries, and invoices.
- HR & Payroll: Keeps employee records, attendance, leave, and runs payroll with correct calculations.
- Reports & Dashboards: Clear, real-time dashboards with export to Excel/PDF.

2) How the System Is Organized
Think of the system like a set of connected applications working together.

System overview
![System Overview](img/system-overview.png)

- People at BFH use the web screens (on computer, tablet, or phone).
- The application processes your requests and talks to the database.
- A fast service keeps background tasks moving (reminders, alerts, and scheduled jobs).
- The system can connect to other services like SMS, banks, or sensors when needed.

3) Where It Runs
We provide two environments:

- Staging: for testing and sign-off by BFH before going live.
- Production: the live system used every day, with daily backups and monitoring.

Deployment view
![Deployment](img/deployment.png)

4) How Work Moves Through the System
Here is a typical data flow from Sales and Purchasing into stock and the accounts. Everything links automatically, so manual double entry is reduced.

Process flow
![Data Flow](img/data-flow.png)

5) Your Key Records (High-Level)
The system holds master records like Customers, Suppliers, Items, Warehouses, Employees, plus transaction records like Invoices, Orders, and Stock Moves. This keeps reports accurate and consistent.

Data model (simple view)
![Data Model](img/data-model.png)

6) Security and Access
- Secure login with strong password rules; optional two-factor authentication.
- Each person only sees what their role allows (for example: Accountant vs. Warehouse Clerk).
- All activity is logged so we can see who did what and when.
- Backups are encrypted and stored safely.

Security overview
![Security](img/security.png)

7) Getting Data In and Out
- We can import old data from Excel/CSV files.
- The system can send messages (like reminders) via SMS/WhatsApp.
- Reports export to Excel/PDF.

8) Quality and Go-Live
- We test the building blocks and how they work together.
- You test the system in Staging before we go live.
- After go-live, we monitor the system and keep daily backups.

9) Ongoing Support
- We will handle updates, small changes, and add new features as BFH grows.

Appendix: How updates are delivered
![CI/CD](img/ci-cd.png)

10) Project Timeline (Plain Language)
Here is a practical schedule. We keep activities overlapping so we can go live faster. Exact dates will be agreed at kickoff.

Phase | What You’ll See | When
--- | --- | ---
Plan | We map your processes and lock scope | Weeks 1–2
Set Up | Test and live systems, secure access, backups, monitoring | Weeks 2–3
Configure | Finance, Inventory, HR/Payroll, Sales screens and rules | Weeks 3–5
Load Data (Round 1) | We import your masters and opening balances | Weeks 4–6
Tailor & Reports | We adjust forms, approvals, and build key reports | Weeks 5–8
Connect | SMS/WhatsApp, payments/bank (if needed) | Weeks 6–8
Test (UAT) | Your team tests real scenarios, we fix issues | Weeks 8–10
Train | Hands-on training and quick guides | Weeks 9–10
Go Live | Switch to the live system | Week 11
Stabilize | Close support to ensure smooth operations | Weeks 12–13

11) Costing (Simple Budget)
These are ballpark figures in USD; we’ll fine-tune after the planning workshops.

One-time setup (once only)

Item | What’s included | Amount
--- | --- | ---
Planning | Workshops and delivery plan | $2,000
Set Up | Staging/Production, backups, monitoring | $1,500
Configure | Core modules (Finance, Inventory, HR/Payroll, Sales) | $3,000
Data Load | Masters and openings (trial + final) | $2,500
Tailoring & Reports | Forms, approvals, 6 reports/prints | $4,000
Integrations | SMS/WhatsApp, banking/payments (basic) | $1,500
Training | Two role-based sessions + materials | $1,500
Go Live & Support | Cutover and 2 weeks hypercare | $1,500
Contingency | Buffer for unknowns (~10%) | $1,500
Estimated Total (one-time) |  | $19,000

Monthly (recurring)

Item | What’s included | Amount / month
--- | --- | ---
Cloud & Backups | Hosting and encrypted daily backups | $200
Monitoring | Availability and error alerts | $50
Support | Business-hours support and small changes | $300
Estimated Monthly Total |  | $550

Notes
- Third-party charges (SMS credits, payment gateways, bank APIs) are billed by the providers.
- Extra reports/print formats beyond the first six will be quoted.
- On-site visits (if needed) are billed at cost.

