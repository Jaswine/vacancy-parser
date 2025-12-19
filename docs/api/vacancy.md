
## 📋 Vacancy


### Creating a job parsing task

#### Request

`POST /api/parsing/jobs/`

```json
{
  "filters": {
    "title": "",
    "skills": [],
    "сomplete_skill_match": false,
    "location": "New York",
    "type": "",
    "salary": {
      "salary_range_min":  "",
      "salary_range_max": ""
    }
  },
  "urls": [
    "https://example.com", 
    "https://example.com"
  ]
}
```

#### Response

```json
{
  "job_id": "c1a8f1d4",
  "status": "pending"
}
```


### Checking parsing status

#### Request

`GET /api/parsing/jobs/{job_id}`

#### Response

```json
{
  "status": "completed",
  "progress": 100,        
  "stats": {
    "pages": 10,
    "vacancies_found": 87,
    "errors": 1
  }
}
```


### Getting vacancies

#### Request

`GET /api/vacancies?job_id={job_id}&page={page}&page_size={page_size}`

#### Response

```json
{
  "page": 1,
  "page_size": 10,
  "total_pages": 15,
  "total_items": 150,
  "data": [
    {
      "id": "1",
      "title": "Middle Backend Developer",
      "company_name": "ACME",
      "skills": ["Python", "Django"],
      "location": {
        "location": "New York",
        "status": true 
      },
      "salary": {
        "salary_from": 2000,
        "salary_to": 3000,
        "currency": "USD"
      },
      "employment_type": "full_time",
      "experience_level": "Middle",
      "summary": "....",
      "source_url": "https://example.com",
      "active_status": "Watched",
      "posted_at": "2025-12-19T12:00:00Z",
      "scraped_at": "2025-12-19T12:00:00Z"
    }
  ]
}
```

### Getting vacancy

#### Request

`GET /api/vacancies/{vacancy_id}`

#### Response

```json
{
  "id": "1",
  "title": "Middle Backend Developer",
  "company_name": "ACME",
  "skills": ["Python", "Django"],
  "location": {
    "location": "New York",
    "status": true 
  },
  "salary": {
    "salary_from": 2000,
    "salary_to": 3000,
    "currency": "USD"
  },
  "employment_type": "full_time",
  "experience_level": "Middle",
  "summary": "....",
  "source_url": "https://example.com",
  "active_status": "Watched",
  "posted_at": "2025-12-19T12:00:00Z",
  "scraped_at": "2025-12-19T12:00:00Z"
}
```

