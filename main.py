from tasks import add

result = add.delay(4, 6)
print('Görev sıraya alındı:', result)
print('Görev sonucu:', result.get(timeout=10))
