# %% imports
import sys
import os
import subprocess

# %% parameters
msetup = 8
mdev = "MOT01"
mtopic = "/S00" + str(msetup) + "/" + mdev + "/RECM"
mcmd = "FLUO+"

# %% scripts
while True:
    in_val = int(input(
        "Please input an integer between 0 (=off) and 100 (=max). Anything else ends the program."))
    if in_val >= 0 and in_val < 101:
        mcmdsend = ["mosquitto_pub", "-h", "localhost",
                    "-t", mtopic, "-m", mcmd + str(in_val)]
        subprocess.run(mcmdsend)
        print("Changed to {} ".format(" ".join(mcmdsend)))
    else:
        break
