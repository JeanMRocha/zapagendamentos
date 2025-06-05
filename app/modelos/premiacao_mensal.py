from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.modelos import Usuario, Bonus, CategoriaUso, RankingMensal

def executar_premiacao_mensal(db: Session):
    hoje = datetime.utcnow()
    mes_referencia = hoje.strftime("%Y-%m")
    usuarios = db.query(Usuario).all()

    categorias = db.query(CategoriaUso).order_by(CategoriaUso.min_agendamentos).all()
    ranking = sorted(usuarios, key=lambda u: u.agendamentos_mes, reverse=True)

    for idx, usuario in enumerate(ranking):
        # Ranking Top 5 (local pode ser melhorado com filtro por cidade)
        if idx < 5:
            ranking_entry = RankingMensal(
                usuario_id=usuario.id,
                cidade="Santa Maria Madalena",  # por enquanto fixo
                mes=mes_referencia,
                posicao=idx + 1,
                destaque=True
            )
            db.add(ranking_entry)

        # Categoria por uso
        for categoria in categorias:
            if usuario.agendamentos_mes >= categoria.min_agendamentos and (
                categoria.max_agendamentos is None or usuario.agendamentos_mes <= categoria.max_agendamentos):

                usuario.categoria_atual = categoria.nome
                usuario.badge = categoria.selo
                bonus = Bonus(
                    usuario_id=usuario.id,
                    tipo="categoria",
                    valor_creditos=categoria.recompensa_creditos,
                    validade=datetime.utcnow() + timedelta(days=categoria.validade_dias),
                    descricao=f"Bônus por atingir categoria {categoria.nome}"
                )
                db.add(bonus)
                break

        # Resetar contadores mensais
        usuario.agendamentos_mes = 0

    db.commit()
    print(f"Premiação mensal de {mes_referencia} executada com sucesso.")
