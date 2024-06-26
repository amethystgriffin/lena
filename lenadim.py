import cv2
import matplotlib.pyplot as plt

# Carrega a imagem
imagem_colorida = cv2.imread('lena_color.png')

# Converte a imagem para níveis de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Converte a imagem para preto e branco (binariza)
_, imagem_preto_branco = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Exibe as imagens usando matplotlib
plt.figure(figsize=(10, 5))

# Imagem colorida
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB))
plt.title('Imagem Colorida')
plt.axis('off')

# Imagem em níveis de cinza
plt.subplot(1, 3, 2)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Níveis de Cinza')
plt.axis('off')

# Imagem em preto e branco
plt.subplot(1, 3, 3)
plt.imshow(imagem_preto_branco, cmap='gray')
plt.title('Imagem Preto e Branco')
plt.axis('off')

plt.tight_layout()
plt.show()
