import torch

# Print PyTorch version
print("PyTorch Version:", torch.__version__)

# Check CUDA availability
cuda_available = torch.cuda.is_available()
print("CUDA Available:", cuda_available)

# Print the CUDA version used to build PyTorch
if cuda_available:
    print("CUDA Version PyTorch is built with:", torch.version.cuda)
else:
    print("CUDA is not available. PyTorch is using CPU mode.")