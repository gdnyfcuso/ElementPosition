
import aircv as ac

def getPositionBylocationmap(posimg):
    print(posimg['spath'])
    print(posimg['dpath'])
    imsrc = ac.imread(posimg['spath'])
    imobj = ac.imread(posimg['dpath'])
    # find the match position
    return ac.find_template(imsrc, imobj)
if __name__ == "__main__":
    print("start")
    po=dict(spath=r'aa.png',dpath=r'bb.png')
    pos=getPositionBylocationmap(po)
    print(pos)
    print("end")