
import requests
import json # Import json for pretty printing the output

url = "https://www.lesswrong.com/graphql"
query = """
query {
  posts(input: {
    terms: {
      view: "top"
      limit: 2000
      after: "2022-01-01T00:00:00.000Z"
    }
  }) {
    results {
      title
      pageUrl
      baseScore
      score
      voteCount
      postedAtFormatted
    }
  }
}
"""

# Define headers similar to what a browser might send from GraphiQL
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    # It seems LessWrong specifically requires the Referer or Origin header
    'Referer': 'https://www.lesswrong.com/graphiql',
    'Origin': 'https://www.lesswrong.com',
    # Adding a common browser User-Agent can also help sometimes
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Send the POST request with the query payload and the defined headers
    response = requests.post(url, json={'query': query}, headers=headers)

    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    print(f"Status Code: {response.status_code}")
    print("Response Data:")
    # Pretty print the JSON response
    print(json.dumps(response.json(), indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Body: {e.response.text}")