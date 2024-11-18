from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def generate_text(prompt):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {"Authorization": "Bearer Your_API_Key"}
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "top_p": 0.95,
            "do_sample": True
        }
    }
    
    app.logger.debug(f"Sending request to API with payload: {payload}")
    response = requests.post(API_URL, headers=headers, json=payload)
    app.logger.debug(f"API response: {response.text}")
    return response.json()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_bio", methods=["POST"])
def generate_bio():
    user_input = request.json
    app.logger.debug(f"Received user input: {user_input}")
    
    try:
        # Create the prompt
        prompt = f"""Task: Generate a dating profile bio
Career: {user_input['career']}
Personality traits: {', '.join(user_input['traits'])}
Interests: {', '.join(user_input['interests'])}
Relationship Goals: {user_input['relationshipGoals']}

Generate an engaging, authentic, and concise dating profile bio based on the above information. Keep it under 150 words."""
        
        app.logger.debug(f"Generated prompt: {prompt}")
        
        # Generate the bio
        response = generate_text(prompt)
        app.logger.debug(f"Generated response: {response}")
        
        # Extract the generated text
        if isinstance(response, list) and len(response) > 0:
            bio = response[0].get('generated_text', '').replace(prompt, '').strip()
        else:
            bio = response.get('generated_text', '').replace(prompt, '').strip()
            
        app.logger.debug(f"Final bio: {bio}")
        return jsonify({"bio": bio})
    
    except Exception as e:
        app.logger.error(f"Error generating bio: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
