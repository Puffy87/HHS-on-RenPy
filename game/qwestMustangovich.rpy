label mileQwest1:
    $ clrscr()
    $ st1 = getChar('female')
    $ st2 = getChar('female')
    $ st3 = getChar('futa')
    $ hadSex(st1,mustangovich)
    $ t = mustangovich
    show hall as bg
    show expression 'pic/events/mile_1/1.png' at top as tempPic
    'Вы замечаете плачущую ученицу и подходите к ней. Она сидит на полу и рыдает. Переодически её руки прижимаются к нижней части живота, как будто у неё что то болит'
    player.say 'Что случилось? Тебя мальчишки обидели?'
    st1.say 'Меня изнасиловал наш физрук [t.name]! Его огромный член трахал меня с такой силой, что он по моему мне всё порвал!'
    'Несмотря на её слова, крови не видно, и вряд ли у неё всё так серьёзно, как она говорит. Скорее всего в ней говорит больше обида, чем боль.'
    player.say 'Что он с тобой сделал? - спрашиваете вы, успокаивая и поглаживая её по плечам'
    show storage as bg
    show expression 'pic/events/mile_1/2.jpg' at top as tempPic
    st1.say 'Он попросил меня принести мяч из кладовки, и когда я наклонилась, чтобы взять его из корзины, он схватил меня сзади, прижал к козлам, и...'
    'Не в силах продолжать свой рассказ, [st1.name] захлёбывается в рыданиях.'
    player.say 'Ты уверена, что это был он?'
    show hall as bg
    show expression 'pic/events/mile_1/1.png' at top as tempPic
    st1.say 'Ну а у кого ещё в нашей школе 30 сантиметровый член?'
    'Увидев ваши брови, которым высота вашего лба стала резко недостаточной для восхождения, ученица смущённо замолкает.'
    player.say 'Та-а-ак, и сколько же членов ты уже перемерила???, - удивлённо вопрошаете вы, но ученица не дождавшись окончания реплики, убегает, невзирая на "боль и унижение".'
    hide tempPic
    player.say 'Мне надо всерьёз поговорить с физкультурником на эту тему. Иш ты, горячий горный парень, решил совместить физкультуру с сексуальным образованием! Да и не может у человека быть член в 30 сантиметров. Ну не бывает таких просто!'
    show gym as bg
    'Вы направляетесь в спортзал, но тут никого нет. Странно, обычно на перемене тут полно народу. Интересно, где виновник вашего визита, [t.name]?'
    menu:
        'И где он прячется?'
        'Посмотреть в раздевалке':
            'Подходя к раздевалке, вы услышали странные стоны.'
            show changeRoom as bg
            show expression 'pic/events/mile_1/3.png' at top as tempPic
            $penis = int(st3.body.parts['пенис'].size)
            player.say 'Ага, вот ты и попался, грязный извращенец! - закричали вы открывая дверь, и с удивлением уставились на [penis] сантиметровый член ученицы [st3.fname].'
            '"Что за чёрт?" - успели вы подумать, прежде чем белая струя спермы ударила прямо в лицо.'
            $ player.coverSperm('лицо','грудь')
            show expression 'pic/events/mile_1/4.png' at right as tempPic
            'Вы как стояли с открытым, так и стоите. Только теперь рот полон спермы, уж не нарочно ли ученица умудрилась? Да и ученица ли?'
            st3.say 'Простите меня пожалуйста, я не хотела!'
            '"Что за невезучий день, сначала [t.fname], теперь ещё и это."'
            player.say 'Давно ли этот инструмент у тебя? - интересуетесь вы с улыбкой.'
            st3.say 'Поговаривают, что существуют препараты, которые делают девчёнок такими, но я родилась с членом.'
            'Школьница смущённо опускает глаза на свой приборчик.'
            st3.say 'Сначала родители хотели от меня отказаться, но колдунья сказала, что я принесу им счастье.'
            player.say 'Не знаю как родителей, но меня ты сегодня осчастливила конечно... Кстати не подскажешь, где наш физрук?'
            st3.say '[t.name]? Он в кладовке, с моей подругой [st2.fname].'
            hide tempPic
            player.say '"Вся школа чтоли уже в курсе? Я директор в конце концов или нет?"'
            'Не долго думая, вы слегка отряхиваетесь и направляетесь в кладовку.'
            jump mileQwest1_storage
        'Посмотреть в кладовке':
            jump mileQwest1_storage
            
