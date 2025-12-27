
## 💳 Subscribe

Subscription types:

| Title   | Links/hour  | Add. features                      | Price |
|---------|-------------|------------------------------------|-------|
| Free    | 20          | History 7 days, export to CSV/XLS  | 0$    |
| Pro     | 50          | History 30 days, export to CSV/XLS | 6$    |
| Premium | 100         | History 90 days, export to CSV/XLS | 20$   |
| Custom  | Any         | History XX days, export to CSV/XLS | ?$    |


## Subscription endpoints

### Create a subscription

#### Request

`POST /api/subscraptions/`

```json
{
  "name": "Free",
  "links_per_hour": 20,
  "price": 0.0,
  "currency": "USD",
  "description": "Basic rate, up to 20 links/hour",
  "features": ["history_7_days", 
        "export_to_csv", "export_to_xls", "export_to_txt"]
}
```

#### Response

```json
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
```


### Update subscription by id

#### Request

`PATCH /api/subscraptions/{id}/update`

```json
{
  "name": "Pro"
}
```

**Other fields**

- links_per_hour
- price
- currency
- description
- features


#### Response

```json
{
  "message": "The subscription was updated successfully"
}
```


### Remove subscription by id

#### Request

`DELETE /api/subscraptions/{id}/delete`

#### Response

```json
{
  "message": "The subscription was removed successfully"
}
```


## User subscriptions

### Show all user subscriptions

#### Request

`GET /api/user-subscriptions/`

**Filters**

- account_email: `alex@example.com`
- account_username: `alex`
- subscription_name: `Free`
- subscription_links_per_hour: `20`
- starts_at / expires_at: `2025-12-24T15:05:00Z`
- status: `active`

**Sorting**

- sort_by: `starts_at`, `expires_at`, `status`;
- order: `asc`, `desc`;

### Response

```json
{
  "page": 1,
  "page_size": 20,
  "total_pages": 15,
  "total_items": 150,
  "data": [
    {
      "id": 1,
      "account": {
          "id": 1,
          "username": "alex",
          "email": "alex@example.com"
      },
      "subscription": {
          "id": 1,
          "name": "Free",
          "links_per_hour": 20,
          "price": 0.0,
          "currency": "USD",
          "description": "Basic rate, up to 20 links/hour",
          "features": ["history_7_days", 
            "export_to_csv", "export_to_xls", "export_to_txt"]
      },
      "starts_at": "2025-12-24T15:05:00Z",
      "expires_at": "2026-1-24T15:05:00Z",
      "status": "active"
    }
  ]
}
```

### Create a user subscription 
    
#### Request

`POST /api/user-subscriptions/`

#### Response

```json
{
  "id": 1,
  "account_id": 1, 
  "subscription_id": 1,
  "starts_at": "2025-12-24T15:05:00Z",
  "expires_at": "2026-1-24T15:05:00Z",
  "status": "active"
}
```


### Find user subscription by ID

#### Request

`GET /api/user-subscriptions/{id}/`

#### Response

```json
{
  "id": 1,
  "account": {
      "id": 1,
      "username": "alex",
      "email": "alex@example.com"
  },
  "subscription": {
      "id": 1,
      "name": "Free",
      "links_per_hour": 20,
      "price": 0.0,
      "currency": "USD",
      "description": "Basic rate, up to 20 links/hour",
      "features": ["history_7_days", 
        "export_to_csv", "export_to_xls", "export_to_txt"]
  },
  "starts_at": "2025-12-24T15:05:00Z",
  "expires_at": "2026-1-24T15:05:00Z",
  "status": "active"
}
```