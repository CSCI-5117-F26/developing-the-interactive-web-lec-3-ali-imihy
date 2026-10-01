from halo import Halo


count = 99
while count > 0:
  spinner = Halo(text="TIME UNTIL DEATH:" + str(count), spinner='dots', color='red', )
  spinner.start()


  count -= 1