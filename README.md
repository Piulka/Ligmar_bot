## Ligmar_bot
# Бот в данный момент умеет:
1. Запуск производить с точки респа на 25 локации
2. Первыйм делом ищет клетки с чампами вокруг себя, если не нашел, то ищет клетки с алтарями и сундуками, после клетки с 1 мобом, если и тех не нашел, то нападает на 2 мобов.
3. Использует скилы война:
    * При вступлении в бой, использует удар-стан
    * Если не наложен бафф защиты - накладывает
    * Потом по очереди пинок и панч, пока не убьет всех мобов на клетке
    * Если хп меньше заданного - использует сразу хилку и скилл-хилл
    * Если маны меньше чем на использовании баффа защиты - использует хилку
    * При вступлении в бой с чампом - юзает вторй скилл защиты (который на короткое время)
4. Если во время боя персонаж умер - идет в город, ищет 25 локацию и заходит на нее, далее воюет
5. Если инвентарь забился - использует портал, все фиолетовые шмотки складирует на склад, остальные продает и возвращается на склад
6. Таблица в консоле с онлаин обновлением, которая показывает:
 * Кол-во найденных алтарей
 * Кол-во найденных сундуков
 * Кол-во зачищенных клеток с 1 мобов
 * Кол-во зачищенных клеток с 2 мобами
 * Кол-во зачищенных клетом с чампами
 * Сколько фиолок отправил на склад
 * Сколько раз сходил в магазин чтобы все продать
 * Кол-во смертей
 * Общее время работы скрипта
 7. Если скрипт застревает и не находит цели - телепортируется в город и заного заходит на локацию

# Особенности использования:
1. Все координаты поиска изображения поделенные на 2 (в свзи с тем, что у меня эти координаты по дефолту умножаются на 2). При необходимости нужно убрать логику деления координат (в mob_actions убрать //= 2 и в image_utils убрать // 2).
2. Все изображения в папке - взятые с моего экрана с моим разрешение. При необходимости сделать все скрины со своего экрана и заменить изображения.
3. Комбинация клавиш для остановки скрипта установленна на Mac систему. При необходимости нужно cmd заменить на ctrl или заменить комбинацию клавишь на свою (в keyboard_utils).
4. Путь к папке с изображениями заменить на свой (в image_utils).
5. Разрешение игры должно может изменяться в зависимости от маштабируемости окна, советую оставить стандартный масштаб, но удленнить вниз до того момента, пока не будет увеличиваться масштаб.
    * В mob_actions заменить pyautogui.scroll(-100, x=1285, y=586) на свои координаты и длину скролла(исходя из своего разрешения). Координаты можно проверить скриптом coord.py
6. В main изменить значение в обновлении ценира зоны, скриптом coord_pixel померить от центра кнопки открытия карты, до центра клетки где стоит персонаж, при этом заранее отцентровать его, вписать разницу значений заместо 170

 # Дополнительные скрипты:
 1. coord_pixel.py - показывает координаты места, где установлен курсов (после нажатия на Enter)
 2. image.py - показывает наличие изображения на экране и показывает точность (до еденицы) (путь к изображению изменить на свой)
 3. colour_pixel.py - показывает цвет пикселя