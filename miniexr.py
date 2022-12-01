import minexr
FILENAME= "20221110_134425642.exr"
fp = open(FILENAME, 'rb')
reader = minexr.load(fp)
rgba = reader.select(['Color.R','Color.G','Color.B','Color.A'])