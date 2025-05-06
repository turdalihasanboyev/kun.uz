```python
from datetime import datetime

datetime.today().strftime("%d-%m-%Y-%H-%M-%S")

# yuqori darajada unikal va lokal timezone ni qo'llamaydi

### Natija: kun-oy-yil-soat-minut-sekund

datetime.now().strftime("%d-%m-%Y")

# pastroq darajada unikal va lokal timezone ni qo'llaydi

### Natija: kun-oy-yil
```
