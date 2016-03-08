#############################################################
#Создание айтемов
#############################################################
init python:
    #Cоздание предметов
    napkin = Tool(purpose = 'clean')
    napkin.name = _('Салфетка')
    napkin.cost = 100
    napkin.picto = 'pic/items/napkin.jpg'
    napkin.durability = 10
    napkin.type = 'tool'
    
    mat = Tool(purpose = 'clean')
    mat.name = _('Циновка')
    mat.cost = 1500
    mat.picto = 'pic/items/mat.jpg'
    mat.durability = 1000
    mat.type = 'hidden'
    
    clubPanties = Tool(purpose = 'sell')
    clubPanties.name = _('Поношенные трусики')
    clubPanties.cost = 100
    clubPanties.picto = 'pic/items/clubPanties.jpg'
    clubPanties.durability = 10
    clubPanties.type = 'tool'
    
    camera = Tool(purpose = 'camera')
    camera.name = _('Камера')
    camera.cost = 2000
    camera.picto = 'pic/items/camera.png'
    camera.durability = 100
    camera.type = 'tool'
    
    sandwich = Food( energy = 250 )
    sandwich.name = _('Сэндвич')
    sandwich.cost = 0
    sandwich.picto = 'pic/items/sandwich.jpg'
    sandwich.durability = 1
    sandwich.type = 'food'

    eDrink = Food(energy = 100)
    eDrink.name = _('Энергетик')
    eDrink.cost = 150
    eDrink.picto = 'pic/items/edrink.jpg'
    eDrink.durability = 1
    eDrink.type = 'food'
    
    tablet = Food(energy = -50)
    tablet.name = _('Таблеточка')
    tablet.cost = 150
    tablet.picto = 'pic/items/tablet.jpg'
    tablet.durability = 1
    tablet.type = 'lust'
    
    rawFood = Food(energy = 400)
    rawFood.name = _('Сырая еда')
    rawFood.cost = 500
    rawFood.picto = 'pic/items/food.jpg'
    rawFood.durability = 10
    rawFood.type = 'hidden'
    
    
    
    allItems = [napkin, sandwich, eDrink, rawFood, clubPanties]

    # Создание подарков
    textBook = Present(
        name = 'Набор учебников',
        sex = 'any',
        cost = 1000,
        reputation = 10,
        picto = 'pic/items/textBook.jpg',
        durability = 90
    )
    allItems.append(textBook)
    
    helicopter = Present(
        name = 'Вертолётик',
        sex = 'male',
        cost = 2000,
        loy = 10,
        picto = 'pic/items/helicopter.jpg',
        durability = 30
    )
    allItems.append(helicopter)
    
    pneumatics = Present(
        name = 'Пневматика',
        sex = 'male',
        cost = 5000,
        loy = 25,
        picto = 'pic/items/pneumatics.jpg',
        durability = 90
    )
    allItems.append(pneumatics)
    
    ring = Present(
        name = 'Золотое кольцо',
        sex = 'female',
        cost = 2000,
        loy = 10,
        picto = 'pic/items/ring.jpg',
        durability = 30
    )
    allItems.append(ring)
    
    perfume = Present(
        name = 'Элитные духи',
        sex = 'female',
        cost = 5000,
        loy = 25,
        picto = 'pic/items/perfume.jpg',
        durability = 90
    )
    allItems.append(perfume)
    
# Создание айтемов сексшопа
    aphrodisiac = Tool(purpose = 'aphrodisiac')
    aphrodisiac.name = _('Лёгкий афродизиак')
    aphrodisiac.cost = 200
    aphrodisiac.picto = 'pic/items/aphrodisiac.jpg'
    aphrodisiac.durability = 1
    aphrodisiac.type = 'sexShop'
    allItems.append(aphrodisiac)
    
    rope = Tool(purpose = 'qwest')
    rope.name = _('Грубая верёвка')
    rope.cost = 100
    rope.picto = 'pic/items/rope.png'
    rope.durability = 1
    rope.type = 'sexShop'
    allItems.append(rope)

    chloroform = Tool(purpose = 'qwest')
    chloroform.name = _('Хлороформ')
    chloroform.cost = 10000
    chloroform.picto = 'pic/items/chloroform.png'
    chloroform.durability = 1
    chloroform.type = 'sexShop'
    allItems.append(chloroform)
    
