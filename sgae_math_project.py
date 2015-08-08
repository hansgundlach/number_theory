x,y = var('x,y')
html("<h1>triple integrater<h1>")
permutations = ["dx dy","dy dx"]
@interact

def  interplay(order= permutations,function= input_box(sin(x)),lower_x_bound= input_box(0),upper_x_bound = input_box(1),lower_y_bound=input_box(0),upper_y_bound=input_box(1),showGraph = checkbox(default = True)):
     if permuatations = "dx,dy":
         result = function.integrate(x,lower_x_bound,upper_x_bound).integrate(y,lower_y_bound,upper_y_bound)
     else:
        result =  function.integrate(y,lower_y_bound,).integrate(x,lower_x_bound,upper_x_bound)
    
    
    
    
     graph = plot3d(function,(x,lower_x_bound,upper_x_bound),(y,lower_y_bound,upper_y_bound),fill=True,color = "orange",spin = 4)
     if showGraph == True :
          
          html("<h3>Graph of Integrated Region</h3>")
          show(graph)
     html("<h3>Numerical Result</h3>")
     show(result)
html("<p> Created by Hans Gundlach </p>")
