class MyFormulas:
    def square(self,num):
        print(f'Square is {num*num}')


    def area_of_circle(self,r):
        print(f'Area of circle is {3.1416*r**2}') 


obj1 = MyFormulas()
obj1.area_of_circle(5)
obj1.square(10)