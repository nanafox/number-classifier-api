#!/usr/bin/env python3

"""Schema for number classification API."""

from pydantic import BaseModel, Field


class NumberResponse(BaseModel):
    """Schema for successful responses."""

    number: int = Field(examples=[371, 12])
    is_prime: bool = Field(examples=[False, False])
    is_perfect: bool = Field(examples=[False, False])
    properties: list[str] = Field(examples=[["armstrong", "odd"], ["even"]])
    digit_sum: int = Field(examples=[11, 3])
    fun_fact: str = Field(
        examples=[
            "371 is a narcisstic number.",
            "12 is the smallest weight for which a cusp form exists.",
        ]
    )


class NumberErrorResponse(BaseModel):
    """Schema for error responses."""

    number: str = Field(examples=["number", "hello"])
    error: bool = True
