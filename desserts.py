"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def __init__(self, name, flavor, price):
      """Initializing"""
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      self.cache[name] = self


    def add_stock(self, amount):
      """Add cupcakes by given amount to quantity"""

      self.qty += amount


    def sell(self, amount):
      """Sell the given amount of cupcakes and update quantity"""

        #make sure quantity amount never goes below zero 
        #if no cupcakes print sold out 
        #sell cupcakes and update self.qty

      if self.qty == 0:
        print("Sorry, these cupcakes are sold out")
        return

      if self.qty < amount:
        self.qty = 0
        return

      self.qty -= amount


    @staticmethod
    def scale_recipe(ingredients, amount):
      """Scale the list of ingredients by the given amount of cupcakes"""
     
     #ingredients is a list of tuples with ing name and quantity
     #Calling a static method: Cupcake.scale_recipe([('flour', 1), ('eggs', 3), 2])

      for ingredient_name, ingredient_qty in ingredients:
        ingredients = (ingredient_name, ingredient_qty * amount)

      return ingredients


    @classmethod
    def get(cls, name):
      """Return a cupcake from cache dictionary"""
      #if name doesn't exist then print non existant 

      if name not in cache: 
        print("Sorry, that cupcake doesn't exist")
        return

      return cls.cache[name]



if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
