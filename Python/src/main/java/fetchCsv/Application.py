from urllib import request
csvUrl = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
def downloadFile(url):
    response = request.urlopen(url)
    lines = str(response.read()).split('\\r');
    file = open('csvFile.csv', 'w')
    for line in lines:
        file.write(line + '\n')
    file.close()
downloadFile(csvUrl)