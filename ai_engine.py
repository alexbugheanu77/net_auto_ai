import openai
from config import OPENAI_API_KEY, MODEL, TEMPERATURE, MAX_TOKENS

openai.api_key = OPENAI_API_KEY


def generate_network_commands(prompt):
    """
    Generates network configuration commands based on a natural language prompt using OpenAI's API.

    Args:
        prompt (str):  The natural language prompt describing the desired network configuration.

    Returns:
        str:  The generated network commands (e.g., Cisco IOS commands), or None if an error occurred.
    """
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        return response['choices'][0]['message']['content']

    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return None


if __name__ == '__main__':
    # Example Usage
    user_prompt = "Configure VLAN 20 with name 'Data' on interface GigabitEthernet0/1 on a Cisco switch."
    commands = generate_network_commands(user_prompt)

    if commands:
        print("Generated Commands:\n", commands)
    else:
        print("Failed to generate commands.")