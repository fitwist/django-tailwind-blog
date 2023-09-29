from pywebcopy import save_website

links = ['https://www.helenkapatsa.ru/skoshiennost', 
    'https://www.helenkapatsa.ru/courses', 
    'https://www.helenkapatsa.ru/sluchainaia-vielichina', 
    'https://www.helenkapatsa.ru/slovesnyye-vlozheniya', 
    'https://www.helenkapatsa.ru/skip-gramm', 
    'https://www.helenkapatsa.ru/katieghorialnaia-pieriemiennaia', 
    'https://www.helenkapatsa.ru/chislovaia-pieriemiennaia', 
    'https://www.helenkapatsa.ru/tenzor', 
    'https://www.helenkapatsa.ru/niekontroliruiemoie-obuchieniie', 
    'https://www.helenkapatsa.ru/viektor', 
    'https://www.helenkapatsa.ru/tsielievaia-pieriemiennaia', 
    'https://www.helenkapatsa.ru/mashinnoie-obuchieniie', 
    'https://www.helenkapatsa.ru/google-colab', 
    'https://www.helenkapatsa.ru/modiel', 
    'https://www.helenkapatsa.ru/statistika', 
    'https://www.helenkapatsa.ru/linieinaia-rieghriessiia', 
    'https://www.helenkapatsa.ru/degrees-of-freedom', 
    'https://www.helenkapatsa.ru/kvantil', 
    'https://www.helenkapatsa.ru/standartnoie-otklonieniie', 
    'https://www.helenkapatsa.ru/vriemiennaia-mietka', 
    'https://www.helenkapatsa.ru/priznak', 
    'https://www.helenkapatsa.ru/vyborka', 
    'https://www.helenkapatsa.ru/moshchnost', 
    'https://www.helenkapatsa.ru/pandas-profiling', 
    'https://www.helenkapatsa.ru/korrieliatsiia', 
    'https://www.helenkapatsa.ru/prophet', 
    'https://www.helenkapatsa.ru/matritsa', 
    'https://www.helenkapatsa.ru/chiernyi-iashchik', 
    'https://www.helenkapatsa.ru/nauka-o-dannykh', 
    'https://www.helenkapatsa.ru/matritsa-oshibok', 
    'https://www.helenkapatsa.ru/razvedochnyy-analiz-dannykh-chast-1', 
    'https://www.helenkapatsa.ru/razvedochnyy-analiz-dannykh-chast-2', 
    'https://www.helenkapatsa.ru/bystroie-kodirovaniie', 
    'https://www.helenkapatsa.ru/prokliatiie-razmiernostiei', 
    'https://www.helenkapatsa.ru/normalnoie-raspriedielieniie', 
    'https://www.helenkapatsa.ru/tochnost-izmierienii', 
    'https://www.helenkapatsa.ru/sriednieie-znachieniie', 
    'https://www.helenkapatsa.ru/vybros', 
    'https://www.helenkapatsa.ru/normalizatsiia', 
    'https://www.helenkapatsa.ru/paiplain', 
    'https://www.helenkapatsa.ru/standartizatsiia', 
    'https://www.helenkapatsa.ru/dataset', 
    'https://www.helenkapatsa.ru/mietod-k-blizhaishikh-sosiedie', 
    'https://www.helenkapatsa.ru/standartizovannaia-otsienka', 
    'https://www.helenkapatsa.ru/kontroliruiemoie-obuchieniie', 
    'https://www.helenkapatsa.ru/nabliudieniie', 
    'https://www.helenkapatsa.ru/priediktor', 
    'https://www.helenkapatsa.ru/miediana', 
    'https://www.helenkapatsa.ru/ekstsiess', 
    'https://www.helenkapatsa.ru/dispiersiia', 
    'https://www.helenkapatsa.ru/obuchieniie-s-chastichnym-privliechieniiem-uchitielia', 
    'https://www.helenkapatsa.ru/kak-osvaivat-data-science', 
    'https://www.helenkapatsa.ru/gienieralnaia-sovokupnost', 
    'https://www.helenkapatsa.ru/data-saiientist', 
    'https://www.helenkapatsa.ru/trienirovochnyie-dannyie', 
    'https://www.helenkapatsa.ru/validatsionnyye-dannyye', 
    'https://www.helenkapatsa.ru/tiestovyie-dannyie', 
    'https://www.helenkapatsa.ru/tochechnaya-diagramma', 
    'https://www.helenkapatsa.ru/vriemiennoi-riad', 
    'https://www.helenkapatsa.ru/p-znachieniie', 
    'https://www.helenkapatsa.ru/nulievaia-ghipotieza', 
    'https://www.helenkapatsa.ru/iskusstviennyi-intielliekt', 
    'https://www.helenkapatsa.ru/post', 
    'https://www.helenkapatsa.ru/logharifmichieskaia-potieria', 
    'https://www.helenkapatsa.ru/sriedniekvadratichieskaia-oshibka', 
    'https://www.helenkapatsa.ru/mietod-ghlavnykh-komponient', 
    'https://www.helenkapatsa.ru/kritierii-khi-kvadrat', 
    'https://www.helenkapatsa.ru/datafrieim', 
    'https://www.helenkapatsa.ru/funktsiia-potieri', 
    'https://www.helenkapatsa.ru/spraviedlivost', 
    'https://www.helenkapatsa.ru/dierievo-rieshienii', 
    'https://www.helenkapatsa.ru/beghghingh', 
    'https://www.helenkapatsa.ru/loghistichieskaia-rieghriessiia', 
    'https://www.helenkapatsa.ru/gipierparamietr-c', 
    'https://www.helenkapatsa.ru/kross-validatsiia', 
    'https://www.helenkapatsa.ru/kvantovoie-mashinnoie-obuchieniie', 
    'https://www.helenkapatsa.ru/optimization', 
    'https://www.helenkapatsa.ru/mnoghosloinyi-piertsieptron', 
    'https://www.helenkapatsa.ru/mietod-opornykh-viektorov', 
    'https://www.helenkapatsa.ru/glubokoye-obucheniye', 
    'https://www.helenkapatsa.ru/pravilo-assotsiatsii', 
    'https://www.helenkapatsa.ru/alghoritm', 
    'https://www.helenkapatsa.ru/rieghriessiia', 
    'https://www.helenkapatsa.ru/sviortochnaia-nieironnaia-siet', 
    'https://www.helenkapatsa.ru/mietod-k-sriednikh', 
    'https://www.helenkapatsa.ru/nieironnaia-siet', 
    'https://www.helenkapatsa.ru/tensorflow', 
    'https://www.helenkapatsa.ru/gomoskiedastichnost', 
    'https://www.helenkapatsa.ru/funktsiia-aktivatsii', 
    'https://www.helenkapatsa.ru/riekurrientnaia-nieirosiet', 
    'https://www.helenkapatsa.ru/iarlyk', 
    'https://www.helenkapatsa.ru/bolshiie-dannyie', 
    'https://www.helenkapatsa.ru/epokha', 
    'https://www.helenkapatsa.ru/moda', 
    'https://www.helenkapatsa.ru/smieshchieniie', 
    'https://www.helenkapatsa.ru/obuchieniie-s-podkrieplieniiem', 
    'https://www.helenkapatsa.ru/pravilo-bolshogho-paltsa', 
    'https://www.helenkapatsa.ru/tensorboard', 
    'https://www.helenkapatsa.ru/dialogflow', 
    'https://www.helenkapatsa.ru/obrabotka-iestiestviennogho-iazyka', 
    'https://www.helenkapatsa.ru/oshibka', 
    'https://www.helenkapatsa.ru/stokhastichieskii-ghradiientnyi-spusk', 
    'https://www.helenkapatsa.ru/epsilon', 
    'https://www.helenkapatsa.ru/kross-entropiia', 
    'https://www.helenkapatsa.ru/sluchainyi-lies', 
    'https://www.helenkapatsa.ru/pierieobuchieniie', 
    'https://www.helenkapatsa.ru/adaboost', 
    'https://www.helenkapatsa.ru/pakiet', 
    'https://www.helenkapatsa.ru/chat-bot', 
    'https://www.helenkapatsa.ru/iadiernyi-mietod', 
    'https://www.helenkapatsa.ru/standardscaler', 
    'https://www.helenkapatsa.ru/funktsiia', 
    'https://www.helenkapatsa.ru/polie', 
    'https://www.helenkapatsa.ru/insait', 
    'https://www.helenkapatsa.ru/gistoghramma', 
    'https://www.helenkapatsa.ru/sushchnost', 
    'https://www.helenkapatsa.ru/otzyv', 
    'https://www.helenkapatsa.ru/tableau', 
    'https://www.helenkapatsa.ru/altiernativnaia-ghipotieza', 
    'https://www.helenkapatsa.ru/poeliemientnaia', 
    'https://www.helenkapatsa.ru/namierieniie', 
    'https://www.helenkapatsa.ru/tieplovaia-karta', 
    'https://www.helenkapatsa.ru/softmaks', 
    'https://www.helenkapatsa.ru/propusk', 
    'https://www.helenkapatsa.ru/kaggle', 
    'https://www.helenkapatsa.ru/klassifikatsiia', 
    'https://www.helenkapatsa.ru/klikstrim', 
    'https://www.helenkapatsa.ru/mietod-loktia', 
    'https://www.helenkapatsa.ru/gipierparamietr', 
    'https://www.helenkapatsa.ru/gipierploskost', 
    'https://www.helenkapatsa.ru/graf', 
    'https://www.helenkapatsa.ru/ostatok', 
    'https://www.helenkapatsa.ru/silhouette-method', 
    'https://www.helenkapatsa.ru/statsionarnost', 
    'https://www.helenkapatsa.ru/slabyi-iskusstviennyi-intielliekt', 
    'https://www.helenkapatsa.ru/silnyi-iskusstviennyi-intielliekt', 
    'https://www.helenkapatsa.ru/obnaruzhieniie-moshiennichieskikh-opieratsii', 
    'https://www.helenkapatsa.ru/tochka-pieriesiechieniia', 
    'https://www.helenkapatsa.ru/multikolliniearnost', 
    'https://www.helenkapatsa.ru/krughovaia-diaghramma', 
    'https://www.helenkapatsa.ru/mieshok-slov', 
    'https://www.helenkapatsa.ru/pytorch', 
    'https://www.helenkapatsa.ru/noutbuk', 
    'https://www.helenkapatsa.ru/impuls', 
    'https://www.helenkapatsa.ru/avtokorrieliatsiia', 
    'https://www.helenkapatsa.ru/smote-pieriesemplirovaniie', 
    'https://www.helenkapatsa.ru/osnovannaia-na-plotnosti-prostranstviennaia-klastierizatsiia-dlia-prilozhienii-s-shumami', 
    'https://www.helenkapatsa.ru/modiel-boksa-dzhienkinsa', 
    'https://www.helenkapatsa.ru/liemmatizatsiia', 
    'https://www.helenkapatsa.ru/sravneniye-konstruktorov-chat-botov', 
    'https://www.helenkapatsa.ru/modiel-kholta-vintiersa', 
    'https://www.helenkapatsa.ru/roc-krivaia', 
    'https://www.helenkapatsa.ru/gradiientnyi-bustingh-2', 
    'https://www.helenkapatsa.ru/paradoks-simpsona', 
    'https://www.helenkapatsa.ru/klaster', 
    'https://www.helenkapatsa.ru/token', 
    'https://www.helenkapatsa.ru/kovariatsiia', 
    'https://www.helenkapatsa.ru/viebkhuk', 
    'https://www.helenkapatsa.ru/utiechka-dannykh', 
    'https://www.helenkapatsa.ru/anonimizatsiia', 
    'https://www.helenkapatsa.ru/stemming', 
    'https://www.helenkapatsa.ru/chastichnaia-avtokorrieliatsiia', 
    'https://www.helenkapatsa.ru/modielirovaniie-ottoka', 
    'https://www.helenkapatsa.ru/uklon', 
    'https://www.helenkapatsa.ru/shum', 
    'https://www.helenkapatsa.ru/upravliaiemyi-riekurrientnyi-blok', 
    'https://www.helenkapatsa.ru/vazhnost-priznaka', 
    'https://www.helenkapatsa.ru/n-ghramm', 
    'https://www.helenkapatsa.ru/tiest-diki-fulliera', 
    'https://www.helenkapatsa.ru/k-blochnaia-kross-validatsiia', 
    'https://www.helenkapatsa.ru/minmaxscaler', 
    'https://www.helenkapatsa.ru/pulingh', 
    'https://www.helenkapatsa.ru/dolia-lozhnykh-polozhitielnykh-klassifikatsii', 
    'https://www.helenkapatsa.ru/klass', 
    'https://www.helenkapatsa.ru/prieobrazovaniie-furie', 
    'https://www.helenkapatsa.ru/tsiepnoie-pravilo', 
    'https://www.helenkapatsa.ru/ievklidovo-rasstoianiie', 
    'https://www.helenkapatsa.ru/dvoinik-modielirovaniie-look-alike-modeling', 
    'https://www.helenkapatsa.ru/piertsieptron', 
    'https://www.helenkapatsa.ru/t-kritierii-stiudienta-t-test', 
    'https://www.helenkapatsa.ru/otbor-priznakov', 
    'https://www.helenkapatsa.ru/analiz-tonalnosti-tieksta', 
    'https://www.helenkapatsa.ru/poliarnost', 
    'https://www.helenkapatsa.ru/ciezonnost', 
    'https://www.helenkapatsa.ru/koghorta', 
    'https://www.helenkapatsa.ru/docker', 
    'https://www.helenkapatsa.ru/tieoriema-baiiesa', 
    'https://www.helenkapatsa.ru/vizualizatsiia-dannykh', 
    'https://www.helenkapatsa.ru/bert', 
    'https://www.helenkapatsa.ru/etl', 
    'https://www.helenkapatsa.ru/vertica', 
    'https://www.helenkapatsa.ru/power-bi', 
    'https://www.helenkapatsa.ru/hadoop', 
    'https://www.helenkapatsa.ru/lieksiema', 
    'https://www.helenkapatsa.ru/apache-spark', 
    'https://www.helenkapatsa.ru/yadernoye-sglazhivaniye', 
    'https://www.helenkapatsa.ru/raspoznavaniie-emotsii', 
    'https://www.helenkapatsa.ru/raspoznavaniie-obiektov', 
    'https://www.helenkapatsa.ru/airflow', 
    'https://www.helenkapatsa.ru/raspoznvaniie-lits', 
    'https://www.helenkapatsa.ru/klastierizatsiia', 
    'https://www.helenkapatsa.ru/otsienka-f1', 
    'https://www.helenkapatsa.ru/kompiutiernoie-zrieniie', 
    'https://www.helenkapatsa.ru/greenplum', 
    'https://www.helenkapatsa.ru/gietieroskiedastiichnost-heteroscedasticity', 
    'https://www.helenkapatsa.ru/rieghuliarnoie-vyrazhieniie', 
    'https://www.helenkapatsa.ru/sriedniaia-absoliutnaia-oshibka', 
    'https://www.helenkapatsa.ru/transformers', 
    'https://www.helenkapatsa.ru/transformiery', 
    'https://www.helenkapatsa.ru/ekstremalnyy-gradiyentnyy-busting', 
    'https://www.helenkapatsa.ru/dvustoronnii-tiest', 
    'https://www.helenkapatsa.ru/korrieloghramma', 
    'https://www.helenkapatsa.ru/khranilishche-dannykh', 
    'https://www.helenkapatsa.ru/skhodimost-convergence', 
    'https://www.helenkapatsa.ru/raspoznavaniie-pozy', 
    'https://www.helenkapatsa.ru/solver', 
    'https://www.helenkapatsa.ru/koeffitsiient-dzhini', 
    'https://www.helenkapatsa.ru/ml-vs-dl', 
    'https://www.helenkapatsa.ru/mietod-obratnogho-rasprostranieniia-oshibki', 
    'https://www.helenkapatsa.ru/vidy-mietrik', 
    'https://www.helenkapatsa.ru/vidy-validatsii', 
    'https://www.helenkapatsa.ru/vidy-funktsii-aktivatsii', 
    'https://www.helenkapatsa.ru/untitled', 
    'https://www.helenkapatsa.ru/knigha-mashinnoie-obuchieniie-dostupnym-iazykom', 
    'https://www.helenkapatsa.ru/adam', 
    'https://www.helenkapatsa.ru/tiest-na-normalnost-normality-test', 
    'https://www.helenkapatsa.ru/9-vieshchiei-kotoryie-pomoghli-mnie-stat-data-saiientistom', 
    'https://www.helenkapatsa.ru/kafka', 
    'https://www.helenkapatsa.ru/bustingh', 
    'https://www.helenkapatsa.ru/vypadaiushchii-sloi', 
    'https://www.helenkapatsa.ru/nieironnaia-mashina-tiuringha', 
    'https://www.helenkapatsa.ru/yazyk-strukturirovannykh-zaprosov', 
    'https://www.helenkapatsa.ru/clickhouse', 
    'https://www.helenkapatsa.ru/alghoritm-poiska-po-sietkie', 
    'https://www.helenkapatsa.ru/podghonka-krivykh', 
    'https://www.helenkapatsa.ru/mlops'
    ]


i = 0
while i < len(links):
    save_website(
        url=links[i],
        project_folder="/Users/elenakapatsa/Repositories/django-tailwind-blog/migrating/ghost_backup",
        project_name=f"{links[i]}",
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )
    i += 1