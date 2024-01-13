import random
import time
import os
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')
print("""
  _                 _       
 | |               (_)      
 | |     ___   __ _ _ _ __  
 | |    / _ \ / _` | | '_ \ 
 | |___| (_) | (_| | | | | |
 |______\___/ \__, |_|_| |_|
               __/ |        
              |___/         
""")
print("Trang Đăng Nhập Quản Trị")

adm = str("chien")
paswd = str("123456")

admin = input("Tên Tài Khoản : ")
passwd = input("Mật Khẩu : ")
if admin == adm:
        if passwd == paswd:
                print("Login Thành Công")
                time.sleep(2)
else:
        print("Tên Tài Khoản Hoặc Mật Khẩu Không Đúng !")
        exit()

chat_list = [
        "thâm vklll",
        "thâm vãi",
        "thâm như dái chó",
        "đánh tài ra xỉu",
        "đánh xỉu ra tài dkmmmmmmm",
        "mong húp tay này",
        "cho em húp 1 tay đi",
        "thông 4 tay",
        "thông 7 tay rồiiiiiii",
        "nettttttttttttttttttttttttt",
        "con chó admin",
        "thg làm game như buồi tao",
        "vãi cả cứt, cút ra đảo luôn",
        "game súc vật",
        "néttttt",
        "địt mẹ mày",
        "chua như cứt mèo thế này",
        "cầu 1-1 bú đi các em",
        "bẻ 1-1 luôn , sợ chó gì",
        "cầu 4321 đẹp thế ",
        "nét cầu 2112",
        "2112 kìa , bẻ là ngu đấy",
        "quên 2112 đi, cầu 212 đấy",
        "ngu thế",
        "do tham thôi:(",
        "dẩm lồn thật sự",
        "bẻ tài bằng chết",
        "CÓ CHẾT CŨNG PHẢI RA XỈU",
        "xỉu tất tay",
        "xỉu tiếp",
        "dỉu tieeps",
        "xỉu 10 bú đi các cháu",
        "631 đéo phải nặn đâu , tất xỉu đi",
        "kakakakak, lukaku kìa",
        "ngon rồi",
        "xỉu ra đảo nhé",
        "đm cay dái thế nhỉ",
        "vcl kìa?",
        "sao đm chán đời thế nhỉ",
        "muốn đấm thg top 1",
        "thg ad chim lỏ ra xỉu đi",
        "vai ca lon",
        "huppp",
        "cut roi",
        "vaiz lồn lại gãy",
        "địt mẹ sao lại có tài xỉu nhỉ",
        "game cứt chó này",
        "game đớp nhiều tiền vkl",
        "Thằng Lồn ad",
        "32 ra 6 đmmmmmmm",
        "thằng làm game súc vật vãi",
        "thg top 1 sống bỉ",
        "hahahahahah",
        "đi ỉa, bốc cứt lên ăn cho đỡ đói",
        "cút luôn",
        "ra đảo luôn, dkmmm",
        "dit to chung may",
        "có chết cũng tài",
        "bẻ tài bằng được",
        "bọn mày trêu tao à ?",
        "tiền chứ có phải lá mít đéo đâu ?",
        "dkm tham vãi lồn",
        "top 1 lộc đi",
        "tài ad ơi",
        "dỉu đi ad",
        "bú dcmmmmmmmm",
        "đập nát con game",
        "đánh tay nào chết tay đấy dkm",
        "1 phát ăn thì nó trả, địt mẹ game",
        "Tài hahahahahahahah",
        "Dm chó má vl",
        "bịp vãi cả lồn ra",
        "rút đc tiền mà ?",
        "tay này xịt, bố vào quay hũ",
        "may nó trả",
        "mừ ba",
        "dm chó game",
        "dm Xỉu rồiii",
        "TÀIIIIIIIIIIIIIIIIIIII",
        "xỉuuuuuuuuuuuuuuu",
        "má",
        "631",
        "642",
        "542",
        "cầu mong ad cho em bú 1 tay",
        "toàn bot nch với nhau à ??",
        "Chênh vênh chưa ?",
        "chim cút luôn rồi",
        "hết tay này t đéo phải đi wave nưac",
        "Lol má game",
        "Chênh vênh vcl",
        "Syyyyyyyyyyyyyy",
        "KÉP 10 TAY SAU",
        "Messsi cứ emm",
        "Ronaldooo Bú",
        "Messi rồi",
        "Cmmmmm ad",
        "BU X6",
        "hết 10m",
        "hôm nay chênh vênh quá ae",
        "bắt con tài",
        "bú con xỉu",
        "xỉu nét",
        "xỉu ra đảo",
        "XỈU RA ĐẢO",
        "có lồn xỉu",
        "NÉT TÀI",
        "lag à?",
        "5, 8",
        "nặn là thua",
        "dcm, haizz",
        "vl, giờ mới đặt",
        "may vcl, may đéo đặt cược",
        "đm",
        "?",
        "lại bệt rồi",
        "ôm bệt đi, bẻ là ngu",
        "bệt kìa",
        "bẻ là ngu, là cút",
        "bọn ngu hay đi bẻ",
        "123 nặn đẹp luôn",
        "X",
        "T",
        "xỉu cc",
        "địt mẹ tài",
        "lại trả vãi lồn game",
        "xin con xỉu ad ơi",
        "xin con tài admin owiiiiii",
        "đm cuộc đời",
        "xỉu 6",
        "tài 11",
        "vị này là vị lồn",
        "bọn máu cặc",
        "biết mà cố chấp",
        "xỉu về , xỉu về",
        "dmmmmmmmmmm",
        "rơi xâu vl",
        "tê vãi dái",
        "net ko",
        "lụm , lụm",
        "rồi bịp",
        "cu cứu",
        "1",
        "1-1 có à ?",
        "Dkmmmmmmmmmmmm",
        "Địt Mẹ Vãi lồn game ??",
        "vkl 63 ra 1, nghỉ mẹ đi",
        "chơi làm cc j nữa ?",
        "Húpppppp:)!",
        "Bú Ae ơi kk",
        "uồi",
        "admin đẹp zaiiiiiii vãi bướm",
        "Top 1 lộc tôi đi:)",
        "Cầu lồn gì đây ??",
        "Địt con mẹ",
        "tay này đéo ăn, tối bố nhảy sông",
        "Ngu rồi",
        "Bọn củ cặc này",
        "phán như đầu buồi bố m ý?",
        "Gãy 5m rồi",
        "đkmmmmmmmm cay dái thế",
        "Đkm thg ad buồi lồn",
        "Ae lộc tôi đc k:(",
        "Uớc đc ae lộc ạ",
        "vãi lồn cầu kìa",
        "chán vãi cứt",
        "cầu kiểu đéo gì vậy",
        "Nốt Tay này nghỉ",
        "đéo chơi nưa",
        "Tất Tay tài đi",
        "Tài toooooo",
        "Bú Tài",
        "Tài ra đảo",
        "Bú, nặn 65 vứt bát",
        "nặn làm cặc gì nx",
        "húp chưaaaaa",
        "63 ra 2",
        "ngon đét",
        "bú, 61 ra 4",
        "tưởng tối nay ăn cứt thay cơm",
        "Bú 10m",
        "Xỉu to",
        "Nổ hũ",
        "NỔ HŨ",
        "nổ",
        "hũ to vc",
        "thg ad sướng vkl",
        "Bú con xỉu đi ae",
        "Nặn 31 đập bát",
        "22 nặn làm đéo rì nữa ae =))",
        "ui sời , nét như sony",
        "Admin đẹp trai thế chứ lị",
        "cầu đẹp vkl",
        "done tôi với ae",
        "Bọn củ cặc",
        "chmay phán kiểu đéo rì đây ?",
        "Bọn ngu lồn cứ thích phán",
        "ad khoá mẹ mõm chno đi",
        "húppppppp",
        "húp",
        "mùi này mới là mùi tiền kk",
        "thơm phức haha",
        "nétt con tài",
        "Nét Con xỉu",
        "cầu bẻ đấy ae",
        "nét chưa kkkkkk",
        "múp nước thế =))",
        "thôi nghỉ",
        "tao đi rút tiền đây",
        "LÊN CHUẨN TÀI 12",
        "chết mẹ rồi",
        "Trả Cc đkmm",
        "đéo hiểu cầu",
        "chán",
        "xỉu to đi ae",
        "dkm ad",
        "tứ 11",
        "LÊN CON XỈU",
        "chênh vênh",
        "VÃI LỒN",
        "vãi cặc thật sự luôn",
        "Ôm đi",
        "bẻ là chết",
        "game bịp vãi",
        "cầu bịp",
        "XỈU TO",
        "admin ơi, cho em bú 1 tay đi",
        "đù, đấm thông 5 tay",
        "Vẫn Tài Được",
        "lại xỉu, dcm chán",
        "boss cân vkl",
        "vãi cứt trả tiền ạ",
        "xỉu 3 nổ hũ",
        "BÚ X10",
        "bú T12",
        "game khốn nạn",
        "đấm nốt tay tao rút",
        "cho adm",
        "bịp kk",
        "chấp nhận số phận thôi",
        "nút 1 của tao đâu ??",
        "nút 11 kìa",
        "đm bịp rồi",
        "gãy nhiều vãi lồn",
        "xúc cứt ăn vã rồi",
        "tối nay bỏ nhà đi bụi",
        "thế là mất con xe",
        "dcu m admin",
        "tài tiếp",
        "có cải cứt tài",
        "bip roi",
        "phải bắt bằng được con 22",
        "vc",
        "15",
        "14",
        "T11",
        "10",
        "9",
        "X8",
        "X7",
        "mútt",
        "6",
        "câm mồm",
        "ngu thì chết",
        "tham thì thâm",
        "đéo tài , tao đi ỉa.",
        "ĐÉO XỈU, T OFF RÚT TIỀN",
        "cân đi đm chúng m",
        "Game này rút đc không ae?",
        "game này rút đc",
        "Phán đi kìa, thánh phán đâu",
        "thể hiện tài năng thánh phán đi",
        "phán đc đấy",
        "Phán như đầu buồi ý",
        "phán cái máu lồn",
        "gãy all",
]

