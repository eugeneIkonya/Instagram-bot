test=['sheila_gitau', 'maryjoel_', 'goddess.wathira', 'iamcardib', 'cohmedy', 'odi_wa_muranga', 'iamexray', '_ruffo__', 'abuyakimani1', 'lizz__wanda', 'thecupcakefactoryke', 'yoo__bros', 'da.ph.in.eki.ru.bi', 'minihoodclips', 's.hanisee_', 'kate.kabi', 'spaaaaamatozoa', 'konshens', 'hiuhu_', 'hits_the_blunt', 'kelsey_maliga', 'pickndropkenya', 'majorfreaks', '_laicey_carly_', 'm.arion_wendy_', 'pet_juicy', 'yungbeyt', 'just_sherrie_', 'mumbuaaa', 'lynn_lavina', 'thetavke', 'cynthiathuku', 'topshumor', '_hwembo_', 'funnyhoodvidz', 'everlyn_asiko_', 'vanstavel_', '_yvan___', 'ciiku_mo', 'watchifhigh', 'ikonya_mukuria', 'limes', 'drunkfailz', 'thatyorubaguy', 'foi__wambui', 'pubity', 'angelanzioki', 'calligraphyvideo', 'mwapea_', 'memezar', 'curiouspeter', 'keju_', 'siggy_lai', 'soinnocentparent', 'todayyearsold', 'm.wangola', 'lleshan', 'z.ighe', 'art.ig', 'tunnie_bear', 'kyalo_betty_', 'latest_memes_ke', 'pulselivekenya', 'gakii__c.m', 'thrifttttts', 'jetlaggedbuddy', '_.kago', 'lovllyn_maya', '_k.debbie', 'majuek_', '11_tiller', 'yasminetehrani_', 'nduunge', 'alvinsaviola', 'weed420memes', 'muthakka', 'bryanmitei', 'mitchell_tonui', '_.tamika_', 'puriitychege', '_iamjoyce._', 'nicole.zani', 'danklords_', '_r.a.b.z', 'mbvrire', 'slovi.a', 'bigmood_judi', 'brandon_anthony__', 'gangstasandhoes__', '_k.iing', 'cynthia___bailes', 'daddylonglegz._', 'michy_tallam', '_t.aio', '_shaygitau', '_muthoni_j_', 'phynahkimani', '_therealwendee', 'joshua.thumbi', 'shiechero', '_naphtali_', '_theetimah_', '_nyamwaya', '__betsy_bonnie', 'maxwell.tk', 'wambugzzz', '_chanta.l', '_.mutinda._', 'jean.loris', 'zawadi_kimutai', 'smithxv', 'nvee_drip', 'qunechi', 'suzanne_njuguna', 'shannie_keisha', 'fozziebearx', '_kitinya_', 'athena.topan', 'chrisbrownofficial', '_.chech._', 'lewis.n_k', 'joymurraya', 'trappi3', 'melissa_c.k', '4sn.rayo', 'kantesaint', 'murithi___', 'nduta__', 'ahlam.heykal', 'michellekinyua_', 'michellegathuku', 'muuojosephine', '__kimanga', 'gats_ian', 'a.michuu']
test2=["@"+word for word in test]
test_string=','.join(test2)

n=10
final = [test2[i * n:(i + 1) * n] for i in range((len(test2) + n - 1) // n )]
print(final)
for lists in final:
    word=','.join(lists)
    print(word)
