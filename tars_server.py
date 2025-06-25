from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/tars", methods=["POST"])
def tars_reply():
	data = request.get_json()
	prompt = data.get("prompt", "")
	try:
		response = openai.ChatCompletion.create(
			model="gpt-4o"
			messages=[{"role": "user", "content": prompt}]
		)
		reply = response["choices"][0]["message"]["content"]
		return jsonify({"reply": reply})
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
	return "Hello from TARS!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
