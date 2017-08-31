# -*- coding:utf-8 -*-
import os,sys,imp,time,json,re
import lib.config_
import  lib.file
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


chk_job_setting()