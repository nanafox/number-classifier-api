#!/usr/bin/env python3

"""This module defines the endpoint to hit the Numbers API and return the fun
facts."""

from typing import Annotated

import httpx
from fastapi import FastAPI, Query, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app import lib
from app.schemas.number import NumberErrorResponse, NumberResponse

app = FastAPI(
    title="Number Classification API",
    version="v1",
    description="",
    contact={
        "name": "Maxwell Nana Forson",
        "website": "https://mnforson.live",
        "email": "nanaforsonjnr@gmail.com",
    },
    docs_url="/api/swagger-docs",
    redoc_url="/api/docs",
)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["GET", "HEAD"]
)

NUMBERS_API_URL = "http://numbersapi.com/{number}/math"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    _: Request, exc: RequestValidationError
):
    invalid_input = exc.errors()[0].get("input")

    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            NumberErrorResponse(number=invalid_input, error=True)
        ),
    )


@app.get("/api/classify-number", include_in_schema=False)
@app.get(
    "/api/classify-number/",
    response_model=NumberResponse,
    operation_id="classify_number",
    summary="Get Number Classfication",
    status_code=status.HTTP_200_OK,
    tags=["number-classification"],
    responses={
        200: {"description": "Successful Response", "model": NumberResponse},
        400: {"description": "Invalid input", "model": NumberErrorResponse},
    },
)
async def classify_number(
    number: Annotated[int, Query(description="The number to classify")],
) -> NumberResponse:
    """Returns a classification of the number along with a random fun fact.

    The response contains the following details:

      - Whether the number is prime
      - Whether the number is perfect
      - Whether the number is odd or even
      - Whether the number is an Armstrong type
      - The digit sum of the number
      - A fun fact about the number

    You are required to provide the `number` as a query parameter. It is a
    **required** parameter. Omitting it will return an error.
    """
    response = httpx.get(NUMBERS_API_URL.format(number=number))

    return NumberResponse(
        number=number,
        is_prime=lib.is_prime(number),
        is_perfect=lib.is_perfect(number),
        properties=lib.build_number_properties(number),
        digit_sum=lib.digit_sum(number),
        fun_fact=response.text,
    )
