def notes():
  # to access memory address of pointers game needs to
  # run CE or VEH with dbvm/trueplay disabled
  pass

def game_plan():
  # A: linear acceleration
  # B: sideways
  # C: rotation... 6DOF?

  # 1: ---get acceleration data---
  #  1.1: figure out how to find base addresses
  #   1.1.1: Bypass anti-cheat for Forza
  #   1.1.2: Find addresses for the 6 DOF
  #   1.1.3: Find address for G-Force Value 
  #  1.2: script to print the data live
  # 2: ---translate the data into a motion model---
  #  2.1: start with linear only
  #  2.2: add sideways
  # 3: ---implement with the vest---
  #  3.1: together with 2.1
  pass

def telemetry_data():
# acceleration_x
# acceleration_y
# acceleration_z
# velocity_x
# velocity_y
# velocity_z
# angular_velocity_x
# angular_velocity_y
# angular_velocity_z
# yaw
# pitch
# roll
# Center of Gravity position (distance from front and rear axis, and height)
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
  # forza out packet struct:
  # https://forums.forzamotorsport.net/turn10_postst128499_Forza-Motorsport-7--Data-Out--feature-details.aspx
  # forza python api:
  # https://github.com/nettrom/forza_motorsport
  # speed hack guy:
  # https://www.unknowncheats.me/forum/members/2246238.html?__cf_chl_captcha_tk__=6b247b85de859926cbd99a3bc187d1c5a8572b45-1590791366-0-AXFqaQcJrtl6BQyn3G8YqvM-Jw1VNLIrNac_cz_5QXAM9_DLxV9gXb4a3vIfZNjQ2VTv2SgSlPT1ymCw8OK4f0i4D7Db0-Q2ljw8jtaWRZItStJj4m71hnvZBZ2Jq2VeotY3WT31b8ySULN3SBkywox8JMtHrXViI0DMx1NQmyAWA3KO8fmUSbDYIqStwQBIHZqMLKev_c9igmuf728CNe-vG2KCX1CLFj8nHfd7FgHnW298-5TONQZPrYIsdwtlhhJddtf90erRzDQ2ttYTe3wT1YhYqOoUF1oHIcYqPgbVXkSRb4cVAhykYt5tBAugVu6AIIyoIYNeVfCmoDNHKTMVZ_nCWzschQ1aSwy9UkqXTdbq0N6d8G48kabBa2J34tw4-xgECuKCemMbP-x2VstvgcCjrC20TXgJwjMDsmupm6087Gw1c8Blz5hjbaXdhLHc5-rdhuWhhtzIXRCCAtBJaHQKm3kRWwgeQKTBrk1lpJqKGzZ9cObU3CK6tFD9WFJpXUNcVr5etsWcPD_12KWKWzZ9pJDkvB13xWtQk4smHQPlvs4W_9fZIg3rOOH-nxAB4yAMKbviUPPnRI-EE4Q
  
  pass