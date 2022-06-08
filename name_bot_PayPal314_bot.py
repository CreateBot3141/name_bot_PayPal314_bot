
def get_name (user_id):
    name = ''
    for line in str(user_id):
        sn = ''
        if line == '0':
            sn = 'a'
        if line == '1':
            sn = 'o'
        if line == '2':
            sn = 'y'
        if line == '3':
            sn = 'f'
        if line == '4':
            sn = 'h'
        if line == '5':
            sn = 'j'
        if line == '6':
            sn = 'r'
        if line == '7':
            sn = 'm'
        if line == '8':
            sn = 'g'
        if line == '9':
            sn = 'b'
        name = name + sn
    return  name   

def balans (user_id,namebot,сurrency):
    import iz_func
    itog = 0
    db,cursor = iz_func.connect ()
    sql = "select id,summ from money_log where namebot = '"+str(namebot)+"' and user_id = '"+str(user_id)+"' and currency = '"+str(сurrency)+"' "
    cursor.execute(sql)
    results = cursor.fetchall()    
    itog = 0        
    for row in results:
        id,summ = row.values()
        itog = itog + summ
    return itog  

def chek (user_id,namebot,сurrency):
    import iz_func
    db,cursor = iz_func.connect ()
    sql = "select id,summ,сurrency,key_kod from secret_key where status = 'Активный' and user_id = '"+str(user_id)+"' and сurrency = '"+str(сurrency)+"' "
    cursor.execute(sql)
    results = cursor.fetchall()        
    itog = 0
    for row in results:
        id,summ,сurrency,key_kod = row.values()
        itog = itog + summ
    return itog    

def ask_bin (user_id,namebot,сurrency): ### BTC/UAH 
    import ccxt
    import json
    client = ccxt.client = ccxt.binance ()
    orderbook = client.fetch_order_book (сurrency)  ### BTC/UAH
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    return ask

