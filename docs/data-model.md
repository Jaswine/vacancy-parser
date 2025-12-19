
## Overview

This document describes the canonical data model
used by the system to store and provide
job openings obtained from corporate websites.

Regardless of the structure of the source website, all data
is converted to a uniform format before being saved.

## Description

### Vacancy

Canonical representation of a job vacancy obtained
from a corporate website.

#### Fields

```
- id: UUID
  Unique vacancy identifier

- title: string
  Vacancy title

- company_name: string
  Company

- skills: text
  Skills (Python, Django, Java, Pytest, Grafana)

- location: string | null
  Location is available

- location_status: bool
- Location is specified or not

- salary_from: number | null
- salary_to: number | null
- currency: string | null

- employment_type: enum
  Employment type (full_time, part_time, contract)

- experience_level: enum
  Experience level (junior, middle, senior)

- summary: text
  Vacancy description

- source_url: string
  URL of the job posting

- active_status: bool 
  whether the user has viewed the vacancy

- posted_at: datetime | null
- scraped_at: 
```

## Normalization Rules

- Job titles are converted to plain text without HTML
- ...

## Data Lifecycle

1. The HTML page is loaded by the parser.
2. Raw fields are extracted.
3. The data is transferred to the normalization module.
4. A canonical model is formed.
5. The data is saved in storage.
6. The API returns the data to the client.


