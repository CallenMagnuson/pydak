from daktronics import DakSerial, Daktronics

if __name__ == '__main__':
    print("UDP MULTICAST 21000")
    dak_data = DakSerial()
    dak = Daktronics("baseball", dak_data)
    while True:
        dak.update()
        print("--------------------------------------------------------------")
        print("Ball: "+dak['Ball'])
        print("Strike: "+dak['Strike'])
        print("Out: "+dak['Out'])
        print("Inning: "+dak['Inning'])
        print("Home Hits: "+dak['Home Hits'])
        print("--------------------------------------------------------------")
