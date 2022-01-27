from ircamera import Camera

ircamera = Camera('20112117.xml')
ircamera.read_settings("Profile 1", "settings.yml")
ircamera.set_dir("./images")
ircamera.set_format("png")
# ircamera.set_radiation_parameters(1.0, 1.0, -2000.0) # Emissivity of 1
ircamera.set_radiation_parameters(0.5, 1.0, -2000.0) # Emissivity of 0.5
ircamera.show(use_colorbar=True, save_csv=True)
