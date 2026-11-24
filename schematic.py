import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
fig,ax=plt.subplots(figsize=(10,4.6)); ax.set_xlim(0,100); ax.set_ylim(0,46); ax.axis("off")
def box(x,y,w,h,t,fc,ec,fs=8.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.4,rounding_size=1.2",fc=fc,ec=ec,lw=1.2)); ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs)
def arr(a,b,c,d,col="#444"): ax.add_patch(FancyArrowPatch((a,b),(c,d),arrowstyle="-|>",mutation_scale=11,lw=1.1,color=col))
box(1,30,12,10,"Laser +\nmodulated\ndata","#eef3fb","#2c4a7a")
box(18,28,15,14,"Phase-only SLM\nsegmented into\nK sub-apertures\n(beam steering)","#fff6e6","#b36b00")
box(38,28,15,14,"Per-segment\npolarisation marker\n(retarder array:\nH, V, ...)","#eaf6ec","#2e7d32")
arr(13.6,35,17.5,35); arr(33.6,35,37.5,35)
# coverage grid
x0,y0,s=62,8,9
lab="HVHVHVHVH"
for i in range(3):
    for j in range(3):
        k=3*i+j; c="#c9daf8" if lab[k]=="H" else "#d9ead3"
        ax.add_patch(Circle((x0+s*j+4.5,y0+s*i+4.5),5.6,fc=c,ec="#555",alpha=0.6,lw=0.8)); ax.text(x0+s*j+4.5,y0+s*i+4.5,lab[k],ha="center",va="center",fontsize=9,weight="bold")
for (a,b) in [(53.6,38),(53.6,35),(53.6,32)]: arr(a,b,63,30-0.0*(b-35))
ax.text(75.5,38.5,"Overlapping coverage cells\n(receiver plane)",ha="center",fontsize=8.5)
box(1,4,52,18,"Received intensity at a point served by beams $j$:\n$I=\\sum_{j,k}E_jE_k^*\\,G_{jk}$,   $G_{jk}=\\langle m_k|m_j\\rangle$\n\ncoherent ($G_{jk}=1$): deep fades where beams overlap\northogonal markers on neighbouring cells: no fade between them\nphase dithering: removes fades only after averaging many SLM frames","#f7f7f7","#777",fs=8.2)
fig.savefig("results/OWC_Transmitter_Overview.png",dpi=300,bbox_inches="tight"); print("ok")
