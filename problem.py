for _ in range(int(input())):
   M, B, D, T = [float(input()) for _ in range(4)]
   print(_)
   
   g = 5.5 + M*T # Describes equation of circle
   xc = 5.5/M + T # midpoint of circle on x-axis
   a = M**2 + B**2 # 'a' term of quadratic

   def line_circle(h):
      b = -2*M*g + 2*B*h # 'b' term of quadratic
      c = g**2 + h**2 - 0.25 # 'c' term of quadratic
      return b**2 - 4*a*c >= 0 # does quadratic equation have a solution

   h = -D # head of the first bike
   x = -h / B # when first bike reaches line 

   if not line_circle(h) and xc < x: 
      print("Max beats the first bicycle")
      continue

   for i in range(1,10):
      h0 = -D -4*(i-1) -2 # tail of previous bike
      x0 = -h0 / B # when previous bike leaves line
      h1 = -D -4*i # head of current bike
      x1 = -h1 / B # when current bike reaches line

      if line_circle(h0): print(f'Collision with bicycle {i+1}'); break 
      if line_circle(h1): print(f'Collision with bicycle {i+2}'); break
      if x0 < xc < x1: print(f'Max crosses safely after bicycle {i+1}'); break

   h = -D -4*9 -2 # tail of last bike
   x = -h / B # when last previous bike leaves line
   if not line_circle(h) and x < xc:
      print(f'Max crosses safely after bicycle 10')
      
      
   