def bid_bin (user_id,namebot,сurrency): ### BTC/UAH 
    import ccxt
    import json
    client = ccxt.client = ccxt.binance ()
    orderbook = client.fetch_order_book (сurrency)  ### BTC/UAH
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    return bid

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    #import iz_game
    #import iz_main
    import time
    import iz_telegram
    #message_old = message_in
    label = 'send'
    label = 'n send'

    if message_in == 'Карта':         
        message_out = 'Обязательно введите карту'
        markup  = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)
        status = ""
    
    if message_in == 'Отмена':         
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        status = ''
        #exit (0)

    if message_in == 'Отменить': 
        message_out = 'Отмена операции'
        markup  = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        status = ''
        #exit (0)

    if message_in == 'Кoшелек':   
        #iz_func.save_variable (user_id,"status",'',namebot)     
        status = ''
        label = 'no send'
        summ_fiat_griv = balans (user_id,namebot,'гривны')
        print ('[summ_fiat_griv]',summ_fiat_griv)
        summ_fiat_BTC  = balans (user_id,namebot,'BTC')
        summ_fiat_USDT = balans (user_id,namebot,'USDT')
        summ_chek_griv = chek   (user_id,namebot,'гривны')
        summ_chek_USDT = chek   (user_id,namebot,'USDT')
        summ_chek_BTC  = chek   (user_id,namebot,'BTC')
        summ_exit_griv = balans (user_id,namebot,'гривны_перевод')
        summ_fiat_griv = '{:.2f}'.format (summ_fiat_griv)
        summ_fiat_BTC  = '{:.2f}'.format (summ_fiat_BTC)
        summ_fiat_USDT = '{:.2f}'.format (summ_fiat_USDT)
        summ_chek_griv = '{:.2f}'.format (summ_chek_griv)
        summ_chek_USDT = '{:.2f}'.format (summ_chek_USDT)
        summ_chek_BTC  = '{:.2f}'.format (summ_chek_BTC)
        summ_exit_griv = '{:.2f}'.format (summ_exit_griv)
        name = get_name (user_id)
        iz_telegram.save_variable (user_id,namebot,'name',name)
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_griv',summ_fiat_griv)
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_BTC',summ_fiat_BTC)
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_USDT',summ_fiat_USDT)
        iz_telegram.save_variable (user_id,namebot,'summ_chek_griv',summ_chek_griv)
        iz_telegram.save_variable (user_id,namebot,'summ_chek_USDT',summ_chek_USDT)
        iz_telegram.save_variable (user_id,namebot,'summ_chek_BTC',summ_chek_BTC)
        iz_telegram.save_variable (user_id,namebot,'summ_exit_griv',summ_exit_griv)
        
        #print ('[summ_fiat_griv]',summ_fiat_griv)
        
        answer = iz_telegram.send_message (user_id,namebot,'Кошелек','S',message_id)
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in == 'Новый': 
        answer = iz_telegram.send_message (user_id,namebot,'Укажите валюту пополнения','S',message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in == 'Создать_Гривны':
        label = 'no send'
        #message_out = '<b>Укажите сумму:</b>' + '\n'
        #message_out = message_out + '\n'
        #message_out = message_out + '‼️Подарочный чек можно подарить только один раз, после активации получателем деньги нельзя будет вернуть.'
        #markup = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)         
        
        #iz_func.save_variable (user_id,"Валюта",'Гривны',namebot) 
        #iz_func.save_variable (user_id,"status",'сумма чека',namebot) 
        
        iz_telegram.save_variable (user_id,namebot,"Валюта",'Гривны')
        iz_telegram.save_variable (user_id,namebot,"status",'сумма чека')
        
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        answer = iz_telegram.send_message (user_id,namebot,'Создать Гривны','S',0)
        #exit (0)

    if message_in == 'Создать_BTC':
        label = 'no send'
        #message_out = '<b>Укажите сумму:</b>' + '\n'
        #message_out = message_out + '\n'
        #message_out = message_out + '‼️Подарочный чек можно подарить только один раз, после активации получателем деньги нельзя будет вернуть.'
        #markup = ''        
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        
        #iz_func.save_variable (user_id,"Валюта",'BTC',namebot) 
        #iz_func.save_variable (user_id,"Валюта",'BTC',namebot) 
        
        iz_telegram.save_variable (user_id,namebot,"Валюта",'BTC')
        iz_telegram.save_variable (user_id,namebot,"Валюта",'BTC')
                
        answer = iz_telegram.send_message (user_id,namebot,'Создать BTC','S',0)
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        exit (0)

    if message_in == 'Создать_USDT':            
        label = 'no send'
        #message_out = '<b>Укажите сумму:</b>' + '\n'
        #message_out = message_out + '\n'
        #message_out = message_out + '‼️Подарочный чек можно подарить только один раз, после активации получателем деньги нельзя будет вернуть.'
        #markup = ''        
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        
        #iz_func.save_variable (user_id,"Валюта",'USDT',namebot) 
        #iz_func.save_variable (user_id,"status",'сумма чека',namebot) 
        
        iz_telegram.save_variable (user_id,namebot,"Валюта",'USDT')
        iz_telegram.save_variable (user_id,namebot,"status",'сумма чека')
        
        
        answer = iz_telegram.send_message (user_id,namebot,'Создать USDT','S',0)
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Созданный чек':        
        label = 'no send'
        markup      = ''
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where status = 'Активный' and user_id = '"+str(user_id)+"'  "
        cursor.execute(sql)
        results = cursor.fetchall()    
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        for row in results:
            id,summ,сurrency,key_kod = row.values()
            message_out = str(id) + ': На сумму: '+ str(summ)+' '+str(сurrency) + "\n"
            mn01 = types.InlineKeyboardButton(text=message_out,callback_data = "kod_"+str(id))
            markup.add(mn01)    
        message_out = 'Созданный чек'    
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in == 'Купить':  
        import iz_func   
        import iz_telegram      
        print ('[+] ----------------------------- [+]')
        iz_telegram.save_variable (user_id,namebot,'status','')        
        iz_telegram.save_variable (user_id,namebot,'status','Ввод BTC купить')        
        ask = ask_bin (user_id,namebot,'BTC/UAH') ###        
        iz_telegram.save_variable (user_id,namebot,'ask',str(ask))                
        answer = iz_telegram.send_message (user_id,namebot,'Купить02','S',message_id)        
        status = ''
        print ('[+] ----------------------------- [+]')

    if message_in == 'Замена_на_USDT_Купить':  
        answer = iz_telegram.send_message (user_id,namebot,'Купить03','S',message_id)      
        #iz_func.save_variable (user_id,'status','Ввод USDT купить',namebot)  
        iz_telegram.save_variable (user_id,namebot,'status','Ввод USDT купить')
        ask = ask_bin (user_id,namebot,'USDT/UAH') ###
        
        #iz_func.save_variable (user_id,'ask',str(ask),namebot)
        iz_telegram.save_variable (user_id,namebot,'ask',str(ask))
        
        answer = iz_telegram.send_message (user_id,namebot,'Купить04','S',message_id)    
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Замена_на_BTC_Купить':  
        answer = iz_telegram.send_message (user_id,namebot,'Купить01','S',message_id)      
        iz_func.save_variable (user_id,'status','Ввод BTC купить',namebot)  
        ask = ask_bin (user_id,namebot,'BTC/UAH') ###
        iz_func.save_variable (user_id,'ask',str(ask),namebot)
        answer = iz_telegram.send_message (user_id,namebot,'Купить02','S',message_id)
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Продать':
        import iz_func   
        import iz_telegram              
        iz_telegram.save_variable (user_id,namebot,'status','')
        iz_telegram.save_variable (user_id,namebot,'status','Ввод BTC продать')
        bid = bid_bin (user_id,namebot,'BTC/UAH') ###        
        iz_telegram.save_variable (user_id,namebot,'bid',str(bid))
        answer = iz_telegram.send_message (user_id,namebot,'Продать02','S',message_id)
        status = ''

    if message_in == 'Замена_на_USDT_Продать': 
        answer = iz_telegram.send_message (user_id,namebot,'Продать03','S',message_id)  

        
        #iz_func.save_variable (user_id,'status','Ввод USDT продать',namebot)  
        iz_telegram.save_variable (user_id,namebot,'status','Ввод USDT продать')
        
        
        bid = bid_bin (user_id,namebot,'USDT/UAH') ###
        
        #iz_func.save_variable (user_id,'bid',str(bid),namebot)
        iz_telegram.save_variable (user_id,namebot,'bid',str(bid))
        
        answer = iz_telegram.send_message (user_id,namebot,'Продать04','S',message_id)      
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Замена_на_BTC_Продать':
        answer = iz_telegram.send_message (user_id,namebot,'Продать01','S',message_id)  
        iz_telegram.save_variable (user_id,namebot,'status','Ввод BTC продать')                
        bid = bid_bin (user_id,namebot,'BTC/UAH') ###
        iz_telegram.save_variable (user_id,namebot,'bid',str(bid))        
        answer = iz_telegram.send_message (user_id,namebot,'Продать02','S',message_id) 
        status = ''

    if message_in.find ('ПродатьBTC_') != -1:
        import iz_func
        word = message_in.replace('ПродатьBTC_','') 
        volume_buy = 0
        summ       = 0
        db,cursor = iz_func.connect ()
        sql = "select id,volume_sell,summ,comment from application where id = "+str(word)+" limit 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        for rec in data: 
            id,summBTC,summGRV,comment = rec.values()
            print ('[+] BTC:',id,summBTC,summGRV,comment)
        ##iz_func.add_money (-1*summBTC,'BTC','Продажа BTC',namebot,user_id)
        ##iz_func.add_money (summGRV,'гривны','Продажа BTC',namebot,user_id)
        message_id = comment
        sql = "UPDATE application SET status = 'Конвертированно' WHERE `id` = '"+str(word)+"'"
        cursor.execute(sql)
        db.commit() 
        from telebot import types
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        markup.row("Карта")
        message_out = "✅Сделка совершена" + "\n"
        message_out = message_out + "" + "\n"
        message_out = message_out + "Продано: "+str(summBTC)+" BTC " + "\n"
        #iz_func.save_variable (user_id,'summBTC',str(summBTC),namebot)  
        message_out = message_out + "Получено: "+str(summGRV)+" KOR " + "\n"
        #iz_func.save_variable (user_id,'summGRV',str(summGRV),namebot)          
        message_out = message_out + "" + "\n"
        message_out = message_out + "Укажите номер банковской карты в валюте UAH (Украина) для перевода денег: " + "\n"        
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        iz_telegram.save_variable (user_id,namebot,'status','Введите карту для перевода_'+str(word))        
        status = ''

    if message_in.find('ПродатьUSDT') != -1: 
        word = message_in.replace('ПродатьUSDT_','') 
        #message_out = "Конвертация валюты"
        #markup      = ""  
        #answer     = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        volume_buy = 0
        summ       = 0
        db,cursor = iz_func.connect ()
        sql = "select id,volume_sell,summ,comment from application where id = "+str(word)+" limit 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        for rec in data: 
            id,summUSDT,summGRV,comment = rec.values()
            print ('[+] USDT:',id,summUSDT,summGRV,comment)

        iz_func.add_money (-1*summUSDT,'USDT','Продажа USDT',namebot,user_id)
        iz_func.add_money (summGRV,'гривны','Продажа USDT',namebot,user_id)
        message_out = "✅Сделка совершена" + "\n"
        message_out = message_out + "" + "\n"
        message_out = message_out + "Продано: "+str(summUSDT)+" USDT " + "\n"
        message_out = message_out + "Получено: "+str(summGRV)+" kor " + "\n" 
        message_out = message_out + "" + "\n"
        message_out = message_out + "Укажите номер банковской карты в валюте UAH (Украина) для перевода денег: " + "\n"
        #iz_func.save_variable (user_id,'status','Введите карту для перевода_'+str(word),namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','Введите карту для перевода_'+str(word)) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in.find ('money_BTC') != -1:
        message_in = 10
        lastid,checkout_url,address,amount = iz_func.chek (message_in,'BTC',user_id,namebot,"Пополнение счета")
        
        #iz_func.save_variable (user_id,"Номер чека",str(lastid),namebot) 
        #iz_func.save_variable (user_id,"Валюта",'BTC',namebot) 
        iz_telegram.save_variable (user_id,namebot,"Номер чека",str(lastid))
        iz_telegram.save_variable (user_id,namebot,"Валюта",'BTC')        
        
        answer = iz_telegram.send_message (user_id,namebot,'Новый чек','S',message_id) 
        markup = ''
        message_out = address
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in.find ('money_USDT') != -1:
        if 1==1:
            message_in = 10
            lastid,checkout_url,address,amount = iz_func.chek (10000,'USDT',user_id,namebot,"Пополнение счета")
            
        #iz_func.save_variable (user_id,"Номер чека",str(lastid),namebot)     
        #iz_func.save_variable (user_id,"Валюта",'USDT',namebot) 
        
        iz_telegram.save_variable (user_id,namebot,"Номер чека",str(lastid))
        iz_telegram.save_variable (user_id,namebot,"Валюта",'USDT')
        
        
        answer = iz_telegram.send_message (user_id,namebot,'Новый чек USDT','S',message_id)  
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in.find ('money_RUB') != -1:
        message_out = 'Укажите сумму пополнения (Рубли)' + '\n'
        
        #iz_func.save_variable (user_id,"Валюта",'Рубли',namebot) 
        iz_telegram.save_variable (user_id,namebot,"Валюта",'Рубли')
        
        from telebot import types    
        markup = types.InlineKeyboardMarkup(row_width=4)
        mn01 = types.InlineKeyboardButton(text="BTC",callback_data  = "money_BTC")
        mn02 = types.InlineKeyboardButton(text="USDT",callback_data = "money_USDT")
        mn03 = types.InlineKeyboardButton(text="Гривны",callback_data  = "money_GRV")        
        markup.add(mn01)    
        markup.add(mn02)    
        markup.add(mn03)    
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,"Валюта",'Рубли')
        
        #exit (0)

    if message_in.find ('money_GRV') != -1:
        #message_out = ''
        message_out = '<b>Введите сумму пополнения в гривнах</b>' + '\n'
        ##message_out = message_out + 'Введите сумму пополнения в гривнах:' + '\n'
        message_out = message_out + '' + '\n'
        message_out = message_out + '🔍При пополнении в этом направлении вы автоматически покупаете валюту которая привязана к этом боту (KOR) соотношение KOR и UAH 1:1' + '\n'
        message_out = message_out + '' + '\n'
        message_out = message_out + '📌После пополнения вы сможете обменять KOR на BTC или USDT автоматически за высчетом комиссии системы.' + '\n'
        message_out = message_out + 'Помощь - @....' + '\n'
        
        
        #iz_func.save_variable (user_id,"Валюта",'Гривны',namebot) 
        #iz_func.save_variable (user_id,"status",'Ввод суммы в гривнах',namebot) 
        
        iz_telegram.save_variable (user_id,namebot,"Валюта",'Гривны')
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод суммы в гривнах')
        
        
        #markup = ''
        
        from telebot import types    
        markup = types.InlineKeyboardMarkup(row_width=4)
        mn01 = types.InlineKeyboardButton(text="Назад",callback_data  = "Назад в баланс")
        markup.add(mn01)    
        
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        #answer = iz_telegram.send_message (user_id,namebot,'Введите сумму пополнения в гривнах','S',message_id)  
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in.find ('Пополнить баланс') != -1 or message_in.find ('Назад в баланс') != -1:
        message_out = 'Выберете валюту для пополнения кошелька:'+'\n'
        message_out = message_out + '(Для того что бы пополнить с карты, необходимо выбрать `Пополнить KOR`)'
        #message_out = message_out + 'Помощь - @....
        message_out = message_out + 'Помощь - @...' + '\n'
        from telebot import types    
        markup = types.InlineKeyboardMarkup(row_width=4)
        mn01 = types.InlineKeyboardButton(text="BTC",callback_data    = "money_BTC")
        mn02 = types.InlineKeyboardButton(text="USDT",callback_data   = "money_USDT")
        mn03 = types.InlineKeyboardButton(text="Пополнить KOR",callback_data = "money_GRV")
        mn04 = types.InlineKeyboardButton(text="Отмена",callback_data = "Отмена")
        markup.add(mn03)    
        markup.add(mn01)    
        markup.add(mn02) 
        markup.add(mn04) 
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('Выполнен_') != -1:
        markup = ''
        word = message_in.replace('Выполнен_','')
        message_out = 'Заявка № '+str(word) + ' Выполнен\n'
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        db,cursor = iz_func.connect ()
        sql = "UPDATE application SET status = 'Выполнен' WHERE `id` = '"+str(word)+"'"
        cursor.execute(sql)
        db.commit()
        sql = "select id,user_id from application where id = "+str(word)+" "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,user_id_send = row.values()
            answer = iz_telegram.send_message (user_id_send,namebot,'Заявка выполнена клиент','S',0) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('Отказать_') != -1:
        markup = ''
        word = message_in.replace('Отказать_','')
        message_out = 'Заявка № '+str(word) + ' Отказан \n'
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        db,cursor = iz_func.connect ()
        sql = "UPDATE application SET status = 'Отказан' WHERE `id` = '"+str(word)+"'"
        cursor.execute(sql)
        db.commit()
        sql = "select id,user_id from application where id = "+str(word)+" "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,user_id_send = row.values()
            answer = iz_telegram.send_message (user_id_send,namebot,'Заявка отказана клиент','S',0) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in == '/task':
        db,cursor = iz_func.connect ()
        sql = "select id,namebot,summ,address from application where namebot = '"+namebot+"' and status = '' "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,namebot,summ,address = row.values()
            markup = ''
            from telebot import types    
            markup = types.InlineKeyboardMarkup(row_width=4)
            mn01 = types.InlineKeyboardButton(text="Выполнен",callback_data = "Выполнен_"+str(id))
            mn02 = types.InlineKeyboardButton(text="Отказать",callback_data = "Отказать_"+str(id))
            markup.add(mn01,mn02)    
            message_out = 'Заявка № '+str(id) + '\n'
            message_out = message_out + '\n'            
            message_out = message_out + 'Сумма: '+str(summ) + '\n'
            message_out = message_out + 'Адрес: '+str(address) + '\n'            
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)
        
    if message_in == 'Вывод':
        message_out = 'Укажите валюту вывода:' + '\n'
        message_out = message_out + '' + '\n'
        message_out = message_out + 'Вывод осуществляется на внешний адрес - BTC или USDT' + '\n'
        from telebot import types    
        markup = types.InlineKeyboardMarkup(row_width=4)
        mn01 = types.InlineKeyboardButton(text="BTC",callback_data = "Выбор_BTC")
        mn02 = types.InlineKeyboardButton(text="USDT",callback_data = "Выбор_USDT")
        mn03 = types.InlineKeyboardButton(text="Отмена",callback_data = "Отмена")
        markup.add(mn01,mn02)
        markup.add(mn03)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)  
        
        #iz_func.save_variable (user_id,"Колличество вывода","",namebot)
        #iz_func.save_variable (user_id,"Адрес вывода","",namebot)
        
        iz_telegram.save_variable (user_id,namebot,"Колличество вывода","")
        iz_telegram.save_variable (user_id,namebot,"Адрес вывода","")
        
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'Выбор_BTC':
        answer = iz_telegram.send_message (user_id,namebot,'Укажите объем для перевода BTC','S',0) 
        
        #iz_func.save_variable (user_id,"status",'ВыводBTC',namebot) 
        iz_telegram.save_variable (user_id,namebot,"status",'ВыводBTC')
        
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Выбор_USDT':
        answer = iz_telegram.send_message (user_id,namebot,'Укажите объем для перевода USDT','S',message_id) 
        
        #iz_func.save_variable (user_id,"status",'ВыводUSDT',namebot) 
        iz_telegram.save_variable (user_id,namebot,"status",'ВыводUSDT')
        
        
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if message_in == 'Создать чек' or message_in == 'Создать чек обратно': 
        label = 'no send'
        summ_fiat_griv = balans (user_id,namebot,'гривны')
        summ_fiat_BTC  = balans (user_id,namebot,'BTC')
        summ_fiat_USDT = balans (user_id,namebot,'USDT')
        summ_fiat_griv = '{:.2f}'.format (summ_fiat_griv)
        summ_fiat_BTC  = '{:.2f}'.format (summ_fiat_BTC)
        summ_fiat_USDT = '{:.2f}'.format (summ_fiat_USDT)
        
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_griv',str(summ_fiat_griv))
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_BTC',str(summ_fiat_BTC))
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_USDT',str(summ_fiat_USDT))
        
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_griv',str(summ_fiat_griv))
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_BTC',str(summ_fiat_BTC))
        iz_telegram.save_variable (user_id,namebot,'summ_fiat_USDT',str(summ_fiat_USDT))
        
        answer = iz_telegram.send_message (user_id,namebot,'Создать чек быстро','S',message_id)
        status = ''
        
        
        #iz_func.save_variable (user_id,"status",'',namebot)         
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in.find ('КупитьBTC_') != -1:
        import iz_func
        word = message_in.replace('КупитьBTC_','') 
        volume_buy = 0
        summ       = 0
        db,cursor = iz_func.connect ()
        sql = "select id,volume_buy,summ,comment from application where id = "+str(word)+" limit 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        for rec in data: 
            id,summBTC,summGRV,comment = rec.values()
            print ('[+] BTC:',id,summBTC,summGRV,comment)
        #iz_func.add_money (summBTC,'BTC','Покупка BTC',namebot,user_id)
        #iz_func.add_money (-1*summGRV,'гривны','Покупка BTC',namebot,user_id)
        message_id = comment
        sql = "UPDATE application SET status = 'Конвертированно' WHERE `id` = '"+str(word)+"'"
        cursor.execute(sql)
        db.commit()       
        message_out = "✅Сделка совершена" + "\n"
        message_out = message_out + "" + "\n"
        message_out = message_out + "Куплено: "+str(summBTC)+" BTC " + "\n"
        message_out = message_out + "Потрачено: "+str(summGRV)+" KOR " + "\n" 
        message_out = message_out + "" + "\n"
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        status = ''        
        iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')        

    if message_in == 'КупитьUSDT': 
        #message_out = "Конвертация валюты"
        #markup      = ""  
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        summUSDT = float(iz_func.load_variable (user_id,'КупитьОбъемUSDT',namebot))
        summGRV  = float(iz_func.load_variable (user_id,'КупитьОбъемГривны',namebot))
        iz_func.add_money (summUSDT,'USDT','Покупка USDT',namebot,user_id)
        iz_func.add_money (-1*summGRV,'гривны','Покупка USDT',namebot,user_id)
        message_out = "✅Сделка совершена" + "\n"
        message_out = message_out + "" + "\n"
        message_out = message_out + "Куплено: "+str(summUSDT)+" USDT " + "\n"
        message_out = message_out + "Потрачено: "+str(summGRV)+" KOR " + "\n" 
        message_out = message_out + "" + "\n"
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'Созданный чек':        
        label = 'no send'
        markup      = ''
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where status = 'Активный' and user_id = '"+str(user_id)+"'  "
        cursor.execute(sql)
        results = cursor.fetchall()    
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        for row in results:
            id,summ,сurrency,key_kod = row.values()
            message_out = str(id) + ': На сумму: '+ str(summ)+' '+str(сurrency) + "\n"
            mn01 = types.InlineKeyboardButton(text=message_out,callback_data = "kod_"+str(id))
            markup.add(mn01)    
        message_out = 'Созданный чек'    
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')        
        
        #exit (0)

    if message_in == 'Выданный чек':        
        label = 'no send'
        markup      = ''
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod,user_id_activator from secret_key where status = 'Использован'  and user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        results = cursor.fetchall()    
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        for row in results:
            id,summ,сurrency,key_kod,user_id_activator = row.values()
            message_out = str(id) + ': На сумму: '+ str(summ)+' '+str(сurrency) +' Получил:'+str(user_id_activator)+"\n"
            mn01 = types.InlineKeyboardButton(text=message_out,callback_data = "eee_"+str(id))
            markup.add(mn01)    
        message_out = 'Выданный чек'
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'Пополнение средств':                    
        import iz_func
        label = 'no send'
        markup      = ''
        db,cursor = iz_func.connect ()
        sql = "select id,summ,currency,status from wallet where user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        results = cursor.fetchall()    
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        for row in results:
            id,summ,currency,status = row.values()
            message_out = 'Счет № '+str(id)+' на сумму: '+ str(summ)+' '+str(currency) +' '+status+"\n"
            mn01 = types.InlineKeyboardButton(text=message_out,callback_data = "wallet_"+str(id))
            markup.add(mn01) 
        message_out = 'Пополнение средств'    
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')        
        #exit (0)

    if message_in == 'Отчет':
        label = 'no send'
        message_out = '<b>Отчет</b>'
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        mn01 = types.InlineKeyboardButton(text ='Список созданных чеков ',callback_data = "Созданный чек")
        mn02 = types.InlineKeyboardButton(text ='Обналиченые чеки',callback_data = "Выданный чек")
        mn03 = types.InlineKeyboardButton(text ='Пополнения средств',callback_data = "Пополнение средств")
        markup.add(mn01)
        markup.add(mn02)
        markup.add(mn03)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')                
        #exit (0)

    if message_in == 'sitting01':
        sitting01 = iz_func.load_variable (user_id,"sitting01",namebot)
        if sitting01 == '':
            sitting01 = 'Да'
        if sitting01 == 'Да': 
            sitting01 = 'Нет'
        else: 
            sitting01 = 'Да'
            
        iz_func.save_variable (user_id,"sitting01",sitting01,namebot) 
        iz_telegram.save_variable (user_id,namebot,"sitting01",sitting01)        
        
        message_in = 'Настройки'
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'sitting02':
        sitting02 = iz_func.load_variable (user_id,"sitting02",namebot)        
        print ('[1]',sitting02)
        if sitting02 == '':
            sitting02 = 'Да'
        if sitting02 == 'Да': 
            sitting02 = 'Нет'
        else: 
            sitting02 = 'Да'
        print ('[2]',sitting02)    
        
        #iz_func.save_variable (user_id,"sitting02",sitting02,namebot)    
        iz_telegram.save_variable (user_id,namebot,"sitting02",sitting02)
        
        message_in = 'Настройки'
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'sitting03':
        sitting03 = iz_func.load_variable (user_id,"sitting03",namebot)
        if sitting03 == '':
            sitting03 = 'Да'
        if sitting03 == 'Да': 
            sitting03 = 'Нет'
        else: 
            sitting03 = 'Да'
        #iz_func.save_variable (user_id,"sitting03",sitting03,namebot) 
        iz_telegram.save_variable (user_id,namebot,"sitting03",sitting03)
        message_in = 'Настройки'
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if message_in == 'Настройки':
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)        
        sitting01 = iz_func.load_variable (user_id,"sitting01",namebot)
        sitting02 = iz_func.load_variable (user_id,"sitting02",namebot)
        sitting03 = iz_func.load_variable (user_id,"sitting03",namebot)
        if sitting01 == '':
            sitting01 = 'Да'
        if sitting02 == '':
            sitting02 = 'Да'
        if sitting03 == '':
            sitting03 = 'Да'
        if sitting01 == 'Да':
            sitting01 = 'Выводить имя '
        if sitting01 == 'Нет':
            sitting01 = 'Не выводить имя '
        if sitting02 == 'Да':
            sitting02 = 'Пароль включен'
        if sitting02 == 'Нет':
            sitting02 = 'Пароль выключен '
        if sitting03 == 'Да':
            sitting03 = 'Гривны'
        if sitting03 == 'Нет':
            sitting03 = 'Рубли'
        mn01 = types.InlineKeyboardButton(text=sitting01,callback_data = "sitting01")
        mn02 = types.InlineKeyboardButton(text=sitting02,callback_data = "sitting02")
        markup.add(mn01)
        markup.add(mn02)
        message_out = "Настройки"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('delete_') != -1:
        label = 'no send'
        word = message_in.replace('delete_','')
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where id = "+str(word)+" "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,summ,сurrency,key_kod = row.values()            
            sql = "UPDATE secret_key SET status = 'Удален' WHERE `id` = '"+str(word)+"'"
            cursor.execute(sql)
            db.commit()
            iz_telegram.add_money (user_id,namebot,summ,'гривны','Удаление кода '+key_kod,'')
            markup = ''
            message_out = 'Код уничтожен и больше не действует'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('hedden_') != -1:
        label = 'no send'
        word = message_in.replace('hedden_','')
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where id = "+str(word)+" "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,summ,сurrency,key_kod = row.values()
            markup = ''
            message_out = 'Код спрятан ,но действует'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('kod_') != -1:
        label = 'no send'
        word = message_in.replace('kod_','')
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where id = "+str(word)+" "
        cursor.execute(sql)
        results = cursor.fetchall()    
        for row in results:
            id,summ,сurrency,key_kod = row.values()
            from telebot import types
            markup = types.InlineKeyboardMarkup(row_width=4)
            mn01 = types.InlineKeyboardButton(text ='Удалить код',callback_data = "delete_"+str(id))
            mn02 = types.InlineKeyboardButton(text ='Спрятать',callback_data = "hedden_"+str(id))
            markup.add(mn01,mn02)            
            answer = iz_telegram.bot_send (user_id,namebot,key_kod,markup,message_id) 
            time.sleep (10)
            answer = iz_telegram.bot_send (user_id,namebot,"Информация спрятана для безопасности",'',message_id) 
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('Активные чеки') != -1:
        label = 'no send'
        db,cursor = iz_func.connect ()
        sql = "select id,summ,сurrency,key_kod from secret_key where status = 'Активный' and user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        results = cursor.fetchall()    
        message_out = ""
        message_out = message_out +  "⏳Активные чеки" + "\n"
        message_out = message_out +  "" + "\n"
        message_out = message_out +  "Тут показаны подарочные чеки которые вы создали, но их еще не активировал получатель, вы можете в любой момент удалить созданый вами подарочный чек, вернув деньги себе на баланс, для этого выберете чек ниже:"
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        for row in results:
            id,summ,сurrency,key_kod = row.values()
            key = str(id) + ': На сумму: '+ str(summ)+' KOR\n'
            mn01 = types.InlineKeyboardButton(text=key,callback_data = "kod_"+str(id))
            markup.add(mn01)
            
        mn01 = types.InlineKeyboardButton(text="Назад в чек",callback_data = "Создать чек обратно")
        markup.add(mn01)
            
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)    
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if message_in.find ('/start') != -1:
        import iz_telegram
        label = 'no send'  
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #iz_telegram.save_variable (user_id,namebot,"status",'')
        iz_telegram.save_variable (user_id,namebot,'status','')

    if status == 'сумма пополнения':
        label = 'no send'
        valuta = iz_func.load_variable (user_id,"Валюта",namebot)         
        if valuta == 'Гривны':
            answer = iz_telegram.create_chek_summ (message_in,valuta,'',namebot,user_id)
            message_out = ''
            message_out = message_out + 'Создан чек №' + str(answer) + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Сумма: ' +str(message_in) +' '+valuta + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'пополнение счета телеграмм бота' + '\n'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)

        if valuta == 'Рубли':
            answer = iz_telegram.create_chek_summ (message_in,valuta,'',namebot,user_id)
            message_out = ''
            message_out = message_out + 'Создан чек №' + str(answer) + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Сумма: ' +str(message_in) +' '+valuta + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'пополнение счета телеграмм бота' + '\n'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)

        if valuta == 'BTC':
            lastid,checkout_url,address,amount = iz_func.chek (message_in,'BTC',user_id,namebot,"Пополнение счета")
            print ('[+]',lastid,checkout_url,address,amount)
            message_out = ''
            message_out = message_out + 'Создан чек №' + str(lastid) + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Сумма: ' +str(amount) +' '+valuta + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'пополнение счета телеграмм бота' + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Адрес:' + '\n'
            message_out = message_out + address + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Адрес проверки поступления' + '\n'
            message_out = message_out +  checkout_url + '\n'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)

        if valuta == 'USDT':
            lastid,checkout_url,address,amount = iz_func.chek (message_in,'BTC',user_id,namebot,"Пополнение счета")
            print ('[+]',lastid,checkout_url,address,amount)
            message_out = ''
            message_out = message_out + 'Создан чек №' + str(lastid) + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Сумма: ' +str(amount) +' '+valuta + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'пополнение счета телеграмм бота' + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Адрес:' + '\n'
            message_out = message_out + address + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Адрес проверки поступления' + '\n'
            message_out = message_out +  checkout_url + '\n'
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if status == 'сумма чека':
        if label == 'no send':
            #iz_func.save_variable (user_id,"status","",namebot)
            iz_telegram.save_variable (user_id,namebot,'status','')
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
            #exit (0)


        ### Проверяем что это число
        try:
            summ = float(message_in)
            if summ == 0:
                #iz_func.save_variable (user_id,"status","",namebot)
                iz_telegram.save_variable (user_id,namebot,'status','')
                message_out = "Отмена создания чека"
                answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                #exit (0)
        except Exception as e:
            summ = 0

        if summ != 0 and summ > 0:
            valut_chek = iz_func.load_variable (user_id,"Валюта",namebot) 
            if valut_chek == 'Гривны':
                summ_fiat_griv = balans (user_id,namebot,'гривны')
                if summ_fiat_griv >= summ:
                    #iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    
                    #iz_func.save_variable (user_id,"summ чека",str(summ),namebot)
                    #iz_func.save_variable (user_id,"валюта чека","KOR",namebot)
                    
                    iz_telegram.save_variable (user_id,namebot,"summ чека",str(summ))
                    iz_telegram.save_variable (user_id,namebot,"валюта чека","KOR")
                    
                    #message_out = '🎁Подарочный чек на сумму: '+str(summ)+' kor успешно создан!'
                    #message_out = message_out +''+'\n'
                    #message_out = message_out + 'Для активации получателю необходимо отправить его боту '+'\n'
                    #message_out = message_out +''+'\n'
                    #answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)               
                    
                    #answer = iz_telegram.bot_send (user_id,namebot,"Подарочный чек на сумму",'',0)
                    answer = iz_telegram.send_message (user_id,namebot,'Подарочный чек на сумму','S',0) 
                    
                    sm = iz_telegram.get_secret_kod ()
                    db,cursor = iz_func.connect ()
                    sql = "INSERT INTO secret_key (`user_id`,`summ`,`namebot`,`key_kod`,`service_kod`,`сurrency`,`begin_t`,`end_t`,`status`) VALUES ('{}',{},'{}','{}','{}','{}',0,0,'Активный')".format (user_id,message_in,namebot,sm,'чек','гривны')         
                    cursor.execute(sql)
                    db.commit()   
                    message_out = sm
                    markup      = ''
                    iz_telegram.add_money (user_id,namebot,-1*summ,'гривны','Замараживание кода '+sm,'')
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                else:
                    iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    message_out = 'Недостаточно денег на счете'+'\n'
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)

            if valut_chek == 'USDT':
                summ_fiat_USDT = balans (user_id,namebot,'USDT')
                if summ_fiat_USDT >= summ:
                    iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    
                    iz_func.save_variable (user_id,"summ чека",str(summ),namebot)
                    iz_func.save_variable (user_id,"валюта чека","USDT",namebot)
                    
                    iz_telegram.save_variable (user_id,namebot,"summ чека",str(summ))
                    iz_telegram.save_variable (user_id,namebot,"валюта чека","USDT")
                    
                    
                    #message_out = 'Чек на сумму: '+str(summ)+' USDT.'+'\n'
                    #message_out = message_out +''+'\n'
                    #message_out = '🎁Подарочный чек на сумму: '+str(summ)+' USDT успешно создан!'
                    #message_out = message_out +''+'\n'
                    #message_out = message_out + 'Для активации получателю необходимо отправить его боту '+'\n'
                    
                    #answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)                
                    
                    #answer = iz_telegram.bot_send (user_id,namebot,"Подарочный чек на сумму",'',0)
                    answer = iz_telegram.send_message (user_id,namebot,'Подарочный чек на сумму','S',0) 
                    
                    sm = iz_telegram.get_secret_kod ()
                    db,cursor = iz_func.connect ()
                    sql = "INSERT INTO secret_key (`user_id`,`summ`,`namebot`,`key_kod`,`service_kod`,`сurrency`,`begin_t`,`end_t`,`status`) VALUES ('{}',{},'{}','{}','{}','{}',0,0,'Активный')".format (user_id,message_in,namebot,sm,'чек','USDT')         
                    cursor.execute(sql)
                    db.commit()   
                    message_out = sm
                    markup      = ''
                    iz_telegram.add_money (user_id,namebot,-1*summ,'USDT','Замараживание кода '+sm,'')
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                else:
                    #iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    message_out = 'Недостаточно денег на счете'+'\n'
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)


            if valut_chek == 'BTC':
                summ_fiat_BTC = balans (user_id,namebot,'BTC')
                print ('        [summ_fiat_BTC]',summ_fiat_BTC)
                if summ_fiat_BTC >= summ:
                    iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    #message_out = 'Чек на сумму: '+str(summ)+' BTC.'+'\n'
                    #message_out = message_out +''+'\n'
                    
                    #iz_func.save_variable (user_id,"summ чека",str(summ),namebot)
                    #iz_func.save_variable (user_id,"валюта чека","BTC",namebot)

                    iz_telegram.save_variable (user_id,namebot,"summ чека",str(summ))
                    iz_telegram.save_variable (user_id,namebot,"валюта чека","BTC")
                    
                    #message_out = '🎁Подарочный чек на сумму: '+str(summ)+' BTC успешно создан!'
                    #message_out = message_out +''+'\n'
                    #message_out = message_out + 'Для активации получателю необходимо отправить его боту '+'\n'
                    #answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)                
                    #answer = iz_telegram.bot_send (user_id,namebot,"Подарочный чек на сумму",'',0)                    
                    answer = iz_telegram.send_message (user_id,namebot,'Подарочный чек на сумму','S',0) 
                    sm = iz_telegram.get_secret_kod ()
                    db,cursor = iz_func.connect ()
                    sql = "INSERT INTO secret_key (`user_id`,`summ`,`namebot`,`key_kod`,`service_kod`,`сurrency`,`begin_t`,`end_t`,`status`) VALUES ('{}',{},'{}','{}','{}','{}',0,0,'Активный')".format (user_id,message_in,namebot,sm,'чек','BTC')         
                    cursor.execute(sql)
                    db.commit()   
                    message_out = sm
                    markup      = ''
                    iz_telegram.add_money (user_id,namebot,-1*summ,'BTC','Замараживание кода '+sm,'')
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                else:
                    #iz_func.save_variable (user_id,"status","",namebot)
                    iz_telegram.save_variable (user_id,namebot,'status','')
                    message_out = 'Недостаточно денег на счете'+'\n'
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
        else:
            message_out = "Укажите положительную сумму."
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)

        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if status == 'ВыводBTC':
        label = 'no send'
        try:
            summ = float(message_in)
            if summ == 0:
                #iz_func.save_variable (user_id,"status","",namebot)
                iz_telegram.save_variable (user_id,namebot,'status','')
                message_out = "Отмена процедуры вывода средств"
                answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                #exit (0)
        except Exception as e:
            summ = 0
            message_out = "Значение должно быть число"
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
        summ_fiat_BTC = balans (user_id,namebot,'BTC')
        if summ != 0 and summ >= 0.0001 and summ_fiat_BTC >= summ:
            answer = iz_telegram.send_message (user_id,namebot,'Адрес вывода средств BTC','S',message_id) 
            
            #iz_func.save_variable (user_id,"Колличество вывода",message_in,namebot)
            #iz_func.save_variable (user_id,"status","АдресBTC",namebot)
            
            iz_telegram.save_variable (user_id,namebot,"Колличество вывода",message_in)
            iz_telegram.save_variable (user_id,namebot,"status","АдресBTC")
            
            
        else:    
            message_out = "Укажите правильно сумму"
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)   

    if status == 'ВыводUSDT':
        label = 'no send'
        try:
            summ = float(message_in)
            if summ == 0:
                #iz_func.save_variable (user_id,"status","",namebot)
                iz_telegram.save_variable (user_id,namebot,'status','')
                
                message_out = "Отмена процедуры вывода средств"
                answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                #exit (0)
        except Exception as e:
            summ = 0
            message_out = "Значение должно быть число"
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)   
        summ_fiat_USDT = balans (user_id,namebot,'USDT') 
        if summ != 0 and summ >= 1 and summ_fiat_USDT >= summ:
            answer = iz_telegram.send_message (user_id,namebot,'Адрес вывода средств USDT','S',message_id) 
            
            #iz_func.save_variable (user_id,"Колличество вывода",message_in,namebot)
            #iz_func.save_variable (user_id,"status","АдресUSDT",namebot)
            
            iz_telegram.save_variable (user_id,namebot,"Колличество вывода",message_in)
            iz_telegram.save_variable (user_id,namebot,"status","АдресUSDT",message_in)
            
        else:    
            message_out = "Укажите правильно сумму"
            answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)   
        status = ''
        iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if status == 'АдресBTC':
        answer = iz_telegram.send_message (user_id,namebot,'Заявка принята.','S',message_id) 
        
        #iz_func.save_variable (user_id,"status","",namebot)
        #iz_func.save_variable (user_id,"Адрес вывода",message_in,namebot)
        
        iz_telegram.save_variable (user_id,namebot,'status','')
        iz_telegram.save_variable (user_id,namebot,"Адрес вывода",message_in)
        
        
        summ   =  iz_func.load_variable (user_id,"Колличество вывода",namebot)
        address =  iz_func.load_variable (user_id,"Адрес вывода",namebot)
        db,cursor = iz_func.connect ()
        iz_telegram.add_money (user_id,namebot,float(summ) * -1,'BTC','Замараживание на вывод ','')
        sql = "INSERT INTO `application` (summ,address,user_id,namebot,сurrency) VALUES ({},'{}','{}','{}','BTC')".format (summ,address,user_id,namebot)
        cursor.execute(sql)
        db.commit()
        
        #iz_func.save_variable (user_id,"Колличество вывода","",namebot)
        #iz_func.save_variable (user_id,"Адрес вывода","",namebot)
        
        iz_telegram.save_variable (user_id,namebot,"Колличество вывода","")
        iz_telegram.save_variable (user_id,namebot,"Адрес вывода","")
        
        message_out = 'Поступила новая заявка'
        iz_func.send_message_all_admin (namebot,message_out)
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot)
        iz_telegram.save_variable (user_id,namebot,'status','')        
        
        #exit (0)

    if status == 'АдресUSDT':
        message_out = "Заявка принята. Заявка обрабытывается"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
        
        #iz_func.save_variable (user_id,"status","",namebot)
        #iz_func.save_variable (user_id,"Адрес вывода",message_in,namebot)
        
        iz_telegram.save_variable (user_id,namebot,'status','')  
        iz_telegram.save_variable (user_id,namebot,"Адрес вывода",message_in)  
        
        summ   =  iz_func.load_variable (user_id,"Колличество вывода",namebot)
        address =  iz_func.load_variable (user_id,"Адрес вывода",namebot)
        db,cursor = iz_func.connect ()
        iz_telegram.add_money (user_id,namebot,float(summ) * -1,'USDT','Замараживание на вывод ','')
        sql = "INSERT INTO `application` (summ,address,user_id,namebot,сurrency) VALUES ({},'{}','{}','{}','USDT')".format (summ,address,user_id,namebot)
        cursor.execute(sql)
        db.commit()
        
        #iz_func.save_variable (user_id,"Колличество вывода","",namebot)
        #iz_func.save_variable (user_id,"Адрес вывода","",namebot)
        
        iz_telegram.save_variable (user_id,namebot,"Колличество вывода","")  
        iz_telegram.save_variable (user_id,namebot,"Адрес вывода","")  
        
        message_out = 'Поступила новая заявка'
        iz_func.send_message_all_admin (namebot,message_out)
        status = ''
        
        #iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        
        #exit (0)

    if status == 'Ввод BTC продать':   #### ВВод числа колличества BTC
        import iz_func
        message_in = message_in.replace (",",".")
        markup = ''
        message_out = 'Скрыто'
        answer = iz_func.load_variable (user_id,'answer',namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
        markup = ''
        message_out = ''
        message_out = message_out + "Идет рассчет сделки"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,'ПродатьОбъемBTC',message_in)                
        bid = bid_bin (user_id,namebot,'BTC/UAH') ###  
        try:
            summ = bid * float (message_in)/1    
        except Exception as e:
            summ = 0
        if summ != 0 and summ > 500:
            summ_fiat_BTC  = balans (user_id,namebot,'BTC')            
            if summ_fiat_BTC >= float (message_in): 
                iz_telegram.save_variable (user_id,namebot,'ПродатьОбъемГривны',str(summ))                
                db,cursor   = iz_func.connect () 
                sql = "INSERT INTO application (`namebot`,`user_id`,`volume_sell`,`sell_name`,`price`,summ,address,answer,buy_name,chenge,comment,link,status,volume_buy,сurrency) VALUES ('{}','{}',{},'{}',{},{},'','','','','','','',0,'')".format (namebot,user_id,message_in,'BTC',bid,summ)
                cursor.execute(sql)
                db.commit()
                lastid = cursor.lastrowid         
                message_out = ''
                message_out = message_out + "Обмен номер № "+str(lastid)+"" + "\n"
                message_out = message_out + "" + "\n"
                message_out = message_out + "Будет списано "+str(message_in)+" BTC" + "\n"
                message_out = message_out + "" + "\n"
                message_out = message_out + "Вы заказали: "+str(summ)+" KOR" + "\n"
                message_out = message_out + "Если вы уверены нажмите продать⬇️" + "\n"
                from telebot import types    
                markup = types.InlineKeyboardMarkup(row_width=4)
                mn01 = types.InlineKeyboardButton(text="Продать",callback_data = "ПродатьBTC_"+str(lastid))
                mn02 = types.InlineKeyboardButton(text="Отменить",callback_data = "Отменить")
                markup.add(mn01)
                markup.add(mn02)
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
                iz_telegram.save_variable (user_id,namebot,'status','')                
                sql = "UPDATE application SET comment = '"+str(answer)+"' WHERE `id` = '"+str(lastid)+"'"
                cursor.execute(sql)
                db.commit()  
            else:    
                message_out = 'Недостаточно средст BTC на счете'
                markup  = ''
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer)                 
        else:    
            message_out = 'Введите коректную цифру_1'
            markup  = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
        #status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        
        #exit (0)

    if status == 'Ввод USDT продать': 
        message_in = message_in.replace (",",".")
        
        #iz_func.save_variable (user_id,'ПродатьОбъемUSDT',message_in,namebot) 
        iz_telegram.save_variable (user_id,namebot,'ПродатьОбъемUSDT',message_in)
        
        bid = ask_bin (user_id,namebot,'USDT/UAH') ###  
        try:
            summ = bid * float (message_in)/1    
        except Exception as e:
            summ = 0
        if summ != 0 and summ > 500:
            #summ = bid * float (message_in)/1
            summ_fiat_USDT  = balans (user_id,namebot,'USDT')
            if summ_fiat_USDT >= float (message_in): 
            
                #iz_func.save_variable (user_id,'ПродатьОбъемГривны',str(summ),namebot) 
                iz_telegram.save_variable (user_id,namebot,'ПродатьОбъемГривны',str(summ))
                
                db,cursor   = iz_func.connect () 
                sql = "INSERT INTO application (`namebot`,`user_id`,`volume_sell`,`sell_name`,`price`,summ,address,answer,buy_name,chenge,comment,link,status,volume_buy,сurrency) VALUES ('{}','{}',{},'{}',{},{},'','','','','','','',0,'')".format (namebot,user_id,message_in,'BTC',bid,summ)
               #sql = "INSERT INTO application (`namebot`,`user_id`,`volume_sell`,`sell_name`,`price`,summ,address,answer,buy_name,chenge,comment,link,status,volume_buy,сurrency) VALUES ('{}','{}',{},'{}',{},{},'','','','','','','',0,'')".format (namebot,user_id,message_in,'BTC',bid,summ)
                cursor.execute(sql)
                db.commit()
                lastid = cursor.lastrowid         
                message_out = ''
                message_out = message_out + "Обмен номер № "+str(lastid)+"" + "\n"
                message_out = message_out + "" + "\n"
                message_out = message_out + "Будет списано "+str(message_in)+" USDT" + "\n"
                message_out = message_out + "" + "\n"
                message_out = message_out + "Вы заказали: "+str(summ)+" kor" + "\n"
                message_out = message_out + "Если вы уверены нажмите продать⬇️" + "\n"
                from telebot import types    
                markup = types.InlineKeyboardMarkup(row_width=4)
                mn01 = types.InlineKeyboardButton(text="Продать",callback_data = "ПродатьUSDT_"+str(lastid))
                mn02 = types.InlineKeyboardButton(text="Отменить",callback_data = "Отменить")
                markup.add(mn01)
                markup.add(mn02)
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
                
                #iz_func.save_variable (user_id,'status','',namebot)  
                iz_telegram.save_variable (user_id,namebot,'status','')
                
                sql = "UPDATE application SET comment = '"+str(answer)+"' WHERE `id` = '"+str(lastid)+"'"
                cursor.execute(sql)
                db.commit()  

            else:    
                message_out = 'Недостаточно средст USDT на счете'
                markup  = ''
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)    

        else:    
            #iz_func.save_variable (user_id,'status','',namebot) 
            message_out = 'Введите коректную цифру_2'
            markup  = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        #status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if status == 'Ввод суммы в гривнах':
        try:
            summ = float(message_in)
        except Exception as e:
            summ = 0
        if summ >= 5: 
            lastid = 143        
            message_out = ''
            message_out = message_out + '☑️Создан инвойс на пополнение №143' + '\n'
            message_out = message_out + 'Сумма: '+str(message_in)+' UAH' + '\n'
            summ_bonus  = float(message_in)*102/100
            message_out = message_out + 'Будет куплено: '+str(summ_bonus)+' KOR' + '\n'
            message_out = message_out + 'Для того что бы пополнить баланс, оплатите по ссылке ниже⬇️' + '\n'
            message_out = message_out + '' + '\n'
            message_out = message_out + 'Xxxxxxxx.link' + '\n'
            #iz_func.save_variable (user_id,"status",'',namebot) 
            iz_telegram.save_variable (user_id,namebot,'status','')
            markup = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        else:
            message_out = 'Укажите правельную сумму'
            markup = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
            #iz_func.save_variable (user_id,"status",'',namebot) 
            iz_telegram.save_variable (user_id,namebot,'status','')
        status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        
        #exit (0)

    if status == 'Ввод BTC купить':   #### ВВод числа колличества BTC
        import iz_func
        message_in = message_in.replace (",",".")
        markup = ''
        message_out = 'Скрыто'
        answer = iz_func.load_variable (user_id,'answer',namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
        markup = ''
        message_out = ''
        message_out = message_out + "Идет рассчет сделки"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        
        #iz_func.save_variable (user_id,'КупитьОбъемBTC',message_in,namebot) 
        iz_telegram.save_variable (user_id,namebot,'КупитьОбъемBTC',message_in)
        
        ask = ask_bin (user_id,namebot,'BTC/UAH') ###  
        try:
            summ = ask * float (message_in)/1    
        except Exception as e:
            summ = 0
        summ_fiat_GRV  = balans (user_id,namebot,'гривны')
        if summ != 0 and summ > 500 and summ_fiat_GRV >= summ:
            summ = ask * float (message_in)/1
            #iz_func.save_variable (user_id,'КупитьОбъемГривны',str(summ),namebot) 
            iz_telegram.save_variable (user_id,namebot,'КупитьОбъемГривны',str(summ))            
            db,cursor   = iz_func.connect () 
            sql = "INSERT INTO application (`namebot`,`user_id`,`volume_buy`,`buy_name`,`price`,summ,address,answer,sell_name,chenge,comment,link,status,volume_sell,сurrency) VALUES ('{}','{}',{},'{}',{},{},'','','','','','','',0,'')".format (namebot,user_id,message_in,'BTC',ask,summ)
           #sql = "INSERT INTO application (`namebot`,`user_id`,`volume_sell`,`sell_name`,`price`,summ,address,answer,buy_name,chenge,comment,link,status,volume_buy,сurrency) VALUES ('{}','{}',{},'{}',{},{},'','','','','','','',0,'')".format (namebot,user_id,message_in,'BTC',bid,summ)
            cursor.execute(sql)
            db.commit()
            lastid = cursor.lastrowid         
            message_out = ''
            message_out = message_out + "Обмен номер № "+str(lastid)+"" + "\n"
            message_out = message_out + "" + "\n"
            message_out = message_out + "Будет списано "+str(summ)+" KOR" + "\n"
            message_out = message_out + "" + "\n"
            message_out = message_out + "Вы заказали: "+str(message_in)+" BTC" + "\n"
            message_out = message_out + "Если вы уверены нажмите купить⬇️" + "\n"
            from telebot import types    
            markup = types.InlineKeyboardMarkup(row_width=4)
            mn01 = types.InlineKeyboardButton(text="Купить",callback_data = "КупитьBTC_"+str(lastid))
            mn02 = types.InlineKeyboardButton(text="Отменить",callback_data = "Отменить")
            markup.add(mn01)
            markup.add(mn02)
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
            #iz_func.save_variable (user_id,'status','',namebot) 
            iz_telegram.save_variable (user_id,namebot,'status','')
            sql = "UPDATE application SET comment = '"+str(answer)+"' WHERE `id` = '"+str(lastid)+"'"
            cursor.execute(sql)
            db.commit()  
        else:    
            message_out = 'Введите коректную цифру_4'
            #iz_func.save_variable (user_id,'status','',namebot) 
            markup  = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
            if 500 > summ:
                message_out = 'Сумма меньше минимально-дозволенной'
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
            if summ_fiat_GRV <= summ:
                message_out = 'Не хватает средств на балансе'
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
        #status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if status == 'Ввод USDT купить': 
        import iz_func
        message_in = message_in.replace (",",".")
        iz_func.save_variable (user_id,'КупитьОбъемUSDT',message_in,namebot)
        iz_telegram.save_variable (user_id,namebot,'КупитьОбъемUSDT',message_in)        
        ask = ask_bin (user_id,namebot,'USDT/UAH') ###  
        try:
            summ = ask * float (message_in)/1    
        except Exception as e:
            summ = 0
        summ_fiat_GRV  = balans (user_id,namebot,'гривны')    
        if summ != 0 and summ > 500 and summ_fiat_GRV >=summ:
            summ = ask * float (message_in)/1
            
            #iz_func.save_variable (user_id,'КупитьОбъемГривны',str(summ),namebot) 
            iz_telegram.save_variable (user_id,namebot,'КупитьОбъемГривны',str(summ)) 
            
            
            lastid = 100
            message_out = ''
            message_out = message_out + "Обмен номер № "+str(lastid)+"" + "\n"
            message_out = message_out + "" + "\n"
            message_out = message_out + "Будет списано "+str(summ)+" KOR" + "\n"
            message_out = message_out + "" + "\n"
            message_out = message_out + "Вы заказали: "+str(message_in)+" USDT" + "\n"
            message_out = message_out + "Если вы уверены нажмите купить⬇️" + "\n"
            from telebot import types    
            markup = types.InlineKeyboardMarkup(row_width=4)
            mn01 = types.InlineKeyboardButton(text="Купить",callback_data = "КупитьUSDT")
            mn02 = types.InlineKeyboardButton(text="Отменить",callback_data = "Отменить")
            markup.add(mn01)
            markup.add(mn02)
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
            #iz_func.save_variable (user_id,'status','',namebot)  
            iz_telegram.save_variable (user_id,namebot,'status','')
        else:    
            message_out = 'Введите коректную цифру_3'
            markup  = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
            print ('[+]',summ,summ_fiat_GRV)
            if 500 > summ:
                message_out = 'Сумма меньше минимально-дозволенной'
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
            if summ_fiat_GRV <= summ:
                message_out = 'Не хватает средств на балансе '+str(summ_fiat_GRV)+". Введите нужную сумму"
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
            if 0 == summ:
                message_out = 'Вы точно ввели число?'
                answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,answer) 
        #status = ''
        #iz_func.save_variable (user_id,"status",'',namebot) 
        #exit (0)

    if status.find ('Введите карту для перевода') != -1:
        word = status.replace('Введите карту для перевода_','') 
        answer = iz_telegram.send_message (user_id,namebot,'Cредства отправлены на вашу карту','S',0)        
        db,cursor = iz_func.connect ()
        sql = "UPDATE application SET address = '"+str(message_in)+"' WHERE `id` = "+str(word)+""
        iz_func.save_variable (user_id,'status','',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        cursor.execute(sql)
        db.commit()       
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        status = ''
        iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)

    if label == 'send':
        db,cursor = iz_func.connect ()
        sql = "SELECT id,user_id,summ,сurrency FROM `secret_key` where key_kod = '"+str(message_in)+"' and status = 'Активный' "
        cursor.execute(sql)
        data = cursor.fetchall()
        lb = 'No'
        for rec in data: 
            lb = 'Yes'
            id_kod,user_id_kod,summ_kod,currency_kod = rec.values()            
            if str(user_id_kod) == str(user_id):
                message_out = 'Созданный Вами код не может быть активирован Вами'
                answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
            else:
                message_out = 'Активация кода\n'
                message_out = message_out + "Ваш баланс увеличен на "+str(summ_kod) + " kor"
                answer = iz_telegram.bot_send (user_id,namebot,message_out,'',0)
                message_out = 'Ваш чек активирован'+'\n'
                message_out = message_out +''+'\n'
                message_out = message_out +'Номер чека:'+str(id_kod)+'\n'
                message_out = message_out +'Сумма: '+str(summ_kod)+'\n'
                message_out = message_out +'Получатель: '+str(get_name (user_id))+'\n'
                answer = iz_telegram.bot_send (user_id_kod,namebot,message_out,'',0)
                sql = "UPDATE secret_key SET user_id_activator = '"+str(user_id)+"' WHERE `id` = '"+str(id_kod)+"'"
                cursor.execute(sql)
                db.commit()
                sql = "UPDATE secret_key SET status = 'Использован' WHERE `id` = '"+str(id_kod)+"'"
                cursor.execute(sql)
                db.commit()
                iz_telegram.add_money (user_id,namebot,summ_kod,currency_kod,'Активация чека: '+str(id_kod),'Оплачен чеком')
        status = ''
        iz_func.save_variable (user_id,"status",'',namebot) 
        iz_telegram.save_variable (user_id,namebot,'status','')
        #exit (0)














