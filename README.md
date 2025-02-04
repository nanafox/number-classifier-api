# Number Classification API

## API Specification

- Endpoint: `GET <live-proudction-url>/api/classify-number`
- Required Query Parameter: `number`
  - Query Parameter Type: `integer`
- Example Request: `GET <live-proudction-url>/api/classify-number?number=371`
- Example Response

  ```json
  {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }
  ```

## Errors

- Example Request: `GET <live-proudction-url>/api/classify-number?number=alphabet`
- Example Error Response for invalid input

  ```json
  {
      "number": "alphabet",
      "error": true
  }
  ```

## Development

### Prerequisites

- Python 3.8+

1. Clone or fork the repo

    ```bash
    git clone https://github.com/nanafox/number-classifier-api.git 
    ```

2. Change directory into the repo

    ```bash
      cd classify-number-api
    ```

3. Create a virtual environment environment

    ```bash
    python3 -m venv .venv
    ```

4. Source the environment and install dependencies

    ```bash
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

5. Run the local server

    ```bash
    fastapi dev
    ```

6. Access the interactive (Swagger) docs at `http:localhost:8000/api/swagger-docs`

7. Access Documentation at `http://localhost:8000/api/docs`
