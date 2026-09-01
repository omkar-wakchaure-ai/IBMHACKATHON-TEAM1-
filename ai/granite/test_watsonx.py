import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

api_key = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
url = os.getenv("WATSONX_URL")

print("API key loaded:", bool(api_key))
print("Project ID loaded:", bool(project_id))
print("URL:", url)

credentials = Credentials(
    url=url,
    api_key=api_key
)

model = ModelInference(
   model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=project_id
)

response = model.generate_text(
    prompt="Say hello in one sentence."
)

print("\nIBM Granite response:")
print(response)