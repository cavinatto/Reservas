from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db
import requests

routes = Blueprint("routes", __name__)

# Verifica se a turma existe na API principal
def validar_turma(turma_id):
    try:
        resposta = requests.get(f"http://localhost:8000/api/turmas/{turma_id}")
        return resposta.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# Cria nova reserva
@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json

    turma_id = dados.get("turma_id")
    if not turma_id:
        return jsonify({"erro": "turma_id é obrigatório"}), 400

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada na API principal"}), 400

    nova_reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(nova_reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

# Lista todas as reservas
@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        }
        for r in reservas
    ])

# Detalhar uma reserva por ID
@routes.route("/reservas/<int:reserva_id>", methods=["GET"])
def obter_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    return jsonify({
        "id": reserva.id,
        "turma_id": reserva.turma_id,
        "sala": reserva.sala,
        "data": reserva.data,
        "hora_inicio": reserva.hora_inicio,
        "hora_fim": reserva.hora_fim
    })

# Atualizar uma reserva
@routes.route("/reservas/<int:reserva_id>", methods=["PUT"])
def atualizar_reserva(reserva_id):
    dados = request.json
    reserva = Reserva.query.get(reserva_id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    turma_id = dados.get("turma_id")
    if turma_id and not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada na API principal"}), 400

    reserva.turma_id = turma_id or reserva.turma_id
    reserva.sala = dados.get("sala", reserva.sala)
    reserva.data = dados.get("data", reserva.data)
    reserva.hora_inicio = dados.get("hora_inicio", reserva.hora_inicio)
    reserva.hora_fim = dados.get("hora_fim", reserva.hora_fim)

    db.session.commit()
    return jsonify({"mensagem": "Reserva atualizada com sucesso"})

# Excluir uma reserva
@routes.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def excluir_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    db.session.delete(reserva)
    db.session.commit()
    return jsonify({"mensagem": "Reserva excluída com sucesso"})
