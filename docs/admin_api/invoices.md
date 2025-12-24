
## 📋 Invoices


## Invoices

### Find all invoices

#### Request

`GET /api/admin/invoices/`
    
#### Response

```json
{
  "invoices": [
    {
      "id": 101,
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

`GET /api/admin/transactions/`
    
#### Response

```json

```