#######################################################################
#  Верхняя одежда
#######################################################################
    clothing = []
    
    jaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    jaket.cover = ['верх']
    jaket.durability = 100
    jaket.name = _('Пиджак')
    jaket.cost = 1500
    jaket.picto = 'pic/items/jaket.png'
    jaket.type = 'clothing'
    jaket.description = _('Обычный, довольно строгий пиджак. Прекрасно влияет на репутацию, если вас в нём видят.')
    clothing.append(jaket)
    
    freejaket = Clothing(
    lust = 10,
    corr = 25,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    freejaket.cover = ['верх']
    freejaket.durability = 100
    freejaket.name = _('Пиджак с вырезом')
    freejaket.cost = 2500
    freejaket.picto = 'pic/items/freejaket.png'
    freejaket.type = 'clothing'
    freejaket.description = _('Свободный пиджак. Очень свободный и с глубоким декольте. Выглядит сексуально.')
    clothing.append(freejaket)
    
    skimpyjacket = Clothing(
    lust = 25,
    corr = 50,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpyjacket.cover = ['верх']
    skimpyjacket.durability = 50
    skimpyjacket.name = _('Полоски ткани')
    skimpyjacket.cost = 5500
    skimpyjacket.picto = 'pic/items/skimpyjacket.png'
    skimpyjacket.type = 'clothing'
    skimpyjacket.description = _('Довольно дорогой топ, который скорее подчёркивает выше грудь, нежели скрывает её. Выглядит весьма вызывающе.')
    clothing.append(skimpyjacket)
    
#############################################################

    studstrictjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'strict')
    studstrictjaket.cover = ['верх']
    studstrictjaket.durability = 10000
    studstrictjaket.name = _('Девчачий строгий пиджак')
    studstrictjaket.cost = 1500
    studstrictjaket.picto = 'pic/items/studstrictjaket.png'
    studstrictjaket.type = 'clothing'
    studstrictjaket.description = _('Строгий пиджачок, тщательно скрывающий все половые признаки.')
    clothing.append(studstrictjaket)
 
    studjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'uniform')
    studjaket.cover = ['верх']
    studjaket.durability = 10000
    studjaket.name = _('Девчачий пиджак')
    studjaket.cost = 1500
    studjaket.picto = 'pic/items/studjaket.png'
    studjaket.type = 'clothing'
    studjaket.description = _('Обычный школьный пиджак. Кто то считает его сексуальным, но сами ученики - нет.')
    clothing.append(studjaket)
    
    studsexyjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    studsexyjaket.cover = ['верх']
    studsexyjaket.durability = 10000
    studsexyjaket.name = _('Сексуальный пиджачок')
    studsexyjaket.cost = 1500
    studsexyjaket.picto = 'pic/items/studsexyjaket.png'
    studsexyjaket.type = 'clothing'
    studsexyjaket.description = _('Симпатичный пиджачок с большим вырезом внизу. Открывает сексуальный вид на плоский животик девушки.')
    clothing.append(studsexyjaket)
    
    studskimpyjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    studskimpyjaket.cover = ['верх']
    studskimpyjaket.durability = 10000
    studskimpyjaket.name = _('Что-то невесомое')
    studskimpyjaket.cost = 1500
    studskimpyjaket.picto = 'pic/items/studskimpyjaket.png'
    studskimpyjaket.type = 'clothing'
    studskimpyjaket.description = _('Нужна замена картинки')
    clothing.append(studskimpyjaket)
    
    studDress = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studDress.cover = ['верх','низ']
    studDress.durability = 10000
    studDress.name = _('Простое платье')
    studDress.cost = 1500
    studDress.picto = 'pic/items/studDress.png'
    studDress.type = 'clothing'
    studDress.description = _('Нужна замена картинки')
    clothing.append(studDress)
    
    studHarness = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'bdsm')
    studHarness.cover = ['верх','низ']
    studHarness.durability = 10000
    studHarness.name = _('Кожанная сбруя')
    studHarness.cost = 1500
    studHarness.picto = 'pic/items/studHarness.png'
    studHarness.type = 'clothing'
    studHarness.description = _('Кожанные, клёпанные полоски плотно обхватывающие тело ученицы. Они скорее подчёркивают формы школьницы, нежели скрывают их.')
    clothing.append(studHarness)
    
    studJaketM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'uniform')
    studJaketM.cover = ['верх']
    studJaketM.durability = 10000
    studJaketM.name = _('Мужской пиджак')
    studJaketM.cost = 1500
    studJaketM.picto = 'pic/noimage.gif'
    studJaketM.type = 'clothing'
    studJaketM.description = _('Простой школьный пиджак. Ничем не выделяется.')
    clothing.append(studJaketM)
    
    studStrictJaketM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'strict')
    studStrictJaketM.cover = ['верх']
    studStrictJaketM.durability = 10000
    studStrictJaketM.name = _('Строгий пиджак')
    studStrictJaketM.cost = 1500
    studStrictJaketM.picto = 'pic/noimage.gif'
    studStrictJaketM.type = 'clothing'
    studStrictJaketM.description = _('Строгий, бесформенный гкольный пиджак. В нём ученик выглядит как ботан и совсем не вызывает никакого желания.')
    clothing.append(studStrictJaketM)
    
    # studJaketM = Clothing(
    # lust = 0,
    # corr = 0,
    # reputation = 1,
    # char = 'stud',
    # sex = 'male',
    # purpose = 'uniform')
    # studJaketM.cover = ['верх']
    # studJaketM.durability = 10000
    # studJaketM.name = _('Школьный пиджак')
    # studJaketM.cost = 1500
    # studJaketM.picto = 'pic/noimage.gif'
    # studJaketM.type = 'clothing'
    # studJaketM.description = _('Тут будет красивое описание предмета')
    # clothing.append(studJaketM)
    
    tShirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    tShirt.cover = ['верх']
    tShirt.durability = 10000
    tShirt.name = _('Футболка')
    tShirt.cost = 1500
    tShirt.picto = 'pic/noimage.gif'
    tShirt.type = 'clothing'
    tShirt.description = _('Обычная футболка для обычного дня. Многим нравится, и вы не исключение.')
    clothing.append(tShirt)
    
    studLeather = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'bdsm')
    studLeather.cover = ['верх','низ']
    studLeather.durability = 10000
    studLeather.name = _('Кожанная сбруя')
    studLeather.cost = 1500
    studLeather.picto = 'pic/noimage.gif'
    studLeather.type = 'clothing'
    studLeather.description = _('Металлические кольца удерживают кожанные ремни, обхватывающие тело ученика. Чёрный Властелин был бы в восторге!')
    clothing.append(studLeather)
    
