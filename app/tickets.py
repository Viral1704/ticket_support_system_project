from flask import Blueprint, request, jsonify 

from app.models import Ticket

from app import db

tickets = Blueprint('tickets', __name__)


@tickets.route('', methods = ['POST'])
def create_ticket():
    from app.auth import get_user_from_token
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'message' : 'Title is required'}), 400
    
    description = data.get('description')

    new_ticket = Ticket(title = title, description = description, user_id = user.id)

    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'ticket_id' : new_ticket.id,
                    'title' : new_ticket.title,
                    'description' : new_ticket.description,
                    'status' : new_ticket.status
                    }), 201



@tickets.route('', methods = ['GET'])
def get_my_tickets():
    from app.auth import get_user_from_token
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    tickets = Ticket.query.filter_by(user_id = user.id).all()
    tickets_list = []
    for ticket in tickets:
        tickets_list.append({
            'id' : ticket.id,
            'title' : ticket.title,
            'description' : ticket.description,
            'status' : ticket.status
        })
    return jsonify({'tickets' : tickets_list}), 200