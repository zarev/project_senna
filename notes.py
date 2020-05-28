def notes():
  # to access memory address of pointers game needs to
  # run CE or VEH with dbvm/trueplay disabled
  pass

def game_plan():
  # A: linear acceleration
  # B: sideways
  # C: rotation... 6DOF?

  # 1: ---get acceleration data---
  #  1.1: figure out how to base addresses
  #   1.1.1: Find addresses for the 6 DOF
  #   1.1.2: Find address for G-Force Value 
  #  1.2: perform AOB scan to find static address for acceleration
  #  1.3: script to print the data live
  # 2: ---translate the data into a motion model---
  #  2.1: start with linear only
  #  2.2: add sideways
  # 3: ---implement with the vest---
  #  3.1: together with 2.1
  pass

def references():

  # haptics for controllers:
  # https://hal.archives-ouvertes.fr/hal-01524537/document
  # potential haptic vest: 
  # http://www.korfx.com
  # sim dashboard guthub:
  # https://github.com/Alex-developer/OneHUD/tree/master/ProjectCars2
  # READ/WRITE in game memory:
  # https://www.youtube.com/watch?v=Mm3ZK3uAeuo
  # find static memory addresses in games:
  # https://www.youtube.com/watch?v=hfWOAFsYnFA
  # if nothing else works, more address fishing:
  # https://www.youtube.com/watch?v=eU4UGVvQDME&feature=youtu.be
  # forum that suggested above:
  # https://forum.cheatengine.org/viewtopic.php?p=5743349&sid=21d9cea6a573769709636496dc7e5671
  # moar blogs:
  # https://www.cheatengine.org/forum/viewtopic.php?t=608724&sid=c0f8c32bec03a1f0a5f16db08e98121a
  # pointer map with 2 pointers:
  # https://www.youtube.com/watch?v=nQ2F2iW80Fk
  # game hacking website:
  # https://www.dev798.com/archives/2262
  # list of haptic suits(most bankrupt):
  # https://en.wikipedia.org/wiki/Haptic_suit
  # monster simulator: https://www.youtube.com/watch?v=hQLF06rwzVE
  # create AOB:
  # https://www.youtube.com/watch?v=5GQ6nOi9oQ0
  pass