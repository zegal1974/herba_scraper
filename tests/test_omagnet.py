
import os

from herba_scraper.omagnet import Omagnet


class TestOmagnet:

    def test_parse(self):
        with open('tests/files/0magnet.html', 'r', encoding='utf-8') as f:
            content = f.read()
            om = Omagnet()
            data = om.parse(content)

            assert data['link'] == 'magnet:?xt=urn:btih:39abde08e8260eeef8a894686e7700a5d4d09526&dn=ipx-994&xl=7079391874&tr=http://sukebei.tracker.wf:8888/announce&tr=http://1337.abcvg.info:80/announce&tr=http://bt.okmp3.ru:2710/announce&tr=http://bz.tracker.bz:80/announce&tr=http://fxtt.ru:80/announce&tr=http://ipv6.1337.cx:6969/announce&tr=http://ipv6.govt.hu:6969/announce&tr=http://nyaa.tracker.wf:7777/announce&tr=http://open-v6.demonoid.ch:6969/announce&tr=http://open.acgnxtracker.com:80/announce&tr=http://p2p.0g.cx:6969/announce&tr=http://share.camoe.cn:8080/announce&tr=http://t.acg.rip:6699/announce&tr=http://t.overflow.biz:6969/announce&tr=http://torrentsmd.com:8080/announce&tr=http://tr.cili001.com:8070/announce&tr=http://tracker.bt4g.com:2095/announce&tr=http://tracker.computel.fr:80/announce&tr=http://tracker.files.fm:6969/announce&tr=http://tracker.gbitt.info:80/announce&tr=http://tracker.ipv6tracker.ru:80/announce&tr=http://tracker.k.vu:6969/announce&tr=http://tracker.mywaifu.best:6969/announce&tr=http://tracker.servequake.com:9999/announce&tr=http://trackme.theom.nz:80/announce&tr=http://v6-tracker.0g.cx:6969/announce&tr=http://www.all4nothin.net:80/announce.php&tr=http://www.wareztorrent.com:80/announce&tr=https://1337.abcvg.info:443/announce&tr=https://opentracker.i2p.rocks:443/announce&tr=https://t1.hloli.org:443/announce&tr=https://tr.abiir.top:443/announce&tr=https://tr.abir.ga:443/announce&tr=https://tr.burnabyhighstar.com:443/announce&tr=https://tracker.foreverpirates.co:443/announce&tr=https://tracker.gbitt.info:443/announce&tr=https://tracker.imgoingto.icu:443/announce&tr=https://tracker.kuroy.me:443/announce&tr=https://tracker.lilithraws.cf:443/announce&tr=https://tracker.lilithraws.org:443/announce&tr=https://tracker.loligirl.cn:443/announce&tr=https://tracker.m-team.cc:443/announce.php&tr=https://tracker.nanoha.org:443/announce&tr=https://tracker.tamersunion.org:443/announce&tr=https://tracker1.520.jp:443/announce&tr=https://trackme.theom.nz:443/announce&tr=udp://open.stealth.si:80/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce'
            assert data['info_hash'] == '39abde08e8260eeef8a894686e7700a5d4d09526'
            assert data['filesize'] == 7075958620
            assert data['files'] == "[{\"name\":\"ipx-994.mp4\",\"size\":7054483783},{\"name\":\"x u u 6 2 . c o m.mp4\",\"size\":12677283},{\"name\":\"最 新 位 址 獲 取.txt\",\"size\":136},{\"name\":\"社 區 最 新 情 報.mp4\",\"size\":15089008},{\"name\":\"聚 合 全 網 H 直 播.html\",\"size\":150}]"
