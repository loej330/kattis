for _ in range(int(input())):
   M, B, D, T = [ float(input()) for _ in range(4) ]
   
   g = 5.5 + M*T # Describes equation of circle
   x = 5.5/M + T # midpoint of circle on x-axis
   a = M**2 + B**2 # 'a' term of quadratic

   def col(h): # intersection between max's circle and a line
      b = -2*M*g + 2*B*h # 'b' term of quadratic
      c = g**2 + h**2 - 0.25 # 'c' term of quadratic
      return b**2 - 4*a*c >= 0 # does quadratic equation have a solution

   def run():
      H = [ ((-D - 4*i), (-D - 4*i - 2)) for i in range(10) ]
      X = [ ((-h0 / B), (-h1 / B)) for h0, h1 in H ]
      if x < X[0][0] and not col(H[0][0]): return "Max beats the first bicycle"
      for i in range(10):
         if col(H[i][0]) or col(H[i][1]): return f'Collision with bicycle {i+1}'
      for i in range(9,0,-1):
         if x > X[i][1]: return f'Max crosses safely after bicycle {i+1}'
   print(run())