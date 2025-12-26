
## 📋 Invoices


## Invoices

### Find all invoices

#### Request

`GET /api/admin/invoices?subscription_name=Pro&sort_by=price&order=asc&page=1&limit=20`

- page 
- limit

**Filters**

- subscription_name: `Pro`, `Free`... - Filter by subscription name;
- status: `pending`, `success`, `failed`, `refunded` - Filter by status;
- amount_from / amount_to - Filter by amount;
- status - Filter by status;
- created_at / paid_at: `2025-12-01` - Filtering by time;
- 

**Sorting**

- sort_by: `amount`, `subscription_name`, `status`, `created_at`, `paid_at`, `expires_at`;
- order: `asc`, `desc`;
    
#### Response

```json
{
  "page": 1,
  "page_size": 20,
  "total_pages": 15,
  "total_items": 150,
  "data": [
    {
      "id": 101,
      "account": {
          "id": 1,
          "username": "alex",
          "email": "alex@example.com"
      },
      "amount": 6.0,
      "currency": "USD",
      "status": "pending",            
      "payment_url": "https://payment-provider.com/pay/xyz789",
      "expires_at": "2026-01-31T23:59:59Z",
      "created_at": "2026-01-01T00:00:00Z"
    }
  ]
}
```

### Get invoice by id

`GET /api/admin/invoices/{id}/`
    
#### Response

```json
{
  "id": 101,
  "account": {
          "id": 1,
          "username": "alex",
          "email": "alex@example.com"
  },
  "subscription": {
      "id": 1,  
      "name": "Pro",
      "links_per_hour": 50,
      "price": 6.0,
      "currency": "USD",
      "description": "Pro rate, up to 50 links/hour",
      "features": ["history_30_days", 
        "export_to_csv", "export_to_xls", "export_to_txt"]
  },
  "amount": 6.0,
  "currency": "USD",
  "status": "paid",  
  "period_start": "2025-12-01",
  "period_end": "2025-12-31",
  "created_at": "2025-11-25T12:00:00Z",
  "paid_at": "2025-11-26T10:00:00Z",
  "transactions": {
      "id": 301,
      "amount": 6.0,
      "currency": "USD",
      "status": "pending",       
      "provider": "stripe",
      "provider_tx_id": "txn_abc123",
      "created_at": "2025-12-24T15:05:00Z"
    }
}
```


## Transactions

### Find all transactions

#### Request

`GET /api/admin/transactions?status=success,refunded&page=1&limit=20`

- page 
- limit

**Filter** 

- status: `pending`, `success`, `failed`, `refunded` - Filter by status;
- provider: `stripe` - Filter by provider;
- subscription_name: `Pro`, `Free` - Filter by subscription name;
- created_at / paid_at: `2025-12-01` - Filtering by time;
- amount_from / amount_to - Filter by amount;

**Sorting**

- sort_by: `created_at`, `paid_at`, `amount`, `status`, `provider`, `subscription_name`;
- order: `asc`, `desc`;
    
#### Response

```json
{
  "page": 1,
  "page_size": 20,
  "total_pages": 15,
  "total_items": 150,
  "data": [
    {
      "id": 301,
      "account": {
          "id": 1,
          "username": "alex",
          "email": "alex@example.com"
      },
      "invoice_id": 101,
      "subscription_name": "Pro",
      "amount": 9.99,
      "currency": "USD",
      "status": "success",
      "provider": "stripe",
      "provider_tx_id": "txn_abc123",
      "created_at": "2025-12-24T15:05:00Z",
      "paid_at": null
    },
    {
      "id": 302,
      "account": {
          "id": 1,
          "username": "alex",
          "email": "alex@example.com"
      },
      "invoice_id": 102,
      "subscription_name": "Premium",
      "amount": 19.99,
      "currency": "USD",
      "status": "pending",
      "provider": "stripe",
      "provider_tx_id": "txn_def456",
      "created_at": "2025-12-25T12:00:00Z",
      "paid_at": null
    }
  ]
}
```

### Find transaction by ID

#### Request

`GET /api/admin/transactions/{id}/`

#### Response

```json
{
  "id": 301,
  "account":  {
    "id": 1, 
    "username": "alex",
    "email": "user@example.com"
  },
  "subscription_name": "Pro",
  "amount": 9.99,
  "currency": "USD",
  "status": "success",
  "provider": "stripe",
  "provider_tx_id": "txn_abc123",
  "created_at": "2025-12-24T15:05:00Z",
  "paid_at": null,
  "invoice_id": 101,
  "invoice": {
    "id": 101,
    "period_start": "2025-12-24T15:05:00Z",
    "period_end": "2025-12-24T15:05:00Z",
    "status": "paid",
    "amount": 9.99,
    "currency": "USD"
  }
}
```