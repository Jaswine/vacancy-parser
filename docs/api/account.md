
## 👤 Account Endpoints

### Find account data

#### Request

`GET /api/account/me/`

#### Response

```json
{
  "username": "alex",
  "email": "alex@example.com",
  "last_login": "2025-12-19T12:00:00Z",
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
```


### Change account data

#### Request

`PATCH /api/account/me/`

- username - New username
- email - New email

```json
{
  "email": "johndoe@example.com"
}
```

#### Response

```json
{
    "message": "Email was updated successfully!"
}

```


### Delete account

#### Request

`DELETE /api/account/delete/`

#### Response

```json
{
    "message": "Account was deleted successfully!"
}

```


