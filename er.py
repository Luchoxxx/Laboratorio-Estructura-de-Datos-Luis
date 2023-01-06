def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Prueba del código

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(30))

