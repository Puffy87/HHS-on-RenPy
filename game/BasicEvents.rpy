init:
    image cleanFace = "pic/events/bodyclean/face1.jpg"
    image cleanMouth = "pic/events/bodyclean/mouth1.jpg"
    image cleanBody = "pic/events/bodyclean/body1.jpg"
    image cleanHands = "pic/events/bodyclean/hands1.jpg"
    image cleanFeet = "pic/events/bodyclean/feet1.jpg"
    image cleanPussy = "pic/events/bodyclean/pussy1.jpg"
    image cleanAss = "pic/events/bodyclean/ass1.jpg"

label shower:
    hide screen stats_screen
    $ rands = renpy.random.randint(1, 8)
    show expression ("pic/events/bathroom/%d.jpg" % rands) at top

    if player.stats.dirty == 0:
        'Вы искупались, хотя и не были особо грязными. Как же Вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'
    else:
        'Вы смыли с себя запах немытого тела. Как же Вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'

    if player.isSperm() > 0:
        $temp = player.printSperm()
        'Теперь [temp] больше не в сперме.'

    $changetime(15)
    $player.cleanAll()
    $move(curloc)

label cleanFace:
    hide screen stats_screen #скрываем интерфейс
    show cleanFace at top #Показываем картинку
    'Ваше лицо перемазано в сперме. Густые её капли покрывают щеки, носик, губки, пару капель застряли в полосах'
    menu: #меню всё делает за вас
        'Чем бы вытереть эту липкую жидкость?' #текст под меню
        'Вытереть салфетками' if player.hasItem('Салфетка') == True: #показывается, если салфетки ещё есть
            'Вы вытерли салфетками Ваше лицо. Теперь оно сияет прежним внутренним светом!'
            if player.apply('Салфетка') == False:
                'ОШИБКА!!!'#Убираем одну салфетку
            $ player.clean('лицо') #чистим лицо
        'Попытаться вытереть руками':
            $changetime(10) #увеличиваем время
            if rand(1,3) == 1: #Вызываем кастомный рандом
                'На удивление Вам удалось аккуратными движениями пальчиков снять семя с лица, и незаметно стряхнуть её на землю. Личико опять чистое!'
                $ player.clean('лицо') #чистим лицо
            else:
                'Вы лишь ещё сильнее размазали сперму по лицу, вдобавок испачкав руки.'
                $ player.coverSperm('руки') #Заляпываем ещё и руки
        'Да мне и так хорошо!':
            pass #просто пропуск
    $ move(curloc) #Возврат на последнюю локацию

label cleanMouth:
    hide screen stats_screen #скрываем интерфейс
    show cleanMouth at top #Показываем картинку
    'Ваш рот полон спермы. Вы чувствуете её густую терпкость на своём языке.'
    menu:
        'Мне надо избавиться от неё'
        'Выплюнуть':
            $ player.clean('рот')
            'Вы незаметно сплевываете в сторонку. Теперь у Вас чистый ротик'
        'Проглотить' if player.stats.corr > 20:
            'Вы проглатываете тягучую сперму, и ощущаете как Ваш желудок наполняется соками Вашего последнего любовника. Вы чувствуете небольшое возбуждения и развратность этого действия.'
            $ player.stats.lust += 10
            $ player.stats.corr += 1
            $ player.clean('рот')
        'Ммм Ффф ммм ууу!':
            pass
    $ move(curloc) #Возврат на последнюю локацию

label cleanBody:
    hide screen stats_screen
    show cleanBody at top
    'После обильного семяизвержения Ваше тело перемазано в сперме, капли виднеются повсюду.'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы быстрыми движениями вытерли салфетками тягучие капли и очистили себя!'
            $ player.apply('Салфетка')
            $ player.clean('грудь')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление Вам удалось аккуратными движениями пальцев снять сперму с тела, и стряхнуть её. Вроде бы получилось незаметно!'
                $ player.clean('грудь')
            else:
                'Вы лишь ещё сильнее размазали сперму, вдобавок испачкав руки.'
                $ player.coverSperm('руки')
        'Да вроде бы и так неплохо выглядит!':
            pass
    $ move(curloc)

label cleanHands:
    hide screen stats_screen
    show cleanHands at top
    'Ваши руки перемазаны в сперме. Густые капли маслянистой жидкости приятны на ощупь.'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы вытерли салфетками руки.'
            $ player.apply('Салфетка')
            $ player.clean('руки')
        'Облизать' if player.stats.corr > 40:
            'Вы облизали свои руки от спермы. Это было одновременно приятно и возбуждающе.'
            $ player.stats.lust += 10
            $ player.stats.corr += 2
            $ player.clean('руки')
        'Само высохнет и отвалится!':
            pass
    $ move(curloc)

label cleanFeet:
    hide screen stats_screen
    show cleanFeet at top
    'На Ваших ножках виднеются тягучие белые пятна. Это привлекает очень много ненужного внимания!'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы аккуратными движениями вытерли салфетками ноги. Ножки как ножки, только красивые!'
            $ player.apply('Салфетка')
            $ player.clean('ноги')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление Вам удалось аккуратными движениями пальцев снять сперму с ножек, и незаметно стряхнуть её. Ножки как ножки, только красивые!'
                $ player.clean('ноги')
            else:
                'Вы лишь ещё сильнее размазали сперму по ногам, вдобавок испачкав руки.'
                $ player.coverSperm('руки')
        'Да вроде и так красиво!':
            pass
    $ move(curloc)

