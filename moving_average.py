import torch

def moving_average(model, model_ema, beta=0.999):
    for param, param_ema in zip(model.parameters(), model_ema.parameters()):
        param_ema.data = torch.lerp(param.data, param_ema.data, beta)    
