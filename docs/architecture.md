
## Overview

The system is implemented as a modular monolith and consists
of logically isolated modules, each of which is responsible 
for its own area of responsibility.

Interaction between modules is carried out through
explicit interfaces and imported classes, without network interaction.

## Description

### API Module

**Responsibility**
- Processing HTTP requests
- Validating input data
- Generating API responses

**Depends on**
- Parsing Module (parser)

**Does NOT**
- Does not contain parsing logic

### Parsing Module

**Responsibility**
- Loading HTML pages
- Extracting job vacancies
- Working with DOM / selectors
- Converting data to a single model
- Cleaning and normalizing values
- Converting currencies, dates, locations

**Public Interface**
- `parse_site(url)`
- `parse_vacancy_page(html)`

**Does NOT**
- Doesn't work with HTTP API

## Project Structure

```
vacancy-parser/
├── alembic/                  # Database
│   ├── versions/             # Migrations
│   ├── env.py
│   └── script.py.mako
├── src/
│   ├── api/                  # API
│   │   ├── exceptions/       # Exceptions
│   │   ├── routes/           # Routes
│   │   ├── schemas/          # Schemas
│   │   ├── services/         # Services
│   │   ├── utils/            # Utils
│   │   └── main.py
│   ├── core/                 # Main 
│   │   ├── configs/          # Settings
│   │   ├── db/               # Database
│   │   ├── repositories/     # Repositories
│   │   ├── schemas/          # Schemas
│   │   ├── services/         # Services
│   │   └── utils/            # Utils
│   └── parser/               # Parser
│       ├── services/         # Services
│       ├── utils/            # Utils
│       └── main.py
├── tests/
│   └── main.py 
...
```

## Module Dependencies

- API Module (api) → Parsing Module (parser)
- Parsing Module (parser) → Core

## Why Modular Monolith

At the current stage, the project has been implemented as a modular monolith
to simplify development and reduce infrastructure complexity.

The architecture allows for further separation of modules
into separate services without changing their internal logic.