label cleanPussy:
    hide screen stats_screen
    show cleanPussy at top
    'Ваша киска полна спермы. Вы чувствуете её влажное хлюпанье при каждом движении.'
    menu:
        'Ммм. Надо что то сделать с этим.'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Отойдя в сторонку и немного присев, Вы выдавили из своей киски всю сперму прямо на салфетку. Еще раз протерев всё начисто, Вы удовлетворились результатом.'
            $ player.apply('Салфетка')
            $ player.clean('вагина')
        'Попытаться достать её руками' if player.stats.corr > 50:
            $changetime(10)
            'Отойдя в сторонку, вы запустили свои шаловливые пальчики, и принялись доставать из вашей киски сгустки спермы и стряхивать их на пол. Ритмичные движения пальцев в вашей щёлки не добавляют спокойствия.'
            'Через 10 минут работа была закончена, но руки оказались перемазаны в ваших соках и чужой сперме.'
            $ player.clean('вагина')
            $ player.coverSperm('руки')
            $ player.stats.lust += 10
            $ player.stats.corr += 2
        'Это может и подождать.':
            pass
    $ move(curloc)

label cleanAss:
    hide screen stats_screen
    show cleanAss at top
    'Внутри Вашей попки полно семени. Вы чувствуете её влажное хлюпанье при каждом движении.'
    menu:
        'Не самое приятное чувство.'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Отойдя в сторонку Вы аккуратно протёрли салфетками попу. Теперь все чисто.'
            $ player.apply('Салфетка')
            $ player.clean('анус')
        'Попытаться достать её руками' if player.stats.corr > 60:
            $changetime(10)
            'Отойдя в сторонку, вы присели на корточки и запустили свой палец в вашу заднюю дырочку. Неожиданный спазм заставил выделиться из попки не только сперму.'
            if player.hasItem('Салфетка') == True:
                'Хорошо, что у вас оказались салфетки, которыми вы протёрли всё начисто. И стоило заморачиваться с пальцем? - подумали Вы.'
            else:
                'К сожалению вытереть новый конфуз оказалось не чем, и теперь от вас попахивает.'
                $ player.stats.dirty += 1
            $ player.clean('анус')
        'Это может и подождать! Да! Наверное...':
            pass
    $ move(curloc)

label sleep:
    hide screen stats_screen
    python:
        # Изнашивание одежды, если спите в ней.
        for x in player.wear:
            if rand(1,2) == 1:
                x.durability -= 1
                player.checkDur()
                
        global hour, ptime, last_sleeped
        hour_up = 7
        if hour >= 0:
            start_hour = hour - 24
        else:
            start_hour = hour
        sleeped = 0
        while player.stats.energy < player.stats.health and start_hour < hour_up and sleeped < 12:
            changetime(60)
            start_hour += 1
            player.stats.energy += rand(100,125)
            sleeped += 1
        player.reset()
        last_sleeped = ptime
        if rand(1,3) > 2:
            tryEvent('loc_dreams')
        renpy.jump('loc_dreams')

label loc_dreams:
    hide screen show_stats
    $ rands = rand(1,11)
    show expression ("pic/locations/home/dream/no%d.jpg" % rands) at top
    'В это раз Вам ничего не снилось и, провалившись в ласковые объятия сна, Вы отлично выспались.'
    $ move('loc_bedroom')

label naked:
    if player.getClothPurpose('swim'):
        show expression ("pic/events/various/bikini.png") at top
    else:
        show expression ("pic/events/various/naked.jpg") at top

    player.say 'Я не могу выходить на улицу в таком виде!!!'
    $ move(prevloc)

label loc_swim:
    show beach
    if player.stats.energy < 200:
        player.say 'Я слишком устала, чтобы плавать... Пора возвращаться домой.'
    elif player.getClothPurpose('swim') == False:
        player.say 'Я не могу плавать в одежде!'
    else:
        hide screen show_stats
        $ rands = rand(1,5)
        show expression ("pic/events/beach/swim_norm%d.jpg" % rands) at top
        'Вы поплавали часок, и немного устали. По крайней мере Ваша физическая форма улучшилась.'
        $ changetime(60)
        $ player.stats.energy -= rand(100,300)
        $ player.stats.health += rand (10,20)
        $ player.cleanAll()
    $ move('loc_beach')
    
label loc_taxi:
    show expression 'pic/locations/taxi.jpg'
    $ money = player.money
    menu:
        'Куда поедем? Городочек маленький, проезд в любую сторону всего по 50.'
        'Пляж' if curloc != 'loc_beach' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_beach')
        'Домой' if curloc != 'loc_street' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_home')
        'На торговую' if curloc != 'loc_shopStreet' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_shopStreet')
        'К школе' if curloc != 'loc_entrance' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_entrance')
        'Я передумала' if money >= 50:
            $ move (curloc)
        'Простите, но у меня нет денег' if money < 50:
            $ move (curloc)

label unconsciousSchool:
    show expression 'pic/events/uncon/1.jpg' at top
    'Вы упали без сознания от переутомления. Вы пролежали пару часов, пока Вас не нашли случайные ученики.'
    'Проснувшись, Вы обнаружили, что Вас обыскивали, верхняя одежда снята, на теле синяки.'
    if player.money > 200:
        $ player.money -= rand(100,200)
    $ setRep(2,-2)
    $ player.setEnergy(200)
    $ changetime(rand(100,200))
    $ move(curloc)
    
label unconsciousOther:
    show expression 'pic/events/uncon/2.jpg' at top
    'Вы упали без сознания от переутомления прямо на улице. Вы пролежали пару часов, пока Вас не нашли случайные люди.'
    'Проснувшись, Вы обнаружили свежее пятно спермы на одежде.'
    $ player.body.parts['грудь'].sperm = True
    if player.money > 200:
        $ player.money -= rand(100,200)
    $ setRep(10,-2)
    $ player.setEnergy(200)
    $ changetime(rand(100,200))
    $ move(curloc)