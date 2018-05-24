import codecs, json, sys

data = []
i = 0

read_file = sys.argv[1]
output_file = sys.argv[2]

with codecs.open(read_file, 'rU', 'utf-8') as f:
		for line in f:
			strr = json.loads(line)
			strr = str(strr)
			data.append(strr)
			sp = strr.split(',')
			
			etc = ""
			for i in range(len(sp)):
				sp[i] = str(sp[i])
				if "LAT" in sp[i]:
					LAT = sp[i].split(':')[1]
				elif "LNG" in sp[i]:
					LNG = sp[i].split(':')[1]
				else:
					etc = etc + sp[i]
					if i != len(sp) -1:
						etc = etc + ", "
			if LAT != "" and LNG != "":
				location = "{ location : { type: 'Point', coordinates:[" + LNG + ", " + LAT+"]}," + etc
				location = location.replace("'", "\"")
			
			with open(output_file, 'a') as file:
				file.write(location+'\n')

			i = i+1
