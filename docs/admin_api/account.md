
## 👤 Account Endpoints


### Get all accounts

#### Request

`GET /api/admin/accounts/`

#### Response

```json
{
  "accounts": [
    {
      "username": "alex",
      "email": "alex@example.com",
      "account_type": "SIMPLE",
      "account_status": "ACTIVE",
      "last_login": "2025-12-19T12:00:00Z",
      "last_active": "2025-12-19T12:00:00Z",
      "created_at": "2025-12-19T12:00:00Z",
      "link_lists_count": 1,
      "subscriptions": [
        {
          "id": 1,  
          "name": "Free",
          "links_per_hour": 20,
          "price": 0.0,
          "currency": "USD",
          "description": "Basic rate, up to 20 links/hour",
          "features": ["history_7_days", 
            "export_to_csv", "export_to_xls", "export_to_txt"]
        }
      ],
      "parsing_runs_count": 10
    }
  ]
}
```

### Get account by id / username

#### Request

`GET /admin-api/accounts/{username}/`

#### Response

```json
{
  "accounts": [
    {
      "username": "alex",
      "email": "alex@example.com",
      "account_type": "SIMPLE",
      "account_status": "ACTIVE",
      "last_login": "2025-12-19T12:00:00Z",
      "last_active": "2025-12-19T12:00:00Z",
      "created_at": "2025-12-19T12:00:00Z",
      "link_lists_count": 1,
      "link_lists": [
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
      ],
      "subscriptions": [
        {
          "id": 1,
          "name": "Free",
          "links_per_hour": 20,
          "price": 0.0,
          "currency": "USD",
          "description": "Basic rate, up to 20 links/hour",
          "features": [
            "history_7_days",
            "export_to_csv",
            "export_to_xls",
            "export_to_txt"
          ]
        }
      ],
      "parsing_runs_count": 10,
      "parsing_runs": [
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
      ]
    }
  ]
}
```


### Delete account by id / username

#### Request

`DELETE /admin-api/accounts/{username}/delete/`

#### Response

```json
{
  "message": "Account was deleted successfully!"
}
```


### Block account by id / username

#### Request

`PATCH /admin-api/accounts/{username}/block/`

#### Response

```json
{
  "message": "Account was blocked successfully!"
}
```