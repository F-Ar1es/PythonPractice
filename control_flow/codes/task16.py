money=100
s=0
for gongji in range(21):
    for muji in range(34):
        for xiaoji in range(301):
            s=5*gongji+3*muji+xiaoji/3
            if s==money and gongji+muji+xiaoji==100:
                print(f"公鸡 {gongji} 只，母鸡 {muji} 只，小鸡 {xiaoji} 只")