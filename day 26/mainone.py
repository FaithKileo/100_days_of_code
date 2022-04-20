with open("day 26/fileone.txt") as dataone_file:
    data_one = dataone_file.readlines() 
    
with open("day 26/filetwo.txt") as datatwo_file:
    data_two = datatwo_file.readlines()
    

result = [ int(n) for n in data_one if n in data_two ] 
print(result)