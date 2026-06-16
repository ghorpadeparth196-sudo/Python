# variable scoop  = where a variable is visible and accesible
# scoop resolution = (LEGB) local -> Enclosed -> Global -> Built-in 

# #local
# def func1():
#     x=1
#     print(x)

# def func2():
#     x=2
#     print(x)

# func1()
# func2()

#Enclosed
def func1():
      x=2
      def func2():
            print(x)
func1()
    