user_list = [
        "hupdiem",
        "thgadngu",
        "netnhusony",
        "aiuxhwbzeu6",
        "eqyntuwuez",
        "uwwynxkwual",
        "_hupdicacem",
        "bunuoclon",
        "hlpnuochau",
        "3consoi",
        "phaidoidoi",
        "nguyenngoc",
        "namden",
        "nguyentien",
        "phonggia",
        "hoangbach",
        "levu01",
        "nguyenbuonhehe",
        "phamgiang2",
        "hoangha06",
        "_nam_con_",
        "hoang_hau",
        "phambao05",
        "huydzdz",
        "abczewi07",
        "allintai",
        "latdonhacai",
        "xiu50m",
        "tai100m",
        "bangkhuang",
        "chenhvenh",
        "cuocsongbonchen",
        "hupcontai",
        "legiahuy2",
        "admindepzaithe",
        "lulzs82",
        "namsicola9",
        "khanhsky",
        "khanhbua01vip",
        "fakerno1",
        "xinnhecaitop",
        "top1vetay",
        "quanp006",
        "xinloca4",
        "TaoLaHuy",
        "haha11",
        "sao22win",
        "done678",
        "ancut123",
        "phchien72",
        "nguyendung4",
        "tranhoanganh",
        "hoangthanh2",
        "tranuquoc08",
        "vip999c",
        "az100c",
        "yb86",
        "thu789",
        "han2003",
        "rlbytinh",
        "huhuhu",
        "ahihi______82729",
        "36pho",
        "vmptd27",
        "393sunwin",
        "sun____winno1",
        "________cu1________",
        "quynhchi1",
        "letai03",
        "leanhtai",
        "xinbinhyen07",
        "luanguku",
        "kunaguero",
        "xin_duoc_nhat",
        "go_lai_tat_ca",
        "golai200m",
        "proooooo22",
        "kkkngao",
        "cuongdieu21",
        "sontran05",
        "____chenh____venh",
        "____bon_____chen_",
        "___cuoc___song31__",
        "__bu_con_tai____",
        "huanrose",
        "khanh_buavip",
        "ditmetaixiu",
        "_lamlaitatca_",
        "lukaku7777",
        "nohukhongtam",
        "ronaldodz38",
        "24quetoi",
        "88quetoi",
        "quenghich555",
        "lucky999999",
        "emba5599",
]

