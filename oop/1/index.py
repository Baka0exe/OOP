class Goods:
    title = "Мороженое"
    weight = 151
    tp = "Еда"
    price = 12321

Goods_one = Goods()
Goods_two = Goods()

print ("one:")

print(Goods_one.weight)
print(Goods_one.price)

Goods_two.weight = 100
Goods_two.price = 12232

print ("two:")

print(Goods_two.weight)
print(Goods_two.price)


class Car:
    model = None
    color = None
    number = None


Car.model = "Тойота"
Car.color = "Черный"
Car.number = "П34А123"


print (Car.__dict__)