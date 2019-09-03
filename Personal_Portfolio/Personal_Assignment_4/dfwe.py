waterRband = dataset[3:4, 1179:1195, 23:57]      # water feature in red band
waterGband = dataset[2:3, 1179:1195, 23:57]      # water feature in green band
waterBband = dataset[1:2, 1179:1195, 23:57]      # water feature in blue band
waterNIRband = dataset[7:8, 1179:1195, 23:57]    # water feature in Near Infrared band

# vegetation matrix in red, green, blue and NIR bands
vegRband = dataset[3:4, 605:660, 1044:1087]      # vegetation feature in red band
vegGband = dataset[2:3, 605:660, 1044:1087]      # vegetation feature in green band
vegBband = dataset[1:2, 605:660, 1044:1087]      # vegetation feature in blue band
vegNIRband = dataset[7:8, 605:660, 1044:1087]    # vegetation feature in Near Infrared band

# urban matrix in red, green, blue and NIR bands
urbanRband = dataset[3:4, 791:817, 277:307]      # urban feature in red band
urbanGband = dataset[2:3, 791:817, 277:307]      # urban feature in green band
urbanBband = dataset[1:2, 791:817, 277:307]      # urban feature in blue band
urbanNIRband = dataset[7:8, 791:817, 277:307]    # urban feature in Near Infrared band