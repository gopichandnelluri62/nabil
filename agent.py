# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from google.adk.agents import Agent
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Import the refactored tool and the enhanced prompt for BigQuery
import tools
import prompt

# Load environment variables from the .env file
load_dotenv()

# --- Agent Definition ---

# The name of the model to be used by the root agent.
# This should be a powerful model capable of reasoning and function calling.
ROOT_AGENT_MODEL = os.environ.get("ROOT_AGENT_MODEL", "gemini-2.5-flash")

# This is the main agent for interacting with the BigQuery database.
# Its instruction is the comprehensive prompt we've built, which contains all the
# database context and reasoning logic. The agent's tool is the SQL query executor.
root_agent = Agent(
    name="bigquery_agent",
    model=ROOT_AGENT_MODEL,
    description="An agent that understands questions about a BigQuery database, generates SQL, executes it, and provides answers.", # Updated description
    instruction=prompt.BIGQUERY_PROMPT,
    tools=[
        tools.query_bigquery,
    ],
)

# --- Web Server Definition (REQUIRED BY GUNICORN) ---
# This is the application object that Gunicorn will serve.
# We're creating a basic Flask app as the entry point.
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """A simple health check endpoint to confirm the service is running."""
    return jsonify({"status": "ok", "message": "Dixie Agent is up and running!"})

# The following is a placeholder for your main agent endpoint.
@app.route("/agent", methods=["GET", "POST"])
def agent_handler():
    """Placeholder for the main agent logic."""
    if request.method == "GET":
        return jsonify({"message": "This is the agent endpoint. Please use a POST request with a JSON body."})
    
    try:
        user_input = request.json.get("query")
        if not user_input:
            return jsonify({"error": "Missing 'query' field in request body."}), 400

        # --- Your agent processing logic would go here ---
        # For now, we'll return a simple response.
        return jsonify({"response": f"Received your query: '{user_input}'. Agent logic is not yet implemented."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
