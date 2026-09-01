"""
IBM Granite client for FreshStock AI.
"""

import os

from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

from ai.granite.prompts import FULL_ANALYSIS_PROMPT


load_dotenv()


WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_URL = os.getenv("WATSONX_URL")


def get_granite_model():
    """Create and return the IBM Granite model."""

    if not WATSONX_API_KEY:
        raise ValueError("WATSONX_API_KEY is missing.")

    if not WATSONX_PROJECT_ID:
        raise ValueError("WATSONX_PROJECT_ID is missing.")

    if not WATSONX_URL:
        raise ValueError("WATSONX_URL is missing.")

    credentials = Credentials(
        url=WATSONX_URL,
        api_key=WATSONX_API_KEY
    )

    model = ModelInference(
        model_id="ibm/granite-4-h-small",
        credentials=credentials,
        project_id=WATSONX_PROJECT_ID,
        params={
            "max_new_tokens": 250,
            "temperature": 0
        }
    )

    return model


def test_granite():
    """Send a simple test prompt to IBM Granite."""

    model = get_granite_model()

    response = model.generate_text(
        prompt=(
            "You are FreshStock AI, an intelligent inventory "
            "assistant. Introduce yourself in one short sentence."
        )
    )

    return response


def generate_ai_recommendation(data):
    """
    Send FreshStock AI analysis results to IBM Granite.
    """

    model = get_granite_model()

    prompt = FULL_ANALYSIS_PROMPT.format(
        product=data["product"],
        store=data["store"],
        predicted_demand=data["forecast"]["predicted_demand"],
        current_stock=data["inventory"]["current_stock"],
        incoming_stock=data["inventory"]["incoming_stock"],
        recommended_order=data["inventory"]["recommended_order"],
        stockout_risk=data["inventory"]["stockout_risk"],
        excess_stock=data["waste"]["excess_stock"],
        days_to_expiry=data["waste"]["days_to_expiry"],
        waste_risk=data["waste"]["waste_risk"]
    )

    response = model.generate_text(
        prompt=prompt
    )

    return response