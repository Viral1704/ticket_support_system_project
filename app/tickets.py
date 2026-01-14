from flask import Blueprint, request, jsonify 

from app.models import Ticket

from app import db

from app.utils import get_user_from_token

tickets = Blueprint('tickets', __name__)


@tickets.route('', methods = ['POST'])
def create_ticket():
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'message' : 'Title is required'}), 400
    
    description = data.get('description')

    priority = data.get('priority', 'low')
    if priority not in ['low', 'medium', 'high', 'urgent']:
        return jsonify({'message' : 'Invalid priority'}), 400
    
    category = data.get('category', 'general')
    if category not in ['general', 'billing', 'technical', 'account', 'bug', 'other']:
        return jsonify({'message' : 'Invalid category'}), 400

    new_ticket = Ticket(title = title, description = description, priority = priority, category = category, user_id = user.id)

    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'ticket_id' : new_ticket.id,
                    'title' : new_ticket.title,
                    'description' : new_ticket.description,
                    'status' : new_ticket.status,
                    'priority' : new_ticket.priority,
                    'category' : new_ticket.category
                    }), 201



@tickets.route('', methods = ['GET'])
def get_my_tickets():
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
            'status' : ticket.status,
            'priority' : ticket.priority,
            'category' : ticket.category
        })
    return jsonify({'tickets' : tickets_list}), 200


@tickets.route('/<int:ticket_id>', methods = ['GET'])
def get_my_ticket(ticket_id):
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    ticket = Ticket.query.get(ticket_id)
    if ticket is None:
        return jsonify({'message' : 'Ticket not found'}), 404
    
    if ticket.user_id != user.id:
        return jsonify({'message' : 'Forbidden'}), 403
    
    return jsonify({
        'id' : ticket.id,
        'title' : ticket.title,
        'description' : ticket.description,
        'status' : ticket.status,
        'priority' : ticket.priority,
        'category' : ticket.category
    }), 200


@tickets.route('/<int:ticket_id>', methods = ['PUT'])
def update_my_ticket(ticket_id):
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    ticket = Ticket.query.get(ticket_id)
    if ticket is None:
        return jsonify({'message' : 'Ticket not found'}), 404
    
    if ticket.user_id != user.id:
        return jsonify({'message' : 'You do not own this ticket'}), 403
    
    data = request.get_json() or {}
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')
    priority = data.get('priority')
    category = data.get('category')

    if title is None and description is None and status is None and priority is None and category is None:
        return jsonify({'message': 'Nothing to update'}), 400

    if title is not None:
        ticket.title = title

    if description is not None:
        ticket.description = description

    if status is not None:
        if status not in ['open', 'in_progress', 'closed']:
            return jsonify({'message' : 'Invalid status'}), 400
        ticket.status = status

    if priority is not None:
        if priority not in ['low', 'medium', 'high', 'urgent']:
            return jsonify({'message' : 'Invalid priority'}), 400
        ticket.priority = priority

    if category is not None:
        if category not in ['general', 'billing', 'technical', 'account', 'bug', 'other']:
            return jsonify({'message' : 'Invalid category'}), 400
        ticket.category = category

    db.session.commit()

    return jsonify({
        'id' : ticket.id,
        'title' : ticket.title,
        'description' : ticket.description,
        'status' : ticket.status,
        'priority' : ticket.priority,
        'category' : ticket.category
    }), 200


@tickets.route('/<int:ticket_id>', methods = ['DELETE'])
def delete_my_ticket(ticket_id):
    user = get_user_from_token()
    if user is None:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    ticket = Ticket.query.get(ticket_id)

    if ticket is None:
        return jsonify({'message' : 'Ticket not found'}), 404
    
    if ticket.user_id != user.id:
        return jsonify({'message' : 'Forbidden'}), 403
    
    db.session.delete(ticket)
    db.session.commit()
    return '', 204