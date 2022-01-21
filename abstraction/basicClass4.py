class Person:

    def __init__(self,full_name):
        self.full_name = full_name
        self.restaurants = []

    def add_restaurant(self,restaurant):
        self.restaurants.append(restaurant)

    def get_restaurants(self):
        return self.restaurants

    def get_favorite_restaurant(self):
        best = -1
        favorite = Restaurant("","","$",-1)
        for r in self.restaurants:
            if r.rating > best:
                best = r.rating
                favorite = r
        return favorite

    # def __str__(self):
    #     return f"{self.full_name} is a {self.__class__}"

class Restaurant:

    def __init__(self,name,cuisine,price,rating):
        self.name=name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name

adam = Person("Adam Hayes")
print(adam)
print(adam.full_name)

big_judds = Restaurant("Big Judd's","American","$",4)
adam.add_restaurant(big_judds)
pizza_hut = Restaurant("Pizza Hut","Pizza","$",3)
adam.add_restaurant(pizza_hut)


print(adam.get_restaurants())
print(f"{adam.full_name}'s favorite restaurant is {adam.get_favorite_restaurant()}")

heather = Person("Heather Purser")
print(heather)
print(heather.full_name)