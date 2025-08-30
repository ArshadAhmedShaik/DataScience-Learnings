import requests
import base64

# Step 1: Start the challenge and get session cookies
start_url = "https://workwithus.webminix.com/begin"
session = requests.Session()  # maintains cookies automatically
response = session.get(start_url)
print("Step 1: /begin response preview:")
print(response.text[:200], "...")  # print first 200 chars

# Step 2: Access /find-key with required headers
find_key_url = "https://workwithus.webminix.com/find-key"
headers = {
    "X-Explorer": "Curious_Explorer",
    "Origin": "https://workwithus.webminix.com",
    "User-Agent": "PythonRequests/2.x"
}

response = session.get(find_key_url, headers=headers)

# Step 3: Decode Base64 artifact if response is JSON
try:
    data = response.json()
    # Find the Base64 string in the JSON
    if "coded artifact" in data:
        artifact_base64 = data["coded artifact"]
    else:
        artifact_base64 = list(data.values())[0]  # fallback

    decoded_artifact = base64.b64decode(artifact_base64).decode('utf-8')
    print("\nDecoded artifact from /find-key:")
    print(decoded_artifact)

except Exception as e:
    print("Failed to get JSON or decode:", e)
    print("Response text from /find-key:", response.text)
