odoo.define('dr_snipp.dr_card_query', function (require) {
    'use strict';
    var core = require('web.core')
    var QWeb = core.qweb

    const publicWidget = require('web.public.widget');
    publicWidget.registry.abc = publicWidget.Widget.extend({
        selector: '.dr_product',
        events: {
            'change #input_one': '_onChangeInput',
            'click .dropdown-item' : 'orderchange'
        },
        xmlDependencies: ['/dr_snipp/static/src/xml/dr_card_js.xml'],

        init: function () {
            this.searchTerm = '';
            this.orderBy = '';
            this._super.apply(this, arguments)
        },

        start: function () {
            var def = [this._super.apply(this, arguments)];
            def.push(this._getData());
            return Promise.all(def);
        },

        _getData: function (params) {
            var params = {};
            if (this.searchTerm) {
                params.name = this.searchTerm;
            }
            if (this.orderBy) {
                params.order_val = this.orderBy;
            }
            return this._rpc({
                route: '/product',
                params: params,
            }).then((result) => {
                var message = $(QWeb.render('Product_details', result))
                this.$target.find('.my_item').remove();
                $(message).appendTo(this.$target);
            });
        },

        _onChangeInput: function (ev) {
            let input_data = $(ev.currentTarget).val();
            this.searchTerm = input_data
            console.log(this.searchTerm)
            return this._getData();
        },

        orderchange: function (ev){
            let sort_data = $(ev.currentTarget).attr('data-order');
            this.orderBy = sort_data
            console.log(this.orderBy)
            return this._getData()
        }
    });
});



