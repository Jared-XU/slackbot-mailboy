from slackclient import SlackClient
import time
import os,re

token = os.environ['SLACKBOT_TOKEN']
sc = SlackClient(token)

def parcel_help():
    pass

if sc.rtm_connect():
  while sc.server.connected is True:
        msg_from_slack = sc.rtm_read()
        if msg_from_slack:
            print "got something from slack: {} ".format(msg_from_slack)
            if 'text' in msg_from_slack[0].keys() and msg_from_slack[0]['text'].encode('ascii','ignore').startswith('@mailboy'):
                print msg_from_slack[0]['text'][8::]
                if msg_from_slack[0]['text'][8::].strip() == 'testing' :
                    sc.rtm_send_message("CBCK26G31", "I'm fine!")
                elif msg_from_slack[0]['text'][8::].strip() == 'help':
                    print "You need help!"
                    help_msg = '''You can type any of the following to interact with me:\n@mailboy username,\n@mailboy testing,\n@mailboy quicklookid
                    '''
                    sc.rtm_send_message("CBECMBL01", help_msg)
                else:
                    #suppose everything is handled from here
                    parcel_help()

                    #----make slack bot more interesting!
                    
                    question_slack = msg_from_slack[0]['text'][8::].strip()
                    try:
                      question = 'python quepy/examples/dbpedia/main.py ' + question_slack
                      res=os.popen(question).read()
                    except:
                      pass
                    p = re.match(r'}.*', res, re.M|re.I)
                    if p:
                        print 'match!'
                        print p.group()
                        print p.group(1)
                    sc.rtm_send_message("CBECMBL01", res)
                    #target, query, metadata = dbpedia.get_query(question)
                    #print query
                    #print metadata
            
        time.sleep(1)
else:
    print "Connection Failed"
