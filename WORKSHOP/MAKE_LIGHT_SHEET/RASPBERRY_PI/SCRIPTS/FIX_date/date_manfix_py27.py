# %% IMPORTS
import subprocess
#import re # intended to be used with re.escape(string) to escape strings

# %% RUN THIS SCRIPT AS SUDO-USER
in_ymd = 1
while not len(str(in_ymd))==8:
    in_ymd = input("Please input the day formatted as YYYYMMDD, hence e.g. 20191009 -> ")
in_t = "10:"
while not (len(in_t) == 8):
    in_t =raw_input("Please enter the time as hh:mm:ss in 24h style, hence e.g. 14:02:20 -> ")
subprocess.call(["sudo", "date", "+%Y%m%d","-s", str(in_ymd)])
subprocess.call(["sudo", "date", "+%T","-s", in_t])
print("Changed to {} at {}.".format(in_ymd,in_t))



# %%
