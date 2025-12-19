
## 👤 Account Endpoints


### Change email

#### Request

`PATCH /api/account/change-email/`

```json
{
  "new_email": "johndoe@example.com"
}
```

#### Response

```json
{
    "message": "Email was updated successfully!"
}

```


### Change username

#### Request

`PATCH /api/account/change-username/`

```json
{
  "new_username": "john_doe"
}
```

#### Response

```json
{
    "message": "Username was updated successfully!"
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


