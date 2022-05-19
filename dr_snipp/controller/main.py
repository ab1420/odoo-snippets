from odoo import http
from odoo.http import request


class Productdetails(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def Product(self):
        return request.render("dr_snipp.product_page")

    @http.route('/product', type='json', methods=['POST'], auth='public', website=True)
    def fetch_record(self, **kwargs):
        print("!!!!! kwargs !!!!!!!!", kwargs)
        items = []
        domain = []
        search_name = kwargs.get('name', False)
        order_value = kwargs.get('order_val', False)
        if search_name:
            domain.append(('name', 'ilike', str(search_name)))
        practice_data = request.env['product.template'].sudo().search(domain, order=order_value)
        for rec in practice_data:
            items.append({
                'id': rec.id,
                'name': rec.name,
                'price': rec.list_price,
            })
        return {'data': items}
