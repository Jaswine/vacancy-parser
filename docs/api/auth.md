
## 🔐 Authentication Endpoints


### Sign In

#### Request

`POST /api/auth/sign-in/`

```json
{
  "email": "johndoe@example.com",
  "password": "secret"
}
```

#### Response

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpvaG4iOnsic3RhY2siOiJI",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpvaG4iOnsic3RhY2siOiJI"
}
```


### Registration

#### Request

`POST /api/auth/sign-up/`

```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "secret"
}
```

#### Response

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpvaG4iOnsic3RhY2siOiJI",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpvaG4iOnsic3RhY2siOiJI"
}
```


### Account confirmation, send code

Sending a code to confirm and activate your account

#### Request

`POST /api/auth/verification/`

```json
{
  "email": "johndoe@example.com"
}
```

#### Response

```json
{
  "message": "Verification code sent."
}

```


### Account confirmation, get code

Receiving and checking the submitted code

#### Request

`POST /api/auth/verification/confirm/`

```json
{
  "email": "johndoe@example.com",
  "code": "123456"
}
```

#### Response

```json
{
  "message": "Verification completed successfully."
}

```


### Password reset

Password reset

#### Request

`POST /api/auth/password-reset/`

```json
{
  "email": "johndoe@example.com"
}
```

#### Response

```json
{
    "message": "If the email exists, reset instructions were sent."
}

```


### Reset confirmation (enter code/token)

Reset confirmation (enter code/token)

#### Request

`POST /api/auth/password-reset/confirm/`

```json
{
  "email": "johndoe@example.com",
  "code": "829341",
  "new_password": "********"
}
```

#### Response

```json
{
    "message": "Password was updated successfully!"
}

```
