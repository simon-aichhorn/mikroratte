

class Dijkstra:
    def __init__(self, grid):
        self.grid = grid
        self.waiting=[]
        self.done=[]

    def fastestWay(self, startPos):
        startCell = self.grid[startPos[0]][startPos[1]]
        startCell.cost = 0
        self.waiting.append(startCell)

    def solve(self):
        while(len(waiting) != 0):
            currentItem = min(self.waiting, key=lambda x: x.cost)

            for neighbor in currentItem.connectedTo:
                calcCost = currentItem.cost + neighbor.cost

                if(neighbor.cost == None or calcCost < neighbor.cost):
                    neighbor.cost = calcCost
                    neighbor.previous = neighbor

                neighborAlreadyDone = any(done.x == neighbor.x and done.y == neighbor.y for done in self.waiting)
                if(not neighborAlreadyDone):
                    self.waiting.append(neighbor)

            self.done.append(currentItem)

nn=Cell(0,0)
ne=Cell(0,1)
nz=Cell(0,2)
nd=Cell(0,3)
nv=Cell(0,4)
nf=Cell(0,5)
ns=Cell(0,6)

en=Cell(1,0)
ee=Cell(1,1)
ez=Cell(1,2)
ed=Cell(1,3)
ev=Cell(1,4)
ef=Cell(1,5)
es=Cell(1,6)

zn=Cell(2,0)
ze=Cell(2,1)
zz=Cell(2,2)
zd=Cell(2,3)
zv=Cell(2,4)
zf=Cell(2,5)
zs=Cell(2,6)

dn=Cell(3,0)
de=Cell(3,1)
dz=Cell(3,2)
dd=Cell(3,3)
dv=Cell(3,4)
df=Cell(3,5)
ds=Cell(3,6)

vn=Cell(4,0)
ve=Cell(4,1)
vz=Cell(4,2)
vd=Cell(4,3)
vv=Cell(4,4)
vf=Cell(4,5)
vs=Cell(4,6)

fn=Cell(5,0)
fe=Cell(5,1)
fz=Cell(5,2)
fd=Cell(5,3)
fv=Cell(5,4)
ff=Cell(5,5)
fs=Cell(5,6)

sn=Cell(6,0)
se=Cell(6,1)
sz=Cell(6,2)
sd=Cell(6,3)
sv=Cell(6,4)
sf=Cell(6,5)
ss=Cell(6,6)

nn.addConnectedCell(ne)

ne.addConnectedCell(nn)
ne.addConnectedCell(nz)
ne.addConnectedCell(ee)

nz.addConnectedCell(ne)
nz.addConnectedCell(nd)

nd.addConnectedCell(nz)
nd.addConnectedCell(nv)

nv.addConnectedCell(nd)
nv.addConnectedCell(nf)

nf.addConnectedCell(nv)
nf.addConnectedCell(ns)

ns.addConnectedCell(nf)
ns.addConnectedCell(es)

es.addConnectedCell(ns)
es.addConnectedCell(zs)

zs.addConnectedCell(es)
zs.addConnectedCell(ds)

ds.addConnectedCell(zs)
ds.addConnectedCell(vs)

vs.addConnectedCell(ds)
vs.addConnectedCell(fs)

fs.addConnectedCell(vs)
fs.addConnectedCell(ss)

ss.addConnectedCell(fs)
ss.addConnectedCell(sf)

sf.addConnectedCell(ff)
sf.addConnectedCell(sv)

sv.addConnectedCell(sf)
sv.addConnectedCell(sd)

sd.addConnectedCell(sv)
sd.addConnectedCell(sz)

sz.addConnectedCell(sd)
sz.addConnectedCell(se)

se.addConnectedCell(sz)
se.addConnectedCell(sn)

sn.addConnectedCell(se)
sn.addConnectedCell(fn)

fn.addConnectedCell(sn)
fn.addConnectedCell(vn)

vn.addConnectedCell(fn)
vn.addConnectedCell(dn)

dn.addConnectedCell(vn)
dn.addConnectedCell(zn)

zn.addConnectedCell(dn)
zn.addConnectedCell(en)

en.addConnectedCell(zn)
en.addConnectedCell(ee)

ee.addConnectedCell(en)
ee.addConnectedCell(ne)
ee.addConnectedCell(ez)

ez.addConnectedCell(ee)
ez.addConnectedCell(ed)

ed.addConnectedCell(ez)
ed.addConnectedCell(ev)

ev.addConnectedCell(ed)
ev.addConnectedCell(ef)

ef.addConnectedCell(ev)
ef.addConnectedCell(zf)

zf.addConnectedCell(ef)
zf.addConnectedCell(df)

df.addConnectedCell(zf)
df.addConnectedCell(dv)
df.addConnectedCell(vf)

vf.addConnectedCell(df)
vf.addConnectedCell(ff)

ff.addConnectedCell(vf)
ff.addConnectedCell(sf)

dv.addConnectedCell(df)
dv.addConnectedCell(zv)
dv.addConnectedCell(vv)

zv.addConnectedCell(dv)
zv.addConnectedCell(zd)

zd.addConnectedCell(zv)

vv.addConnectedCell(dv)
vv.addConnectedCell(fv)

fv.addConnectedCell(vv)
fv.addConnectedCell(fd)

fd.addConnectedCell(fv)
fd.addConnectedCell(vd)

vd.addConnectedCell(fd)
vd.addConnectedCell(dd)

dd.addConnectedCell(vd)
dd.addConnectedCell(dz)

dz.addConnectedCell(dd)
dz.addConnectedCell(zz)
dz.addConnectedCell(de)

zz.addConnectedCell(dz)
zz.addConnectedCell(ze)

ze.addConnectedCell(zz)

de.addConnectedCell(dz)
de.addConnectedCell(ve)

ve.addConnectedCell(de)
ve.addConnectedCell(vz)
ve.addConnectedCell(fe)

vz.addConnectedCell(ve)
vz.addConnectedCell(fz)

fz.addConnectedCell(vz)
fz.addConnectedCell(fe)

fe.addConnectedCell(ve)
fe.addConnectedCell(fz)