label mileQwest1_storage:
    show gym as bg
    'Подходя к кладовке вы услышали как, тихие голоса разговаривают о чём то. Вы решили подсмотреть, что же там происходит? Вдруг [t.name] просто объясняет студентке как выполнить сложное упражнение? Хотя кого я обманываю?'
    show storage as bg
    show movie
    play movie 'pic/events/mile_1/5.gif.webm' loop
    'Посмотрев в дверную щель, Вы отшатнулись. Да, Вы в чём то оказались правы. [t.fname] действительно объяснял студентке упражнение. Только оно было не совсем спортивным. Спортивным конечно, но не совсем. За те секунды, что вы провели у двери, вы успели заметить не только тщательность выполнения трюка, но и размеры учителя.'
    player.say '"Японская богоматеринница! Да как же он у него в трусах то умещается? Телескопический что ли?"'
    'Вне зависимости от вашего желания, вы почувствали, что в трусах стало жарко и влажно. Прижавшись к стене, вы стали думать о том, что следует сделать дальше. Учитывая ваше состояние, лучше наверно было бы подождать пока они закончат.'
    $ player.incLust(10)
    $ st2.incCorr(1)
    stop movie
    hide movie
    show gym as bg
    menu:
        'Что делать? Что делать? ЧТО ДЕЛАТЬ?'
        'Подсматривать':
            show storage as bg
            $ player.incCorr(1)
            show expression 'pic/events/mile_1/6.png' at top as tempPic
            'Заглянув во второй раз, Вы увидели, что ситуация поменялась, теперь [st2.fname] сидела на попе, призывно раздвинув киску, а её ножки скользили по влажному от её соков члену учителя.'
            '[t.name] постанывал и совершал импульсивные движения бёдрами. Несмотря на то, что только недавно он надругался над другой ученицей, его эрекция была всё ещё тверда, и член подрагивал от каждого прикосновения юной ступни, готовясь вот-вот извергнуть семя.'
            show gym as bg
            hide tempPic
            show movie
            play movie 'pic/events/mile_1/7.gif.webm' loop
            'Вы и сами не заметили, как ваши пальчики оказались в трусах. Волны удовольствия прокатывались по вашему телу, и трепет оргазма захватил вас почти с первого прикосновения.'
            player.say 'М-м-м, не хватало ещё кончить одновременно с этим, о-о-ох.'
            'Уже не обращая внимания на разврат творящийся в соседней комнате, вы полностью сконцентрировались на ощущениях в ващей похотливой киске. Пальчики порхали всё быстрее, вверх - вниз, провести по губкам, опять к клитору, вниз - вверх.'
            play movie 'pic/events/mile_1/8.gif.webm' loop
            'Вас с головой накрыл оргазм, и, судя по мужским стонам из кладовки, не только вы побывали на эвересте наслаждения.'
            stop movie
            hide movie
            show storage as bg
            show expression 'pic/events/mile_1/9.png' at top as tempPic
            'Немного отдышавшись, вы посмотрели в приоткрытую дверь, и увидели, что измазанные в сперме ножки ученицы до сих пор покоятся на члене физрука. Вы не верите своим глазам, но похоже 30 сантиметровый гигант и не собирается опадать!'
            'Разглядывая перемазанные в сперме ножки ученицы и трепыхающийся в неспадающем возбуждении член, вы ощущаете, как предвкушение наслаждения снова охватывает ваше тело.'
            player.say '"Нет, с этим надо заканчивать!" - Вы решительно берётесь за руччку двери и открываете её.'
            $ lastMastur = ptime
            jump mileQwest1_storageIn
        'Войти':
            jump mileQwest1_storageIn

