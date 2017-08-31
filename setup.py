# -*- coding:utf-8 -*-
import os,sys,imp,time,json,re
import lib.config_
import  lib.file
import lib.database

p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010-628888'))



re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)","192.168.1.1")
exit();



where = {"ServerAsSetId like ": "%TYSV08065287%"}
print where
exit()


def chk_job_setting():
    try:
        content = lib.file.read(lib.config_.BasePath+'/setting.json')
        content=re.sub(r'\/\*.*\*\/','',content)
        content=re.sub(r'\/\/.*\n','\n',content)
        cronjobs=json.loads(content)
        if len(cronjobs)<=0:
            return False,'Not cronjob start!'
        else:
            msg="";
            for cron_name,cron_options in cronjobs.items():
                msg+= cron_options['cron_time']+"\t"+cron_name+"\t"+json.dumps(cron_options['params'])+"\n"
            return True,msg
    except:
        return False,"setting.json json format error!"

# chk_job_setting()


def get_m():
    db = lib.database.load(dbname='devicecenter')

    table = 'device_info'
    field = "ServerId,ServerAsSetId,ServerIP"

    # 单条记录查询
    where = {"ServerId": "12315"}
    info = db.select_info(where, table, field)
    print info
    # 多条记录查询
    where = {"ServerAsSetId like ": "%TYSV08065287%"}
    print where
    exit(1000)
    rows = db.select_list(where, table, field)
    print rows
    exit
    # 插入多条数据
    data = [
        {"ServerId": 100, "ServerAsSetId": "TYSV100", "ServerIP": "11.129.129.159"},
        {"ServerId": 101, "ServerAsSetId": "TYSV101", "ServerIP": "11.129.129.160"}
    ]
    db.insert_data(data, table)
    # # 修改数据
    # data = {"ServerAsSetId": "TYSV100", "ServerIP": "12.129.129.159"},
    # where = {"ServerId": 100}
    # db.update_data(data, where)
    # 删除数据
    where = {"ServerId": 100}
    db.delete_data(where, table)


get_m()

