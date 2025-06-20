# Updated app.py with LiteLLM and model dropdown support
from flask import Flask, render_template, request, jsonify
import requests
import json
import litellm

app = Flask(__name__)

# Define API keys
API_KEYS = {
    "google": "your-google-api-key-here",
    "groq": "your-groq-api-key-here",
    "anthropic": "your-anthropic-api-key-here",
    "openai": "your-openai-api-key-here"
}

# LLM Model Mapping
MODEL_MAP = {
    "Gemini": {"provider": "google", "model": "gemini/gemini-pro"},
    "Groq": {"provider": "groq", "model": "mixtral-8x7b-32768"},
    "Anthropic": {"provider": "anthropic", "model": "claude-3-opus-20240229"},
    "OpenAI": {"provider": "openai", "model": "gpt-4-turbo"}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    format_ = data.get("format", None)
    template = data.get("template", "")
    custom_instructions = data.get("custom_instructions", "").strip()
    dynamic_values = data.get("dynamic_values", {})
    selected_llm = data.get("llm", "Gemini")

    # Handle JSON string in dynamic values
    if isinstance(dynamic_values, str):
        try:
            dynamic_values = json.loads(dynamic_values)
        except Exception:
            dynamic_values = {}

    # Replace placeholders in prompt
    def replace_placeholders(text, values):
        import re
        def replacer(match):
            key = match.group(1)
            val = values.get(key, f"{{{key}}}")
            return json.dumps(val) if isinstance(val, (list, dict)) else str(val)
        return re.sub(r"\{(.*?)\}", replacer, text)

    final_prompt = replace_placeholders(prompt, dynamic_values)

    # Apply format instructions
    if format_ == "json" and template:
        full_prompt = f"{final_prompt}\n\nFormat output as JSON following this template:\n{template}"
    elif format_ == "customize" and custom_instructions:
        full_prompt = f"{final_prompt}\n\nPlease format the output as follows:\n{custom_instructions}"
    else:
        full_prompt = final_prompt

    # Get LLM provider info
    try:
        provider_info = MODEL_MAP[selected_llm]
        provider = provider_info["provider"]
        model = provider_info["model"]
        api_key = API_KEYS.get(provider)

        if not api_key:
            return jsonify({"error": f"No API key found for provider '{provider}'"}), 400

        litellm.api_key = api_key

        # Call LLM
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": full_prompt}]
        )

        # Extract response
        full_text = response["choices"][0]["message"]["content"].strip()

        # Format response
        if format_ == "json":
            try:
                parsed_json = json.loads(full_text)
                pretty_json = json.dumps(parsed_json, indent=2)
                return jsonify({"response": pretty_json})
            except Exception:
                return jsonify({"response": full_text, "warning": "Invalid JSON output from API"})
        else:
            return jsonify({"response": full_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

