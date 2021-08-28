from libs.genrecord import gen_records

f = open("stockdata.bin", "rb")
for name, shares, price in gen_records("<8sif", f):
    # Process data
    pass
