import moment


currentTime = moment.now()
currentTime_inFormat = moment.now().strftime("%H-%M-%S _ %d-%m-%Y")

print(currentTime)
print(currentTime_inFormat)