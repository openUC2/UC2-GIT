import I2CDevice
import time

t1 = 0.2
t2 = 1
t3 = 3

ledarr = I2CDevice.I2CDevice(0x07)
ledarr.send("CLEAR")
time.sleep(2)

ledarr.send("SETPRE", 0)  # setze Pattern 0 aktiv (ohne zu laden)
time.sleep(t1)
ledarr.send("FLYBY", 0)  # setze "normalen" editiermodus Modus

time.sleep(t1)
ledarr.send("PXL", 1, [255, 255, 0])
time.sleep(t1)
ledarr.send("PXL", 3, [255, 255, 255])
time.sleep(t1)
ledarr.send("PXL", 5, [255, 0, 0])
time.sleep(t1)
ledarr.send("PXL", 7, [0, 128, 0])
time.sleep(t1)

ledarr.send("FLYBY", 1)  # "speichere nirgends"- editiermodus

time.sleep(t1)
ledarr.send("PXL", 0, [255, 255, 0])
time.sleep(t1)
ledarr.send("PXL", 2, [255, 255, 255])
time.sleep(t1)
ledarr.send("PXL", 4, [255, 0, 0])
time.sleep(t1)
ledarr.send("PXL", 6, [0, 128, 0])
time.sleep(t1)


ledarr.send("FLYBY", 0)  # speichere wieder pattern im zuletzt aktiven preset
time.sleep(t2)

ledarr.send("SETPRE", 1)  # setze Pattern 1 aktiv (ohne zu laden)

ledarr.send("PXL", 63, [255, 255, 255])
time.sleep(t1)
ledarr.send("PXL", 0, [255, 255, 255])
time.sleep(t1)
ledarr.send("PXL", 7, [255, 0, 0])
time.sleep(t1)
ledarr.send("PXL", 56, [255, 0, 0])

time.sleep(t3)
ledarr.send("PRESET", 0)  # aktiviere pattern 0 und lade es
time.sleep(t3)
ledarr.send("PRESET", 1)  # aktiviere pattern 1 und lade es
