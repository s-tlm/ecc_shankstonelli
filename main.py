# Steven Lam
# 2021
# %% Import modules
from shanks import SECP256K1
from keygen import generate_256_hex

# %% Executing functions
# class SECP256k1 has two methods: find_Points() and show_Points()
pt = SECP256K1(1)
pt.plot_Points()
# %%
generate_256_hex()
# %%
