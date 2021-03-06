from restaurants import app
from flask import request, jsonify, Response
import crud_functions as crud
from dicttoxml import dicttoxml


@app.route('/api/restaurants')
def api_restaurants():
    """Returns JSON data for restaurants, and XML if ?type=xml is used"""
    restaurants = crud.get_restaurants()
    if request.args.get('type') == 'xml':
        xml = dicttoxml([i.serialize for i in restaurants], attr_type=False)
        return Response(xml, mimetype='text/xml')
    else:
        return jsonify(Restaurants=[i.serialize for i in restaurants])


@app.route('/api/restaurant/<int:restaurant_id>/menu')
def api_menu_items(restaurant_id):
    """Returns JSON data for menu items, and XML if ?type=xml is used"""
    menu = crud.get_menu_items(restaurant_id)
    if request.args.get('type') == 'xml':
        xml = dicttoxml([i.serialize for i in menu], attr_type=False)
        return Response(xml, mimetype='text/xml')
    else:
        return jsonify(MenuItems=[i.serialize for i in menu])


@app.route('/api/menu_item/<int:menu_id>')
def api_menu_item(menu_id):
    """Returns JSON data a single menu item, and XML if ?type=xml is used"""
    menu_item = crud.get_menu_item(menu_id)
    if request.args.get('type') == 'xml':
        xml = dicttoxml(menu_item.serialize, attr_type=False)
        return Response(xml, mimetype='text/xml')
    else:
        return jsonify(menu_item.serialize)
