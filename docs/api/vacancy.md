
## 💼 Vacancy

Creating a job for parsing, taking vacancies after parsing, creating links and lists

### Creating a job parsing task

#### Request

`POST /api/parsing/jobs/`

```json
{
  "urls": [
    "https://example.com",
    "https://example.com"
  ],
  "parse_filters": {
    "title": "Python Backend Developer",
    "location": "Serbia",
    "salary": "1000",
    "currency": "USD",
    "required_work_experience": 2,
    "employment_type": "Full Time",
    "work_format": "Remote",
    "experience_level": "Middle",
    "creation_time": "For a month"
  }
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

`GET /api/parsing/jobs/{job_id}/`

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


### Cancel job parsing task

#### Request

`POST /api/parsing/jobs/{job_id}/cancel/`

#### Response

```json
{
  "status": "Canceled"
}
```


### Getting vacancies

#### Request

`GET /api/vacancies?job_id={job_id}
                   &page={page}
                   &page_size={page_size}
                   &format=json`

##### Format

- json (default)
- csv
- txt
- xlsx

#### Response

```json
{
  "page": 1,
  "page_size": 20,
  "total_pages": 15,
  "total_items": 150,
  "data": [
    {
      "id": "1",
      "title": "Middle Backend Developer",
      "company_name": "ACME",
      "skills": ["Python", "Django"],
      "location": "New York",
      "salary": {
        "salary": 2000,
        "currency": "USD"
      },
      "employment_type": "Full Time",
      "work_format": "Remote",
      "experience_level": "Middle",
      "job_url": "https://example.com",
      "active_status": "Watched",
      "posted_at": "2025-12-19T12:00:00Z",
      "scraped_at": "2025-12-19T12:00:00Z"
    }
  ]
}
```


### Getting vacancy

#### Request

`GET /api/vacancies/{vacancy_id}/`

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


### Results statistics

#### Request

`GET /api/vacancies/stats?job_id={job_id}
                         &sections=salary,skills,location
                         &format=json`

##### Sections

- **companies** - List of companies with number of vacancies 
- **locations** - List of locations with number of vacancies
- **salary_stats** - Salary statistics with calculation 
of minimum, average, median, and maximum salaries
- **employment_type** - List of job types with number of vacancies
- **by_work_format** - List of work formats with number of vacancies
- **by_experience** - List of experience with number of vacancies
- **skills** - List of skills with number of vacancies
- **data_completeness** - List of job vacancies filled with data on 
how many vacancies have the specified salary, skills, and location
- **by_list** - Division by lists
- **errors** - Errors

##### Format

- json (default)
- csv
- txt
- xlsx

#### Response

```json
{
  "companies": [
      { 
        "company": "ACME", 
        "vacancies": 6
      },
      { 
        "company": "ILLO", 
        "vacancies": 4
      }
  ],
  "locations": {
    "serbia": 32,
    "remote": 15
  },
  "salary_stats": {
    "average": 2100,
    "median": 2000,
    "min": 800,
    "max": 4500,
    "currency": "USD"
  },
  "employment_type": {
    "full_time": 45,
    "contract": 12
  },
  "by_work_format": {
    "remote": 25,
    "hybrid": 12,
    "onsite": 20
  },
  "by_experience": {
    "junior": 10,
    "middle": 40,
    "senior": 12
  },
  "skills": [
    { 
      "skill": "Python", 
      "count": 45
    },
    { 
      "skill": "Django", 
      "count": 16
    },
    { 
      "skill": "PostgreSQL", 
      "count": 28
    }
  ],
  "data_completeness": {
    "salary_present": 62,
    "skills_present": 80,
    "description_present": 95
  },
  "by_list": {
    "Favorites": 15,
    "Interview": 5
  },
  "errors": {
    "timeout": 3,
    "parse_error": 1,
    "blocked": 2
  }
}

```



### Show all collections

#### Request

`GET /api/collections/?page=1&page_size=20`

#### Response

```json
{
  "page": 1,
  "page_size": 20,
  "total_pages": 1,
  "total_items": 15,
  "data": [
    {
      "id": "1",
      "name": "Favorite companies",
      "total_items": 150,
      "created_at": "2025-12-19T12:00:00Z"
    }
  ]
}
```


### Create a new collection

#### Request

`POST /api/collections/`

```json
{
  "name": "Favorite companies"
}
```

#### Response

```json
{
  "id": "1",
  "name": "Favorite companies",
  "created_at": "2025-12-19T12:00:00Z"
}
```


### Show a collection by id

#### Request

`GET /api/collections/{collection_id}/`

#### Response

```json
{
  "id": "1",
  "name": "Favorite companies",
  "total_items": 150,
  "links": [
    {
      "id": 1,
      "company_name": "ILLO",
      "url": "https://illo.co"
    }
  ],
  "created_at": "2025-12-19T12:00:00Z"
}
```


### Update the collection's name

#### Request

`PATCH /api/collections/{collection_id}/`

```json
{
  "name": "Favorites"
}
```

#### Response

```json
{
  "message": "The collection was updated successfully!"
}
```


### Delete the collection

#### Request

`DELETE /api/collections/{collection_id}/`

#### Response

```json
{
  "message": "The collection was removed successfully!"
}
```



### Show all links

#### Request

`GET /api/collections/{collection_id}/links/`

#### Response

```json
{
  "urls": [
    {
      "id": "1",
      "url": "https://example.com",
      "created_at": "2025-12-19T12:00:00Z"
    }
  ]
}
```


### Create a new link

#### Request

`POST /api/collections/{collection_id}/links/`

```json
{
  "url": "https://example.com"
}
```

#### Response

```json
{
  "id": "1",
  "url": "https://example.com",
  "created_at": "2025-12-19T12:00:00Z"
}
```


### Remove the link

#### Request

`DELETE /api/collections/{collection_id}/links/{id}`

#### Response

```json
{
  "message": "Link was deleted successfully!"
}
```


### Getting job parsing runs

#### Request

`GET /api/collections/{collection_id}/parsing-runs/`

#### Response

```json
{
  "id": 1,
  "started_at": "2025-12-19T12:00:00Z",
  "finished_at": "2025-12-19T12:00:00Z",
  "duration": "00:30:00",
  "status": "completed",
  "links_total": 18,
  "links_processed": 17,
  "vacancies_found": 29,
  "errors_count": 1
}
```