#############################################################
    
#######################################################################
#  Нижняя одежда  
#######################################################################     
    longSkirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    longSkirt.cover = ['низ']
    longSkirt.durability = 100
    longSkirt.name = _('Длинная юбка')
    longSkirt.cost = 1000
    longSkirt.picto = 'pic/items/longSkirt.png'
    longSkirt.type = 'clothing'
    longSkirt.description = _('Длинная, строгая юбка до колен. Подчёркивает вашу строгость и власть.')
    clothing.append(longSkirt)

    shortSkirt = Clothing(
    lust = 10,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    shortSkirt.cover = ['низ']
    shortSkirt.durability = 75
    shortSkirt.name = _('Короткая юбка')
    shortSkirt.cost = 1000
    shortSkirt.picto = 'pic/items/shortSkirt.png'
    shortSkirt.type = 'clothing'
    shortSkirt.description = _('Короткая юбка до середины бедра, которая замечательно подчёркивает ваши прямые ноги. Выглядит сексуально.')
    clothing.append(shortSkirt)
    
    skimpySkirt = Clothing(
    lust = 30,
    corr = 50,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpySkirt.cover = ['низ']
    skimpySkirt.durability = 50
    skimpySkirt.name = _('Широкий пояс')
    skimpySkirt.cost = 1000
    skimpySkirt.picto = 'pic/items/skimpySkirt.png'
    skimpySkirt.type = 'clothing'
    skimpySkirt.description = _('Это скорее не юбка, а просто широкий пояс. Вы уверены, что прохожие видят вашу задницу, даже если вы не наклоняетесь.')
    clothing.append(skimpySkirt)
    
#############################################################

    studstrictskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'strict')
    studstrictskirt.cover = ['низ']
    studstrictskirt.durability = 10000
    studstrictskirt.name = _('Длинная строгая юбка')
    studstrictskirt.cost = 1500
    studstrictskirt.picto = 'pic/noimage.gif'
    studstrictskirt.type = 'clothing'
    studstrictskirt.description = _('Длинная, строгая юбка почти до щиколоток. Это бесформенное произведение сумрачного немецкого гения отпугивает даже сексуальных маньяков.')
    clothing.append(studstrictskirt)
 
    studskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'uniform')
    studskirt.cover = ['низ']
    studskirt.durability = 10000
    studskirt.name = _('Школьная юбка до колен')
    studskirt.cost = 1500
    studskirt.picto = 'pic/items/studskirt.png'
    studskirt.type = 'clothing'
    studskirt.description = _('Симпатичная школьная юбка. Как у всех. Не вызывает ни у окружающих, ни у учеников никаких эмоций.')
    clothing.append(studskirt)
    
    studsexyskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    studsexyskirt.cover = ['низ']
    studsexyskirt.durability = 10000
    studsexyskirt.name = _('Короткая школьная юбка')
    studsexyskirt.cost = 1500
    studsexyskirt.picto = 'pic/items/studsexyskirt.png'
    studsexyskirt.type = 'clothing'
    studsexyskirt.description = _('Короткая юбчёнка, едва прикрывающая попу. Выглядит сексуально.')
    clothing.append(studsexyskirt)
    
    studskimpyskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    studskimpyskirt.cover = ['низ','попа']
    studskimpyskirt.durability = 10000
    studskimpyskirt.name = _('Она называет этот пояс юбкой')
    studskimpyskirt.cost = 1500
    studskimpyskirt.picto = 'pic/items/studskimpyskirt.png'
    studskimpyskirt.type = 'clothing'
    studskimpyskirt.description = _('Ничего не скрывающий пояс. Если забыть надеть трусы, то скандал с голыми ученицами в школе обеспечен.')
    clothing.append(studskimpyskirt)
    
    studPants = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    studPants.cover = ['низ']
    studPants.durability = 10000
    studPants.name = _('Брюки')
    studPants.cost = 1500
    studPants.picto = 'pic/noimage.gif'
    studPants.type = 'clothing'
    studPants.description = _('Простые брюки. Популярны среди мужчин с 19 века.')
    clothing.append(studPants)
    
    studShorts = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'sexy')
    studShorts.cover = ['низ']
    studShorts.durability = 10000
    studShorts.name = _('Шорты')
    studShorts.cost = 1500
    studShorts.picto = 'pic/noimage.gif'
    studShorts.type = 'clothing'
    studShorts.description = _('Обычные шорты. Прекрасно подходят для прогулок в летнюю погоду.')
    clothing.append(studShorts)

