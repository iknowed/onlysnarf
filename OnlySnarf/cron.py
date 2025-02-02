from crontab import CronTab
from OnlySnarf.settings import SETTINGS as settings

################
##### Cron #####
################

def delete(comment):
    cron = CronTab(user=str(settings.CRON_USER))
    cron.remove_all(comment=comment)
    cron.write()
    print("Cron Deleted: {}".format(comment))

def deleteAll():
    cron = CronTab(user=str(settings.CRON_USER))
    cron.remove_all()
    cron.write()
    print("Crons Deleted")

# use cron.comment to set cron name and find crons
def disable(comment):
    # find cron by comment
    cron = find(comment)
    cron.enable(False)
    cron.write()
    print("Cron Disabled: {}".format(comment))

def enable(comment):
    # find cron by comment
    cron = find(comment)
    cron.enable()
    cron.write()
    print("Cron Enabled: {}".format(comment))

def create(comment, args=[], minute=None, hour=None):
    print("Creating Cron: {}".format(comment))
    # if find(comment) is not None:
        # print("Warning: Cron Exists")
    cron = CronTab(user=str(settings.CRON_USER))
    cron.remove_all(comment=comment)
    args = [n.strip() for n in args]
    newCron = cron.new(command="/usr/local/bin/onlysnarfpy -cron {} {} >> /var/log/onlysnarf.log 2>&1".format(comment, " ".join(args)), comment=comment);
    newCron.hour.every(1)
    if minute is not None:
        newCron.minute.on(minute)
    if hour is not None:
        newCron.hour.on(hour)
    cron.write()
    print("Created Cron: {}".format(comment))

def list():
    cron = CronTab(user=str(settings.CRON_USER))
    print("Crons:")
    for job in cron:
        print(job)

def find(comment):
    cron = CronTab(user=str(settings.CRON_USER))
    iter1 = cron.find_comment(str(comment))
    for item in iter1:
        return item
    return False 

def getAll():
    cron = CronTab(user=str(settings.CRON_USER))
    jobs = []
    for job in cron:
        jobs.append(job)
    return jobs

###################
##### Special #####
###################

def discount(user, amount=None, months=None):
    args = ["-action","discount","-user",str(user)]
    if amount: 
        args.append(["-amount"])
        args.append([amount])
    if months:
        args.append(["-months"])
        args.append([months])
    create("discount-"+user, args)

def message(user, text=None, image=None, price=None):
    args = ["-action","message","-user",str(user)]
    if text: 
        args.append(["-text"])
        args.append(["\"{}\"".format(text)])
    if image:
        args.append(["-image"])
        args.append(["\"{}\"".format(image)])
    if price:
        args.append(["-price"])
        args.append(["\"{}\"".format(price)])
    create("message-"+user, args)

def post(text):
    args = ["-action","post","-text","\"{}\"".format(text)]
    create("post-"+user, args)

def upload(opt):
    args = ["-type",str(opt)]
    create("upload", args)

def uploadInput(type_, path):
    args = ["-type",str(type_),"-method","input","-input","\"{}\"".format(path)]
    create("upload-input"+str(path), args)

# check all scenes folders' data.txt's for "releaseDate"
def checkScenes():
    pass

# sends messages to users that were queued for a specific time
def sendQueuedMessages():
    pass

###############
##### Dev #####
###############

def test():
    create("upload-video", args=["-type","video"])
    # create("upload-balls", [], "30", "11")
    # create("check-scenes")
    # disable("upload-video")
    # enable("upload-video")
    return True


# Cron:

# Message:
# - All, etc

# Upload:
# - Gallery
# - Image
# - Video
# - Performer
# - Scene