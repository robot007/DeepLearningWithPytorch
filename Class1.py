# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 07:42:37 2018

@author: zhensong
"""

# It is this easy! 
import torch

# Create a variable of value 1 each.
a = torch.Tensor([1])
b = torch.Tensor([1])

# Add the 2 variables to give you 2, it's that simple!
c = a + b

torch.randn(2,2)

print(torch.cuda.is_available())
# print(torch.cuda.current_device())
# print (torch.cuda.get_device_name(0))