import torch
from fastapi import FastAPI
from typing import Optional

# Intialize app

app = FastAPI()

# Load model
model = None

# Load a JIT exported model
# model = torch.jit.load("model.pt")

# How to export?
# NOTE: Don't export it in this script
# traced_model = torch.jit.trace(model,
#                                example_input,
#                                strict=False,
#                                check_trace=False
#                                )

# model = YOURLIGHTNINGMODEL(args)

# Set model to eval mode so it's not training
# model.eval()

# Check for CPU/GPU
device_name = ""
if torch.cuda.is_available():
    device_name = "cuda"
else:
    device_name = "cpu"


def preprocess(data):
	"""
	Preprocess data
	"""

	return data

def postprocess(data):
	"""
	Postprocess data
	"""

	return data


@app.get("/")
def home():

	return "Hello World"


@app.post("/predict")
async def predict(data: Optional[str] = "REPLACEWITHYOURDATATYPE"):


	# Preprocess
	# data = postprocess(data)

	# with torch.no_grad():
	# 	output = model(data)

	# Post process
	# output = preprocess(output)

	return "Your output"