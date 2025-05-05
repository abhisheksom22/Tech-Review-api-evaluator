# amazonbedrock.py

import boto3
import json

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def summarize_with_claude(prompt):
    body = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.5,
        "anthropic_version": "bedrock-2023-05-31"
    }

    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text'].strip()
