 #coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
import os
import ReadConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

case_path = os.path.join(os.getcwd())
test_report=os.path.join(os.path.dirname(case_path)+"\\report")

# mailto_list = ["kxz@ahbcht.com","792748342@qq.com","sxx@ahbcht.com"]  可以给多个用户发送邮件
mailto_list = [ReadConfig.email]  #收件人邮箱账号
mail_host = "smtp.ahbcht.com"  #发件人邮箱的SMIP服务器
mail_user = "kxz@ahbcht.com"   #发件人的邮件地址
mail_pass = "Bcht@126"  #发件人的邮箱密码

def mail(mail_subject,filename):
      msg=MIMEMultipart()
      msg["From"] = mail_user  # 发件人
      msg["To"] = ";".join(mailto_list)  # 收件人
      msg['Subject'] = mail_subject    #邮件标题

      with open(filename,"rb") as f:
          fc=f.read()
      txt=MIMEText(fc,'html','utf-8')
      msg.attach(txt)
      #构造附件
      att = MIMEText(open(filename, "rb").read(), "base64", "utf-8")
      att["Content-Type"] = "application/octet-stream"
      # 附件名称为中文时的写法
      # att.add_header("Content-Disposition", "attachment", filename=("gbk", "", "5.3版本接口详细测试结果.html"))
      # 附件名称非中文时的写法
      att["Content-Disposition"] = 'attachment; filename="test.html")'
      msg.attach(att)
      smtp = smtplib.SMTP()
      smtp.connect(mail_host)
      smtp.login(mail_user, mail_pass)
      smtp.sendmail(mail_user, mailto_list, msg.as_string())
      smtp.quit()

def new_report(test_dir):
     # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path  # 发送邮件
	
	#def new_report(test_dir):
     # 列举test_dir目录下的所有文件，结果以列表形式返回。
    #lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    #lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    #file_path = os.path.join(test_dir, lists[-1])
    #return file_path  # 发送邮件