#######################################################################
#  Колготки     
#######################################################################     
    browntights = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    browntights.cover = ['ноги']
    browntights.durability = 10
    browntights.name = _('Телесные колготки')
    browntights.cost = 150
    browntights.picto = 'pic/items/browntights.png'
    browntights.type = 'clothing'
    browntights.description = _('Колготки бежевого оттенка. Классические. Как мама рекомендовала.')
    clothing.append(browntights)

    blacktights = Clothing(
    lust = 10,
    corr = 10,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    blacktights.cover = ['ноги']
    blacktights.durability = 10
    blacktights.name = _('Чёрные колготки')
    blacktights.cost = 150
    blacktights.picto = 'pic/items/blacktights.png'
    blacktights.type = 'clothing'
    blacktights.description = _('Мама бы не позволила вам одеть их в школу, потому что чёрный цвет на ногах слишком сексуален.')
    clothing.append(blacktights)
    
    nettights = Clothing(
    lust = 20,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    nettights.cover = ['ноги']
    nettights.durability = 10
    nettights.name = _('Колготки в сетку')
    nettights.cost = 450
    nettights.picto = 'pic/items/nettights.png'
    nettights.type = 'clothing'
    nettights.description = _('Большие чёрные квадратики, покрывающие ваши ноги, будут вызывать у мужского населения определённый интерес.')
    clothing.append(nettights)
    
#######################################################################
    socks = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    socks.cover = ['ноги']
    socks.durability = 10000
    socks.name = _('Тёмные носочки')
    socks.cost = 150
    socks.picto = 'pic/items/socks.png'
    socks.type = 'clothing'
    socks.description = _('Тёмные носочки. Довольно обычны и не привлекают внимания.')
    clothing.append(socks)

    whitesocks = Clothing(
    lust = 10,
    corr = 10,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    whitesocks.cover = ['ноги']
    whitesocks.durability = 10000
    whitesocks.name = _('Белые носочки')
    whitesocks.cost = 150
    whitesocks.picto = 'pic/noimage.gif'
    whitesocks.type = 'clothing'
    whitesocks.description = _('Белые носочки. Выглядят весьма сексуально с любой одеждой.')
    clothing.append(whitesocks)
    
    whitetights = Clothing(
    lust = 20,
    corr = 30,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    whitetights.cover = ['ноги']
    whitetights.durability = 10000
    whitetights.name = _('Белые чулки')
    whitetights.cost = 450
    whitetights.picto = 'pic/noimage.gif'
    whitetights.type = 'clothing'
    whitetights.description = _('Чулочки снежного отенка, слегка не доходящие до края юбочки. Способны свести с ума не подготовленного мужчину.')
    clothing.append(whitetights)
    
#######################################################################   
#  Нижнее бельё    
#######################################################################   
    simpleUnderwear = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    simpleUnderwear.cover = ['грудь','попа']
    simpleUnderwear.durability = 20
    simpleUnderwear.name = _('Простое нижнее бельё')
    simpleUnderwear.cost = 300
    simpleUnderwear.picto = 'pic/items/simpleUnderwear.png'
    simpleUnderwear.type = 'clothing'
    simpleUnderwear.description = _('Лифчик и бюстгалтер. Просто и сердито.')
    clothing.append(simpleUnderwear)
    
    sexyUnderwear = Clothing(
    lust = 5,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    sexyUnderwear.cover = ['грудь','попа']
    sexyUnderwear.durability = 20
    sexyUnderwear.name = _('Красивое нижнее бельё')
    sexyUnderwear.cost = 800
    sexyUnderwear.picto = 'pic/items/sexyUnderwear.png'
    sexyUnderwear.type = 'clothing'
    sexyUnderwear.description = _('В кусочки ткани вставлены небольшие верёвочки, которые удерживают конструкцию на вашем теле. Выглядит сексуально.')
    clothing.append(sexyUnderwear)

    skimpyUnderwear = Clothing(
    lust = 15,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpyUnderwear.cover = ['грудь','попа']
    skimpyUnderwear.durability = 20
    skimpyUnderwear.name = _('Сексуальное нижнее бельё')
    skimpyUnderwear.cost = 1500
    skimpyUnderwear.picto = 'pic/items/skimpyUnderwear.png'
    skimpyUnderwear.type = 'clothing'
    skimpyUnderwear.description = _('Практического смысла это бельё не несёт, так как ничего не скрывает, и лишь облегает ваши интимные места по краям, создавая вокруг них кружевное обрамление.')
    clothing.append(skimpyUnderwear)
    
    pantalons = Clothing(
    lust = -20,
    corr = 0,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sleep')
    pantalons.cover = ['попа','низ']
    pantalons.durability = 2000
    pantalons.name = _('Старые шорты')
    pantalons.cost = 10
    pantalons.picto = 'pic/items/pantaloons.png'
    pantalons.type = 'clothing'
    pantalons.description = _('Старые шорты. В них удобно спать. Но выглядят они страшновато, так что на улицу выходить в них не стоит.')
    clothing.append(pantalons)

    oldShirt = Clothing(
    lust = -20,
    corr = 0,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sleep')
    oldShirt.cover = ['грудь','верх']
    oldShirt.durability = 2000
    oldShirt.name = _('Домашняя футболка')
    oldShirt.cost = 10
    oldShirt.picto = 'pic/items/oldShirt.png'
    oldShirt.type = 'clothing'
    oldShirt.description = _('Ваша любимая со студенческих лет футболка. Классная, но, к сожалению, домашняя. Ходить в ней можно, но вас будут воспринимать как неряху.')
    clothing.append(oldShirt)
    
#######################################################################  
    studpantiesF = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studpantiesF.cover = ['попа']
    studpantiesF.durability = 10000
    studpantiesF.name = _('Трусики')
    studpantiesF.cost = 150
    studpantiesF.picto = 'pic/items/studpantiesF.png'
    studpantiesF.type = 'clothing'
    studpantiesF.description = _('Белые трусики. Ничего необычного, у вас есть такие же.')
    clothing.append(studpantiesF)
    
    studSlip = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studSlip.cover = ['грудь']
    studSlip.durability = 10000
    studSlip.name = _('Лифчик')
    studSlip.cost = 150
    studSlip.picto = 'pic/items/studSlip.png'
    studSlip.type = 'clothing'
    studSlip.description = _('Обычный лифчик. Его можно одеть, а можно и не одевать. Вас всегда радовало это разнообразие.')
    clothing.append(studSlip)
 
    studpantiesM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    studpantiesM.cover = ['попа']
    studpantiesM.durability = 10000
    studpantiesM.name = _('Трусы')
    studpantiesM.cost = 150
    studpantiesM.picto = 'pic/noimage.gif'
    studpantiesM.type = 'clothing'
    studpantiesM.description = _('Мужские боксеры. Не прибавиьть ни отнять.')
    clothing.append(studpantiesM)
    
#######################################################################
#  Купальники 
#######################################################################   

    swimsuit = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    swimsuit.cover = ['грудь','попа','верх','низ','ноги']
    swimsuit.durability = 40
    swimsuit.name = _('Купальник')
    swimsuit.cost = 500
    swimsuit.picto = 'pic/items/swimsuit.png'
    swimsuit.type = 'clothing'
    swimsuit.description = _('Купальник одним куском. Был популярен ещё во времена ваших родителей. Сейчас носится только ханжами и родителями.')
    clothing.append(swimsuit)
    
    bikini_top = Clothing(
    lust = 25,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_top.cover = ['грудь','верх']
    bikini_top.durability = 20
    bikini_top.name = _('Бикини верх')
    bikini_top.cost = 500
    bikini_top.picto = 'pic/items/bikini_top.png'
    bikini_top.type = 'clothing'
    bikini_top.description = _('Чёрный топ бикини прекрасно подчёркивающий форму вашей груди. Особенно когда мокрый.')
    clothing.append(bikini_top)

    bikini_bottom = Clothing(
    lust = 25,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_bottom.cover = ['попа','низ','ноги']
    bikini_bottom.durability = 20
    bikini_bottom.name = _('Бикини низ')
    bikini_bottom.cost = 500
    bikini_bottom.picto = 'pic/items/bikini_bottom.png'
    bikini_bottom.type = 'clothing'
    bikini_bottom.description = _('Бикини боттом. Без Губки Боба. Изящно облегает вашу попу, подчёркивая её изгибы.')
    clothing.append(bikini_bottom)
    
    minibikini = Clothing(
    lust = 40,
    corr = 70,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    minibikini.cover = ['грудь','попа','верх','низ','ноги']
    minibikini.durability = 40
    minibikini.name = _('Минибикини')
    minibikini.cost = 2500
    minibikini.picto = 'pic/items/minibikini.png'
    minibikini.type = 'clothing'
    minibikini.description = _('Изобретён для того, чтобы ещё сильнее подчеркнуть вашу наготу на пляже.')
    clothing.append(minibikini)
    
#######################################################################
    studswimsuit = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'swim')
    studswimsuit.cover = ['грудь','попа','верх','низ','ноги']
    studswimsuit.durability = 40000
    studswimsuit.name = _('Полный купальник')
    studswimsuit.cost = 500
    studswimsuit.picto = 'pic/items/studswimsuit.png'
    studswimsuit.type = 'clothing'
    studswimsuit.description = _('Обычный студенческий купальник. Используется во всех школах города.')
    clothing.append(studswimsuit)

    swimShorts = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'swim')
    swimShorts.cover = ['грудь','попа','верх','низ','ноги']
    swimShorts.durability = 40000
    swimShorts.name = _('Шорты для плавания')
    swimShorts.cost = 500
    swimShorts.picto = 'pic/noimage.gif'
    swimShorts.type = 'clothing'
    swimShorts.description = _('Боксеры для плавания. С верёвочками, чтобы не слетели при нырке.')
    clothing.append(swimShorts)
    
#######################################################################
#  Сеты
#######################################################################   

# спортивная форма
    sportUniform = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sport')
    sportUniform.cover = ['верх','низ']
    sportUniform.durability = 300
    sportUniform.name = _('Спортформа')
    sportUniform.cost = 1500
    sportUniform.picto = 'pic/items/sportUniform.png'
    sportUniform.type = 'clothing'
    sportUniform.description = _('Футболочка, шортики и кроссовки. То, что надо для занятий спортом и ежедневных пробежек!')
    clothing.append(sportUniform)
    
# бдсм форма
    bdsmUniform = Clothing(
    lust = 25,
    corr = 50,
    reputation = -5,
    char = 'teacher',
    sex = 'female',
    purpose = 'bdsm')
    bdsmUniform.cover = ['верх','низ','ноги']
    bdsmUniform.durability = 1000
    bdsmUniform.name = _('БДСМ униформа')
    bdsmUniform.cost = 5500
    bdsmUniform.picto = 'pic/items/bdsmUniform.png'
    bdsmUniform.type = 'clothing'
    bdsmUniform.description = _('Безумная смесь из кожи и латекса, облегающая ваше тело. Выглядит... вызывающе.')
    clothing.append(bdsmUniform)
    
#  Форма Мустанговича
    # blueForm = Clothing(
    # lust = 0,
    # corr = 0,
    # reputation = 0,
    # char = 'teacher',
    # sex = 'male',
    # purpose = 'usual')
    # blueForm.cover = ['верх','низ']
    # blueForm.durability = 10000
    # blueForm.name = _('Спортивный костюм')
    # blueForm.cost = 1500
    # blueForm.picto = 'pic/noimage.gif'
    # blueForm.type = 'clothing'
    # blueForm.description = _('Тут будет красивое описание предмета')
    # clothing.append(blueForm)

    manpants = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'male',
    purpose = 'usual')
    manpants.cover = ['попа']
    manpants.durability = 10000
    manpants.name = _('Красные трусы')
    manpants.cost = 1500
    manpants.picto = 'pic/noimage.gif'
    manpants.type = 'clothing'
    manpants.description = _('Неизменный спутник физрука.')
    clothing.append(manpants)
    
    
    allItems.extend(clothing)
    
#######################################################################
#  Белья нет / не видно
####################################################################### 
    NostudpantiesM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'male',
    purpose = '')
    NostudpantiesM.cover = ['попа']
    NostudpantiesM.durability = 0
    NostudpantiesM.name = _('пах')
    NostudpantiesM.cost = 0
    NostudpantiesM.picto = 'pic/noimage.gif'
    NostudpantiesM.type = 'noclothing'
    NostudpantiesM.description = _('Он явно предпочитает не одевать нижнее белье')

    NostudpantiesF = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'female',
    purpose = '')
    NostudpantiesF.cover = ['попа']
    NostudpantiesF.durability = 0
    NostudpantiesF.name = _('попа')
    NostudpantiesF.cost = 0
    NostudpantiesF.picto = 'pic/items/NostudpantiesF.png'
    NostudpantiesF.type = 'noclothing'
    NostudpantiesF.description = _('Она видимо решила ходить без трусиков')

    NoVisstudpantiesM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'male',
    purpose = '')
    NoVisstudpantiesM.cover = ['попа']
    NoVisstudpantiesM.durability = 0
    NoVisstudpantiesM.name = _('низ')
    NoVisstudpantiesM.cost = 0
    NoVisstudpantiesM.picto = 'pic/noimage.gif'
    NoVisstudpantiesM.type = 'noclothing'
    NoVisstudpantiesM.description = _('К сожалению, одежда не позволяет увидить белье данного человека')

    NoVisstudpantiesF = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'female',
    purpose = '')
    NoVisstudpantiesF.cover = ['попа']
    NoVisstudpantiesF.durability = 0
    NoVisstudpantiesF.name = _('низ')
    NoVisstudpantiesF.cost = 0
    NoVisstudpantiesF.picto = 'pic/items/NoVisstudpantiesF.png'
    NoVisstudpantiesF.type = 'noclothing'
    NoVisstudpantiesF.description = _('К сожалению, одежда не позволяет увидить её трусики')

    NostudSlip = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'female',
    purpose = '')
    NostudSlip.cover = ['грудь']
    NostudSlip.durability = 0
    NostudSlip.name = _('Грудь')
    NostudSlip.cost = 0
    NostudSlip.picto = 'pic/items/NostudSlip.png'
    NostudSlip.type = 'noclothing'
    NostudSlip.description = _('Лифчик точно не включен в состав её гардероба')

    NoVisstudSlip = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = '',#stud',
    sex = 'female',
    purpose = '')
    NoVisstudSlip.cover = ['грудь']
    NoVisstudSlip.durability = 0
    NoVisstudSlip.name = _('верх')
    NoVisstudSlip.cost = 0
    NoVisstudSlip.picto = 'pic/items/NoVisstudSlip.png'
    NoVisstudSlip.type = 'noclothing'
    NoVisstudSlip.description = _('К сожалению, одежда не позволяет увидить её лифчик')


#######################################################################
