
## Overview

The service is designed for automated parsing of job vacancies provided in the form of URLs.

## Description

Most job openings are posted directly on company websites.
Collecting such data manually or through custom scripts requires
considerable time and does not scale well.

This service solves the problem of mass collection of job openings
from corporate websites without manual configuration for each source.

## Data Flow

1. The user submits a list of job sites
2. The system analyzes the page structure
3. The parser extracts job listings and related data
4. The data is normalized to a single model
5. The results are saved and made available via API

## Capabilities

- Parsing job vacancies from arbitrary websites
- Support for different page structures (cards, lists, pagination)
- Automatic data normalization
- Duplicate detection and filtering

## Non-Goals

- The service is not intended for parsing closed platforms (LinkedIn, hh)
- Does not bypass CAPTCHA and protections
- Does not guarantee 100% success for all sites

## Assumptions & Limitations

- Websites must be publicly accessible
- Job pages must not require authorization
- The structure of the website may change over time
