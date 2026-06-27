import mph

client = mph.Client(version="6.4", port=2036)
models = client.models()

model = models[0]

# SAFE MODE
# no auto-save