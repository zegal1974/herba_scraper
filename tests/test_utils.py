from herba_scraper.utils import Utils


class TestUtils:
    def test_get_file_type(self):
        assert Utils.get_file_type("abc.png") == Utils.FILETYPE_IMAGE
        assert Utils.get_file_type("abc.mp4") == Utils.FILETYPE_MOVIE
        assert Utils.get_file_type("abc.mkv") == Utils.FILETYPE_MOVIE
        assert Utils.get_file_type("abc.srt") == Utils.FILETYPE_SUBTT
        assert Utils.get_file_type("abc.torrent") == Utils.FILETYPE_TORRENT
        assert Utils.get_file_type("abc") == Utils.FILETYPE_OTHER
        assert Utils.get_file_type(".test") == Utils.FILETYPE_OTHER

    def test_is_image(self):
        assert Utils.is_image("abc.png")
        assert Utils.is_image("abc.jpg")

    def test_is_movie(self):
        assert Utils.is_movie("abc.mp4")
        assert Utils.is_movie("abc.mkv")

    def test_is_subtitle(self):
        assert Utils.is_subtitle("abc.srt")
        assert Utils.is_subtitle("abc.ass")

    def test_Utils(self):
        assert Utils.get_code("abc-100.png") == ("ABC", 100)
        assert Utils.get_code("abc-100c.png") == ("ABC", 100)
        assert Utils.get_code("test-abc-100c.png") == ("ABC", 100)
        assert Utils.get_code("example.com@TEST001C.mp4") == ("TEST", 1)
        assert Utils.get_code("example.com@TEST-123-nyap2p.com") == ("TEST", 123)
        assert Utils.get_code("example.com@TEST-123_2000k.mp4") == ("TEST", 123)
        assert Utils.get_code("example.com@TT-1234_2000k.mp4") == ("TT", 1234)
        assert Utils.get_code("test-abc-001ds") == ("ABC", 1)
        assert Utils.get_code("test-abc00001ds") == ("ABC", 1)
        assert Utils.get_code("[FHD]TEST-001") == ("TEST", 1)
        assert Utils.get_code("1avop00060hhb.mp4") == ("AVOP", 60)

    def test_decode(self):
        assert Utils.decode("abc-001") == ("ABC", "001", "")
        assert Utils.decode("abc-001a") == ("ABC", "001", "")
        assert Utils.decode("abc-001_test") == ("ABC", "001", "TEST")
        assert Utils.decode("abc-001_2023-02-10") == ("ABC", "001", "2023-02-10")
        assert Utils.decode("abcde-001_2023-02-10") == ("ABCDE", "001", "2023-02-10")
        assert Utils.decode("ab-001_2023-02-10") == ("AB", "001", "2023-02-10")
        assert Utils.decode("abcd001") == ("ABCD", "001", "")
        # assert Utils.decode("set-abcd001") == ('ABCD', "001", '')

    def test_convert_size(self):
        assert Utils.convert_size("1.5GB") == 1.5 * 1024 * 1024 * 1024
        assert Utils.convert_size("1.5gb") == 1.5 * 1024 * 1024 * 1024
        assert Utils.convert_size("1.5MB") == 1.5 * 1024 * 1024
        assert Utils.convert_size("1.5KB ") == 1.5 * 1024
        assert Utils.convert_size("1024") == 1024

    def test_get_magnet_info_hash(self):
        assert Utils.get_magnet_info_hash("magnet:?xt=urn:btih:abcd") == "abcd"
        assert Utils.get_magnet_info_hash("magnet:?xt=urn:btih:abcd&tr=http://tracker.example.com/announce") == "abcd"
        assert Utils.get_magnet_info_hash('magnet:?xt=urn:btih:39abde08e8260eeef8a894686e7700a5d4d09526&dn=ipx-994&xl=7079391874&tr=http://sukebei.tracker.wf:8888/announce&tr=http://1337.abcvg.info:80/announce&tr=http://bt.okmp3.ru:2710/announce&tr=http://bz.tracker.bz:80/announce&tr=http://fxtt.ru:80/announce&tr=http://ipv6.1337.cx:6969/announce&tr=http://ipv6.govt.hu:6969/announce&tr=http://nyaa.tracker.wf:7777/announce&tr=http://open-v6.demonoid.ch:6969/announce&tr=http://open.acgnxtracker.com:80/announce&tr=http://p2p.0g.cx:6969/announce&tr=http://share.camoe.cn:8080/announce&tr=http://t.acg.rip:6699/announce&tr=http://t.overflow.biz:6969/announce&tr=http://torrentsmd.com:8080/announce&tr=http://tr.cili001.com:8070/announce&tr=http://tracker.bt4g.com:2095/announce&tr=http://tracker.computel.fr:80/announce&tr=http://tracker.files.fm:6969/announce&tr=http://tracker.gbitt.info:80/announce&tr=http://tracker.ipv6tracker.ru:80/announce&tr=http://tracker.k.vu:6969/announce&tr=http://tracker.mywaifu.best:6969/announce&tr=http://tracker.servequake.com:9999/announce&tr=http://trackme.theom.nz:80/announce&tr=http://v6-tracker.0g.cx:6969/announce&tr=http://www.all4nothin.net:80/announce.php&tr=http://www.wareztorrent.com:80/announce&tr=https://1337.abcvg.info:443/announce&tr=https://opentracker.i2p.rocks:443/announce&tr=https://t1.hloli.org:443/announce&tr=https://tr.abiir.top:443/announce&tr=https://tr.abir.ga:443/announce&tr=https://tr.burnabyhighstar.com:443/announce&tr=https://tracker.foreverpirates.co:443/announce&tr=https://tracker.gbitt.info:443/announce&tr=https://tracker.imgoingto.icu:443/announce&tr=https://tracker.kuroy.me:443/announce&tr=https://tracker.lilithraws.cf:443/announce&tr=https://tracker.lilithraws.org:443/announce&tr=https://tracker.loligirl.cn:443/announce&tr=https://tracker.m-team.cc:443/announce.php&tr=https://tracker.nanoha.org:443/announce&tr=https://tracker.tamersunion.org:443/announce&tr=https://tracker1.520.jp:443/announce&tr=https://trackme.theom.nz:443/announce&tr=udp://open.stealth.si:80/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce') == "39abde08e8260eeef8a894686e7700a5d4d09526"
        