label mileQwest1_storageIn:
    show storage as bg
    show expression 'pic/events/mile_1/10.png' at top as tempPic
    'Войдя Вы видите, что [t.name] опять сажает школьницу на себя.'
    player.say 'Да ты с ума сошёл, кобель! Здесь что по твоему, школа или бордель??? - орёте вы на физрука.'
    '[st2.fname] в панике собирает вещи, и пытается улизнуть.'
    player.say 'Ты кем себя возомнил? Быком осеменителем высшего разряда? - продолжаете вы неиствоствовать.'
    if player.isSperm() != 2:
        show expression getCharImage(t,'dialog') as temp1
        '[t.name] мямлит что то невразумительное, ученица шмыгает за дверь.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'Какие бабушкины лекарства, что ты мелешь?'
        show expression getCharImage(t,'dialog') as temp1
        '[t.name] в панике объясняет вам, что он ничего не может с собой поделать. Его стояк не прекращается с самого утра, с того самого момента, как он перепутал свои стероиды с бабушкиным лекарством от сердца. Домой в таком состоянии он возвращаться не может, так как там только одна комната и одна бабушка.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'А какого чёрта ты на ученицу полез? - всё ещё не понимаете вы.'
        show expression getCharImage(t,'dialog') as temp1
        t.say 'Да если бы я сам! Она сама на меня запрыгнула! Вон, спросите у неё сами!'
        'Тут [t.name] замечает, что ученица уже улизнула.'
        t.say 'Вот ведь дрянь маленькая!'
        'Отведя взгляд, вы замечаете, что физрук до сих пор сидит без штанов, а его многосантиметровое достоинство ,подрагивая, смотрит вам прям в лицо.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'Кажется я знаю, как решить твою проблему с обоюдным удовольствием, - хищно улыбаясь, говорите Вы, облизывая острым язычком губы.'
        show expression 'pic/events/mile_1/11.png' at top as tempPic
        'Несмотря на то, что судя по влажности и температуре между ног у вас там тропические джунгли, вы решаете сначала попробовать на вкус то, что запихнёте в себя позже.'
        'Вы оголяете свои груди и вставляете между ними просто царский пенис. Одно только это действие заставило его выделить приличную порцию эякулята, смазывающего ложбинку в которой уместился член.'
        player.say 'Дааа, таблеточки то непростые, - замечаете вы.'
        t.say 'Нгггг, - стонет в ответ физрук.'
        player.say 'Ты уже готов кончить? Как же ты смог удовлетворить тех девчёнок с такой то скорострельностью???'
        'Не желая терять ни капли спермы из этого монстра, Вы обхватываете его губами, и он спустя секунду орошает вам глотку густым и пахучим веществом.'
        'Улыбаясь, вы поднимаете голову к своему любовнику, как вдруг чувствуете на себе чей то взгляд.'
        hide tempPic
        show expression getCharImage(st2,'dialog') as temp1
        st2.say 'Я смотрю Вы мою игрушку решили отобрать? Могли бы и попросить, я бы дала Вам попользоваться. Ну что, дальше - втроём?'
        '[st2.fname] игриво склонила голову набок и ждёт вашего ответа.'
        'Судорожно сглотнув сперму, вы ощущаете как она пожаром прокатывается по вашему пищеводу, и на вас резко накатывает неукротимое желание продолжить свой род во что бы то не стало.'
        player.say '"Ой-ой. Похоже в семени содержалось довольно много действущего вещества из таблеточек." - в панике проносится у вас в голове, пока вы безуспешно пытаетесь совладать с растущим возбуждением.'
        player.say 'Да что ТЫ СЕБЕ ПОЗВОЛЯЕШЬ! Я против! Да уж лучше я сама...'
        'Очередной приступ скручивает вашу матку, и из киски вырывается тонкая струйка влаги, обильно смазывающая вашу промежность.'
        player.say 'Хотя чёрт с ним, только родителям о проишествии - молчок!'
        show expression getCharImage(player,'dialog') as temp2
        st2.say'Конечно! - радостно восклицает ученица, и вы обе поворачиваетесь к притихшему физруку'
        hide temp1
        hide temp2
    else:
        '[t.name] в панике объясняет вам, что он ничего не может с собой поделать. Его стояк не прекращается с самого утра, с того самого момента, как он перепутал свои стероиды с бабушкиным лекарством от сердца. Домой в таком состоянии он возвращаться не может, так как там только одна комната и одна бабушка. '
        hide tempPic
        'Пока вы заняты этими объяснениями, ученица совершает обходной маневр. Аккуратно подойдя к вам, она вдруг лижет вас в щёку.'
        st2.say 'Мммм, [st3.fname], - мечтательно закатывая глаза шепчет она.'
        player.say 'Что???'
        'Вы с ужасом понимаете, что со всеми этими делами совсем забыли привести себя в порядок.'
        st2.say 'Я просто помогала учителю сбросить напряжение, причём даже без секса как такового. К тому же, и Вы тоже без дела не сидели. Ваши стоны за дверью не слышали разве что в Чикаго. Ну что, может быть продолжим втроём?'
        'Перед вашими глазами пролетают "ученица" в раздевалке, то, что вы увидели в кладовке, ноздри щекотит острый аромат секса. Ваша киска сжимается в сладкой неге от предвкушения того, как её может заполнить до сих пор торчащий между ног физрука предмет.'
        player.say '"А ну его всё к чёрту! Один раз живём!" - пролетает у вас в голове.'
        player.say 'А что, давай, - улыбаетесь вы, - Только родителям - молчок! Договорились?'
        show expression getCharImage(st2,'dialog') as temp1
        show expression getCharImage(player,'dialog') as temp2
        st2.say'Конечно! - радостно восклицает ученица, и вы обе поворачиваетесь к притихшему физруку'
        hide tempPic
        hide temp1
        hide temp2
    show movie
    play movie 'pic/events/mile_1/12.gif.webm' loop
    'Началась бесконечная оргия. Вы прыгали на неунывающем члене физрука, а [st2.fname] уселась ему на лицо. Ваши языки переплетались, и вас трясло от вожделения.'
    play movie 'pic/events/mile_1/13.gif.webm' loop
    'Спустя пару часов и пару оргазмов Вы всё ещё прыгали на его члене. [st2.fname] тоже подустала, но не слазила со своего насеста, постоянно ощущая, как неутомимый язык физрука ласкал её лоно.'
    stop movie
    hide movie
    show expression 'pic/events/mile_1/16.jpg' at top as tempPic
    'Оргазм! Очередной оргазм! Множественный оргазм! Боже, да [t.fname] просто неутомим! Похоже действие этих таблеток так легко не прекратить.'
    show movie
    play movie 'pic/events/mile_1/14.gif.webm' loop
    'Мдаа, Вам уже не 16 лет. Утомившись, вы предоставили инициативу по отсосу напарнице.'
    stop movie
    hide movie
    show expression 'pic/events/mile_1/15.jpg' at top as tempPic
    '[st2.fname] продолжает сосать член, вы нехотя полизываете его. Боже, у вас уже всё болит от этих скачек. Губы опухли, язык не слушается, между ног тоже не всё в порядке. Пора с этим заканчивать.'
    show expression 'pic/events/mile_1/17.jpg' at top as tempPic
    '[st2.fname] в полубессознательном состоянии висит на руках физрука, в то время как вы, вытащив его член из вагины, вгрызаетесь в него зубами.'
    t.say 'AAAAAA, ты что, обезумела? - кричит от боли [t.name], - Зачем ты это сделала???'
    player.say 'Смотри, - показываете вы рукой вниз на опадающий член. Хех, не в стоячем состоянии он выглядит не таким грозным!'
    t.say 'Фух, спасибо, кажется отпускает. Да и возбуждения больше не чувствуется. - радуется физрук'
    player.say 'Твою мать! Ты трахал нас 7 часов, а всё решалось так просто!, - возмущаетесь Вы -  [st2.fname], а ты что об этом всём думаешь?'
    st2.say 'Ммммннннмммннндаааа, - в полубессознательном состоянии вырвалось у неё.'
    show expression 'pic/events/mile_1/18.jpg' at top as tempPic
    'Спустя некоторое время, попив чай, отдонув и приведя себя в порядок, вы раздаёте указания.'
    player.say 'Значит так, - начинаете вы, - [t.fname], ты доставляешь ученицу домой в целости и сохранности. Надеюсь мы сбили твой стояк. Если нет - сбивай его хоть кирпичём. Понятно?'
    t.say 'Угу, - мямлит поникший физрук.'
    player.say '[st1.fname], ты ведёшь себя нормально, сегодня был обычный день, устала ты потому, что сегодня был кросс на 5 км последним уроком. Уяснила?'
    st2.say ' Ага! - радостно восклицает она, - а мы ещё как нибудь повторим?'
    player.say 'Может быть, радость моя, может быть, - ласково говорите вы.'
    player.say 'И да, [t.name], теперь ты будешь голосовать за любые мои предложения на педсовете. Ясненько?'
    t.say 'А как же иначе! Может быть сразу за секс на физкультуре проголосуем?'
    'Лицо физрука принимает мечтательное выражение.'
    player.say 'Но но! Разогнался. Для начала хотя бы форму этим, - Вы киваете на ученицу, - поменяем.'
    python:
        mile_quest_1 = 1
        t.incLoy(20)
        t.incCorr(20)
        t.incLust(-100)
        t.incFun(10)
        st2.incLoy(20)
        st2.incCorr(20)
        st2.incLust(-100)
        st2.incFun(10)
        player.incCorr(20)
        player.incLust(-100)
        player.incFun(10)
        player.incEnergy(-700)
        changetime(8*60)
        player.coverSperm('лицо','рот','попа','вагина','ноги')
        move('loc_home')
        