os.system('cls' if os.name == 'nt' else 'clear')

def menu_admin():
        print("""
           _____  __  __ _____ _   _ 
     /\   |  __ \|  \/  |_   _| \ | |
    /  \  | |  | | \  / | | | |  \| |
   / /\ \ | |  | | |\/| | | | | . ` |
  / ____ \| |__| | |  | |_| |_| |\  |
 /_/    \_\_____/|_|  |_|_____|_| \_|
                                     
                        (Pham Chien)

Tool Quản Trị Viên Tài Xỉu

1, Quản Lý Tài Xỉu
2, Quản Lý Chat online
3, Quản Lý Số dư người chơi
4, Quản Lý nạp tiền
5, Quản Lý rút tiền
6, Quản Lý Thông Tin Người Chơi
7, Đăng Xuất
""")
        menu = input("Vui Lòng Chọn Mục : ")
        if menu == "1":
                while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("BẮT ĐẦU PHIÊN MỚI..")
                        print("Bắt Đầu Đặt Cược")
                        print("")
                        stt = 0
                        for i in range(1, 300):
                                stt += 1
                                bot = random.choice(user_list)
                                tien_cuoc = random.randint(1, 100)
                                duoi_tien = [ ",000,000", ",000" ]
                                duoi_tien = random.choice(duoi_tien)
                                dat_cuoc = [ "TÀI", "XỈU" ]
                                dat_cuoc = random.choice(dat_cuoc)
                                print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL} đã đặt cược {Fore.RED}{Style.BRIGHT}{dat_cuoc}{Style.RESET_ALL} với số tiền cược là {Fore.YELLOW}{Style.BRIGHT}{tien_cuoc}{duoi_tien}${Style.RESET_ALL}")
                                time.sleep(0.10)
                        print("")
                        tiens1 = random.randint(250, 950)
                        tiens2 = random.randint(250, 950)
                        duoi_tien = [ f",{tiens2},{tiens1}", f",{tiens1},{tiens2}" ]
                        print(f"Hết Thời Gian Cược.")
                        tiens1 = random.randint(250, 950)
                        duoi_tien = random.choice(duoi_tien)
                        bot_cuoc1 = random.randint(99, 500)
                        print(f"TÀI : {bot_cuoc1} --> {Fore.YELLOW}{Style.BRIGHT}{tiens1}{duoi_tien}${Style.RESET_ALL}")
                        duoi_tien1 = [ f",{tiens1},{tiens2}", f",{tiens2},{tiens1}" ]
                        duoi_tien1 = random.choice(duoi_tien1)
                        bot_cuoc2 = random.randint(99, 500)
                        print(f"XỈU : {bot_cuoc2} --> {Fore.YELLOW}{Style.BRIGHT}{tiens2}{duoi_tien1}${Style.RESET_ALL}")
                        time.sleep(10)
                        print("1, Thay đổi các viên xí ngầu/xúc xắc")
                        print("2, Ngẫu Nhiên Xúc Xắc")
                        choose = input("Vui Lòng Chọn : ")
                        if choose == "1":
                                xn1 = int(input("Nhập Kết quả 1 : "))
                                xn2 = int(input("Nhập Kết quả 2 : "))
                                xn3 = int(input("Nhập Kết quả 3 : "))
                                kq = int(xn1 + xn2 + xn3)
                                tai = [11,12,13,14,15,16,17,18]
                                xiu = [3,4,5,6,7,8,9,10]
                                print("Đang Tung Xúc Xắc..")
                                time.sleep(1)
                                if kq in tai:
                                        print(f"Kết Quả Phiên Này Là : {Fore.RED}{Style.BRIGHT}{xn1}-{xn2}-{xn3} TÀI {kq}{Style.RESET_ALL}")
                                        time.sleep(10)
                                if kq in xiu:
                                        print(f"Kết Quả Phiên Này Là : {Fore.RED}{Style.BRIGHT}{xn1}-{xn2}-{xn3} XỈU {kq}{Style.RESET_ALL}")
                                        time.sleep(10)

                        if choose == "2":
                                xn1 = random.randint(1,6)
                                xn2 = random.randint(1,6)
                                xn3 = random.randint(1,6)
                                kq = int(xn1 + xn2 + xn3)
                                tai = [11,12,13,14,15,16,17,18]
                                xiu = [3,4,5,6,7,8,9,10]
                                print("Đang Tung Xúc Xắc..")
                                time.sleep(1)
                                if kq in tai:
                                        print(f"Kết Quả Phiên Này Là : {Fore.RED}{Style.BRIGHT}{xn1}-{xn2}-{xn3} TÀI {kq}{Style.RESET_ALL}")
                                        time.sleep(10)
                                if kq in xiu:
                                        print(f"Kết Quả Phiên Này Là : {Fore.RED}{Style.BRIGHT}{xn1}-{xn2}-{xn3} XỈU {kq}{Style.RESET_ALL}")
                                        time.sleep(10)
        if menu == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                stt = 0
                while True:
                        stt += 1
                        bot = random.choice(user_list)
                        chat = random.choice(chat_list)
                        print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL} : {chat}")
                        time.sleep(0.30)

        if menu == "3":
                while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("TNV   |   Số Dư")
                        stt = 0
                        for bot in user_list:
                                stt += 1
                                xu = random.randint(1, 100)
                                duoi_xu = [ ",000,000", ",000" ]
                                duoi_xu = random.choice(duoi_xu)
                                print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL} Số Dư Tài Khoản Còn : {Fore.YELLOW}{Style.BRIGHT}{xu}{duoi_xu}${Style.RESET_ALL},")
                        time.sleep(50)

        if menu == "4":
                while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("STT  |   TNV  |   Số Tiền Nạp   |    Phương Thức Nạp   |    Mã Giao Dịch")
                        stt = 0
                        for i in range(1, 150):
                                stt += 1
                                code = random.randint(11111111, 999999999)
                                bot = random.choice(user_list)
                                nap = random.randint(10, 100)
                                duoi_xu = [",000,000", ",000"]
                                duoi_xu = random.choice(duoi_xu)
                                pt_nap = [ "Nạp Bank" ]
                                pt_nap = random.choice(pt_nap)
                                print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL}  |  {nap}{duoi_xu}   |   {pt_nap}   |   MVN{code}")
                        time.sleep(1000)

        if menu == "5":
                while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("STT  |   TNV  |   Số Tiền RÚT   |   Ngân Hàng   |    Mã Giao Dịch  | STK")
                        stt = 0
                        for i in range(1, 150):
                                stt += 1
                                code = random.randint(11111111, 9999999999)
                                stk = random.randint(11111111, 9999999999)
                                bot = random.choice(user_list)
                                nap = random.randint(200, 500)
                                duoi_xu = [",000,000", ",000"]
                                duoi_xu = random.choice(duoi_xu)
                                pt_nap = [ "VCB", "BDIV", "AGRB", "MB", "VTB" ]
                                pt_nap = random.choice(pt_nap)
                                print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL}  |  {nap}{duoi_xu}   |   {pt_nap}   |   MWVC{code}   |   {stk}")
                        time.sleep(1000)

        if menu == "6":
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                        stt = 0
                        print("STT  |   TNV  |   SDT   |  Ngày Đăng Ký  |  Số Dư")
                        for bot in user_list:
                                xu = random.randint(1, 500)
                                duoi_xu = [",000,000", ",000"]
                                duoi_xu = random.choice(duoi_xu)
                                sdt = random.randint(111111111, 999999999)
                                date = random.randint(1, 30)
                                date2 = random.randint(1, 12)
                                date_c = ["2023", "2024"]
                                date_c = random.choice(date_c)
                                stt += 1
                                print(f"{stt}, {Fore.GREEN}{Style.BRIGHT}{bot}{Style.RESET_ALL}  |  0{sdt}  | {date}/{date2}/{date_c}  |  {xu}{duoi_xu}$")
                        time.sleep(100000)

        if menu == "7":
                print("Đăng xuất thành công")
                exit()

menu_admin()
