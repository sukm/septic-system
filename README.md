
# Septic System

## Table of Contents

- [Septic System](#septic-system)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Style](#style)
  - [Quick Start](#quick-start)
  - [Test](#test)
  - [API Documentation](#api-documentation)
      - [End Points](#end-points)
        - [GET /key](#get-key)
  - [Next Steps](#next-steps)

## Requirements

- Python 3.7

## Style

- [PEP 8](https://www.python.org/dev/peps/pep-0008/)

## Quick Start

1. Clone the repo

```
$ git clone https://github.com/sukm/caching-service.git
$ cd caching-service
```

2. Initialize and activate a virtualenv:

```
$ python3.7 -m venv env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

5. Run the development server:

```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

Leaving the virtual environment

```
$ deactivate
```

## Test

The data was mocked with Postman Mock Server

```
$ python -m unittest
```

## API Documentation

#### End Points

| Description                                          | Endpoint    |
| -----------------------------------------------------| ----------- |
| [Check whether a home has a septic system](#get-key) | GET /api/v1 |


##### GET /key

- **Method:**
  `GET`

- **Required:**

  `address`, `zipcode`

- **Params**

  ```
  {
      "zipcode": "90274",
      "address": "43 Valmonte Plaza"
  }
  ```

- **Success Response:**
  - **Code:** 200
  ```
  {
      "address": "43 Valmonte Plaza",
      "has_septic": true,
      "zipcode": "90274"
  }
  ```

- **Error Response:**
  - **Code:** 404
  ```
  {
      "message": "Property not found"
  }
  ```
## Next Steps
- Add validators
- Add Authentication
- Create a config file and store it on cloud object storage 
- if service gets larger, utilize flask_restful for maintainability 