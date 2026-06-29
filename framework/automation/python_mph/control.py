"""
COMSOL AI Framework v0.5 - Python mph safe control template.

This script connects to a COMSOL 6.4 Server session.

Safety:
- Lists models before acting.
- Does not save by default.
- Does not overwrite GUI-opened .mph files.
"""

import mph

VERSION = "6.4"
PORT = 2036

client = mph.Client(version=VERSION, port=PORT)
models = client.models()

print(f"Connected to COMSOL Server {VERSION} on port {PORT}")

if not models:
    raise RuntimeError("No model found on COMSOL Server. Open or attach a model first.")

print("Available models:")
for i, model in enumerate(models):
    print(f"[{i}] {model}")

# Select explicitly after user confirmation.
MODEL_INDEX = 0
model = models[MODEL_INDEX]

print(f"Attached model: {model}")

# Example read-only operation:
# print(model.parameters())

# Example safe parameter update after engineering review:
# model.parameter("U_in", "0.1[m/s]")

print("No save performed. Save from COMSOL GUI unless Python save-as is explicitly approved.")
