print('oi')
bolas = "https://i.imgur.com/rgTSap6.png"
amarelo = 'https://i.imgur.com/FwCTxwE.png'
azul = 'https://i.imgur.com/ERl5wQU.png'
rosa = 'https://i.imgur.com/goMGtsi.png'
vermelho = 'https://i.imgur.com/hNCB7v3.png'
palito = 'https://imgur.com/20BUCM6.png'
from browser import html


class Torre:
    def __init__(self):
        def move(ev):
            if bl <=
            self.destino <= bl
            self.destino, self.origem = self.origem, self.destino
            print(self.origem.id, self.destino.id)
        def move2(ev):
            self.palito2 <= bl
        def move3(ev):
            self.origem <= bl

        dm = html.DIV(Id="a_mao", style="position:absolute; left:80px; top:10px;")
        pa = html.IMG(src=palito, width="30px").bind("click", move3)
        dpa = html.DIV(src=pa, style="position:absolute; left:105px; top:50px;")
        pa2 = html.IMG(src=palito, width="30px").bind("click", move2)
        dpa2 = html.DIV(src=pa2, style="position:absolute; left:250px; top:50px;")
        bl = html.IMG(Id="bola_vermelha", src=vermelho, width="80px").bind("click", move)
        dp = html.DIV(Id="o_palito", style="position:absolute; left:80px; top:200px;")
        self.destino = dm
        self.origem = dp
        self.palito = dpa
        self.palito2 = dpa2
        dpa <= pa
        dpa2 <= pa2
        dp <= bl
    def mostra(self):
        return [self.palito, self.palito2, self.destino, self.origem]


def torre():
    return Torre().mostra()



