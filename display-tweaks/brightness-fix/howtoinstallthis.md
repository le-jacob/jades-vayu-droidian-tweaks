Another goofy solution to a goofy problem.
Why this patch when the phone already has high enough brightness? Well when you move the brightness slider, the display will get very dim, and its pretty much unfixable unless you restart the phone.
The "phosh-brightness-patch.py" script basically runs the script of "/usr/bin/droidian-adapt-fix-phosh-brightness-xiaomi-vayu.sh", but continuously, with an option to change the brightness to your liking.

# PRE-REQUISITIES
- Poco X3 Pro with Droidian (of course)
- Root access (need to install the service)

# HOW TO INSTALL
1. Open a terminal window (or ssh into the phone if enabled)
2. Download everything
3. Move the "brightnessfix.service" and "phosh-brightness-patch.py" into a place that you won't delete (i recommend: /root/.scripts/)
4. In case you move files elsewhere than my recommended directory, modify the "Exec=" part of the service file to run "phosh-brightness-patch.py" in the place you moved it to.
5. Run 'systemctl disable droidian-adapt-fix-phosh-brightness-xiaomi-vayu' and 'systemctl stop droidian-adapt-fix-phosh-brightness-xiaomi-vayu' to prevent conflict. (As root)
6. And finally run 'systemctl enable /root/.scripts/brightnessfix.service' (As root)
## You have now (probably) finished the basic setup, now when you accidentally dim the display, it will come back to 100% in a few seconds!
### You definetly want to control the brightness of course.. so follow this.
1. Move "phosh-brightness-patch-gui.py" to some place (i recommend: /home/droidian/Programs/)
2. Move "brightness_control.desktop" to "/usr/share/applications" (the place where app shortcuts exist)
3. In case you move the GUI script elsewhere, change the "Exec=" part of the desktop file to the place of "phosh-brightness-patch-gui.py".
4. Pray that this goofy ass solution works
