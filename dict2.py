biodata={"name":"puja","middle_name":"khumansangbhai",\
         "fruit":["mango","graps","orange","apple"],\
            "district":"bhavnagar","weight":50}
vegs=["potato","tomato","onion"]
veg1=dict.fromkeys(vegs)
print(veg1)
print(veg1.get('tomato'))
veg1['potato']='20kg'
veg1['tomato']='50kg'
veg1['onion']='30kg'
print(veg1)
print(veg1.items())

print(veg1.get('banana',"not available"))
veg2=veg1.copy()
print(veg2)
print(biodata.pop('middle_name'))
print(biodata)
print(biodata.popitem())
print(biodata)
print(biodata.popitem())
print(biodata)
biodata.update({'District':"surat"})
print(biodata)
print(biodata.keys())
print(biodata.values())

biodata.clear()
print(biodata)