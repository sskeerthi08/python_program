import glob

read_files = glob.glob("*.json")
with open("merge1.json", "w") as outfile:
    outfile.write('{}'.format(
        ','.join([open(f, "r").read() for f in read_files])))
