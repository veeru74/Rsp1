i
# Create Iterator and return numbers that strating with one and each sequence will increase ny one:
  class Numbers:
      def __iter__(self): 
          self.a = 1
          return self
      def __next__(self):
          x = self.a
          self.a += 1
          return x
 myclass = Numbers()
 myiter = iter(myclass) 
 print(next(myiter))
 print(next(myiter))
 print(next(myiter))
 print(next(myiter))
 print(next(myiter))
 print(next(myiter))
 print(next(myiter))

