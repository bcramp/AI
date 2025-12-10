import torch

# If the .pth file contains the entire model object
model = torch.load('car_dqn_model.pth')

# Print statement to say the model has been loaded
print(f"I have loaded the model!")

# Prints the model
print(model)
