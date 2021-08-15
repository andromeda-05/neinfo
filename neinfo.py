


#Ожидаем ввод
cmd_in = input ()
#Инициализируем парсер командной строки
cmd_parser = cCmdParser(cmd_in)
#Запускаем обработчик команд
cmd_proc = cCmdProc(cCmdParser.cmd, cCmdParser.param)
#Если команда отсутствует или несоответствуют параметры
#выполняем выход с сообщением
if !cmd_proc.status :
   pass # exit wiht message
print (cmd_proc.res)
