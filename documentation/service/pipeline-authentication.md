# Pipeline Authentication

## Overview

The data pipeline needs to be authenticated to access the web service endpoints, e.g. `create-term`, `list-terms`.

## OAuth2 Authentication Server

Our service will act as an OAuth2 authorization server, which means it will handle issuing tokens to the data pipeline.

Our data pipeline will be registered as a client application with the OAuth2 server. This will create a client ID and client secret for the data pipeline.

## Storing Client Credentials

The client ID and client secret will be stored in the relevant secure storage solution for our data pipeline, e.g. Azure Key Vault, AWS Secrets Manager, etc. This will ensure that they are protected and accessible only to the data pipeline.

## Obtaining Access Tokens

The first step in the data pipeline will be a function that retrieves the client ID and client secret from the secure storage solution.

```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Retrieve client ID and secret from Key Vault
keyvault_name = "your-keyvault-name"
kv_uri = f"https://{keyvault_name}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=kv_uri, credential=credential)

client_id = client.get_secret("client-id").value
client_secret = client.get_secret("client-secret").value
```

This function will then use these credentials to request an access token from the OAuth2 server.

The access token will be used to authenticate the data pipeline when making requests to the web service endpoints.

```python

import requests

def get_access_token(client_id, client_secret):
    response = requests.post(
        'https://your-api.com/o/token/',
        data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
    )

    if response.status_code == 200:
        return response.json().get('access_token')
        client.set_secret("pipeline-token", token)
    else:
        raise Exception("Failed to retrieve access token")
```

The access token will be stored in the data pipeline's secure storage solution. This means that it is accessible to all functions in the data pipeline that need to make requests to the web service endpoints.

```python
import requests

keyvault_name = "your-keyvault-name"
kv_uri = f"https://{keyvault_name}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(
    vault_url=kv_uri,
    credential=credential
)

def make_request():
    access_token = client.get_secret("pipeline-token").value

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(
        'https://your-api.com/api/endpoint/',
        headers=headers
    )
```

## Token expiry

We will set the token expiry time to 1 hour, which should be long enough to complete the data pipeline run.

If required, we can implement a refresh token mechanism to obtain a new access token without requiring the data pipeline to re-authenticate. This will be useful if the data pipeline takes longer than 1 hour to run.
