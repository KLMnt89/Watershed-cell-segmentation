import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Креирај output папка ако не постои
os.makedirs("../images/output", exist_ok=True)

# Вчитај ја сликата
img = cv2.imread("../images/input/img.png")

# grayscale (едноканална слика)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Примени гаусово заматување
blur = cv2.GaussianBlur(gray, (5, 5), 0)  # отстранување на шумови (кернел, стандардна девијација)

# Otsu бинаризација
ignore, thresh = cv2.threshold(blur, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # thresh - бинаризирана слика (пикселите се или бели или црни)

# Морфолошко затворање
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)  # да се пополнат мали дупки или празнини

# Distance transform
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)  # за секој пиксел колку е далеку од најблискиот пиксел

# Бинаризација на distance map со помала вредност за подобро разделување
ignore, sure_fg = cv2.threshold(dist_transform, 0.4 * dist_transform.max(), 255,
                                0)  # максималната вредност од целата слика
sure_fg = np.uint8(sure_fg)  # ги конвертира сите пиксели во 8-битни цели броеви

# Позадина
sure_bg = cv2.dilate(closing, kernel, iterations=3)  # ја зголемува светлата област

# Нејасна зона
unknown = cv2.subtract(sure_bg, sure_fg)  # област каде не сме сигурни дали припаѓаат на клетките или на позадината

# Маркери за watershed
ignore, markers = cv2.connectedComponents(sure_fg)  # пребројува поврзани компоненти
markers = markers + 1  # watershed алгоритмот користи 0 за означување на „непознатата" област па затоа поместуваме се за +1
markers[unknown == 255] = 0  # пиксели кои треба да се обработат посебно

# Примена на watershed
markers = cv2.watershed(img, markers)

# Исцртани рабови на клетките на слика која е копија
img_ws = img.copy()
img_ws[markers == -1] = [0, 0, 255]  # рабовите со црвена боја каде што алгоритмот ги поставил границите

# Броење на клетки (ги игнорираме маркерите: позадина (1) и рабовите (-1))
unique_labels = np.unique(markers)
num_cells = len(unique_labels[(unique_labels != 1) & (unique_labels != -1)])

# Зачувај ги сликите одделно
cv2.imwrite("../images/output/original.png", img)
cv2.imwrite("../images/output/watershed_result.png", img_ws)

# Прикажи резултати
plt.figure(figsize=(14, 7))

# Првиот прозорец - оригинална слика
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Оригинална слика", fontsize=20, fontweight='bold')
plt.axis('off')
plt.grid(False)

# Вториот прозорец - слика со watershed сегментација
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_ws, cv2.COLOR_BGR2RGB))
plt.title(f"Watershed сегментација\nБрој на клетки: {num_cells}", fontsize=20, fontweight='bold')
plt.axis('off')
plt.grid(False)

plt.tight_layout(pad=3)
plt.savefig("../images/output/comparison.png", dpi=150, bbox_inches='tight')
plt.show()