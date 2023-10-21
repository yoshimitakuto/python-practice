import json
import os
import sys

import boto3
import botocore


module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww


# ---- ⚠️ Un-comment and edit the below lines as needed for your AWS setup ⚠️ ----

# os.environ["AWS_DEFAULT_REGION"] = "<REGION_NAME>"  # E.g. "us-east-1"
# os.environ["AWS_PROFILE"] = "<YOUR_PROFILE>"
# os.environ["BEDROCK_ASSUME_ROLE"] = "<YOUR_ROLE_ARN>"  # E.g. "arn:aws:..."

boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None)
)

boto3_bedrock.list_foundation_models()

prompt_data = """Command: Write me a blog about making strong business decisions as a leader.

Blog:
"""

body = json.dumps({"inputText": prompt_data})
modelId = "amazon.titan-tg1-large"
accept = "application/json"
contentType = "application/json"

response = bedrock_runtime.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType
)
response_body = json.loads(response.get("body").read())

print(response_body.get("results")[0].get("outputText"))


# prompt = "Please introduce 10 great tourist attractions in Japan."

# kwargs = {
#   "modelId": "anthropic.claude-v1",
#   "contentType": "application/json",
#   "accept": "*/*",
#   "body": {
#     "prompt": "\n\nHuman: "+ prompt +"\n\nAssistant:",
#     "max_tokens_to_sample": 300,
#     "temperature": 0.5,
#     "top_k": 250,
#     "top_p": 1,
#     "stop_sequences": [
#       "\\n\\nHuman:"
#     ],
#     "anthropic_version": "bedrock-2023-05-31"
#   }
# }

# print(kwargs)


# res = boto3_bedrock.invoke_model_with_response_stream(**kwargs)

# stream = res.get('body')
# if stream:
#     for event in stream:
#         chunk = event.get("chunk")
#         if chunk:
#             print(json.loads(chunk.get('bytes')).get('completion'), end="")