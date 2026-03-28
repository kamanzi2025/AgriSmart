# AgriSmart

A desktop agricultural advisory application for smallholder farmers in East Africa, focused on bean cultivation. Built with Python and Tkinter.

## Features

- **Planting Advisory** — Region-specific bean variety recommendations and planting windows for Season A and Season B
- **Pest Management** — Search-based pest diagnosis with treatment and prevention advice for 6+ common pests
- **Soil Management** — Educational reference on soil fertility, crop rotation, and pH/liming
- **Farm Finance Tracker** — Add revenue/cost transactions per season and view profit/loss summaries

## Project Structure

```
AgriSmart/
├── root/
│   └── main.py                # Application entry point
├── forms/                     # UI layer (Tkinter windows)
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   ├── finance.py
│   ├── pest.py
│   ├── planting.py
│   └── soil.py
├── models/
│   └── __init__.py            # User, FinancialRecord, PestReport, PlantingAdvisory dataclasses
├── services/                  # Business logic
│   ├── auth_service.py
│   ├── financial_service.py
│   ├── pest_service.py
│   └── planting_service.py
└── utils/
    ├── theme.py               # Color palette and fonts
    └── session.py             # Current user session state
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| GUI | Tkinter (Python built-in) |
| Language | Python 3.10+ |
| Data Models | Python dataclasses |
| Authentication | SHA256 password hashing (hashlib) |
| Storage | In-memory (prototype/demo) |

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Tkinter (included with standard Python installations)

### Running the App

```bash
cd AgriSmart
python root/main.py
```

### Demo Accounts

The application is pre-seeded with demo accounts for testing:

| Role | Description |
|------|-------------|
| Farmer | Primary user — accesses all features |
| Extension Officer | Agricultural advisory role |
| Administrator | System administration |

## Supported Regions

| Country | Regions |
|---------|---------|
| Rwanda | Kigali, Huye, Musanze, Rubavu |
| Kenya | Nairobi |
| Uganda | Kampala |
| Tanzania | Dar es Salaam |

Each region has tailored bean variety recommendations and planting windows optimized for the local climate.

## Architecture

The application follows a layered architecture with clear separation of concerns:

- **Forms** — UI windows built with Tkinter
- **Services** — Business logic and in-memory data management
- **Models** — Type-safe dataclasses for all domain objects
- **Utils** — Shared theming and session management

Financial records include an `is_synced` flag designed for future cloud synchronization.

## User Roles

- **Farmer** — Smallholder farmer, primary user
- **Extension Officer** — Agricultural advisory professional
- **Cooperative Leader** — Manages farmer groups
- **Administrator** — System administration
