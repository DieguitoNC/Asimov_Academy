# %% 
import logging
# %%

logging.basicConfig(filename="app.log", level=logging.DEBUG)

# %%
log = logging.getLogger()
# %%
log.info("Ola")
# %%
log.level
# %%
