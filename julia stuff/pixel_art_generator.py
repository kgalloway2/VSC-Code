# Pixel art generator (suggested implementation: any programming language you want to master). 
# Build a tool that takes an image as input and samples the image to produce pixel art as output. 

# this is to generate the colors I need for the palette

palette = []

inc_list = [0.0, 0.33, 0.66, 1.0]

for a in inc_list:
    for b in inc_list:
        for c in inc_list:
            palette.append((a,b,c))

for i in palette:
    print("RGB{N0f8}",i,",")
