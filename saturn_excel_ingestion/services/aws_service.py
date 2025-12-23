import boto3
import json

def get_secret(secret_name, region_name,profile_name):
    """
    Retrieves a secret from AWS Secrets Manager using a profile.
    :param secret_name: Name of the secret in AWS Secrets Manager.
    :param region_name: AWS region where the secret is stored.
    :return: A dictionary with the secret values or None if an error occurs.
    """
    try:
        # Create a session using the profile
        session = boto3.Session(profile_name=profile_name)

        # Create a Secrets Manager client
        client = session.client("secretsmanager", region_name=region_name)

        # Fetch the secret value
        response = client.get_secret_value(SecretId=secret_name)

        # Return the secret as a JSON dictionary if it's a valid JSON string
        if "SecretString" in response:
            return json.loads(response["SecretString"])
        else:
            print("The secret does not contain a valid string.")
            return None

    except Exception as e:
        print(f"Error retrieving the secret: {e}")
        return None
    